#Satoshi 9k1 Sentiment
import twitter
import pprint
import json

CONSUMER_KEY = '5b2mJxc4VFxkBjT77XvnpCT45'
CONSUMER_SECRET = 'Ll9gmcikUwBnh3DLHtjZuGwwtNjDbfwsr5aZtM9kvUxELbl9ka'
OAUTH_TOKEN = '962565255359447040-HYou9s5w31Z89tNc7VyDoL5ybI7HvQV'
OAUTH_TOKEN_SECRET = 'MV8nlPvIF8rbnOGsn7swufCIIcm75KSIMZXG9rowsW55f'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

print (twitter_api)

WORLD_WOE_ID = 1

US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

q = '#bitcoin'

count = 100

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

#iterate through 5 more batches of results by following the cursor

for _ in range(5):
    print ("Length of Statuses" , len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError as e: #No More results when next_results doesn't exist
        break

# create a dictionary from next_results, which has the following form
        kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']

#show one sample search result by slicing the list...
print(json.dumps(statuses[0], indent=1))