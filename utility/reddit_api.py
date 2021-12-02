from datetime import date
import praw
import json
import random

with open("./setup/cog_config.json") as f:
    config = json.load(f)

def praw_get(search):
        reddit = praw.Reddit(
                                client_id = config["client_id"],
                                client_secret = config["client_secret"],
                                username = config["username"],
                                password = config["password"],
                                user_agent = config["user_agent"],
                                check_for_async = False
                            )
        submissions = reddit.subreddit(search).hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in submissions if not x.stickied)
        
        
        if "jpg" in submission.url or "png" in submission.url:
            return submission

        else:
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)
                return submission
