from bs4 import BeautifulSoup
import configparser
import requests
import csv

def getPageForCourse(courseCode):
    try:
        url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-department&dept=' + courseCode
        return requests.get(url)
    except: 
        return None

def getCourseCodeAndTitles(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    listOfTr = soup.find_all('tr')
    result = []
    # skipping the first and the last
    for x in range(1, (len(listOfTr) - 1)):
        try:
            courseCode = listOfTr[x].find_all('td')[0].find("a").text 
            title = listOfTr[x].find_all('td')[1].text
            tup = (courseCode, title)
            result.append(tup)
        except: 
            continue

    return result

def writeToCSV(array):
    with open('./data/courses.csv', 'w+') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in array: 
            writer.writerow([row[0], row[1]])

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    # config.get('DATABASE', 'username'):w

    page = getPageForCourse('CPSC')
    if page is not None: 
        courses = getCourseCodeAndTitles(page)
        writeToCSV(courses)

if __name__ == "__main__":
    print('Main:')
    main()
