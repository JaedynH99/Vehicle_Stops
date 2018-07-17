import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
people = []

class CensusData:
    def __init__(self,total_race, total_gender):
        self.total_race=total_race
        self.total_gender=total_gender

def load_file_census(file_name):
    global people
    with open('DemographicCensus.csv') as f:
        readCSV = csv.reader(f, delimiter=',')
        for row in readCSV:
           people.append(row[3])
        print(type(people))
    f.close()

load_file_census('DemographicCensus.csv')

