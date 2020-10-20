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
  title = mdcontent.split("\n",2)[0].split("#")[1].strip()
  print(i,title)
  main_html = mdparser(mdcontent)
  with open(str(i)+".html",'w') as f:
    content = template.render(i=i,main_html=main_html,title=title)
    f.write(content)
    f.close()
  
