import praw
import os

DEFAULT_LIMIT = 10

CLIENT_ID = os.environ["R_CLIENT_ID"]
CLIENT_SECRET = os.environ["R_CLIENT_SECRET"]
USER_NAME = os.environ["R_USER_NAME"]
USER_PASS = os.environ[("R_USER_PASS"]

r = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, username=USER_NAME, password=USER_PASS, user_agent='Test script')


jokes_sub = list(r.user.subreddits())[0]


def get_joke_random():
    rj = jokes_sub.random()

    joke = {
        "id": rj.id,
        "url": rj.url,
        "upvote_ratio": rj.upvote_ratio,
        "over_18": rj.over_18,
        "name": rj.name,
        "title":rj.title,
        "body":rj.selftext
    }

    return joke

def get_joke_new(limit=DEFAULT_LIMIT):
    r_j = jokes_sub.new(limit=limit)

    jokes = []
    for j in r_j:
        jo = {
            "id": j.id,
            "url": j.url,
            "upvote_ratio": j.upvote_ratio,
            "over_18": j.over_18,
            "name": j.name,
            "title":j.title,
            "body":j.selftext
        }

        jokes.append(jo)

    return jokes



def get_joke_controversial(time_filter, limit=DEFAULT_LIMIT):
    r_j = jokes_sub.controversial(time_filter, limit=limit)

    jokes = []
    for j in r_j:
        jo = {
            "id": j.id,
            "url": j.url,
            "upvote_ratio": j.upvote_ratio,
            "over_18": j.over_18,
            "name": j.name,
            "title":j.title,
            "body":j.selftext
        }

        jokes.append(jo)

    return jokes

def get_joke_rising(time_filter, limit=DEFAULT_LIMIT):
    r_j = jokes_sub.random_rising(time_filter, limit=limit)

    jokes = []
    for j in r_j:
        jo = {
            "id": j.id,
            "url": j.url,
            "upvote_ratio": j.upvote_ratio,
            "over_18": j.over_18,
            "name": j.name,
            "title":j.title,
            "body":j.selftext
        }

        jokes.append(jo)

    return jokes



def get_joke_top(time_filter, limit=DEFAULT_LIMIT):
    r_j = jokes_sub.top(time_filter, limit=limit)

    jokes = []
    for j in r_j:
        jo = {
            "id": j.id,
            "url": j.url,
            "upvote_ratio": j.upvote_ratio,
            "over_18": j.over_18,
            "name": j.name,
            "title":j.title,
            "body":j.selftext
        }

        jokes.append(jo)

    return jokes


#if __name__ == "__main__":
print(get_joke_top('day' ,limit=7))
