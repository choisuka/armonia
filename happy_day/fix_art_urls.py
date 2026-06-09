# -*- coding: utf-8 -*-
"""
Wikipedia Commons 그림 URL을 원본(수 MB~수십 MB)에서
썸네일(800px, 빠른 로드)로 변환
"""
import re

def convert_to_thumb(html, width=800):
    def replace(m):
        url = m.group(1)
        # commons/{a}/{ab}/{filename}.jpg  → commons/thumb/{a}/{ab}/{filename}.jpg/{width}px-{filename}.jpg
        pat = r'(https://upload\.wikimedia\.org/wikipedia/commons/)([0-9a-f]/[0-9a-f]{2}/)(.+\.(?:jpg|jpeg|png))'
        tm = re.match(pat, url, re.IGNORECASE)
        if tm:
            base, hashpath, filename = tm.group(1), tm.group(2), tm.group(3)
            new_url = f"{base}thumb/{hashpath}{filename}/{width}px-{filename}"
            return f"img:'{new_url}'"
        return m.group(0)

    pattern = r"img:'(https://upload\.wikimedia\.org/wikipedia/commons/[^']+)'"
    return re.sub(pattern, replace, html)

for fname in ['index.html', 'monthly.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    before = len(re.findall(r"img:'https://upload\.wikimedia", html))
    html = convert_to_thumb(html)
    after  = len(re.findall(r"img:'https://upload\.wikimedia\.org/wikipedia/commons/thumb/", html))
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"{fname}: {before} URLs → {after} converted to thumb")

print("Done!")
