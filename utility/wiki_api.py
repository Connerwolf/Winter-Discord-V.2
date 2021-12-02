import wikipedia

def wiki(search,lenght=None):
    try:
        res = wikipedia.summary(search,sentences=lenght)
        return res

    except Exception:
        return None

def wiki_suggest(search):
    res = wikipedia.search(search)
    for r in res:
        res = {r}
        return res
