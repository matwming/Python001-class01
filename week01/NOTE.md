学习笔记
# Python
For basic grammar notes, check my notion:
[https://www.notion.so/ming114/Python-40a505ec69de422d8bc528948b0194e4]
```python
# how to create a virtual environment
python3 -m venv venv1

# how to activate the virtual environment
source venv1/bin/activate

# a short cut is 
pipenv shell

# install packages in virtual environment
pipenv shell install requests

# or use requirements.txt
pipenv shell -r requirements.txt
```

# Scrapy

## Core components of Scrapy
It consists of:
* Engine
* Scheduler
* Downloader
* Spiders
* Item Pipelines
* Downloader Middlewares
* Spider Middlewares

# How to use xpath
* '//div[@class="hd"]' : look for all div tags with class equals hd
* './a/span/test()' : look for the next a tag and inside of it look for the first span tag and get its text

For more comprehensive instruction, check this out:
[https://devhints.io/xpath#prefixes]