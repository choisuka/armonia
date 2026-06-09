# 날씨 조건 및 테마

## 8가지 날씨 조건

| 조건 key | 한국어 | 이모지 | CSS class | WMO 코드 |
|----------|--------|--------|-----------|----------|
| `clear` | 맑음 | ☀️ | clear | 0 |
| `partlyCloudy` | 구름 조금 | ⛅ | partlyCloudy | 1, 2, 3 |
| `cloudy` | 흐림 | ☁️ | cloudy | 45, 48 (안개도 여기) |
| `foggy` | 안개 | 🌫️ | foggy | 45, 48 |
| `drizzle` | 이슬비 | 🌦️ | drizzle | 51~57 |
| `rainy` | 비 | 🌧️ | rainy | 61~67, 80~82 |
| `snowy` | 눈 | ❄️ | snowy | 71~77, 85, 86 |
| `thunderstorm` | 천둥번개 | ⛈️ | thunderstorm | 95~99 |

## CSS 테마 변수 (`:root` → `body.{class}` 오버라이드)

```css
body.clear        { --A:#fef3c7; --B:#fed7aa; --P:#d97706; --T:#78350f; }
body.partlyCloudy { --A:#dbeafe; --B:#e0f2fe; --P:#0284c7; --T:#0c4a6e; }
body.cloudy       { --A:#e2e8f0; --B:#cbd5e1; --P:#475569; --T:#1e293b; }
body.foggy        { --A:#d1fae5; --B:#ecfdf5; --P:#059669; --T:#064e3b; }
body.drizzle      { --A:#dbeafe; --B:#c7d2fe; --P:#4f46e5; --T:#1e3a8a; }
body.rainy        { --A:#c7d2fe; --B:#a5b4fc; --P:#4338ca; --T:#312e81; }
body.snowy        { --A:#e0f2fe; --B:#f0f9ff; --P:#0369a1; --T:#0c4a6e; }
body.thunderstorm { --A:#1e1b4b; --B:#312e81; --P:#a5b4fc; --T:#e0e7ff; }
```

- `--A`, `--B`: 배경 그라디언트 시작/끝 색
- `--P`: 강조색 (버튼, 제목 등)
- `--T`: 텍스트 색
- `--card`: 카드 배경 (기본 `rgba(255,255,255,.88)`, thunderstorm은 어둡게)

## `getCondition(code)` 함수 (index.html)

```js
function getCondition(code){
  if(code===0)           return 'clear';
  if(code<=3)            return 'partlyCloudy';
  if(code<=48)           return 'foggy';
  if(code<=57)           return 'drizzle';
  if(code<=67||code<=82) return 'rainy';
  if(code<=77||code<=86) return 'snowy';
  return 'thunderstorm';
}
```

## body 클래스 적용

```js
document.body.className = DB[cur].cls;
```