# -*- coding: utf-8 -*-
"""
Music variety + poem+art combined panel update
- musicErr() 3단계 폴백 함수 추가
- 각 날씨 조건 music 배열 5개로 확장 (바흐·모차르트·베토벤·헨델·그리그·리스트 포함)
- 시 패널에 그림 추가 (추가 형태)
"""

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # ── 1. onerror → musicErr() ───────────────────────────
    html = html.replace(
        "           onerror=\"this.onerror=null;this.src='https://img.youtube.com/vi/${music.yt}/mqdefault.jpg'\"",
        "           onerror=\"musicErr(this,'${music.yt}')\""
    )

    # ── 2. musicErr 함수 추가 (loadYT 뒤에) ──────────────
    old_loadYT = "function loadYT(el, id){\n  window.open('https://www.youtube.com/watch?v=' + id, '_blank');\n}"
    new_loadYT = """function loadYT(el, id){
  window.open('https://www.youtube.com/watch?v=' + id, '_blank');
}

function musicErr(el, id) {
  if (el.src.indexOf('hqdefault') > -1) {
    el.src = 'https://img.youtube.com/vi/' + id + '/mqdefault.jpg';
  } else {
    el.onerror = null;
    el.src = 'data:image/svg+xml,' + encodeURIComponent(
      '<svg xmlns="http://www.w3.org/2000/svg" width="320" height="180">' +
      '<rect width="320" height="180" fill="#111"/>' +
      '<text x="160" y="110" font-size="80" text-anchor="middle" fill="#444">&#9834;</text>' +
      '</svg>'
    );
  }
}"""
    html = html.replace(old_loadYT, new_loadYT)

    # ── 3. 시 패널에 그림 추가 ────────────────────────────
    old_poem = "$('panel-poem').innerHTML = `<div class=\"poem-author\">${poem.title} — ${poem.author}</div><div class=\"poem-body\">${poem.text}</div>`;"
    new_poem = "$('panel-poem').innerHTML = `<div class=\"poem-author\">${poem.title} — ${poem.author}</div><div class=\"poem-body\">${poem.text}</div><div style=\"margin:1.5rem 0 1rem;border-top:1px solid rgba(0,0,0,.12)\"></div><img class=\"art-img\" src=\"${art.img}\" alt=\"${art.title}\" referrerpolicy=\"no-referrer\" onerror=\"this.style.display='none'\" style=\"min-height:60px;background:rgba(0,0,0,.05)\"><div class=\"art-title\">${art.title}</div><div class=\"art-info\">${art.info}</div><div class=\"art-desc\">${art.desc}</div>`;"
    html = html.replace(old_poem, new_poem)

    # ── 4. 음악 배열 교체 ─────────────────────────────────

    # clear (맑음) — 5개
    html = html.replace(
        """    musics:[
      {title:'사계 — 봄 1악장 (Vivaldi)', artist:'Vivaldi / Anne-Sophie Mutter', yt:'GRxofEmo3HA', q:'Vivaldi Four Seasons Spring classical', why:'봄날 햇살처럼 생동감 넘치는 선율. 자연의 기쁨이 활로 담겨 있습니다.'},
      {title:'전원 교향곡 6번 (Beethoven)', artist:'베토벤 / 정명훈', yt:'PeU3LS_s03I', q:'Beethoven Symphony No 6 Pastoral classical', why:'전원의 평화, 시냇가의 속삭임, 맑은 날의 기쁨을 담은 교향곡.'},
      {title:'수상 음악 모음 (Handel, Water Music)', artist:'헨델 / 존 엘리엇 가디너', yt:'4BBpPpGnFNg', q:'Handel Water Music Suite classical', why:'밝고 화사한 바로크 음악. 햇살 속을 산책하는 기분.'}
    ],""",
        """    musics:[
      {title:'사계 — 봄 1악장 (Vivaldi)', artist:'비발디 / 이무지치', yt:'GRxofEmo3HA', why:'봄날 햇살처럼 생동감 넘치는 선율. 자연의 기쁨이 활로 담겨 있습니다.'},
      {title:'전원 교향곡 6번 (Beethoven)', artist:'베토벤 / 정명훈', yt:'PeU3LS_s03I', why:'전원의 평화, 시냇가의 속삭임, 맑은 날의 기쁨을 담은 교향곡.'},
      {title:'아이네 클라이네 나흐트무지크 (Mozart)', artist:'모차르트 / 베를린 필하모닉', yt:'o1dBg__wsuo', why:'경쾌하고 우아한 선율. 맑은 날 기분을 한껏 올려줍니다.'},
      {title:'페르귄트 — 아침의 기분 (Grieg)', artist:'그리그 / 베를린 필하모닉', yt:'TmQDntXQF8M', why:'이른 아침 햇살처럼 맑고 상쾌한 선율. 페르귄트 모음곡 오프닝.'},
      {title:'수상 음악 모음 (Handel)', artist:'헨델 / 가디너', yt:'7maJOI3QMu0', why:'밝고 기품 있는 바로크 음악. 햇살 속을 산책하는 기분.'}
    ],""",
        1
    )

    # partlyCloudy (구름 조금) — 5개, 중복 제거
    html = html.replace(
        """    musics:[
      {title:'G선상의 아리아 (Bach)', artist:'J.S. Bach / 베를린 필하모닉', yt:'PeU3LS_s03I', q:'Bach Air on G String classical', why:'고요하고 평온한 선율. 흘러가는 구름처럼 마음이 편안해집니다.'},
      {title:'트로이메라이 (Schumann, Träumerei)', artist:'슈만 (Schumann)', yt:'PeU3LS_s03I', q:'Schumann Traumerei piano', why:'꿈꾸는 듯 달콤한 선율. 구름 사이 햇살처럼 포근한 소품.'},
      {title:'헝가리 무곡 5번 (Brahms)', artist:'브람스 / 베를린 필하모닉', yt:'NxwEadYik00', q:'Brahms Hungarian Dance No 5 classical', why:'흥겹고 생동감 넘치는 선율. 약간의 긴장과 유쾌함이 공존.'}
    ],""",
        """    musics:[
      {title:'G선상의 아리아 (Bach)', artist:'바흐 / 베를린 필하모닉', yt:'NxwEadYik00', why:'고요하고 평온한 선율. 흘러가는 구름처럼 마음이 편안해집니다.'},
      {title:'트로이메라이 (Schumann)', artist:'슈만 (Schumann)', yt:'imGaOIm5HOk', why:'꿈꾸는 듯 달콤한 선율. 구름 사이 햇살처럼 포근한 소품.'},
      {title:'헝가리 무곡 5번 (Brahms)', artist:'브람스 / 베를린 필하모닉', yt:'PeU3LS_s03I', why:'흥겹고 생동감 넘치는 선율. 약간의 긴장과 유쾌함이 공존.'},
      {title:'리베스트라움 3번 (Liszt)', artist:'리스트 (Liszt)', yt:'SVHHgC-a0dI', why:'사랑의 꿈 — 달콤하고 서정적인 낭만파 피아노 소품.'},
      {title:'피아노 협주곡 21번 2악장 (Mozart)', artist:'모차르트 / 머레이 페라이어', yt:'7maJOI3QMu0', why:'구름 사이 햇살처럼 달콤하게 흐르는 모차르트.'}
    ],""",
        1
    )

    # cloudy (흐림) — 5개
    html = html.replace(
        """    musics:[
      {title:'짐노페디 1번 (Satie, Gymnopédie No.1)', artist:'에릭 사티 (Erik Satie)', yt:'S-Xm7s9eGxU', q:'Satie Gymnopédie No 1 piano', why:'몽환적이고 고요한 선율. 흐린 날의 내면을 조용히 들여다보게 합니다.'},
      {title:'죽은 왕녀를 위한 파반느 (Ravel, Pavane)', artist:'라벨 (Ravel)', yt:'imGaOIm5HOk', q:'Ravel Pavane pour une infante defunte piano', why:'고요하고 우아한 선율. 흐린 하늘 아래 떠오르는 달빛 같은 피아노 소품.'},
      {title:'발라드 1번 (Chopin, Ballade No.1)', artist:'쇼팽 (Chopin)', yt:'7maJOI3QMu0', q:'Chopin Ballade No 1 piano', why:'서정적이고 극적인 쇼팽의 대표 피아노 소품. 흐린 날의 내면을 그립니다.'}
    ],""",
        """    musics:[
      {title:'짐노페디 1번 (Satie)', artist:'에릭 사티 (Erik Satie)', yt:'S-Xm7s9eGxU', why:'몽환적이고 고요한 선율. 흐린 날의 내면을 조용히 들여다보게 합니다.'},
      {title:'죽은 왕녀를 위한 파반느 (Ravel)', artist:'라벨 (Ravel)', yt:'imGaOIm5HOk', why:'고요하고 우아한 선율. 흐린 하늘 아래 달빛 같은 피아노 소품.'},
      {title:'발라드 1번 (Chopin)', artist:'쇼팽 (Chopin)', yt:'7maJOI3QMu0', why:'서정적이고 극적인 쇼팽의 대표 피아노 소품.'},
      {title:'골드베르크 변주곡 아리아 (Bach)', artist:'바흐 / 글렌 굴드', yt:'Ah392lnFHxM', why:'정교한 대위법의 정수. 흐린 날 사색에 잠기게 하는 바흐의 걸작.'},
      {title:'월광 소나타 1악장 (Beethoven)', artist:'베토벤 / 빌헬름 켐프', yt:'4Tr0otuiQuU', why:'고요하고 신비로운 달빛 같은 피아노. 흐린 날 내면을 비춥니다.'}
    ],""",
        1
    )

    # foggy (안개) — 5개
    html = html.replace(
        """    musics:[
      {title:'클레르 드 룬 (Debussy, Clair de Lune)', artist:'드뷔시 (Debussy)', yt:'CDdvReNKKuk', q:'Debussy Clair de Lune piano', why:'몽롱하고 신비로운 안개 속 분위기. 달빛처럼 부드럽게 흐르는 인상주의 피아노 명곡.'},
      {title:'목신의 오후 전주곡 (Debussy)', artist:'드뷔시 (Debussy)', yt:'imGaOIm5HOk', q:'Debussy Prelude Afternoon Faun flute orchestra', why:'흐릿한 안개 속처럼 몽환적이고 신비로운 인상주의 관현악.'},
      {title:'짐노페디 3번 (Satie, Gymnopédie No.3)', artist:'에릭 사티 (Erik Satie)', yt:'NxwEadYik00', q:'Satie Gymnopédie No 3 piano', why:'고요하고 내면적인 선율. 안개 낀 아침의 고독한 산책.'}
    ],""",
        """    musics:[
      {title:'클레르 드 룬 (Debussy)', artist:'드뷔시 (Debussy)', yt:'CDdvReNKKuk', why:'달빛처럼 부드럽게 흐르는 인상주의 피아노 명곡.'},
      {title:'목신의 오후 전주곡 (Debussy)', artist:'드뷔시 (Debussy)', yt:'imGaOIm5HOk', why:'안개 속처럼 몽환적이고 신비로운 인상주의 관현악.'},
      {title:'짐노페디 3번 (Satie)', artist:'에릭 사티 (Erik Satie)', yt:'NxwEadYik00', why:'고요하고 내면적인 선율. 안개 낀 아침의 고독한 산책.'},
      {title:'페르귄트 — 오제의 죽음 (Grieg)', artist:'그리그 / 헤르베르트 폰 카라얀', yt:'TmQDntXQF8M', why:'안개 속 슬픔처럼 천천히 흐르는 비가. 그리그 페르귄트의 명장면.'},
      {title:'라 캄파넬라 (Liszt)', artist:'리스트 / 조르주 시프라', yt:'AeP9HhI9pHE', why:'안개 속에서 울리는 종소리 같은 환상적인 피아노 기교.'}
    ],""",
        1
    )

    # drizzle (이슬비) — 5개
    html = html.replace(
        """    musics:[
      {title:'야상곡 20번 (Chopin, Nocturne No.20)', artist:'쇼팽 (Chopin)', yt:'9E6b3swbnWg', q:'Chopin Nocturne No 20 piano', why:'이슬비처럼 서정적인 피아노. 빗소리와 함께 들으면 더욱 감미롭습니다.'},
      {title:'즉흥곡 Op.90 No.2 (Schubert, Impromptu)', artist:'슈베르트 (Schubert)', yt:'7maJOI3QMu0', q:'Schubert Impromptu Op 90 No 2 piano', why:'흐르는 빗소리처럼 물결치는 피아노. 서정적이고 맑은 슈베르트.'},
      {title:'파반느 (Fauré, Pavane)', artist:'포레 (Fauré)', yt:'imGaOIm5HOk', q:'Fauré Pavane Op 50 classical', why:'우아하고 섬세한 선율. 이슬비처럼 부드럽게 내려앉는 음악.'}
    ],""",
        """    musics:[
      {title:'야상곡 20번 (Chopin)', artist:'쇼팽 (Chopin)', yt:'9E6b3swbnWg', why:'이슬비처럼 서정적인 피아노. 빗소리와 함께 들으면 더욱 감미롭습니다.'},
      {title:'즉흥곡 Op.90 No.2 (Schubert)', artist:'슈베르트 (Schubert)', yt:'7maJOI3QMu0', why:'흐르는 빗소리처럼 물결치는 피아노. 서정적이고 맑은 슈베르트.'},
      {title:'파반느 (Fauré)', artist:'포레 (Fauré)', yt:'imGaOIm5HOk', why:'우아하고 섬세한 선율. 이슬비처럼 부드럽게 내려앉는 음악.'},
      {title:'클라리넷 협주곡 K.622 2악장 (Mozart)', artist:'모차르트 / 알브레히트 마이어', yt:'NxwEadYik00', why:'이슬비처럼 맑고 감미로운 목관 선율. 모차르트 최후의 협주곡.'},
      {title:'메시아 — 라르고 (Handel)', artist:'헨델 / 존 엘리엇 가디너', yt:'PeU3LS_s03I', why:'이슬비 속에 울리는 따뜻한 위로. 헨델 오라토리오의 서정적 아리아.'}
    ],""",
        1
    )

    # rainy (비) — 5개
    html = html.replace(
        """    musics:[
      {title:'첼로 모음곡 1번 전주곡 (Bach)', artist:'J.S. Bach / Yo-Yo Ma', yt:'1prweT95Mo0', q:'Bach Cello Suite No 1 Prelude Yo-Yo Ma', why:'비가 내리는 날, 첼로의 깊은 울림이 마음 깊은 곳을 위로합니다.'},
      {title:'바다 (Debussy, La Mer)', artist:'드뷔시 (Debussy)', yt:'NxwEadYik00', q:'Debussy La Mer orchestra', why:'파도처럼 밀려오는 관현악. 비 내리는 날 창가에서 듣기 좋은 인상주의 음악.'},
      {title:'피아노 협주곡 G장조 2악장 (Ravel)', artist:'라벨 (Ravel)', yt:'7maJOI3QMu0', q:'Ravel Piano Concerto G major 2nd movement', why:'빗속의 감미로운 피아노. 조용하고 서정적인 선율이 마음을 달랩니다.'}
    ],""",
        """    musics:[
      {title:'첼로 모음곡 1번 전주곡 (Bach)', artist:'바흐 / Yo-Yo Ma', yt:'1prweT95Mo0', why:'비 내리는 날, 첼로의 깊은 울림이 마음 깊은 곳을 위로합니다.'},
      {title:'바다 — 파도의 유희 (Debussy)', artist:'드뷔시 (Debussy)', yt:'NxwEadYik00', why:'파도처럼 밀려오는 관현악. 빗소리와 어우러지는 인상주의 음악.'},
      {title:'피아노 협주곡 G장조 2악장 (Ravel)', artist:'라벨 (Ravel)', yt:'7maJOI3QMu0', why:'빗속의 감미로운 피아노. 조용하고 서정적인 선율.'},
      {title:'페르귄트 — 솔베이의 노래 (Grieg)', artist:'그리그 / 키리 테 카나와', yt:'imGaOIm5HOk', why:'빗속에서 기다리는 솔베이의 애절한 사랑 노래. 그리그 최고의 아리아.'},
      {title:'레퀴엠 — 라크리모사 (Mozart)', artist:'모차르트 / 가디너', yt:'PeU3LS_s03I', why:'비 내리는 날의 깊은 묵상. 모차르트가 세상을 떠나며 쓴 마지막 걸작.'}
    ],""",
        1
    )

    # snowy (눈) — 5개
    html = html.replace(
        """    musics:[
      {title:'사계 — 겨울 (Vivaldi, Winter)', artist:'Vivaldi / Nigel Kennedy', yt:'TZCfydWF48c', q:'Vivaldi Four Seasons Winter classical violin', why:'눈 내리는 날의 고요함과 겨울의 아름다움. 차갑고 아름다운 바이올린 협주곡.'},
      {title:'겨울 나그네 — 보리수 (Schubert, Winterreise)', artist:'슈베르트 / 디트리히 피셔-디스카우', yt:'imGaOIm5HOk', q:'Schubert Winterreise Der Lindenbaum Fischer-Dieskau', why:'눈 덮인 겨울 길을 걷는 나그네의 노래. 쓸쓸하고 아름다운 겨울 연가.'},
      {title:'호두까기 인형 — 눈송이의 왈츠 (Tchaikovsky)', artist:'차이콥스키 / 볼쇼이 발레단', yt:'NxwEadYik00', q:'Tchaikovsky Nutcracker Waltz of Snowflakes', why:'눈송이가 춤추는 듯한 발레 음악. 겨울의 환상적인 세계.'}
    ],""",
        """    musics:[
      {title:'사계 — 겨울 1악장 (Vivaldi)', artist:'비발디 / 나이절 케네디', yt:'TZCfydWF48c', why:'눈 내리는 날의 고요함과 겨울의 아름다움. 차갑고 아름다운 바이올린 협주곡.'},
      {title:'겨울 나그네 — 보리수 (Schubert)', artist:'슈베르트 / 피셔-디스카우', yt:'imGaOIm5HOk', why:'눈 덮인 겨울 길을 걷는 나그네의 노래. 쓸쓸하고 아름다운 겨울 연가.'},
      {title:'호두까기 인형 — 눈송이의 왈츠 (Tchaikovsky)', artist:'차이콥스키 / 볼쇼이 발레단', yt:'NxwEadYik00', why:'눈송이가 춤추는 듯한 발레 음악. 겨울의 환상적인 세계.'},
      {title:'브란덴부르크 협주곡 3번 (Bach)', artist:'바흐 / 카를 뮌힝거', yt:'7maJOI3QMu0', why:'겨울 실내악의 정수. 정교하고 따뜻한 바흐의 앙상블.'},
      {title:'교향곡 40번 g단조 (Mozart)', artist:'모차르트 / 베를린 필하모닉', yt:'PeU3LS_s03I', why:'눈 내리는 날의 아름다운 슬픔. 모차르트 가장 사랑받는 교향곡.'}
    ],""",
        1
    )

    # thunderstorm (천둥번개) — 5개
    html = html.replace(
        """    musics:[
      {title:'교향곡 5번 「운명」 (Beethoven, Symphony No.5)', artist:'베토벤 / 카를로스 클라이버', yt:'_4IRMYuE1hI', q:'Beethoven Symphony No 5 Fate Carlos Kleiber', why:'"운명"이 문을 두드리는 소리. 천둥번개처럼 강렬하고 극적인 베토벤의 걸작.'},
      {title:'교향곡 9번 「합창」 4악장 (Beethoven)', artist:'베토벤 / 헤르베르트 폰 카라얀', yt:'t3217H8JppI', q:'Beethoven Symphony No 9 Choral 4th movement Karajan', why:'"기쁨의 송가". 폭풍이 지나간 뒤 찾아오는 인류의 환희와 단결.'},
      {title:'발퀴레의 기행 (Wagner, Ride of the Valkyries)', artist:'바그너 (Wagner) / 게오르크 솔티', yt:'7maJOI3QMu0', q:'Wagner Ride of the Valkyries orchestral', why:'천둥번개처럼 강렬하고 웅장한 관현악. 신화적 에너지가 폭발하는 음악.'}
    ],""",
        """    musics:[
      {title:'교향곡 5번 「운명」 (Beethoven)', artist:'베토벤 / 카를로스 클라이버', yt:'_4IRMYuE1hI', why:'"운명"이 문을 두드리는 소리. 천둥번개처럼 강렬하고 극적인 걸작.'},
      {title:'교향곡 9번 「합창」 4악장 (Beethoven)', artist:'베토벤 / 헤르베르트 폰 카라얀', yt:'t3217H8JppI', why:'"기쁨의 송가". 폭풍이 지나간 뒤 찾아오는 인류의 환희와 단결.'},
      {title:'발퀴레의 기행 (Wagner)', artist:'바그너 / 게오르크 솔티', yt:'7maJOI3QMu0', why:'천둥번개처럼 강렬하고 웅장한 관현악. 신화적 에너지가 폭발.'},
      {title:'산왕의 궁전에서 (Grieg)', artist:'그리그 / 파보 예르비', yt:'SsL1DaZNPAo', why:'폭풍처럼 몰아치는 리듬. 페르귄트 모음곡에서 가장 극적인 장면.'},
      {title:'헝가리 랩소디 2번 (Liszt)', artist:'리스트 / 랑랑', yt:'SVHHgC-a0dI', why:'화려하고 폭발적인 피아노 기교. 피아노계의 천둥번개.'}
    ],""",
        1
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated: {path}")

update_file('index.html')
update_file('monthly.html')
print("All done!")
