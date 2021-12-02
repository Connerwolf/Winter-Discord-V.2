import requests
import json
import random

with open("./setup/cog_config.json") as f:
    x = json.load(f)

def tenor(search_term):
        apikey = x["api_key"]
        lmt = 50
        urls = []
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        gifs = json.loads(r.content)
        for r in gifs["results"]:
            for m in r["media"]:
                g = m["gif"]
                res = g["url"]
                urls.append(res)
                
        
        return random.choice(urls)