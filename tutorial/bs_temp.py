from bs4 import BeautifulSoup
import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)
print(soup.find('a',class_='sister').string)
#for a in soup.find("a", class_="sister"):
 #   print(a)
#for sibling in soup.p.next_siblings:
#    print(repr(sibling))
#print(soup.p.prev_sibling)
#print(soup.p.next_sibling.next_sibling)
#p = soup.p
#content = soup.head.title.string
#print(content)
#for parent in  content.parents:
  #  print (parent.name)
#for child in soup.stripped_strings :
#    print(child)
#print(soup.p.children)
#for child in soup.head.children:
 #   print(child)
#soup = BeautifulSoup(open('index.html'))
#print(soup.prettify())
#print(soup.head.contents)
#print(soup.p.contents[0])


#if type(soup.a.string)==bs4.element.Comment:
    
 #   print (soup.a.string)