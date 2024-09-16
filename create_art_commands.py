import glob
import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
import os,sys
import numpy as np
import os,sys,string
from sys import*
import pinyin
import re
from datetime import datetime

# Function to clean the title by removing unwanted symbols and extra spaces
def clean_title(title):
    # Replace various quotation marks with a space
    cleaned_title = re.sub(r'[“”"\'《》()（）:：]+', ' ', title)
    # Remove leading and trailing spaces
    cleaned_title = cleaned_title.replace(" ","")
    return cleaned_title

def update_index_file(year,cate,title,author,content,newhtmlname,index_file):
     first_line = f'<a href="https://yhcqw.github.io/yhcq/{newhtmlname}"target="_blank"><i>{title}({author})</i></a>({year})</br>\n '
     pattern = r'[\(（](http[^\s\)）]+)[\)）]'
     def replace_link(match):
        url = match.group(1)
        return f'<a href="{url}" target="_blank">'
     content = re.sub(pattern, replace_link, content)
     all_content = first_line+'\n'+content+"\n"+'<hr class="linebreak">\n'
     cate_item = ["wenge-begins","mao-begins","society-begins","people-begins","foreign-begins"," mis-begins","discussion-begins"]
     cate_line = []
     today = datetime.today()
     formatted_date = today.strftime("%Y年%-m月%-d日")
     with open(index_file,"r") as indexfile:
         lines = indexfile.readlines()
         for i,line in enumerate(lines):
             if "最后更新" in line:
                 lines[i] = f"最后更新：{formatted_date}</br>\n"
         for cat in cate_item:
            for i,line in enumerate(lines):
                if cat in line:
                    cate_line.append(i+7)
            continue
     if cate == "wenge":
        lines.insert(cate_line[0], all_content + '\n')
     elif cate == "mao":
        lines.insert(cate_line[1], all_content + '\n')
     elif cate == "society":
        lines.insert(cate_line[2], all_content + '\n')
     elif cate == "people":
        lines.insert(cate_line[3], all_content + '\n')
     elif cate == "foreign":
        lines.insert(cate_line[4], all_content + '\n')
     elif cate == "mis":
        lines.insert(cate_line[5], all_content + '\n')
     elif cate == "discussion":
        lines.insert(cate_line[6], all_content + '\n')
     with open(index_file, "w", encoding='utf-8') as newfile:
        newfile.writelines(lines)  # Use writelines() on the file object, not on the list
   
def check_for_repetition(year,title,author,indexhtml):
    with open(indexhtml,"r") as index_html:
         lines = index_html.readlines()
         for line in lines:
             if (line.find('<a href="https://yhcqw.github.io/yhcq') != -1 and line.find(year) != -1 and line.find(title) != -1) or (line.find('<a href="https://yhcqw.github.io/yhcq') != -1 and line.find(year) != -1 and line.find(author) != -1):
                 return False
    return True
          
          
def extract_OEBPS_content(html_file_path):
    html_file_path = f'book/OEBPS/{html_file_path}'
    with open(html_file_path, 'r', encoding='utf-8') as file:
        # Read and parse the HTML file
        html_file_path = f'book/OEBPS/{html_file_path}'
        soup = BeautifulSoup(file, 'html.parser')
        
        # Find the <h2> tag
        h2_tag = soup.find('h2')
        if not h2_tag:
            return "No <h2> tag found in the HTML file."

        # Get all content after <h2> tag
        content = h2_tag.find_all_next()
        
        # Convert the content to string, excluding the last 4 lines
        extracted_lines = []
        for item in content:
            if item.name:
                extracted_lines.append(str(item))
        
        if len(extracted_lines) < 4:
            return "Not enough content to exclude the last 4 lines."

        # Join lines and exclude the last 4 lines
        extracted_text = '\n'.join(extracted_lines)
        return extracted_text

def retrieve_OEBPS(year,title,author,indexfile):
    yr = year[:4]        # First 4 characters for the year
    issue_number = year[4:]  # Last 2 characters for the issue number
    # Remove leading zero from issue number if present and format the output
    title = clean_title(title)
    formatted_issue = f"{yr}年第{int(issue_number)}期"
    print(f"Retrieving {yr}年第{int(issue_number)}期 {title}")
    with open("index1999-2010.txt", "r", encoding="utf-8") as indexfile:
       lines = indexfile.readlines()  # Read all lines at once
       location = None
