# 콘텐츠 DB 구조

## 개요

`DB` 객체에 8가지 날씨 조건별로 콘텐츠가 담겨 있다.
각 조건마다 **quotes, musics, poems, arts, places, books, jobs** 7개 키를 가진다.

```js
const DB = {
  clear: { name, emoji, cls, quotes[], musics[], poems[], arts[], places[], books[], jobs{} },
  partlyCloudy: { ... },
  cloudy: { ... },
  // ... 8개 조건
}
```

## 배열 항목 형식

### quotes (명언) — 3개
```js
{ t: '명언 본문', s: '— 출처' }
```

### musics (음악) — 3개
```js
{
  title:  '곡명 (작곡가)',
  artist: '연주자 / 오케스트라',
  yt:     'YouTube 영상 ID (11자리)',
  q:      '검색 키워드 (사용 안 함, 참고용)',
  why:    '이 날씨에 어울리는 이유'
}
```

### poems (시) — 3개
```js
{
  title:  '시 제목',
  author: '시인 · 발표연도',
  text:   '시 본문 (줄바꿈 \n 사용)'
}
```

### arts (명화) — 3개
```js
{
  title: '작품명',
  info:  '화가 · 연도 · 소장 미술관',
  desc:  '작품 설명',
  img:   'Wikimedia Commons 이미지 URL (600~800px 썸네일)'
}
```

### places (장소) — 4개
```js
{ i: '이모지', n: '장소명', d: '설명' }
```

### books (책) — 3개
```js
{ t: '제목', a: '저자', r: '추천 이유' }
```

### jobs (활동) — 6가지 직업군, 각 3개 활동
```js
{
  student:   ['활동1', '활동2', '활동3'],
  office:    [...],
  home:      [...],
  retired:   [...],
  freelance: [...],
  artist:    [...]
}
```

## 콘텐츠 선택 함수

### index.html — 오늘 날짜 기준
```js
function pick(arr){
  const d = new Date();
  const day = Math.floor((d - new Date(d.getFullYear(), 0, 1)) / 86400000);
  return arr[day % arr.length];
}
```
→ 1월 1일=0, 매일 1씩 증가. 3개짜리 배열은 3일마다 순환.

### monthly.html — 특정 날짜 기준
```js
function pickForDate(arr, dateStr){
  const d = new Date(dateStr + 'T00:00:00');
  const day = Math.floor((d - new Date(d.getFullYear(), 0, 1)) / 86400000);
  return arr[day % arr.length];
}
```

## 이미지 출처
- 명화 이미지: Wikimedia Commons (`upload.wikimedia.org`) — 퍼블릭 도메인, 핫링크 허용
- 음악 썸네일: YouTube (`img.youtube.com/vi/{ID}/hqdefault.jpg`)