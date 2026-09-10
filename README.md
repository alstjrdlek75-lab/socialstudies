# 🎓 EduRecall (사회과 임용 액티브 리콜 & 인터랙티브 기출 학습 플랫폼)

> **중등교사 임용후보자 선정경쟁시험(일반사회)** 대비 전공 4대 과목(사회과교육론, 법학, 사회학, 정치학, 경제학) 핵심 서브노트 암기 및 역대 기출문제(2017~2026학년도) 인터랙티브 학습 웹 애플리케이션입니다.

---

## 🌟 주요 기능 (Key Features)

1. **액티브 리콜 (Active Recall) 마스킹 시스템**
   - **테이프 모드 (Tape Mode)**: 핵심 키워드 및 단락을 마스킹 테이프로 가리고 클릭하여 정답 확인
   - **타이핑 인출 모드 (Type Mode)**: 빈칸에 직접 답안 키워드를 타이핑하여 실시간 정답 채점 및 일치율 피드백
   - **블러 모드 (Blur Mode)**: 전체 텍스트를 블러 처리 후 마우스 호버로 점진적 인출
   - **전체 열기 / 가리기 토글**: 원클릭으로 전체 가림 및 해제 지원

2. **역대 기출문제 아카이브 (2017 ~ 2026학년도 총 213문항)**
   - KICE 한국교육과정평가원 공채 시험지 원문 100% 무수정 반영
   - 그래프, 도표, 삽화, 복잡한 통계표 등 **고해상도 원본 크롭 이미지(300 DPI)** 제공
   - 문항별 모범 정답 및 상세 계산 해설 아코디언 토글 (기본 닫힘 고정)
   - 모바일 & 데스크톱 반응형 뷰어 및 이미지 확대/축소 모달 지원

3. **심층 배경지식 드로어 (Knowledge Drawer)**
   - 각 주제별 빈출 쟁점, 이론적 배경, 관련 학자 및 개념 체계도를 우측 슬라이드 드로어로 제공

4. **학습 진도율 & 복습 주기 관리 (Local Storage)**
   - 주제별 암기 상태(학습 완료, 복습 필요, 에빙하우스 망각 곡선 기반 주기)를 브라우저 로컬 스토리지에 영구 저장

---

## 🛠 기술 스택 (Tech Stack)

- **Frontend**: Vanilla JavaScript (ES6+), HTML5, CSS3
- **Styling**: Tailwind CSS (CDN), Google Material Symbols & Fonts
- **Math & Figures**: KaTeX (수식 렌더링 지원), SVG & High-Res PNG Assets
- **Hosting / Deploy**: Vercel (`deploy.sh` 원클릭 배포) / GitHub Pages
- **Database**: Static In-Memory Datasets (`topics-data.js`, `explanations-data.js`)

---

## 📁 프로젝트 구조 (Directory Structure)

```text
edurecall/
├── index.html              # 메인 애플리케이션 (SPA 뷰어, 상태 관리, 이벤트 핸들러)
├── topics-data.js          # 전공 서브노트 + 기출 213문항 데이터베이스 (window.ALL_TOPICS)
├── explanations-data.js    # 주제별 심층 배경지식 및 해설 데이터베이스 (window.ALL_EXPLANATIONS)
├── package.json            # 프로젝트 메타데이터
├── deploy.sh               # Vercel 프로덕션 배포 스크립트
├── .gitignore              # Git 무시 파일 설정
├── README.md               # 프로젝트 기술 및 협업 문서
└── assets/                 # 정적 에셋 디렉토리
    ├── edu_cover_1x1.png   # 앱 파비콘 및 커버 이미지
    ├── exam/               # 기출 시험지 크롭 고화질 이미지 (exam_YYYY_X_NN.png)
    ├── econ/               # 경제학 메커니즘 다이어그램
    ├── law/                # 법학 체계도
    ├── soc/                # 사회학 구조도
    └── pol/                # 정치학 비교 분석표
```

---

## 🚀 로컬 실행 방법 (Local Development)

별도의 복잡한 빌드 단계(Webpack/Vite 등) 없이 순수 웹 표준 기술로 작동하므로, 로컬 웹 서버만 실행하면 즉시 개발 및 테스트가 가능합니다.

