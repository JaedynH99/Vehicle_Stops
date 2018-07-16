import csv
def load_file (file_name):
    with open('vehicle_stops_2017_datasd.csv') as a:
        for line in a:
            line=line.replace('"','  ')
            for word in (line.split(',')):
                print(word, end = '')

    a.close()

load_file('vehicle_stops_2017_datasd.csv')
