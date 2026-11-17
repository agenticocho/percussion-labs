#!/usr/bin/env python3
"""Generate index.html from labs.json. Never patch the HTML by hand again."""
import json, re, sys

LABS = json.load(open("labs.json"))["sections"]
HTML = open("index.html").read()
SPRITE = re.search(r'<svg xmlns="http://www.w3.org/2000/svg" style="display:none".*?</svg>', HTML, re.S).group(0)
HEAD = HTML[:HTML.find("<section>")]
TAIL = HTML[HTML.rfind("</section>") + len("</section>"):]

GLYPH = ('<svg class="glyph" aria-hidden="true"><use href="#i-{glyph}"/></svg>')
CARD = ('<a class="card" href="{href}">\n'
        '        ' + GLYPH + '\n'
        '        <div class="num">{num:02d}</div>\n'
        '        <h3 class="name">{name}</h3>\n'
        '        <p class="desc">{desc}</p>\n'
        '        <div class="tags">{tags}</div>\n'
        '        <div class="launch">Launch lab <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" '
        'stroke-width="2"><path d="M3 8h10M9 4l4 4-4 4"/></svg></div>\n'
        '      </a>')

NUMWORDS = {n: w for n, w in zip(
    range(0, 100), "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty Twenty-one Twenty-two Twenty-three Twenty-four Twenty-five Twenty-six Twenty-seven Twenty-eight Twenty-nine Thirty Thirty-one Thirty-two Thirty-three Thirty-four Thirty-five Thirty-six Thirty-seven Thirty-eight Thirty-nine Forty Forty-one Forty-two Forty-three Forty-four Forty-five Forty-six Forty-seven Forty-eight Forty-nine Fifty Fifty-one Fifty-two Fifty-three Fifty-four Fifty-five Fifty-six Fifty-seven Fifty-eight Fifty-nine Sixty".split())}

n = 0
out = []
for sec in LABS:
    count = sum(len(f["cards"]) for f in sec["families"])
    out.append('  <section>\n    <div class="section-head">\n'
               f'      <h2>{sec["title"]}</h2>\n'
               f'      <span>{count} labs · {sec["sub"]}</span>\n    </div>')
    for fam in sec["families"]:
        out.append(f'    <div class="family">{fam["family"]}</div>\n    <div class="grid">')
        for c in fam["cards"]:
            n += 1
            tags = "".join(f'<span class="tag">{t}</span>' for t in c["tags"])
            out.append("      " + CARD.format(num=n, tags=tags, href=c["href"],
                                              glyph=c["glyph"], name=c["name"], desc=c["desc"]))
        out.append('    </div>')
    out.append('  </section>')

body = "\n\n".join(out)
head = re.sub(r'<b>\d+</b><i>Laboratories</i>', f'<b>{n}</b><i>Laboratories</i>', HEAD)
head = re.sub(r'content="\w+ browser-native percussion', f'content="{n} browser-native percussion', head)
import re as _re
def _word(k):
    if k in NUMWORDS: return NUMWORDS[k]
    return NUMWORDS.get(k // 10 * 10, str(k)).replace("-", "") + "-" + NUMWORDS.get(k % 10, str(k % 10))
head = _re.sub(r'<h1>[A-Za-z-]+ percussion', f'<h1>{_word(n)} percussion', head)
head = _re.sub(r'Percussion Labs — [A-Za-z-]+ Interactive', f'Percussion Labs — {_word(n)} Interactive', head)
head = _re.sub(r'· \d+ labs, organised by kind ·', f'· {n} labs, organised by kind ·', head)
open("index.html", "w").write(head + body + TAIL)
print(f"  generated {n} labs across {len(LABS)} sections")
