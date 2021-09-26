#!/usr/bin/env python3 

import os
from jinja2 import Template, FileSystemLoader, Environment
import mistune

env = Environment()
env.loader = FileSystemLoader('.')

def main():
    markdownfile = open("markdown-example.md", 'r').read()
    mistuneado = mistune.markdown(markdownfile)
    tmpl = env.get_template('index_template.html')
    html_template_string = tmpl.render(markdowntext=mistuneado)
    template_file = open("index.html", 'w').write(html_template_string)

if __name__ == '__main__':
    main()
