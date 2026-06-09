# -*- coding: utf-8 -*-
"""
Google Art Project / HD 초대용량 이미지만 썸네일로 교체
나머지는 원본 URL 유지
"""

# 원본 URL → 대체 URL 매핑
REPLACEMENTS = {
    # clear[0] Seurat 218MB → 썸네일
    'https://upload.wikimedia.org/wikipedia/commons/b/b7/Georges_Seurat_-_A_Sunday_on_La_Grande_Jatte_--_1884_-_Google_Art_Project.jpg':
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Georges_Seurat_-_A_Sunday_on_La_Grande_Jatte_--_1884_-_Google_Art_Project.jpg/800px-Georges_Seurat_-_A_Sunday_on_La_Grande_Jatte_--_1884_-_Google_Art_Project.jpg',

    # clear[2] Botticelli → 썸네일
    'https://upload.wikimedia.org/wikipedia/commons/0/0b/Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg':
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg/800px-Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg',

    # partlyCloudy[2] Millet → 썸네일
    'https://upload.wikimedia.org/wikipedia/commons/1/1f/Jean-Fran%C3%A7ois_Millet_-_Gleaners_-_Google_Art_Project_2.jpg':
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Jean-Fran%C3%A7ois_Millet_-_Gleaners_-_Google_Art_Project_2.jpg/800px-Jean-Fran%C3%A7ois_Millet_-_Gleaners_-_Google_Art_Project_2.jpg',

    # cloudy[2] & drizzle[1] Klimt 37MB → 소용량 파일
    'https://upload.wikimedia.org/wikipedia/commons/4/40/The_Kiss_-_Gustav_Klimt_-_Google_Cultural_Institute.jpg':
    'https://upload.wikimedia.org/wikipedia/commons/f/f3/Gustav_Klimt_016.jpg',

    # drizzle[2] Starry Night 205MB → 소용량 파일
    'https://upload.wikimedia.org/wikipedia/commons/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg':
    'https://upload.wikimedia.org/wikipedia/commons/c/cd/VanGogh-starry_night.jpg',

    # rainy[0] Caillebotte → 썸네일
    'https://upload.wikimedia.org/wikipedia/commons/1/17/Gustave_Caillebotte_-_Paris_Street%3B_Rainy_Day_-_Google_Art_Project.jpg':
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Gustave_Caillebotte_-_Paris_Street%3B_Rainy_Day_-_Google_Art_Project.jpg/800px-Gustave_Caillebotte_-_Paris_Street%3B_Rainy_Day_-_Google_Art_Project.jpg',

    # snowy[0] Bruegel → 썸네일
    'https://upload.wikimedia.org/wikipedia/commons/d/d8/Pieter_Bruegel_the_Elder_-_Hunters_in_the_Snow_%28Winter%29_-_Google_Art_Project.jpg':
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Pieter_Bruegel_the_Elder_-_Hunters_in_the_Snow_%28Winter%29_-_Google_Art_Project.jpg/800px-Pieter_Bruegel_the_Elder_-_Hunters_in_the_Snow_%28Winter%29_-_Google_Art_Project.jpg',

    # snowy[1] Monet Magpie → 소용량 파일
    'https://upload.wikimedia.org/wikipedia/commons/7/78/Claude_Monet_-_The_Magpie_-_Google_Art_Project.jpg':
    'https://upload.wikimedia.org/wikipedia/commons/a/a5/Claude_Monet_-_La_Pie.jpg',

    # cloudy[1] & thunderstorm[1] Night Watch HD → 소용량 파일
    'https://upload.wikimedia.org/wikipedia/commons/5/5a/The_Night_Watch_-_HD.jpg':
    'https://upload.wikimedia.org/wikipedia/commons/9/94/The_Nightwatch_by_Rembrandt_-_Rijksmuseum.jpg',
}

for fname in ['index.html', 'monthly.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    count = 0
    for old, new in REPLACEMENTS.items():
        if old in html:
            html = html.replace(old, new)
            count += 1
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'{fname}: {count} URLs replaced')

print('Done!')
