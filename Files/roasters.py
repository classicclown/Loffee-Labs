from bs4 import BeautifulSoup
import requests
import pandas as pd



def setup():
    url = 'https://www.loffeelabs.com/roasters-registry/'
    response = requests.get(url)
    html = response.text
    return html

def write_html(html):
    with open('html','w') as f:
        f.write(html)
        print ('HTML written to file')

def open_html():
    with open('html','r') as f:
        return f.read()
    
def scrape_table(html):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.select('tbody tr')
    roasters ={'Name':[],'Region':[],'Country':[],'City':[]}
    for row in rows:
        columns = row.find_all('td')
        roaster = columns[0].get_text()
        region = columns[1].get_text()
        country = columns[2].get_text()
        city = columns[3].get_text()

        roasters['Name'].append(roaster)
        roasters['Region'].append(region)
        roasters['Country'].append(country)
        roasters['City'].append(city)

    roasters_df=pd.DataFrame.from_dict(roasters)
    roasters_df.to_csv('Roasters info',index=False)
    return roasters

def print_info(roasters_info):

    for value, key in roasters_info.items():
        print (value,key)

scraper = setup()
write_html(scraper)
content = open_html()
print_info(scrape_table(content))


