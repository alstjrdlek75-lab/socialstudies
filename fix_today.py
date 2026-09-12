import re

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """
        // If autoSelectTopic is requested, resolve the remembered topic for this subject
        if (autoSelectTopic) {
          const q = searchQuery.toLowerCase().trim();
          const matchIndices = [];
          TOPICS.forEach((topic, idx) => {
            const matchSubj = (activeSubject === 'ALL' || topic.subject === activeSubject);
"""

new_code = """
        // If autoSelectTopic is requested, resolve the remembered topic for this subject
        if (autoSelectTopic) {
          const q = searchQuery.toLowerCase().trim();
          const matchIndices = [];
          const fsrsMap = JSON.parse(localStorage.getItem('edurecall_fsrs_grades')) || {};
          const nowTime = new Date().getTime();
          
          TOPICS.forEach((topic, idx) => {
            let matchSubj = false;
            if (activeSubject === '오늘 복습') {
              const card = fsrsMap[topic.id];
              if (card && card.state !== 0 && card.due && new Date(card.due).getTime() <= nowTime) {
                matchSubj = true;
              }
            } else {
              matchSubj = (activeSubject === 'ALL' || topic.subject === activeSubject);
            }
"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('/Users/mac/.gemini/antigravity/scratch/edurecall/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully fixed setSubjectTab logic for '오늘 복습'")
else:
    print("Could not find the target code block in index.html")
