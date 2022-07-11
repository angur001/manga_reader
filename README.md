# How To Use
```console
mkdir manga_reader
git clone https://github.com/angur001/manga_reader.git
python ./manga.py {manga-name} {chapter}
``` 
The chapter should be an interger between first chapter and the last available chapter or you can write first ot last to access the respective chapters.
If manga name has spaces use - instead for exemple to search for jujustu kaisen last chapter you would do :
```console
python ./manga.py jujustsu-kaisen last
```

requirements :
```console
python -m pip install requests
python -m pip install bs4
python -m pip install webbrowser
python -m pip install pandas
```

For optimum usage it is recommended to add the path of the script to the PATH env variable and so you
would be able to execute the scipt from anywhere.

It is possible to generate an executable from the script and use it instead:
first ```console 
python -m pip install py2exe``` then execute the setup script. It should generate a dist folder with an executable. you can try to add dist to PATH
and execute it from anywhere in the command line.
