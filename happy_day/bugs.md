# 버그 기록 및 해결

## 1. 그림(명화) 이미지가 안 보이는 문제

### 증상
그림 탭을 클릭하면 제목·설명은 보이지만 이미지가 표시되지 않음.

### 원인
`display:none` 상태인 `.panel` 안의 `<img>`는 브라우저가 로드하지 않음.
`loading="lazy"`, `loading="eager"` 모두 해결 안 됨.

### 시도한 방법들 (실패)
- `loading="eager"` → 여전히 display:none 안에서 로드 안 됨
- `new Image()` 프리로드 → onload 타이밍 문제로 불안정
- `data-src` + showTab에서 src 설정 → `!img.src` 조건 버그 (`src=""` 이면 img.src가 현재 페이지 URL 반환)

### 최종 해결 (현재 적용)
```css
/* display:none 제거 → max-height로 숨김 (display:block 유지) */
.panel { display: block; max-height: 0; overflow: hidden; opacity: 0; pointer-events: none; }
.panel.active { max-height: 9999px; opacity: 1; pointer-events: auto; }
```
`display:block`이 유지되므로 이미지가 브라우저에 의해 정상 로드됨.
`<img src="${art.img}">` 직접 설정, data-src 트릭 불필요.

---

## 2. YouTube 동영상 재생 불가 문제

### 증상
음악 탭에서 YouTube iframe이 "동영상을 재생할 수 없음" 표시.

### 원인
일부 YouTube 영상은 소유자가 퍼가기(embed) 기능을 비활성화함.
`youtube.com/embed/ID` URL로 iframe 로드 시 영상 차단됨.

### 해결
iframe 대신 **썸네일 클릭재생** 방식 적용:
```js
// 음악 패널 HTML
`<div class="yt-cover" onclick="loadYT(this,'${music.yt}')">
  <img src="https://img.youtube.com/vi/${music.yt}/hqdefault.jpg"
       onerror="this.src='https://img.youtube.com/vi/${music.yt}/mqdefault.jpg'">
  <div class="yt-play-btn"></div>
</div>
<a href="https://www.youtube.com/watch?v=${music.yt}" target="_blank">↗ YouTube에서 바로 열기</a>`

// 클릭 시 iframe으로 교체
function loadYT(el, id){
  el.innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0" ...></iframe>`;
}
```

### 남은 한계
클릭 후 iframe에서도 "재생 불가"가 뜨는 경우 → 해당 영상 자체의 퍼가기 금지.
→ "↗ YouTube에서 바로 열기" 링크로 우회.

---

## 3. img.src 조건 버그

### 증상
`data-src` 방식에서 조건 `!img.src`가 항상 false.

### 원인
`<img src="">` 상태에서 JS로 `img.src`를 읽으면 빈 문자열이 아닌 **현재 페이지 URL**이 반환됨.

### 해결
`!img.src` → `!img.getAttribute('src')` 또는 조건 자체 제거.
(현재는 display:none 방식 자체를 변경해서 이 문제가 발생하지 않음)

---

## 4. Edit 도구 CRLF 문제

### 증상
Edit 도구에서 "String not found" 오류가 반복 발생.

### 원인
Windows 환경에서 git이 LF → CRLF로 변환. 파일의 실제 줄바꿈이 `\r\n`이지만 Edit 도구는 `\n`으로 검색.

### 해결
- 한 줄짜리 코드나 매우 짧고 고유한 문자열로 검색
- Python 스크립트로 직접 치환:
```python
content = open('index.html', 'r', encoding='utf-8').read()
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
```