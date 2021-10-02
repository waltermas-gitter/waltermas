#!/usr/bin/env python3 

import os
from jinja2 import Template, FileSystemLoader, Environment
import glob


env = Environment()
env.loader = FileSystemLoader('.')

def main():
    posteos = [os.path.splitext(os.path.basename(f))[0] for f in glob.glob("posts/*.html")]
    posteos.remove('post_template')
    posteos.remove('base')
    print(posteos)

    tmpl = env.get_template('index_template.html')
    html_template_string = tmpl.render(posteos=posteos)
    template_file = open("index.html", 'w').write(html_template_string)

if __name__ == '__main__':
    main()
