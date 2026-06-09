# 내사랑 (NaeSarang) 프로젝트

## 프로젝트 개요
부모가 아이에게 화내는 순간을 감지해 감정을 제어할 수 있도록 돕는 웹앱.
단일 HTML 파일 (`index.html`). 서버 없음, 빌드 없음, 외부 라이브러리 없음.

## 기술 스택
- 순수 HTML + CSS + JavaScript (단일 파일)
- Web Audio API (마이크 감지, 진정 음향 생성)
- localStorage (설정 및 기록 저장)
- GitHub Pages 배포 (무료 HTTPS 호스팅)

## 앱 구조 (화면 흐름)
1. **온보딩** → 2. **설정** (사진 업로드, 마이크 감도) → 3. **감지 중** (마이크 모니터링)
→ 4. **개입** (아이 사진 + 메시지 + 진정 음향 + 진동) → 5. **호흡** (4-4-4 박스 호흡)
→ 6. **타이머** (3분) → 7. **마무리** → 8. **기록** (통계 + 시간대 차트)

## 핵심 기능
- 마이크 볼륨 임계치 초과 시 자동 개입 트리거
- 수동 트리거 버튼 (🚨 지금 화났어요)
- 4가지 진정 음향: 멜로디 / 빗소리 / 자장가 / 외부링크
- 경고 징 소리 (`playGong()`) — 임계치 최초 감지 시 즉시 재생
- 폰 진동 (navigator.vibrate)
- 감지 이벤트 로그 (결과: calmed / dismissed / retry)
- 시간대별 패턴 차트

## 진정 음향 상세
- **공통**: 마이크 AudioContext(`audioCtx`) 재사용 — 브라우저 자동재생 정책 우회
- **멜로디** (`startMelody()`): 피아노 음계 + 에코 딜레이, masterGain 0.45
- **빗소리** (`startRain()`): 백색잡음 버퍼 + bandpass 필터(600Hz), gain 0.35
- **자장가** (`startLullaby()`): 브람스 자장가 triangle wave + bass, gain 0.4
- **외부링크** (`openExternalSound()`): localStorage의 URL을 새 탭으로 열기

## 알림 음향
- `playGong()`: 220·440·660Hz 사인파 3개 합성, 즉각적인 강한 충격음
- `alertLock`: 징 소리 중복 방지 (3초), 볼륨 모니터링 자체는 계속 진행

## 주요 함수
- `startMic()` / `stopMic()` - 마이크 스트림 관리 (중복 방지 포함)
- `monitorVolume()` - RMS 기반 볼륨 감지 (highCount 누적 → 단계별 반응)
- `triggerAlert()` - 개입 화면 전환 + 음향 + 진동
- `dismissAlert()` - 무시 후 모니터링 재시작
- `startCalmSound()` / `stopCalmSound()` - 진정 음향 제어
- `playGong()` - 경고 징 소리 즉시 재생
- `saveLog(outcome)` / `openLog()` - 기록 저장 및 렌더링
- `showScreen(name)` - 화면 전환 + 버튼 가시성 관리

## UI / 디자인
- **온보딩**: 보라 그라디언트(#3b1f6b → #1e1040 → #12243a), 파티클 애니메이션
- **타이틀 '내사랑'**: Nanum Brush Script, shimmer + titleFloat 애니메이션
- **폰트**: Nanum Brush Script, Nanum Pen Script, Gaegu, Jua, Poor Story (Google Fonts)
- **버튼**: 보라 그라디언트 (#6b21a8 → #a855f7)
- **음악 선택 버튼**: Poor Story 폰트, 어두운 배경 (#0f3460), 선택 시 빨간 테두리

## 설정값 저장 (localStorage)
- `childPhoto` - 아이 사진 (base64 DataURL)
- `sensitivity` - 마이크 감도 (1~10)
- `logs` - 감지 이벤트 배열 `[{ time, outcome }]`

## 향후 확장 가능 항목
- 스마트워치 심박수 연동 (심박수가 목소리보다 먼저 반응)
- 스마트 조명 API 연동 (Philips Hue 등)
- 음성 톤 분석 (주파수 기반 분노 감지)
- 다중 사용자 / 가족 프로필

## 배포
- GitHub Pages: `https://[아이디].github.io/naesarang`
- 파일 하나만 있으면 됨 (`index.html`)
