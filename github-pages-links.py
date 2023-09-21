import os
import sys
import csv
from urllib.parse import urlparse

file_path = sys.argv[1]
if os.path.exists(file_path):
  original_csv_file = open(file_path, 'r')
  csv_file = open('export-with-pages.csv', 'w')
  writer = csv.writer(csv_file)
  header = ["name", "repository-url", "pages-url"]
  writer.writerow(header)

  reader = csv.reader(original_csv_file)
  next(reader)
  rows = []
  for row in reader:
    rows.append(row)
    name = row[0]
    original_url = urlparse(row[1].removesuffix('.git'))
    original_host = original_url.hostname
    if original_host.endswith('.io'):
      # we have the page
      page = original_url.geturl()
      org_name = original_url.hostname.replace('.github.io', '')
      repo = original_url._replace(netloc='github.com', path='/' + org_name + original_url.path).geturl()
    elif original_host.endswith('.com'):
      # we have the repository
      repo = original_url.geturl()
      org_name = original_url.path.split('/')[1]
      page = original_url._replace(netloc=org_name + '.github.io', path=original_url.path.replace(org_name + '/', '')).geturl()

    writer.writerow([name, repo, page])
