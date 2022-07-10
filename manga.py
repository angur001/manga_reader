#!/usr/bin/env python


import requests
from bs4 import BeautifulSoup
import json
import re
import sys
import webbrowser


def help():
    print(''' \n
    ################ HOW TO USE ################\n
    manga + {the-manga-that-you-want} + {chapter} \n
    ############################################  ''')



if __name__ == "__main__":
        
    # figuring out the name and formating it 
    #############################################################
    realName = list(sys.argv[1].split("-"))
    name = ""
    for word in realName:
        name = name + word.title() + "-"

    name = name[0:len(name)-1]

    # figuring out the available chapters
    ##############################################################
    resp = requests.get("https://mangasee123.com/manga/" + name)
    content = resp.content.decode("utf-8")
    chapter_details_pattern = re.compile("vm.Chapters = (.*);")
    chapter_details_str = chapter_details_pattern.search(content).groups()[0]
    chapter_details_list = json.loads(chapter_details_str)

    chapter_details_dict = {}
    for chapter_detail in chapter_details_list:
        chapter_details_dict[
            int(chapter_detail["Chapter"][1:-1])
        ] = chapter_detail 

    ##############################################################
    # figuring out the chapter 
    ##############################################################
    first = str(min(chapter_details_dict.keys()))
    last = str(max(chapter_details_dict.keys()))
    try:
        chapter = sys.argv[2]
    except Exception as e:
        chapter = last

    if chapter.lower() == "last":
        chapter = last
    elif chapter.lower() == "first":
        chapter = first

    try:
        int(chapter)
        if (chapter < first or chapter > last):
            raise Exception()
    except ValueError as e:
        help()
        sys.exit()
    except Exception as e:
        help()
        sys.exit()


    ###################################################################
    # opening the manga chapter
    ###################################################################
    link = 'https://mangasee123.com/read-online/' + name + "-chapter-" + chapter + ".html"
    req = requests.get(link)
    
    soup = BeautifulSoup(req.text, 'html.parser')
    
    for title in soup.find_all('title'):
        if (title.get_text() == "404 Page Not Found"):
            link = 'https://mangasee123.com/read-online/' + name + "-chapter-" + chapter + "-index-2" + ".html"
        
    webbrowser.open(link, new=2)   
    ###################################################################
