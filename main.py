from bs4 import BeautifulSoup
import configparser
import requests
import csv

def loadCoursesToScrap():
    result = []
    try:
        with open('coursestoscrap.csv') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader: 
                result.extend(row)
    except: 
        pass
    return result

def filters(courseCode, title):
    try:
        words = []
        with open('filters.csv') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                words.extend(row)
        for word in words:
            if word in title:
                return False
    except:
        return False
    return True

def getPageForCourse(courseCode):
    try:
        url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-department&dept=' + courseCode
        return requests.get(url)
    except: 
        return None

def formatCourseCode(courseCode):
    return courseCode.replace(" ", "")

def getCourseCodeAndTitles(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    listOfTr = soup.find_all('tr')
    result = []
    # skipping the first and the last
    for x in range(1, (len(listOfTr) - 1)):
        try:
            courseCode = listOfTr[x].find_all('td')[0].find("a").text 
            title = listOfTr[x].find_all('td')[1].text
            if (filters(courseCode, title)):
                courseCode = formatCourseCode(courseCode)
                tup = (courseCode, title)
                result.append(tup)
        except: 
            continue

    return result

def writeToCSV(array, overwrite):
    mode = 'w+' if overwrite else 'a'
    with open('./data/courses.csv', mode) as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in array: 
            writer.writerow([row[0], row[1]])

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    # config.get('DATABASE', 'username'):w

    courses = loadCoursesToScrap()
    overwrite = 1
    for courseCode in courses:
        page = getPageForCourse(courseCode)
        if page is not None: 
            courses = getCourseCodeAndTitles(page)
            writeToCSV(courses, overwrite)
            overwrite = 0

if __name__ == "__main__":
    main()
