import requests
from bs4 import BeautifulSoup
from dates import dates_of_current_week

__TELKKU_URL = 'http://telkku.com/'

def __get_time(soup):
    return '*' + soup.find("div",{"class" : "card__time_start"}).get_text() + '*'

def __get_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser')
    return soup

def __get_channel(soup):
    tag = soup.find("img",{"class" : "channel__logo"})
    return ' kanavalla: ' + tag['alt']

def __get_info_one(url):
    soup = __get_soup(url)
    time = __get_time(soup)
    description = soup.find("section",{"class" : "card__description"}).get_text()
    channel = __get_channel(soup)
    return time + channel, description

def __get_info_all(href_list):
    all_info = []
    for link in href_list:
        all_info.append(__get_info_one(link))
    return all_info

def __formatted_info(all_info):
    info_text = ''
    if (len(all_info) == 0):
        info_text += "Valitettavasti tanaan ei tule temppareita :("
    else:
        for info in all_info:
            info_text += info[0] + '\n' + info[1] + '\n\n'
            
    return info_text

def __get_hrefs(soup):
    href_links = []
    for link in soup.find_all('a'):
        if ("simpsonit" in link.get('href')):
            href_links.append(__TELKKU_URL + link.get('href'))
    return href_links

def get_info():
    '''returns a matrix of matrix[set][time = 0, description = 1]'''
    soup = __get_soup(__TELKKU_URL)
    href_links = __get_hrefs(soup)
    info = __get_info_all(href_links)
    return __formatted_info(info)

def get_week_schedule():
    week_dates = dates_of_current_week()
    schedule = ''
    for date in week_dates: 
        year = str(date.year)
        month = str(date.month)
        day = str(date.day)
        url = 'tv-ohjelmat/' + year + '-' + month + '-' + day + '/peruskanavat/koko-paiva'
        soup = __get_soup(__TELKKU_URL + url)
        href_links = __get_hrefs(soup)
        for link in href_links:
            soup = __get_soup(link)
            schedule += __get_time(soup) + __get_channel(soup) + '\n'

        schedule += '\n'
        
    return schedule 