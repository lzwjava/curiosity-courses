import subprocess
from tkinter.constants import NO
from bs4 import BeautifulSoup,Tag
from bs4.element import NavigableString
from latex2svg import latex2svg
import random

def clean_mathjax(soup, name, cls):
    previews = soup.findAll(name, {'class': cls})
    for preview in previews:
        preview.decompose()

def wrap_latex(mathjax, equation = False):
    if equation:
        return mathjax.string
    wrap = '$' + mathjax.string + '$'
    return wrap
 
def wrap_svg(svg, equation = False):
    if equation:
        p = BeautifulSoup('<div style="text-align:center;"></div>', features="lxml")
        p.div.append(svg)
        return p
    else:
        return svg    
        
def to_svg(mathjaxs, equation=False):
    for mathjax in mathjaxs:
        print(mathjax.string)
        wrap = wrap_latex(mathjax, equation=equation)
        if wrap is None:
            continue
        out = {}
        try:
            out = latex2svg(wrap)   
        except subprocess.CalledProcessError as err:
            raise err
            # print(err)
            # continue
        node = BeautifulSoup(out['svg'], features="lxml")
        svg = node.find('svg')
        svg.attrs['style'] = 'vertical-align: middle;'
        p = wrap_svg(svg, equation=equation)
        mathjax.insert_after(p)

def main():    
    file = open('The Feynman Lectures on Physics Vol. I Ch. 13_ Work and Potential Energy (A).html')
    content = file.read()
    
    soup = BeautifulSoup(content, features="lxml")
    clean_mathjax(soup, 'span', 'MathJax')
    clean_mathjax(soup, 'div', 'MathJax_Display')
    clean_mathjax(soup, 'span', 'MathJax_Preview')
    
    mathjaxs = soup.findAll('script', {'type': 'math/tex'})
    to_svg(mathjaxs, equation=False)
    
    mathjaxs = soup.findAll('script', {'type': 'math/tex; mode=display'})   
    to_svg(mathjaxs, equation=True)
    
    output_file = open('out.html', 'w')
    output_file.write(soup.prettify())
    output_file.close()

main()

     