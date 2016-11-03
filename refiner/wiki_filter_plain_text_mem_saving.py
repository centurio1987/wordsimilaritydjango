# coding: utf-8
import re
from xml.etree.ElementTree import parse, ElementTree

def findTextTag(revision_tag):
    yield revision_tag.find('{http://www.mediawiki.org/xml/export-0.10/}text'))

def extractRevisionTag(page_tags):
    revision_tags = page_tag.findall('{http://www.mediawiki.org/xml/export-0.10/}revision')
    for revision_tag in revision_tags:
        yield revision_tag

def setParsingWikiXml(file_name):

    tree = parse(file_name)
    root = tree.getroot()
    page_tags = root.findall('{http://www.mediawiki.org/xml/export-0.10/}page')
    text_tags = []

    for text_tag in findTextTag(extractRevisionTag(page_tags)):
        text_tags.append(text_tag)

    yield text_tags

def refineTextTag(text_tags):
    compiler = re.compile(r'\w+')
    for text_tag in text_tags:
        refined_text_tag_list = compiler.findall(str(text_tag.text))
        refined_text_tag = ' '.join(refined_list)
        yield refined_text_tag

def refineText(text_tags):
    for refined_text_tag in refineTextTag(text_tags):
        yield refined_text_tag

def saveText(refined_text):
    refined_text.encode('utf-8')

    with open('./refined_text_full.txt', 'a', encoding='utf-8') as f:
        f.write(refined_text)

if __name__ == "__main__":
    # ##### 텍스트 태그 추출
    text_tags = setParsingWikiXml("./enwiki-latest-pages-articles.xml")

    # ##### 플레인 텍스트 정제
    for refined_text in refineText(text_tags)
        # ##### 텍스트 저장
        saveText(refined_text)
