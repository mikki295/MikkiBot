import requests
from bs4 import BeautifulSoup
from dates import dates_of_current_week

def __get_info_one(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser')
    time = soup.find("div",{"class" : "card__time_start"}).get_text()
    description = soup.find("section",{"class" : "card__description"}).get_text()
    tag = soup.find("img",{"class" : "channel__logo"})
    return time + ' kanavalla: ' + tag['alt'], description

def __get_info_all(href_list):
    all_info = []
    for link in href_list:
        all_info.append(__get_info_one(link))

    return all_info

def __formatted_info(all_info):
    string = ''
    if (len(all_info) == 0):
        string += "Valitettavasti tanaan ei tule temppareita :("
    else:
        for info in all_info:
            string += info[0] + '\n' + info[1] + '\n\n'
            #string += '\n\n*{}*\n{}'.format(info[0],info[1])
            # string += info[0] + '\n\n' + info[1] + '\n\n'

    return string

def get_info(url):
    '''returns a matrix of matrix[set][time = 0, description = 1]'''
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser')
    href_links = []

    for link in soup.find_all('a'):
        if ("salatut-elamat" in link.get('href')):
            href_links.append(url + link.get('href'))    

    info = __get_info_all(href_links)

    return __formatted_info(info)

def get_week_schedule():
    week_dates = dates_of_current_week()
    
    for date in week_dates: 
        year = str(date.year)
        month = str(date.month)
        day = str(date.day)
        url = 'http://telkku.com/tv-ohjelmat/' + year + '-' + month + '-' + day + '/peruskanavat/koko-paiva'
        print(get_info(url))



#    for date in week_dates:
#        year = date.year
#        month = date.month
#        day = date.day
#        url = 'http://telkku.com/tv-ohjelmat/' + year + '-' + month + '-' + day + '/peruskanavat/koko-paiva'
#        res = requests.get(url)
#        soup = BeautifulSoup(res.content('html.parser'))
#        href_links = []
#
#        for
