from __future__ import print_function
import twitter

CONSUMER_KEY = 'yLFt9Su095Apz47F2E5zATepq'
CONSUMER_SECRET = 'haHdXXIiYnXj8z3BgpsgYnqzrVGR160V2VFCUFcIZ3Pgehi6tK'
ACCESS_TOKEN = '560108105-2vqdLiEsNLVd7y8msdeGqwVSB4FBe3POyIjXmymJ'
ACCESS_TOKEN_SECRET = 'QD4iaIbJOU6c4Rv8LUvN6fWBGMPrYYDOWzCNxuRBEOL9i'


# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

users = api.GetFriends()
followers = api.GetFollowers()
print(api.GetHomeTimeline(count=10, since_id=None, max_id=None, trim_user=False, exclude_replies=False, contributor_details=False, include_entities=True))
print(followers)
print([u.screen_name for u in users])
