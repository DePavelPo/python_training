# Разработать программу, скачивающую страницу по указанному URL со всем ее содержимым.

import urllib.request
import os

url = input('Input URL: ')

html = urllib.request.urlopen(url).read()
print('result code:', str(urllib.request.urlopen(url).getcode()))
os.makedirs(os.path.dirname("/files/2_result.html"), exist_ok=True)
with open("/files/2_result.html", 'w') as f:
    f.write(str(html))