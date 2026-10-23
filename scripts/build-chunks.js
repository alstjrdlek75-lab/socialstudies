const fs = require('fs');
const path = require('path');
const vm = require('vm');

const rootDir = path.resolve(__dirname, '..');
const topicsDataPath = path.join(rootDir, 'topics-data.js');
const dataDir = path.join(rootDir, 'data');

if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}

const code = fs.readFileSync(topicsDataPath, 'utf8');
const sandbox = { window: {} };
vm.createContext(sandbox);
vm.runInContext(code, sandbox);

const allTopics = sandbox.window.ALL_TOPICS || [];
const allExplanations = sandbox.window.TOPIC_EXPLANATIONS || {};

const SUBJECT_FILE_MAP = {
  '사회과교육론': 'edu',
  '법학': 'law',
  '사회학': 'soc',
  '정치학': 'pol',
  '경제학': 'econ',
  '기출': 'exam',
  '안내': 'guide'
};

// Build lightweight index (with '사회과교육론' and '안내' pre-hydrated so default landing is 0-latency)
const prehydratedSubjects = new Set(['사회과교육론', '안내']);
const indexTopics = allTopics.map(t => {
  const isPre = prehydratedSubjects.has(t.subject);
  return {
    id: t.id,
    subject: t.subject,
    chapter: t.chapter || '',
    section: t.section || '',
    subsection: t.subsection || '',
    title: t.title || '',
    subtitle: t.subtitle || '',
    examTag: t.examTag || '',
    page: t.page || 1,
    tapeCount: t.tapeCount || 0,
    targetKeywords: Array.isArray(t.targetKeywords) ? t.targetKeywords : [],
    contentHtml: isPre ? (t.contentHtml || '') : '',
    defaultAnswer: isPre ? (t.defaultAnswer || '') : '',
    _hydrated: isPre
  };
});

const preExplanations = {};
allTopics.forEach(t => {
  if (prehydratedSubjects.has(t.subject) && allExplanations[t.id]) {
    preExplanations[t.id] = allExplanations[t.id];
  }
});

const indexJs = `// Auto-generated lightweight boot index + default subject data
window.ALL_TOPICS = ${JSON.stringify(indexTopics)};
window.TOPIC_EXPLANATIONS = ${JSON.stringify(preExplanations)};
window.__EDURECALL_HYDRATED_SUBJECTS__ = { "사회과교육론": true, "안내": true };
window.__EDURECALL_REGISTER_CHUNK__ = function(subject, payload) {
  if (!payload) return;
  if (payload.topics && Array.isArray(window.ALL_TOPICS)) {
    for (var i = 0; i < window.ALL_TOPICS.length; i++) {
      var t = window.ALL_TOPICS[i];
      var data = payload.topics[t.id];
      if (data) {
        t.contentHtml = data.contentHtml || '';
        t.defaultAnswer = data.defaultAnswer || '';
        t._hydrated = true;
      }
    }
  }
  if (payload.explanations) {
    window.TOPIC_EXPLANATIONS = window.TOPIC_EXPLANATIONS || {};
    Object.assign(window.TOPIC_EXPLANATIONS, payload.explanations);
  }
  window.__EDURECALL_HYDRATED_SUBJECTS__ = window.__EDURECALL_HYDRATED_SUBJECTS__ || {};
  window.__EDURECALL_HYDRATED_SUBJECTS__[subject] = true;
};
`;

fs.writeFileSync(path.join(dataDir, 'topics-index.js'), indexJs, 'utf8');
console.log('Created data/topics-index.js:', (Buffer.byteLength(indexJs) / 1024).toFixed(1) + ' KB');

// Build per-subject chunks
Object.entries(SUBJECT_FILE_MAP).forEach(([subject, slug]) => {
  const subjTopics = {};
  const subjExplanations = {};

  allTopics.forEach(t => {
    if (t.subject === subject) {
      subjTopics[t.id] = {
        contentHtml: t.contentHtml || '',
        defaultAnswer: t.defaultAnswer || ''
      };
      if (allExplanations[t.id]) {
        subjExplanations[t.id] = allExplanations[t.id];
      }
      if (t.id.startsWith('ECON-EXAM-')) {
        const baseId = t.id.replace('ECON-', '');
        if (allExplanations[baseId]) {
          subjExplanations[baseId] = allExplanations[baseId];
        }
      }
    }
  });

  // For '기출' chunk, also include any remaining explanations not yet included
  if (subject === '기출') {
    Object.keys(allExplanations).forEach(k => {
      if (k.startsWith('EXAM-') || !subjExplanations[k]) {
        subjExplanations[k] = allExplanations[k];
      }
    });
  }

  const chunkPayload = {
    topics: subjTopics,
    explanations: subjExplanations
  };
  const chunkJs = `window.__EDURECALL_REGISTER_CHUNK__ && window.__EDURECALL_REGISTER_CHUNK__(${JSON.stringify(subject)}, ${JSON.stringify(chunkPayload)});\n`;
  const chunkPath = path.join(dataDir, `chunk-${slug}.js`);
  fs.writeFileSync(chunkPath, chunkJs, 'utf8');
  console.log(`Created data/chunk-${slug}.js (${subject}):`, (Buffer.byteLength(chunkJs) / 1024).toFixed(1) + ' KB');
});
