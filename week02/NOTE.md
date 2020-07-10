学习笔记

### Fake Header
do not forgot to include the following info in headers
* User-Agent
* Referer
* Host

Some websites may require additional info in headers. Double check in chrome.

### learn http debug
httpbin.org

use request.Session() to capture cookies

use webdriver to simulate browser
how to chunk a download file
```python
file_url = 'http://...'
r = requests.get(file_url, stream=True)
with open("python.pdf","wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)

```