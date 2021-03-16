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
        
def clean_script(soup):
    scripts = soup.findAll('script')
    for s in scripts:
        s.decompose()    

def wrap_latex(mathjax, equation = False):
    wrap = ''
    if equation:
        wrap = mathjax.string
    else:
        wrap = '$' + mathjax.string + '$'
    wrap = wrap.replace('label', 'tag')
    return wrap
 
def wrap_svg(svg, equation):
    if equation:
        p = BeautifulSoup(f'<div style="text-align:center;"></div>', features="lxml")
        p.div.append(svg)
        return p.div
    else:
        return svg

def to_svg(mathjaxs, equation=False):
    if equation:
        svg_prefix = 'eq_'
    else:
        svg_prefix = 'in_'
    i = 0
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
            
        f = open(f'svgs/{svg_prefix}{i}.svg', 'w')
        f.write(out['svg'])
        f.close()
        # i += 1
        
        node = BeautifulSoup(out['svg'], features="lxml")        
        svg = node.find('svg')
        svg.attrs['style'] = 'vertical-align: middle;'
        
        # node = BeautifulSoup('<img>', features="lxml")
        # img = node.find('img')
        # img.attrs['src'] = f'./svgs/{svg_prefix}{i}.svg'
        # img.attrs['style'] = 'vertical-align: middle; margin: 0.5em 0;'
        
        svg = node.find('svg')
        svg.attrs['style'] = 'vertical-align: middle;'
        p = wrap_svg(svg, equation)
        mathjax.insert_after(p)
        # if i%3 == 0:            
            
        # print(out['width'])
        # print(out['height'])
        i +=1
        
        

def main():    
    file = open('The Feynman Lectures on Physics Vol. I Ch. 13_ Work and Potential Energy (A).html')
    content = file.read()
    
    soup = BeautifulSoup(content, features="lxml")
    clean_mathjax(soup, 'span', 'MathJax')
    clean_mathjax(soup, 'div', 'MathJax_Display')
    clean_mathjax(soup, 'span', 'MathJax_Preview')
    clean_mathjax(soup,  'p', 'p')
    
    # mathjaxs = soup.findAll('script', {'type': 'math/tex'})
    # to_svg(mathjaxs, equation=False)
    
    mathjaxs = soup.findAll('script', {'type': 'math/tex; mode=display'})   
    to_svg(mathjaxs, equation=True)
    
    clean_script(soup)
    
    output_file = open('out.html', 'w')
    output_file.write(soup.prettify())
    output_file.close()
    
    

main()

     