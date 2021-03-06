# Jokes & Pickup Line Api
--------------------------
This API returns jokes and pickuplines form [r/Jokes](https://www.reddit.com/r/Jokes) and [r/pickuplines](https://www.reddit.com/r/pickuplines)

live-demo: https://jokeandpickupapi.herokuapp.com/

### Parameters

| Parameter         |        Description                 | Required | Default  |                 Constraints                 |
--------------------|------------------------------------|----------|----------|---------------------------------------------|
| ```time_filter``` | time the post was made             |     Yes  |```None```|```['all', 'year', 'month', 'week', 'day']```|
| ```limit```       | Limit the number of post to return |     No   |```10```  | ```Interger```                              |

### Endpoints
``` base_url: https://jokeandpickupapi.herokuapp.com/```

#### Jokes
|     Endpoint                                   |     Description                     | Status |
|------------------------------------------------|-------------------------------------|--------|
|```/joke/random ```                             | Get a random joke                   | Active |
|```/joke/new/<limit> ```                        | Get jokes from New Posts            | Active |
|```/joke/top/<time_filter>/<limit> ```          | Get jokes from Top posts            | Active |
|```/joke/controversial/<time_filter>/<limit> ```| Get jokes from controversial posts  | Active |
|```/joke/rising/<time_filter>/<limit> ```       | Get jokes form Rising posts         | Active |

#### Pickup Lines
|     Endpoint                                     |     Description                            | Status |
|--------------------------------------------------|--------------------------------------------|--------|
|```/pickup/random ```                             | Get a random Pickup Line                   | Active |
|```/pickup/new/<limit> ```                        | Get Pickup Lines from New Posts            | Active |
|```/pickup/top/<time_filter>/<limit> ```          | Get Pickup Lines from Top posts            | Active |
|```/pickup/controversial/<time_filter>/<limit> ```| Get Pickup Lines from controversial posts  | Active |
|```/pickup/rising/<time_filter>/<limit> ```       | Get Pickup Lines form Rising posts         | Active |


#### Example

``` GET https://jokeandpickupapi.herokuapp.com/joke/random ```


``` Response 
    {
          "id": "i5tz0f",
          "url": "https://www.reddit.com/r/Jokes/comments/i5tz0f/how_dare_the_government_infringe_on_my_freedoms/",
          "upvote_ratio": 0.67,
          "over_18": false,
          "name": "t3_i5tz0f",
          "title": "How dare the Government infringe on my freedoms by forcing me to wear a bit of cloth covering a part of my
          body...",
          "body": "Nudists unite!"
    }
```

##### Run the server yourself
###### setting reddit account && getting api keys
+ make a [reddit developer account](https://www.reddit.com/)
+ create a [reddit script app](https://www.reddit.com/prefs/apps/)
+ store the api keys ,username & password in environment variable
```
    CLIENT_ID='client id from the app'
    CLIENT_SECRET='client secret from the app'
    USER_NAME='your reddit username'
    USER_PASS='your reddit password'
```

###### clone repo and run
+ clone the repository
    ``` git clone https://github.com/rgab1508/jokeandpickupapi ```
+ ```cd jokeandpickupapi```
+ ```pip install -r requirements.txt```
+ ```gunicorn wsgi:app```

### dependencies
+ ```flask```
+ ```praw```
