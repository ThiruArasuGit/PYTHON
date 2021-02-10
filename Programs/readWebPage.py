import requests
from bs4 import BeautifulSoup

# Extracting the list of headers from the given url.
response = requests.get(url=r'https://codeburst.io/how-to-scrape-yahoo-finance-using-python-31164aa06468')
print(response.status_code)
if response.status_code == 200:
    res_txt = response.text # Converting into text file
    soup = BeautifulSoup(res_txt, features='html.parser')
    data = soup.find_all("h1") # Find all the headers
    for rs in data:
        rs_str = (str(rs).split('">'))
        fn_str = rs_str[1].split('</h1>')[0]
        print(fn_str)