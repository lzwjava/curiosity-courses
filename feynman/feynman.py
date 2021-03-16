import subprocess
from tkinter.constants import NO
from bs4 import BeautifulSoup,Tag
from bs4.element import NavigableString
from latex2svg import latex2svg
import random

file = open('The Feynman Lectures on Physics Vol. I Ch. 13_ Work and Potential Energy (A).html')
content = file.read()

soup = BeautifulSoup(content, features="lxml")

previews = soup.findAll('span', {'class': 'MathJax'})
for preview in previews:
    preview.decompose()

previews = soup.findAll('div', {'class': 'MathJax_Display'})
for preview in previews:
    preview.decompose()

previews = soup.findAll('span', {'class': 'MathJax_Preview'})
for preview in previews:
    preview.decompose()

mathjaxs = soup.findAll('script', {'type': 'math/tex; mode=display'})

def wrap_latex(str, equation = False):
    if equation:
        return str
    wrap = '$' + mathjax.string + '$'
    # if 'frac' in mathjax.string:
    #     wrap = '$' + mathjax.string + '$'
    if 'FLP' in mathjax.string:
        return None
    elif 'Fig' in mathjax.string:
        return None
    elif 'eps' in mathjax.string:
        return None
    return wrap
    

for mathjax in mathjaxs:
    
    print(mathjax.string)
    wrap = wrap_latex(mathjax.string, equation=True)
    if wrap is None:
        continue
    
    out = {}
    try:
        out = latex2svg(wrap)   
    except subprocess.CalledProcessError as err:
        print(err)
        continue
    # print(out)
    node = BeautifulSoup(out['svg'], features="lxml")
    svg = node.find('svg')
    svg.attrs['style'] = 'vertical-align: middle;'
    mathjax.insert_after(svg)
    # print(out['svg'])
    # break
    # mathjax.replaceWith(out['svg'])    
    
    # print(dir(mathjax))
    # break
    
    # out = latex2svg(wrap)    
    # print(out['svg'])

# print(len(soup.contents))
    
output_file = open('out.html', 'w')
output_file.write(soup.prettify())
output_file.close()
# print(soup.contents)

# out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
# print(out['depth'])
# print(out['svg'])

# svg = open('1.svg', 'w')
# svg.write(out['svg'])
# svg.close()

