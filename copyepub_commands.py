import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
import os,sys
import numpy as np
import os,sys,string
from sys import*
import pinyin
import re
import copyepub_commands

year=np.arange(1999,2017)
mth=np.arange(1,13)
mth= mth.astype(str)
# Use np.char.zfill to pad the strings with zeros
mth= np.char.zfill(mth, 2)
magnum=[]

for i in year:
    for j in mth:
        magnum.append(f'{i}{j}')

def clean_name(name):
    special=["“","”","<",">","《","》","：","（","）","(",")",":","?","-"," ","？",",","，",'"']
#    translation_table = str.maketrans('', '', ''.join(special))
#    new_name = name.translate(translation_table)
    new_name = re.sub(r'[^\w\s]', '', name)
    return new_name

def read_until_ends(file_path):
    linenum=[]
    with open(file_path, 'r') as file:
        for i,line in enumerate(file):
            line=line.replace("\n","")
            line=line.replace(" ","")
            if line in magnum:
                linenum.append(i+1)
            if "<!--ends-->" in line:
                linenum.append(i+1)
                break
    return linenum


def extract_lines(input_file,line_ranges):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    extracted_lines = []
    for start, end in line_ranges:
        extracted_lines.extend(lines[start-1:end])  # Convert to 0-based index
    return extracted_lines

    
def extractinfo(text):
    content=[]
    maga=str(text[0].replace("\n",""))
    maga=maga.replace(" ","")
    if text[1].find("(") != -1:
       title=str(text[1].split("(")[0])
    elif text[1].find("[") != -1:
       title=str(text[1].split("[")[0])
    if "(" in text[1] and ")" in text[1]:
        author =str(text[1].split("(")[1].split(")")[0])
    else:
        author = None
    if author is not None:
       if author.find(" ")==-1:
          authorpy=pinyin.get(author,format="strip")
       else:
          authorpy=pinyin.get(author.split()[0],format="strip")
    else:
        author = " "
        authorpy = " "
    cate=str(text[1].split("[")[1].split("]")[0])
    for i in range(2,len(text)):
        content.append(text[i])
    return maga,title,author,authorpy,cate,content


def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), "html.parser")
    text_lines = []
    for para in soup.find_all("p"):
        text_lines.append(str(para) + '\n')
    return text_lines
#    return "".join(text_lines)  

def txtfile(text,maga,title,author,authorpy,category):
    newfile=f"{category}-{maga}{authorpy.replace(" ","")}.html"
    with open("template.html","r") as Template,open(f"html/{newfile}","w") as texfile:
       template=Template.readlines()
       for i in range(0,len(template)):
           if template[i].find("content begins")>=0:
              linebegin=i
           if template[i].find("content ends")>=0:
              lineend=i    
       for i in range(0,linebegin+1):
           if template[i].find("TITLE")>=0:
              template[i]=template[i].replace("TITLE",title)
           if template[i].find("MAGAZINENUM")>=0:
              year = maga[:4]
              month = maga[4:]
              template[i]=template[i].replace("MAGAZINENUM",f"{year}年第{int(month)}期")
           if template[i].find("AUTHOR")>=0:
              template[i]=template[i].replace("AUTHOR",author)
           texfile.write(template[i])
       for j in text:
           texfile.write(j)
       for i in range(lineend,len(template)):
           texfile.write(template[i])

       return f"{maga} {title} {author} html/{newfile}"

def indexfilelines(indexfile):
    with open(indexfile, "r", encoding="utf-8") as file:
       html_content = file.readlines()
    
    contentbegin = []
    
    for line_num, line in enumerate(html_content, start=1):
        for match in re.finditer(r'<!--(.*?)-->', line):
            comment = match.group(0)
            if "content begins" in comment:
                contentb = line_num
            if "content ends" in comment:
                contente = line_num
            if "wenge-begins" in comment:
                wengeb= line_num
            if "wenge-ends" in comment:
                wengee = line_num
            if "mao-begins" in comment:
                maob = line_num
            if "mao-ends" in comment:
                maoe = line_num
            if "society-begins" in comment:
                societyb = line_num
            if "society-ends" in comment:
                societye = line_num
            if "people-begins" in comment:
                peopleb = line_num
            if "people-ends" in comment:
                peoplee = line_num
            if "foreign-begins" in comment:
                foreignb = line_num
            if "foreign-ends" in comment:
                foreigne = line_num
            if "mis-begins" in comment:
                misb = line_num
            if "mis-ends" in comment:
                mise = line_num
            if "discussion-begins" in comment:
                discussionb = line_num
            if "discussion-ends" in comment:
                discussione = line_num
    return contentb,contente,wengeb,wengee,maob,maoe,peopleb,peoplee,foreignb,foreigne,societyb,societye,misb,mise,discussionb,discussione

def extract_years(input_file, linebegin, lineend):
    with open(input_file, 'r', encoding="utf-8") as file:
        lines = file.readlines()
    
    years = []
    for line_num, line in enumerate(lines[linebegin-1:lineend], start=linebegin):
        # Find comments of the format <!--year-->200908:
        match = re.search(r'<!--year-->(\d{6}):', line)
        if match:
            year = match.group(1)
            years.append((line_num, year))
    
    return years

def rewritecontent(content):
    new_content = []
    for line in content:
        # Check and replace content within parentheses
        if '(' in line and ')' in line:
            match = re.search(r'\((.*?)\)', line)
            if match:
                parenthesis_content = match.group(1)
                if "html" in parenthesis_content:
                    formatted_url = f'<a href="https://yhcqw.github.io/yhcq/{parenthesis_content}" target="_blank">'
                    line = line.replace(f'({parenthesis_content})', f'{formatted_url}')
        if 'link' in line:
            link=line.replace("link:","")
            link=link.replace('\n','')
            line=line.replace("link:",f'<a href="{link}" target="_blank">')
        new_content.append(line)
    return new_content
