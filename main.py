import praw
from prawcore import NotFound

def sub_exists(sub):
  exists = True
  try:
    reddit.subreddits.search_by_name(sub, exact=True)
  except NotFound:
    exists = False
  return exists

reddit = praw.Reddit(user_agent=True, client_id="YOURCLIENTID",client_secret="YOURCLIENTSECRET",username='ACCOUNTUSERNAME',password='ACCOUNTPASSWORD')


bold_start = '\033[1m'
bold_end   = '\033[0m'

def getSub():
  sub = input("What subreddit would you like to search?")
  if sub_exists(sub):
    subreddit = reddit.subreddit(sub)

    for submission in subreddit.stream.submissions():
      try:
        print(bold_start + submission.title + bold_end)
        print()
        print(20*"-")
        
      except Exception as e:
        print(str(e))
  else: 
    print("Subreddit does not exist. Please try another.")
    getSub()


getSub()
