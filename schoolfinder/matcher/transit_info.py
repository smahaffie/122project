'''
Contains all functions that use google maps to calculate transit-related
information between a given school and given home address

'''
import googlemaps
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def check_neighborhood_schools(school_id, neighborhood_schools):
    '''
    checks if a school is a neighborhood school
    Inputs:
        school_id, integer
        neighborhood_schools, list of integers
    Returns:
        boolean
    '''
    if school_id in neighborhood_schools:
        return True

def find_best_route(home, school, travel_mode):
    '''
    Inputs:
        home: address string
        school: address string

    Returns:
        json
    '''
    gmaps = googlemaps.Client(key='AIzaSyBI1IzrUzrfNjmk3flBCg28YlcQcVVUsyE')
    print("Starting gmaps")
    print(home, school, travel_mode)
    directions_json = gmaps.directions(home, school, mode=travel_mode)
    print("Got gmaps")
    best_route = directions_json[0]['legs'][0]
    return best_route


def get_transit_info(home, school):
    '''
    Inputs:
        home: address string
        school: address string

    Returns:
        (trip duration in seconds, 
        time spent walking in seconds, 
        list of tuples of form (type, line/route name) for each public transportation route taken)
    '''
    print("GET TRAVEL INFO IN TRANSIT_INFO")
    best_route = find_best_route(str(home), str(school), 'transit')

    duration_text = best_route['duration']['text']
    duration = best_route['duration']['value']

    walking_time = 0 

    for step in best_route['steps']:
        if step['travel_mode'] == "WALKING":
            walking_time += step['duration']['value']

    return str([round(duration / 60), round(walking_time / 60)])

def get_duration(home, school):
    '''
    Inputs:
        home, string
        school, string

    Returns:
        transit time, integer
    '''
    best_route = find_best_route(str(home), str(school), 'transit')
    return best_route['duration']['value']