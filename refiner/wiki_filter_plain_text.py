# coding: utf-8
import re
from xml.etree.ElementTree import parse, ElementTree

# ##### 텍스트 태그 추출

tree = parse("./enwiki-latest-pages-articles.xml")


root = tree.getroot()
page_tags = root.findall('{http://www.mediawiki.org/xml/export-0.10/}page')
text_tags = []

for page_tag in page_tags:
    revision_tags = page_tag.findall('{http://www.mediawiki.org/xml/export-0.10/}revision')
    for revision_tag in revision_tags:
        text_tags.append(revision_tag.find('{http://www.mediawiki.org/xml/export-0.10/}text'))


# ##### 플레인 텍스트 정제

compiler = re.compile(r'\w+')

refined_list = []

def text_tag_gen(text_tags):
    for text_tag in text_tags:
        compiled = compiler.findall(str(text_tag.text))
        compiled_text = ' '.join(compiled)
        yield compiled_text

for result in text_tag_gen(text_tags):
    refined_list.append(result)


total_text = ' '.join(refined_list)
total_text.encode('utf-8')

with open('./refined_text_full.txt', 'w', encoding='utf-8') as f:
    f.write(total_text)
