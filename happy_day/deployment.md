# 배포 정보

## GitHub Pages

| 항목 | 내용 |
|------|------|
| 저장소 | https://github.com/choisuka/Happy-day |
| 배포 URL | https://choisuka.github.io/Happy-day/ |
| 브랜치 | main |
| 방식 | 정적 파일 직접 배포 (빌드 없음) |

## 배포 절차

```bash
cd C:\Users\USER\happy_day
git add .
git commit -m "변경 내용"
git push origin main
```
push 후 보통 1~5분 내 반영. CDN 캐시 때문에 최대 10~30분 걸릴 수 있음.

## CDN 캐시 문제

GitHub Pages는 Fastly CDN을 사용하며, 새 커밋 후에도 구버전을 서빙하는 경우가 있음.

### 증상
- raw.githubusercontent.com에서는 새 코드가 보임
- choisuka.github.io에서는 구버전이 서빙됨

### 해결책
- 브라우저: Ctrl+Shift+R (강제 새로고침)
- URL에 쿼리 파라미터 추가: `index.html?v=7`
- 새 커밋 push → CDN 캐시 무효화 대기

### 현재 적용된 방어책
```html
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
```
(HTML 메타태그는 CDN 캐시를 완전히 막지는 못하지만 브라우저 캐시를 막음)

## 로컬 테스트

별도 서버 없이 파일을 브라우저로 직접 열 수 있음:
- `C:\Users\USER\happy_day\index.html` → 탐색기에서 브라우저로 드래그
- 단, `navigator.geolocation`은 `file://` URL에서도 동작함 (브라우저 허용 필요)