### 방법 1: VS Code Live Server (가장 권장)
1. VS Code에서 본 프로젝트 폴더를 엽니다.
2. `Live Server` 확장을 설치하고, 우측 하단 `Go Live`를 클릭하거나 `index.html` 우클릭 후 `Open with Live Server`를 선택합니다.

### 방법 2: Python 내장 서버
```bash
# Python 3
python3 -m http.server 8080
# 브라우저에서 http://localhost:8080 접속
```

### 방법 3: Node.js (npx)
```bash
npx serve .
```

---

## 📊 데이터 모델 스키마 (Data Schema)

### `topics-data.js`의 토픽 객체 구조
모든 토픽 데이터는 `window.ALL_TOPICS` 배열에 객체 형태로 저장됩니다.

```javascript
{
  id: "EXAM-2020-B-07",                         // 고유 식별자 (과목코드 or 기출코드)
  subject: "기출",                              // 대분류 (기출, 사회과교육론, 법학, 사회학, 정치학, 경제학)
  chapter: "2020학년도 기출",                   // 중분류 (기출의 경우 'YYYY학년도 기출')
  section: "전공 B",                            // 소분류 (전공 A / 전공 B / 단원명)
  title: "7번. 부정적 외부효과와 피구세 및 코즈 정리 [4점]", // 목록 및 헤더 타이틀
  examTag: "20",                                // 연도 태그
  page: 4,                                      // 교재 또는 시험지 면수
  contentHtml: "<div class=\"mb-4...\">...</div>", // 본문 HTML (문제 지문 + 원본 이미지 + 작성방법)
  defaultAnswer: "1. 정답:\n- ...\n2. 해설:\n...",  // 모범 정답 및 상세 계산 해설
  targetKeywords: ["s_2", "t_1", "코즈 정리"],     // 타이핑 모드 자동 채점 키워드
  tapeCount: 4,                                 // 마스킹 테이프 개수
  groupCount: 1                                 // 그룹 개수
}
```

---

## ⚠️ 기출 문항 추가 및 기여 가이드라인 (Contribution Rules)

본 프로젝트는 국가 공인 임용시험 준비생들이 실제 시험과 100% 동일한 환경에서 훈련할 수 있도록 설계되었습니다. 데이터 추가/수정 시 다음 4대 원칙을 엄격히 준수해야 합니다:

1. **KICE 공식 시험지 원문 무수정 원칙**:
   - 시험지 원문의 텍스트는 토씨 하나, 기호 하나 빠짐없이 **원문 그대로** 유지합니다.
   - AI를 통한 임의 요약, 번역, 영단어 임의 삽입을 절대 금지합니다.
2. **도표/그래프/삽화의 원본 이미지 크롭 필수**:
   - 텍스트나 ASCII 아트, 임의의 HTML 테이블로 시험지의 그래프·도표를 대체하지 않습니다.
   - 반드시 원본 PDF에서 해당 요소를 `300 DPI` 고해상도로 크롭하여 `assets/exam/exam_YYYY_X_NN.png` 형태로 저장하고 `<img>` 태그로 연결합니다.
3. **기출 정답/해설 `<details>` 토글 기본 닫힘 고정**:
   - 스스로 문제를 먼저 풀고 인출할 수 있도록, 기출 상세 해설 `<details>` 태그에 `open` 속성을 절대 부여하지 않습니다. (클릭 시에만 열림)
4. **수식 표기 클린 텍스트화**:
   - 브라우저 호환성 및 화면 렌더링 오류 방지를 위해, 불필요한 LaTeX 구분자(`$`나 `\(`) 대신 깔끔한 유니코드 기호(×, ÷, ², Σ, ⟹)와 이탤릭체(`<i>Q</i>`)를 사용합니다.

---

## 🚢 배포 (Deployment)

본 프로젝트는 Vercel CLI를 통해 원클릭으로 프로덕션에 배포할 수 있습니다:

```bash
# Vercel 로그인 후
./deploy.sh
```

또는 GitHub 저장소의 `main` 브랜치에 푸시하면 연동된 Vercel / GitHub Pages에서 자동 배포됩니다.
