# Jokes & Pickup Line Api
--------------------------
This API returns jokes and pickuplines form [r/Jokes](https://www.reddit.com/r/Jokes) and [r/pickuplines](https://www.reddit.com/r/pickuplines)

live-demo: ```https://placeholder.com```

### Parameters

| Parameter         |        Description                 | Required | Default  |                 Constraints                 |
--------------------|------------------------------------|----------|----------|---------------------------------------------|
| ```time_filter``` | time the post was made             |     Yes  |```None```|```['all', 'year', 'month', 'week', 'day']```|
| ```limit```       | Limit the number of post to return |     No   |```10```  | ```Interger```                              |

### Endpoints
``` base_url: https://placeholder.com ```

#### Jokes
|     Endpoint                                   |     Description                     | Status |
|------------------------------------------------|-------------------------------------|--------|
|```/joke/random ```                             | Get a random joke                   | Active |
|```/joke/new/<limit> ```                        | Get jokes from New Posts            | Active |
|```/joke/top/<time_filter>/<limit> ```          | Get jokes from Top posts            | Active |
|```/joke/controversial/<time_filter>/<limit> ```| Get jokes from controversial posts  | Active |
|```/joke/rising/<time_filter>/<limit> ```       | Get jokes form Rising posts         | Active |


### dependencies 
+ ```flask```
+ ```praw```


