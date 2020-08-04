'''This folder loads the data in ./data/courses.csv onto mongodb atlas'''
from pymongo import MongoClient
import configparser
import csv
import re

config = configparser.ConfigParser()
config.read('config.ini')
db_name = config.get('DATABASE', 'DB_NAME')
db_pw = config.get('DATABASE','DB_PW')
db_user = config.get('DATABASE', 'DB_USER')
db_identifier = config.get('DATABASE', 'DB_IDENTIFIER')

def getYear(courseCode):
    year = re.search(r'\d', courseCode).group()
    return year + "00"

def formData(row):
    courseCode = row[0]
    description = row[1]
    year = getYear(courseCode)
    return {'_id': courseCode, 'description': description,'overall_rating': '-', 'num_reviews': 0, 'year': year}

def insertOne(data, model):
    model.insert_one(data)

def readAndInsertCourses(model):
    with open('./data/courses.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            data = formData(row)
            insertOne(data, model)

def connectToDB():
    url = 'mongodb+srv://'+db_user+':'+db_pw+'@'+db_identifier+'.mongodb.net/'+db_name+'?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'
    return MongoClient(url)

def getCourseModel(client):
    return client[db_name]['Courses']

def load():
    client = connectToDB()
    courses = getCourseModel(client)
    
    newCourse = {'_id':'APSC600', 'overall_rating': '-', 'num_reviews':0, 'description': 'testing', 'year': '600'}
    #insertOne(newCourse, courses)
    readAndInsertCourses(courses)

if __name__ == '__main__':
    load()