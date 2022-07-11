#!/usr/bin/env python


import requests
from bs4 import BeautifulSoup
import json
import re
import sys
import webbrowser
import csv
from difflib import SequenceMatcher
import pandas as pd

csv_file_name = "animeList.csv"

def help():
    print(''' \n
    ################ HOW TO USE ################\n
    manga + {the-manga-that-you-want} + {chapter} \n
    ############################################ \n 
    ''')

def create_csv_file():
    # creating a csv file with all anime
    ##############################################################

    resp = requests.get("https://mangasee123.com/directory/")
    content = resp.content.decode("utf-8")
    anime_details_pattern = re.compile("vm.FullDirectory = (.*);")
    anime_details_str = anime_details_pattern.search(content).groups()[0]
    anime_details_list = json.loads(anime_details_str)

    anime_details_dict = []
    for anime_detail in anime_details_list["Directory"]:
        anime_details_dict.append(anime_detail["i"]) 

    df = pd.DataFrame(anime_details_dict)
    df.to_csv(csv_file_name, index=False)
    
    ##############################################################



if __name__ == "__main__":
        
    # Open animeList file 
    #############################################################

    try:
        f = open(csv_file_name)
    except FileNotFoundError as e:
        print("Creating csv file")
        create_csv_file()
        f = open(csv_file_name)
    file_read = csv.reader(f)
    animeList = list(file_read)
    f.close()

    # figuring out the name and formating it 
    #############################################################

    realName = list(sys.argv[1].split("-"))
    name = ""
    for word in realName:
        name = name + word.title() + "-"

    name = name[0:len(name)-1]

    # find closest manga name in the list 
    #############################################################

    max = 0
    index = 0
    max_index = 0
    for anime in animeList:
        score = SequenceMatcher(None, anime[0], name).ratio()
        if score > max:
            max = score
            max_index = index
        index += 1

    name = animeList[max_index][0]

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

    keys_list = list(chapter_details_dict.keys())
    first = str(min(keys_list))
    last = str(keys_list[0])
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
            print("The chapter you're looking for is unavailable\n")
            raise Exception()
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
