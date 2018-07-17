import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
people = []
# races= []
# genders=[]
stops=[]

class TrafficStop:
    def __init__(self,race, gender):
        self.race = race
        self.gender = gender
    def __str__(self):
        return f'TrafficStop of {self.race}, {self.gender}'

def load_file (file_name):
    global races
    global genders
    with open('vehicle_stops_2017_datasd.csv') as a:
        for line in a:
            line=line.replace('"','  ')
            data = line.split(',')
            if data[3] and data[4]:
                stops.append(TrafficStop (data[3].strip(), data[4].strip()))
                # print(stops[-1].gender)
    #             races.append(data[3])
    #             genders.append(data[4])
    # print(genders)
    # print(races)

    a.close()
# def count_gender():
#     count_M = genders.count(' M ')
#     count_F = genders.count(' F ')
#     print('the amount of females =', count_F)
#     print('the amount of males =', count_M)
#
# def count_race():
#     race_W = races.count('W')
#     race_B = races.count('B')
#     race_A = races.count('')
#     race_O=
#     race_H=
#     race_I=


def gender_count():
    males = [stop for stop in stops if stop.gender=="M"]
    females = [stop for stop in stops if stop.gender=="F"]
    print('the amount of males=', len(males)/len(stops))
    print('the amount of females=',len(females)/len(stops))

def race_count():
    asian = [stop for stop in stops if stop.race =='A' or stop.race=='F' or stop.race=='D' or stop.race=='C' or stop.race=='J' or stop.race=='K' or stop.race=='L' or stop.race=='V' or stop.race=='Z']
    black = [stop for stop in stops if stop.race == 'B']
    # chinese = [stop for stop in stops if stop.race == 'C']
    # cambodian = [stop for stop in stops if stop.race == 'D']
    # filipino = [stop for stop in stops if stop.race == 'F']
    # guamanian = [stop for stop in stops if stop.race == 'G']
    hispanic = [stop for stop in stops if stop.race == 'H']
    american_indian = [stop for stop in stops if stop.race == 'I']
    # japanese = [stop for stop in stops if stop.race == 'J']
    # korean = [stop for stop in stops if stop.race == 'K']
    # laotian = [stop for stop in stops if stop.race == 'L']
    other = [stop for stop in stops if stop.race == 'O']
    pacific_islander = [stop for stop in stops if stop.race == 'P' or stop.race=='G' or stop.race=='S' or stop.race=='U']
    # samoan = [stop for stop in stops if stop.race == 'S']
    # hawaiian = [stop for stop in stops if stop.race == 'U']
    # vietnamese = [stop for stop in stops if stop.race == 'V']
    white = [stop for stop in stops if stop.race == 'W']
    # asian_indian = [stop for stop in stops if stop.race == 'Z']
    # print('the amount of unspecified asians =', len(asian)/len(stops))
    # # print('the amount of blacks =', len(black)/len(stops))
    # print('the amount of chinese =', len(chinese)/len(stops))
    # # print('the amount of cambodians =', len(cambodian)/len(stops))
    # # print('the amount of filipinos =', len(filipino)/len(stops))
    # # print('the amount of guamanians =', len(guamanian)/len(stops))
    # # print('the amount of hispanics =', len(hispanic)/len(stops))
    # # print('the amount of american indians =', len(american_indian)/len(stops))
    # # print('the amount of japanese =', len(japanese)/len(stops))
    # # print('the amount of koreans =', len(korean)/len(stops))
    # # print('the amount of laotians =', len(laotian)/len(stops))
    # # print('the amount of others =', len(other)/len(stops))
    # print('the amount of pacific islanders =', len(pacific_islander)/len(stops))
    # print('the amount of samoans =', len(samoan)/len(stops))
    # print('the amount of hawaiians =', len(hawaiian)/len(stops))
    # print('the amount of vietnamese =', len(vietnamese)/len(stops))
    # print('the amount of whites =',len(white)/len(stops))
    # print('the amount of asian indians =',len(asian_indian)/len(stops))

class CensusData:
    def __init__(self, total_race, total_gender):
        self.total_race = total_race
        self.total_gender = total_gender

def load_file_census(file_name):
    global people
    with open('DemographicCensus.csv') as f:
        readCSV = csv.reader(f, delimiter=',')
        for row in readCSV:
            people.append(row[3])
        print(people)
    f.close()

if __name__=='__main__':
    load_file_census('DemographicCensus.csv')
    n_groups = 7
    means_frank = (people[48], people[47], people [49], people[50], people[51], people[52], people[44])
    means_guido = (85, 62, 54, 20)

    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, means_frank, bar_width,alpha=opacity,color='b',label='Race in County')

    rects2 = plt.bar(index + bar_width, means_guido, bar_width,alpha=opacity,color='g',label='Race in Vehicle Stops')

    plt.xlabel('Person')
    plt.ylabel('Scores')
    plt.title('Scores by person')
    plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
    plt.legend()

    plt.tight_layout()
    plt.show()

race_count()
# gender_count()