#       linenumber = None
    # Loop through lines to find the required information
       for i, line in enumerate(lines):
        # Extract parts from each line
           title_from_index_1999 = clean_title(line.split()[2])
           magnum = line.split()[1]
           if "作者:" in line:
               author_from_index_1999 = line.split("作者:")[1]
           else:
               author_from_index_1999 = "No author"
        # Perform the comparison to find the location
           if (formatted_issue == magnum and title == title_from_index_1999) or (formatted_issue == magnum and author.split()[0] in author_from_index_1999.split()[0]):
              location = line.split()[0]
#              linenumber = i - 1
              break  # Stop loop once location is found
       if location:
          extract_OEBPS_content(str(location))
          return location
       else:
          return f"X:{formatted_issue} {title}"
    
def author_pinyin(author):
    authorpy=pinyin.get(author.split()[0],format="strip")
    return authorpy
    
def extract_notes_from_pages(pagesfile):

    def extract_content(lines):
        year = lines[0].strip()
        pattern = r'\[(.*?)\](.*)\s*[（(](.*?)[）)]$'
        match = re.match(pattern, lines[1])
        if match:
           category = match.group(1).strip()  # Extract category
           title = match.group(2).strip()     # Extract title
           author = match.group(3).strip()    # Extract author
           content = []
           for i in range(2,len(lines)):
              if lines[i].find("SQL") == -1:
#                 content = content + f'{lines[i]}'+"\n"
                 if len(lines[i]) != 1:
                    lines[i] = lines[i].replace("\n","")
                    content.append(f'{lines[i]}</br>')
              else:
                 break
           content_str = "\n".join(content)
        else:
            print(f'{line[0].replace("\n","")} {line[1]} not extracted')
       
        return year,category,title,author,content_str
  
    linebegin= []
    lineend = []
    years = []
    categories = []
    titles = []
    authors = []
    contents = []

    with open(pagesfile, 'r', encoding='utf-8') as file:
         lines = file.readlines()
         
    for index, line in enumerate(lines, start=0):
        if line.strip().isdigit() and len(line.strip()) == 6:
            linebegin.append(index) #continue here line end
    
    for i in range(1,len(linebegin)):
        lineend.append(linebegin[i]-1)
        
    lineend.append(len(lines)-1)
# Iterate over the lines and check for the year-month pattern
    for i in range(0,len(linebegin)):
        if (lines[linebegin[i]+1].find("[") != -1 and lines[linebegin[i]+1].find("]") != -1):
            year,category,title,author,content = extract_content(lines[linebegin[i]:lineend[i]])
            years.append(year)
            categories.append(category)
            titles.append(title)
            authors.append(author)
            contents.append(content)
    return years,categories,titles,authors,contents

    
    

#extract all the OEBPS html files
def list_items_in_epub(epub_file): #write all the path of each html file and the title
    bookinfo=[]
    book = epub.read_epub(epub_file)
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
    for item in items:
       file_path = getattr(item, 'file_name', 'unknown')
    # Access item content (HTML content in bytes)
       content = item.get_content()
    # Optionally, you can decode content if needed
       content_str = content.decode('utf-8')
       soup = BeautifulSoup(content_str, 'html.parser')
       h2_tag = soup.find('h2')
       if h2_tag:
          title = h2_tag.get_text()
          bookinfo.append(f"{file_path} {title}")
    output_file = "epub_items_list.txt"
    with open(output_file, 'w', encoding='utf-8') as file:
       for i in bookinfo:
          file.write(f"{i}\n")
    return bookinfo

def make_html(main_before,main_after,text,newhtmlname,yearmth,title,author):
    year = yearmth[:4]
    month = int(yearmth[4:])  # Convert month part to an integer
    formatted_year = f"{year}年第{month}期"
    line = f'<div style="text-align: center;">\n<span style="font-family: arial; sans-serif; font-size: 16pt">\n<b>{title}</b></br>\n</span>\n<span style="font-family: arial; sans-serif; font-size: 12pt">\n{author}</br>\n炎黄春秋：{formatted_year}</br></br>\n</div>\n</span>\n<span style="font-family: arial; sans-serif; font-size: 12pt; text-align: left;">\n\n'
    
    with open(newhtmlname, 'w', encoding='utf-8') as file:
        file.write(main_before + line + text + main_after)
    print(f"{newhtmlname} written")

    import re

