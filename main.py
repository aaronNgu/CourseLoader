from bs4 import BeautifulSoup
import configparser
import requests

def get(url):
    return requests.get(url)

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    # config.get('DATABASE', 'username'):w

    url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-department&dept=ARCH'
    page = get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all('tr')
    print(result[1].find_all('td')[0].find("a").text)
    print(result[1].find_all('td')[1].text)

if __name__ == "__main__":
    print('Main:')
    main()
