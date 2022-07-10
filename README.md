# How To Use
``` 
mkdir manga_reader
git clone https://github.com/angur001/manga_reader.git
python ./manga.py {manga-name} {chapter}
``` 
if manga name has space write it with - instead for exemple to search for jujustu kaisen last chapter you would do \\
``` python ./manga jujustsu-kaisen last ```

requirements
```
python -m pip install requests
python -m pip install bs4
python -m pip install webbrowser
```
For optimum usage it is recommended to add the path of the script to the PATH env variable and so you
would be able to execute the scipt from anywhere.

It is possible to generate an executable from the script and use it instead:
first ```python -m pip install py2exe``` and execute the execute the scrit setup it should generate a dist folder with an executable that you can place in PATH
and execute it from anywhere in the command line.
