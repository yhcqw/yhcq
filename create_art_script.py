import create_art_commands
import ebooklib
from ebooklib import epub
import shutil
import os
import subprocess
#create_art_commands.retrieve_OEBPS()

# Specify the path to your EPUB file
#epub_file = "book/1999-2010.epub"
#book = create_art_commands.list_items_in_epub("book/1999-2010.epub") #extract all the OEBPS html files to epub_items_list.txt#index1999-2010,.txt is an updated version with full authors

#(https://www.koreatimes.co.kr/www/opinon/2022/05/197_329735.html No Hate Comments Day)
#category:wenge,mao,society,people,mis,foreignhistory,discussion

#compare your article with index199902010.txt and check its location in OEBPS
"""

files = ["html/society-200812xinyu.html"]
for file in files:
    new = file.split("html/")[1]
    create_art_commands.process_copy_and_past_html(file,new)
    file_path = os.path.abspath(new)
    subprocess.run(['open',file_path])

"""
#create_art_commands.rewrite_index("index.html")
#the new index file is index_temp.html, check and change the name to index.html

shutil.copy("index.html","index_temp.html")
date_list = [f"{year:04d}{month:02d}" for year in range(1999, 2011) for month in range(1, 13)]
years,categories,titles,authors,contents = create_art_commands.extract_notes_from_pages("pages.txt")

manual_name = "manual_addition.txt"
#add the extracted text from the OEBPS article to the template
main_before,main_after = create_art_commands.extract_template("template.html")
with open(manual_name,"w") as manual:
  for i in range(0,len(years)):
    print(f"{i}: {years[i]} {categories[i]} {titles[i]} {authors[i]}")
    if years[i] in date_list:
       aut_pinyin = create_art_commands.author_pinyin(authors[i])
       #create an html file to be uploaded
       newhtmlname = f"html/{categories[i]}-{years[i]}{aut_pinyin}.html"
       if os.path.exists(newhtmlname):
          print(f"File {newhtmlname} already exists.")
#          continue
       else:
          location = create_art_commands.retrieve_OEBPS(years[i],titles[i],authors[i],"index1999-2010.txt")
          text = create_art_commands.extract_OEBPS_content(str(location))
          create_art_commands.make_html(main_before,main_after,text,newhtmlname,years[i],titles[i],authors[i])
       value = create_art_commands.check_for_repetition(years[i],titles[i],authors[i],"index_temp.html")
       if value == True:
          create_art_commands.update_index_file(years[i],categories[i],titles[i],authors[i],contents[i],newhtmlname,"index_temp.html") #add new article to index.html
       else:
          print(f'{years[i]} {titles[i]} {authors[i]} already written')
#          continue
    else:
       aut_pinyin = create_art_commands.author_pinyin(authors[i])
       #create an html file to be uploaded
       newhtmlname = f"html/{categories[i]}-{years[i]}{aut_pinyin}.html"
       if os.path.exists(newhtmlname):
           print(f"File {newhtmlname} already exists.")
#           continue
       else:
          text = "\n\n\n"
          create_art_commands.make_html(main_before,main_after,text,newhtmlname,years[i],titles[i],authors[i])
       value = create_art_commands.check_for_repetition(years[i],titles[i],authors[i],"index_temp.html")
       if value == True:
          create_art_commands.update_index_file(years[i],categories[i],titles[i],authors[i],contents[i],newhtmlname,"index_temp.html") #add new article to index.html
          manual.write(f"{years[i]} {categories[i]} {titles[i]} {authors[i]} {newhtmlname}\n")
       else:
          print(f'{years[i]} {titles[i]} {authors[i]} already written')
#          continue

# Check if file is empty
if os.path.getsize(manual_name) != 0:
    print("Please add the following manually: ")
    subprocess.run(['cat', manual_name])

"""
#This copy old content to new template
html_files = create_art_commands.list_html_files("oldhtml") #old html files are in the folder html
for html in html_files:
    create_art_commands.combinefile('template.html',f'oldhtml/{html}',f'html/{html}')

"""
