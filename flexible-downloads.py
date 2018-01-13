import os
import sys
import requests
from bs4 import BeautifulSoup
import wget
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# ask user what URL they want to download things from
url_prompt = "What webpage do you want to download files from?"
url = input(url_prompt)

# tell user to look at the DOM/page source to figure out where files are located
inspect_prompt = "Thank you! Please make sure to inspect the DOM/page source\
for this next portion to guarantee accurate results. You may refer to\
the readme for a reference/specific examples."
print(inspect_prompt)

# ask user if there's a particular extension that the files are located
ext_prompt = "If there is a sub-page these extensions are located in,\
please paste it here. Otherwise, just press enter.\n"
extension = input(ext_prompt)

# ask user for the html tag where the files are nested
html_prompt = "Now, please enter the specific html tag where\
the files you want are located: \n"
tag = input(html_prompt)

# ensure that the links provided are 

# url = 'https://inst.eecs.berkeley.edu/~cs170/fa17/'
# extension = ''
page = requests.get(url + extension)
soup = BeautifulSoup(page.text, 'html.parser')

weekly_rows = soup.find_all(tag)
weekly_links = []

for wk in weekly_rows: 
	lnks = wk.find_all('a')
	if lnks:
		weekly_links.append(lnks)

urls = []
keyword = 'assets'

# keeps lnk if it starts with assets
def extract_link(lnk):
	href = lnk['href']
	if href[0:6] == keyword:
		return url + '/' + href

for lnks in weekly_links:
	extracted_with_none = list(map(extract_link, lnks))
	extracted_without_none = list(filter(lambda x: x is not None, extracted_with_none))
	urls.extend(extracted_without_none)

path = '/Users/Annie/file-downloader/test-folder'
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
