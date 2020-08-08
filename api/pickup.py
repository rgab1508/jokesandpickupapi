import praw
import os

DEFAULT_LIMIT=10

CLIENT_ID = os.environ["R_CLIENT_ID"]
CLIENT_SECRET = os.environ["R_CLIENT_SECRET"]
USER_NAME = os.environ["R_USER_NAME"]
USER_PASS = os.environ["R_USER_PASS"]

r = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, username=USER_NAME, password=USER_PASS, user_agent='Test script')

pickup_sub = list(r.user.subreddits())[2]

def get_pickup_random():
    r_pk = pickup_sub.random()
    
    pickup = {
        "id": r_pk.id,
        "url": r_pk.url,
        "name": r_pk.name,
        "upvote_ratio":r_pk.upvote_ratio,
        "over_18": r_pk.over_18,
        "title": r_pk.title,
        "body": r_pk.selftext
    }
    
    return pickup

def get_pickup_top(time_filter, limit=DEFAULT_LIMIT):
    r_pk = pickup_sub.top(time_filter, limit=limit)
    
    pickups = [] 
    
    for pk in r_pk:
        p = {
            "id": pk.id,
            "url": pk.url,
            "name": pk.name,
            "upvote_ratio":pk.upvote_ratio,
            "over_18": pk.over_18,
            "title": pk.title,
            "body": pk.selftext
        }
        
        pickups.append(p)
        
    return pickups

def get_pickup_controversial(time_filter, limit=DEFAULT_LIMIT):
    r_pk = pickup_sub.controversial(time_filter, limit=limit)
    
    pickups = []
    
    for pk in r_pk:
        p = {
            "id": pk.id,
            "url": pk.url,
            "name": pk.name,
            "upvote_ratio":pk.upvote_ratio,
            "over_18": pk.over_18,
            "title": pk.title,
            "body": pk.selftext
        }
        
        pickups.append(p)
    
    return pickups


def get_pickup_new(limit=DEFAULT_LIMIT):
    r_pk = pickup_sub.new(limit=limit)
    
    pickups = [] 
    
    for pk in r_pk:
        p = {
            "id": pk.id,
            "url": pk.url,
            "name": pk.name,
            "upvote_ratio":pk.upvote_ratio,
            "over_18": pk.over_18,
            "title": pk.title,
            "body": pk.selftext
        }
        
        pickups.append(p)
    
    return pickups



def get_pickup_rising(time_filter, limit=DEFAULT_LIMIT):
    r_pk = pickup_sub.random_rising(time_filter, limit=limit)
    
    pickups = [] 
    
    for pk in r_pk:
        p = {
            "id": pk.id,
            "url": pk.url,
            "name": pk.name,
            "upvote_ratio":pk.upvote_ratio,
            "over_18": pk.over_18,
            "title": pk.title,
            "body": pk.selftext
        }
        
        pickups.append(p)
    
    return pickups


#print(get_pickup_controversial('all'))
