from APICredentials import * # module containing api APICredentials as variables
from random import randint
import markovify
import twitter
import re


api = twitter.Api(  consumer, # set these in the APICredentials module
                    consumer_secret,
                    access,
                    access_secret,
                    tweet_mode = 'extended')

user_name = '' # Twitter UserID without '@' as string

# Gets statuses. Set to exclude retweets and replies, pulling in 200 statuses
user_timeline = api.GetUserTimeline(screen_name = user_name, include_rts = False, exclude_replies = True, count = 200)

# Creates a string with all text content of user statuses
statuses = ""
for s in user_timeline:
    statuses += " " +  s.full_text

# Forces compatibility with ampersands
statuses = statuses.replace('&amp;', '&')
# Remove URL. I copied this off of stackoverflow. I have no idea how regex works
statuses = re.sub(r'^https?:\/\/.*[\r\n]*', '', statuses, flags=re.MULTILINE)

text_model = markovify.Text(statuses)

out_tweet = text_model.make_short_sentence(randint(140, 280))

try:
    status = api.PostUpdate(out_tweet)
except Exception as error:
    print("error updating status")
    print(error)
else:
    print("status updated succesfully")
    print(status.text)