def process_copy_and_past_html(file_path,new_file_name):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Extract content between specified tags
    start_tag = '<span style="font-family: arial; sans-serif; font-size: 12pt; text-align: left;">'
    end_tag = '<a href="https://yhcqw.github.io/yhcq/">返回主目录</a>'

    # Use regex to extract the text between start_tag and end_tag
    match = re.search(f"{re.escape(start_tag)}(.*?){re.escape(end_tag)}", content, re.DOTALL)

    if match:
        extracted_text = match.group(1)  # Extract the matched text
        
        # Process each line in the extracted content
        processed_lines = []
        for line in extracted_text.splitlines():
            # Remove spaces between words
            line = line.replace(" ", "")
            
            # Check if the line contains <h5> and </h5>
            if "<h5>" in line and "</h5>" in line:
                processed_lines.append(line + "<br>\n")
            else:
                processed_lines.append(line + "<br><br>\n")
        
        # Join the processed lines back together
        processed_text = ''.join(processed_lines)

        # Replace the old content with new processed content
        new_content = content.replace(extracted_text, processed_text)

        # Write the new content to new.html
        with open(new_file_name, "w", encoding="utf-8") as new_file:
            new_file.write(new_content)
    else:
        print("Specified tags not found in the file.")



    
def extract_template(templatefile):
    with open(templatefile, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Initialize variables
    main_before = ""
    main_after = ""
    inside_main = False

    # Iterate through lines to separate content
    for line in lines:
        if '<main>' in line:
            main_before += line  # this adds up the lines before <main>
            inside_main = False  #line after main is set to False
            continue
        if '返回主目录' in line:
            main_after += line  # main_after only has the line 返回主目录
            inside_main = True #line after is set to True
            continue
        if inside_main:
            main_after += line  # Concatenate line to main_after string
        else:
            main_before += line  # Concatenate line to main_before string
            
    return main_before,main_after
    
def extract_main_content(articlehtml):
    with open(articlehtml, 'r', encoding='utf-8') as file:
        artlines = file.readlines()
    
    main_content = ""
    inside_main = False
    
    # Iterate through lines to extract content between <main> and </main>
    for artline in artlines:
        if '<main>' in artline:
            inside_main = True  # Start capturing after <main>
            continue  # Skip the line containing <main>
        if '返回主目录' in artline:
            inside_main = False  # Stop capturing before </main>
            continue  # Skip the line containing </main>
        if inside_main:
            main_content += artline  # Concatenate line to main_content string
    
    return main_content


"""
def extract_main_content(articlehtml):
    with open(articlehtml, 'r', encoding='utf-8') as file:
        artlines = file.readlines()
    
    main_content = ""
    inside_art = False
    
    # Iterate through lines to extract content between <main> and 返回主目录
    for artline in artlines:
        if 'content begins' in artline:
            inside_art = True  # Start capturing after content begins
            continue  # Skip the line containing content begins
        if '返回主目录' in artline:
            inside_art = False  # Stop capturing before 返回主目录
            continue  # Skip the line containing 返回主目录
        if 'content ends' in artline:
            continue  # Skip the line containing content ends
        if inside_art:
            main_content += artline  # Concatenate line to main_content string
    
    return main_content
"""


def combinefile(templatefile,articlehtml,newfilename):
    main_before,main_after = extract_template(templatefile)
    main_content = extract_main_content(articlehtml)
    new_content = main_before+main_content+main_after
    with open(newfilename, 'w', encoding='utf-8') as file:
        file.write(new_content)
        
        
def list_html_files(directory):
    # Create the search pattern
    pattern = os.path.join(directory, '*.html')
    
    # Use glob to find all files matching the pattern
    html_files = glob.glob(pattern)
    
    # Extract filenames from the full paths
    html_files = [os.path.basename(file) for file in html_files]
    
    return html_files


def rewrite_index(original_file):
    with open(original_file, 'r', encoding='utf-8') as old_file:
        old_index = old_file.readlines()
    yearline = []
    for i,line in enumerate(old_index):
        if "<!--year-->" in line:
            yearline.append(i)
        if 'mis-ends' in line:
            yearline.append(i)
    for i in range(0,len(yearline)-1):
        extracted_lines = old_index[yearline[i]:yearline[i+1]]
        for j in range(1,len(extracted_lines)):
            match = re.search(r'<!--year-->(.*?):</br>', extracted_lines[0])
            year = match.group(1)
            old_index[yearline[i]] = ""
            if old_index[yearline[i]+j].startswith('<a href="https://yhcqw.github.io/yhcq'):
               old_index[yearline[i]+j] = extracted_lines[j].replace('">', '"><i>').replace('</a>', f'</i></a>({year})')
        with open("new.html", 'w', encoding='utf-8') as new_file:
            new_file.writelines(old_index)
    
    

