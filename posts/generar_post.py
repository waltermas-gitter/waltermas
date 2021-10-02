import markdown
import os, sys
from jinja2 import Template, FileSystemLoader, Environment

env = Environment()
env.loader = FileSystemLoader('.')

if len(sys.argv) < 2: 
    print('no hay archivo')
    exit()

archivo = sys.argv[1]
markdownfile = open(archivo, 'r').read()
html = markdown.markdown(markdownfile, extensions=['fenced_code', 'codehilite'])

tmpl = env.get_template('post_template.html')
html_template_string = tmpl.render(markdowntext=html)
 
htmlname = "%s.html" % os.path.splitext(archivo)[0]
template_file = open(htmlname, 'w').write(html_template_string)
