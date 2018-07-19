import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
people = []
stops=[]
blacks = None
asians = None
hispanics = None
american_indians = None
others = None
pacific_islanders = None
whites = None

class TrafficStop:
    def __init__(self,race, gender):
        self.race = race
        self.gender = gender
    def __str__(self):
        return f'TrafficStop of {self.race}, {self.gender}'

def load_file (file_name):
    global races
    global genders
    with open('vehicle_stops_2017_datasd.csv') as t:
        for line in t:
            line=line.replace('"','  ')
            data = line.split(',')
            if data[3] and data[4]:
                stops.append(TrafficStop (data[3].strip(), data[4].strip()))

    t.close()

def gender_count():
    males = [stop for stop in stops if stop.gender=="M"]
    females = [stop for stop in stops if stop.gender=="F"]
    print('the amount of males=', len(males)/len(stops))
    print('the amount of females=',len(females)/len(stops))

def race_count():
    global stops, blacks, asians, hispanics, american_indians, others, pacific_islanders, whites
    asian = [stop for stop in stops if stop.race =='A' or stop.race=='F' or stop.race=='D' or stop.race=='C' or\
             stop.race=='J' or stop.race=='K' or stop.race=='L' or stop.race=='V' or stop.race=='Z']
    black = [stop for stop in stops if stop.race == 'B']
    hispanic = [stop for stop in stops if stop.race == 'H']
    american_indian = [stop for stop in stops if stop.race == 'I']
    other = [stop for stop in stops if stop.race == 'O']
    pacific_islander = [stop for stop in stops if stop.race == 'P' or stop.race=='G' or stop.race=='S' or stop.race=='U']
    white = [stop for stop in stops if stop.race == 'W']
    blacks = ((len(black)/len(stops))*100)
    asians = ((len(asian)/len(stops))*100)
    hispanics = ((len(hispanic)/len(stops))*100)
    american_indians = ((len(american_indian)/len(stops))*100)
    others = ((len(other)/len(stops))*100)
    pacific_islanders = ((len(pacific_islander)/len(stops))*100)
    whites = ((len(white)/len(stops))*100)

class CensusData:
    def __init__(self, total_race, total_gender):
        self.total_race = total_race
        self.total_gender = total_gender

def load_file_census(file_name):
    global people
    with open('DemographicCensus.csv') as z:
        readCSV = csv.reader(z, delimiter=',')
        for row in readCSV:
            people.append(row[3])
        z.close()

if __name__=='__main__':
    load_file_census('DemographicCensus.csv')
    a = float(people[48])
    b = float(people[46])
    c = float(people[49])
    d = float(people[50])
    e = float(people[51])
    f = float(people[52])
    g = float(people[44])
    load_file('vehicle_stops_2017_datasd.csv')
    race_count()
    n_groups = 7
    means_frank = (a, b, c, d, e, f, g)
    means_guido = (whites, hispanics, blacks, american_indians, asians, pacific_islanders, others)
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
    rects1 = plt.bar(index, means_frank, bar_width,alpha=opacity,color='b',label='Amount of People Residing in San Diego County')
    rects2 = plt.bar(index + bar_width, means_guido, bar_width,alpha=opacity,color='g',label='Amount of People Police Pulled Over')

    plt.xlabel('Race')
    plt.ylabel('Percentage of the Total')
    plt.title('Do police have a racial bias?')
    plt.xticks(index + bar_width, ('White','Hispanic', 'Black', 'American Indian', 'Asian', 'Pacific Islander', 'Other'))
    plt.legend()

    plt.tight_layout()
    plt.show()

