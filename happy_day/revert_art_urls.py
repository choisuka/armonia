# -*- coding: utf-8 -*-
"""
썸네일 URL을 원래 원본 URL로 되돌리기
commons/thumb/{a}/{ab}/{file}/{size}px-{file}  →  commons/{a}/{ab}/{file}
"""
import re

def revert_thumb(html):
    def replace(m):
        url = m.group(1)
        # /thumb/{a}/{ab}/{filename}/{size}px-{filename}
        pat = r'(https://upload\.wikimedia\.org/wikipedia/commons/)thumb/([0-9a-f]/[0-9a-f]{2}/)(.+\.(?:jpg|jpeg|png))/\d+px-.+\.(?:jpg|jpeg|png)'
        tm = re.match(pat, url, re.IGNORECASE)
        if tm:
            base, hashpath, filename = tm.group(1), tm.group(2), tm.group(3)
            return f"img:'{base}{hashpath}{filename}'"
        return m.group(0)

    pattern = r"img:'(https://upload\.wikimedia\.org/wikipedia/commons/thumb/[^']+)'"
    return re.sub(pattern, replace, html)

for fname in ['index.html', 'monthly.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    html = revert_thumb(html)
    count = len(re.findall(r"img:'https://upload\.wikimedia\.org/wikipedia/commons/[0-9a-f]", html))
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"{fname}: reverted, {count} original URLs")

print("Done!")
