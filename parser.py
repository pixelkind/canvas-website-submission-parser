import os
import sys
import csv
from bs4 import BeautifulSoup

dir_path = sys.argv[1]
if os.path.exists(dir_path):
  dirlist = os.scandir(os.path.basename(dir_path))
  csv_file = open('export.csv', 'w')
  writer = csv.writer(csv_file)
  header = ["name", "url"]
  writer.writerow(header)

  for path in dirlist:
    file = open(path, "r")
    content = file.read()
    bs = BeautifulSoup(content, "html.parser")
    url = bs.a["href"]
    title = bs.head.title.text
    name = title.split(": ")[1]
    
    writer.writerow([name, url])

  file.close()