import mistune
import os
from jinja2 import Template

mdparser = mistune.Markdown()

template = None
with open('template/story.html') as f:
  template = Template(f.read())
  f.close()

for mdfilename in os.listdir('md'):
  i = int(mdfilename.split(".")[0])
  mdcontent = open('md/'+mdfilename).read()
  main_html = mdparser(mdcontent)
  with open(str(i)+".html",'w') as f:
    content = template.render(i=i,main_html=main_html)
    f.write(content)
    f.close()
  
