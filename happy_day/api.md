# Open-Meteo API 사용

## 개요
무료, 키 없음, CORS 허용. 날씨 데이터 제공.

---

## index.html — 현재 날씨

```js
async function fetchWeather(lat, lon) {
  const r = await fetch(
    `https://api.open-meteo.com/v1/forecast` +
    `?latitude=${lat}&longitude=${lon}` +
    `&current=weather_code,temperature_2m,relative_humidity_2m,wind_speed_10m` +
    `&timezone=auto`
  );
  return (await r.json()).current;
}
```

### 반환 필드
| 필드 | 설명 |
|------|------|
| `weather_code` | WMO 날씨 코드 (0=맑음, 95+=천둥) |
| `temperature_2m` | 기온 (°C) |
| `relative_humidity_2m` | 습도 (%) |
| `wind_speed_10m` | 풍속 (km/h) |

---

## monthly.html — 16일 예보

```js
async function fetchForecast(lat, lon) {
  const r = await fetch(
    `https://api.open-meteo.com/v1/forecast` +
    `?latitude=${lat}&longitude=${lon}` +
    `&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max` +
    `&timezone=auto&forecast_days=16`
  );
  return (await r.json()).daily;
}
```

### 반환 필드
| 필드 | 설명 |
|------|------|
| `time[]` | 날짜 배열 (YYYY-MM-DD) |
| `weather_code[]` | 날짜별 WMO 코드 |
| `temperature_2m_max[]` | 최고기온 (°C) |
| `temperature_2m_min[]` | 최저기온 (°C) |
| `precipitation_sum[]` | 강수량 (mm) |
| `wind_speed_10m_max[]` | 최대 풍속 (km/h) |

---

## 위치 획득

```js
navigator.geolocation.getCurrentPosition(async pos => {
  const { latitude, longitude } = pos.coords;
  // ...
}, () => {
  // 실패 시 서울 기본값
  load(37.5665, 126.9780, '서울');
});
```

도시명은 Open-Meteo 역지오코딩 API 또는 별도 검색 API로 획득:
```js
// 도시 검색 (monthly.html)
`https://geocoding-api.open-meteo.com/v1/search?name=${query}&count=1&language=ko`
```