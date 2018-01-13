##### PYTHON SCRIPT TO DOWNLOAD FILES FROM WEBPAGES ######
##### -------- by github user, @anniewtang -------- ######
#####  read the readme for instructions & examples  ######

import os
import sys
import requests
from bs4 import BeautifulSoup
import wget
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# TODO: paste the url of the website inside the ""
url = 'https://inst.eecs.berkeley.edu/~cs170/fa17/'
#END

# TODO: if there's a sub-page/extension that the files are located in,
# paste it between the "" — otherwise, leave as is.
extension = "calendar.html"
#END

# TODO: paste the specific html tag that wraps where the files are located
tag = "tbody"
#END

page = requests.get(url + extension)
soup = BeautifulSoup(page.text, 'html.parser')

weekly_rows = soup.find_all(tag)
weekly_links = []

for wk in weekly_rows: 
	lnks = wk.find_all('a')
	if lnks:
		weekly_links.append(lnks)

urls = []

#TODO: if there is a certain keyword that *starts* each link you want
# to use, paste it between the "" 
keyword = "assets"
#END

end = len(keyword)
# keeps lnk if it starts with assets
def extract_link(lnk):
	href = lnk['href']
	if href[0:end] == keyword:
		return url + '/' + href

for lnks in weekly_links:
	extracted_with_none = list(map(extract_link, lnks))
	extracted_without_none = list(filter(lambda x: x is not None, extracted_with_none))
	urls.extend(extracted_without_none)

#TODO: indicate the path where you want your files to be downloaded to
path = "/Users/Annie/file-downloader/test-folder"
#END

select_option_prompt = "Do you want to manually select which files \
you want to keep/download from this webpage?\n\
Enter [Y]es/[N]o/[Q]uit: "
confirm_dl_prompt = "Do you want to download {}?\n\
Enter [Y]es/[N]o/[Q]uit here: "
manual = False

def verify(ans):
	return ans == 'y' or ans == 'yes'
def quit(ans):
	return ans == 'q' or ans == 'quit'

answer = input(select_option_prompt).lower()
if verify(answer):
	manual = True
elif quit(answer):
	sys.exit()

def prompt_user(url, filename):
	answer = input(confirm_dl_prompt.format(filename)).lower()
	if verify(answer):
		wget.download(url, out=path)
		print()
	elif quit(answer):
		return False
	return True

for url in urls:
	r = requests.get(url)
	if r.status_code != 404:
		filename = os.path.basename(url) 
		if manual:
			if not prompt_user(url, filename):
				break
		else:
			print("Downloading {}".format(filename))
			wget.download(url, out=path)
			print()
