import csv
# races= []
# genders=[]
stops=[]

class TrafficStop:
    def __init__(self,race, gender):
        self.race = race
        self.gender = gender

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
    print('the amount of males=', len(males))
    print('the amount of females=',len(females))

def race_count():
    unspecified_asian = [stop for stop in stops if stop.race == 'A']
    black = [stop for stop in stops if stop.race == 'B']
    chinese = [stop for stop in stops if stop.race == 'C']
    cambodian = [stop for stop in stops if stop.race == 'D']
    
load_file('vehicle_stops_2017_datasd.csv')
gender_count()

