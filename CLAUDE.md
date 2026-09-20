# armoonia 프로젝트 지침

## 1. 배포 정보
- 로컬 폴더: `C:\Users\USER\armoonia`
- GitHub 저장소: `choisuka/armonia`
- 실제 라이브 주소: `https://choisuka.github.io/armonia/`
  - ⚠️ `https://choisuka.github.io/`(루트)는 완전히 별개의 저장소(`choisuka/choisuka.github.io`)가 서빙 중인 옛날 버전이다. armoonia를 고쳐도 루트 주소는 안 바뀐다 — 혼동 금지.
- Android 앱(`armoonia_android`, 별도 로컬 폴더)이 WebView로 위 `/armonia/` 주소를 로드한다 (`MainActivity.java`의 `HUB_URL`).

## 2. 구조
- 단일 허브 `index.html` + 실제 내부 폴더로 존재하는 5개 앱: `naesarang`, `happy_day`, `toro`, `science_game`, `world_history`
- 육아 콘텐츠 전용 페이지(전부 "육아 완전 가이드" 섹션 카드에서 연결): `guide_books.html`(그림책), `art_guide.html`(미술), `kids_music.html`(음악), `exercise_guide.html`(운동), `gear_guide.html`(육아용품), `travel_guide.html`(여행)
- 프레임워크·빌드 도구 없음 (Vanilla JS) — GitHub Pages가 파일을 그대로 서빙
- `sw.js` 서비스워커가 캐시 우선(cache-first)으로 동작

## 3. 알려진 함정
- **상대/절대경로 이중화(해결됨)**: armoonia_hub 통합 이전 각 앱이 독립 저장소였던 흔적으로, `index.html` 안에서 같은 앱이 상대경로(내부 복사본)와 절대경로(옛 외부 저장소) 두 가지로 동시에 링크된 적이 있었음. 2026-07-04에 14곳 전부 상대경로로 통일 완료.
- **"카드 설명과 실제 링크가 다른" 버그 패턴 — 재발 주의**: "육아 완전 가이드" 6개 카드 중 음악·운동·필수용품·여행 4개가 전용 페이지 없이 무관한 다른 앱(happy_day, toro, science_game 등)으로 임시 연결되어 있던 게 발견됨. 새 카드나 기능을 추가할 땐 **실제 목적지 페이지가 존재하는지, 카드 설명과 내용이 일치하는지** 반드시 확인할 것.
- **대소문자 변형 주의**: 예전 조사 때 `happy_day`(소문자 내부 경로)와 `Happy-day`(외부, 대문자+하이픈)가 섞여 있어 검색을 놓친 적 있음 — grep/검색 시 대소문자 무시하고 전수 검색할 것.

## 4. sw.js 캐시 버전 규칙 (중요)
- html/js 파일을 수정하면 **반드시 `sw.js`의 `CACHE_NAME` 버전도 같이 올릴 것**(예: v11→v12). 서비스워커가 캐시 우선이라, 버전을 안 올리면 기존 방문자(특히 모바일)에게 변경사항이 반영되지 않는다.
- 다만 **커밋/푸시는 매번 하지 않는다** — 여러 수정을 모아뒀다가 사용자가 명시적으로 요청할 때 한 번에 진행한다(2026-07-04부터 방침).

## 5. 테스트 방법
- 자동화 테스트 없음 — 브라우저에서 직접 렌더링·클릭 동작 확인
- 유튜브 등 외부 리소스 생존 확인: `https://www.youtube.com/oembed?url=...` API로 HTTP 상태만 스캔(재생 없이 확인 가능)
- JS 문법 확인: `node -e "new Function(...)"`로 `<script>` 블록만 빠르게 체크 가능

## 6. 관련 프로젝트와의 관계
- `armoonia_android`(별도 로컬 폴더): WebView로 armoonia 라이브 URL만 로드 — HTML을 안드로이드 프로젝트 안에 넣을 필요 없음(과거 assets 복사 방식은 폐기됨).
- **`toro_math`(수학왕국)는 armoonia와 완전히 분리된 별도 프로젝트**(`C:\Users\USER\toro_math`, 자체 git 저장소·자체 CLAUDE.md 보유). 앱 코드·기능은 서로 섞지 않는다. 단, 첫 화면 "아르모니아를 만든 이유" 카드에 토로매쓰 소개 문장과 주소 링크(`https://choisuka.github.io/toro_math/`)를 두는 것은 허용이며 유지한다(삭제 금지).
  - 변경 이력: 2026-09-20 이전에는 "toro_math 관련 코드·링크를 추가하지 않는다"였음. 이 날 사용자가 "둘 다 완성 단계여서 소개하는 정도의 문장은 관계없다. 토로매쓰 소개와 주소도 추가"라고 결정해 소개·링크만 허용으로 바뀜.
  - 두 프로젝트는 "연결"하지 않는다. 첫 화면 카드는 토로매쓰를 별도 앱으로 소개하고 주소 링크만 줄 뿐이며, "토로매쓰로 이어진다/다음 단계"처럼 이어짐을 뜻하는 표현은 쓰지 않는다. 2026-09-20 사용자 지시: "아르모니아와 토로매쓰는 연결되면 안됨. 단지 주소만 주고 연결." 아르모니아 소개 문장은 "학습의 핵심 코어를 준비하는 시기를 위한 프로그램"으로 정함.
- 앞으로 계속 업그레이드하는 프로젝트는 armoonia와 toro_math 둘뿐이며, 그 외 개별 저장소(naesarang·toro·science_game·world_history·Happy-day 독립 버전, 루트 저장소)는 의도적으로 방치된 레거시다.
