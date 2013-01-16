# Riyaz Faizullabhoy
# 1/14/2013
# The next __ BART trains

""" Given command-line input, formulates and scrapes a URL from bart.gov detailing the requested trip, including times, connections, and fares. Uses BeautifulSoup. """

import bs4
from bs4 import BeautifulSoup
import urllib2, urllib
from datetime import datetime
from station import *
import sys, getopt


def time_compare(trip_time, desired_time):
    if trip_time[0] > desired_time[0]:
        return 1
    elif trip_time[0] < desired_time[0]:
        return -1
    elif trip_time[1] > desired_time[1]:
        return 1
    else:
        return -1


def determine_time(desired_time):
    desired_time = desired_time.lower()
    if "now" in desired_time:
        time = "now"
        hours = datetime.now().hour
        minutes = datetime.now().minute
    else:  
        time_digits = desired_time.strip("am").strip("pm").split(":")
        try:
            minutes = int(time_digits[1])
            hours = int(time_digits[0])
        except Exception:
            raise ValueError("Time input not using valud numerical digits")
        if (desired_time.find("pm") == -1) and hours < 12:
            tail = "AM"
        else:
            tail = "PM"

        if hours >= 24 or hours < 0:
            raise ValueError("Invalid time hour input: " + str(hours) + " must be nonnegative and less than 24")
        if minutes >= 60 or minutes < 0:
            raise ValueError("Invalid time minute input: " + str(minutes) + " must be less nonnegative and than 60")
        if minutes != 0:
            if minutes < 15:
                minutes = 0
            elif minutes == 30:
                minutes = 3
            elif minutes > 45:
                minutes = 0
                hours += 1
            else: 
                minutes = 3
        time = str(hours) + "%3A" + str(minutes) + "0+" + tail
        if tail == "PM" and hours != 12:
            hours += 12
    return time, (hours, minutes)


def extract_time_from_tagline(tag_line):
    tag_string = str(tag_line)
    time = ""
    in_tag = False
    for c in tag_string:
        if c == "<":
            in_tag = True
        elif c == ">":
            in_tag = False
        elif in_tag:
            continue
        elif c not in "1234567890:ap":
            continue
        else:
            time += c
    return time


def extract_station_from_tagline(tag_line):
    tag_string = str(tag_line)
    station = ""
    for c in tag_string:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
            continue
        else:
            station += c
    return station


def extract_train_direction(tag_line):
    tag_string = str(tag_line)
    station_tag_index = tag_string.find("alt=")
    return tag_string[station_tag_index+5] + tag_string[station_tag_index+6] + tag_string[station_tag_index+7] + tag_string[station_tag_index+8]


def find_all_possible_trips(station1, station2, desired_time ="now", query_num =3):

    counter = 1

    time, chosen_time  = determine_time(desired_time)
    orig, dest = match_stations(station1, station2)

    html_doc = urllib2.urlopen("http://bart.gov/schedules/extended.aspx?type=departure&date=today&time={0}&orig={1}&dest={2}".format(time, orig, dest))
    soup = BeautifulSoup(html_doc)
    
    fare = ""
    fare_tag = str(soup.find_all("b"))
    for c in fare_tag:
        if c in "$1234567890.":
            fare += c
    print("\n\nFARE: " + fare + "\n")
    
    routes = soup.contents[3].find_all("tr")[7:]
    return determine_best_routes(routes, chosen_time, query_num)


def determine_best_routes(routes, chosen_time, query_num):
    counter = 0
    for route in routes:
        details = route.find_all("td")
        trains = route.find_all("img")

        first_time = extract_time_from_tagline(details[1])
        first_time = first_time.split(":")
        hour = int(first_time[0])
        if "p" in first_time[1] and hour != 12:    
            hour += 12
        if "a" in first_time[1] and hour == 12:
            hour = 0
        minute = int(first_time[1][0:2])
        
        if time_compare((hour, minute), chosen_time) == -1:
            continue

        else: 
            sets = len(trains)
            set_counter = 0
            while set_counter < sets:
                print(extract_train_direction(details[set_counter*5 + 2]) + "-bound Train:")
                print("\tDEPART: " +  extract_time_from_tagline(details[set_counter*5 + 1]) + "\n")
                print("\t\tFROM: " + extract_station_from_tagline(details[set_counter*5]) + "\n")
                print("\tARRIVE: " +  extract_time_from_tagline(details[set_counter*5 + 4]) + "\n")
                print("\t\tTO: " +  extract_station_from_tagline(details[set_counter*5 + 3]) + "\n")
                set_counter += 1            

            counter += 1
            if counter >= query_num:
                return
                

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h")
    except getopt.GetoptError:
        print '\tpython bart.py departure_station arrival_station time(default = now) number_of_queries(default = 3)'
        sys.exit(2)
    if len(opts) == 2 or len(argv) > 4 and opts[0][0] == '-h':
        print 'usage: \tpython bart.py departure_station arrival_station time(default = now) number_of_queries(default = 3)'
        print '\ndeparture_station and arrival_station names must not include spaces.'
        sys.exit()
    else:
        find_all_possible_trips(*argv)
    
    
if __name__ == "__main__":
   main(sys.argv[1:])
