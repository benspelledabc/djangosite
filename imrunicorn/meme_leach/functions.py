from datetime import datetime
import requests
from .serializer import LeachedMemePreviewSerializer, LeachedMemeSerializer


def leach_save_if_new(meme_to_save):
    saved_entries = 0
    try:

        input_item = {
            "post_link": meme_to_save['postLink'],
            "subreddit": meme_to_save['subreddit'].lower(),
            "title": meme_to_save['title'],
            "url": meme_to_save['url'],
            "nsfw": meme_to_save['nsfw'],
            "spoiler": meme_to_save['spoiler'],
            "author": meme_to_save['author'],
            "ups": meme_to_save['ups']
        }

        serializer = LeachedMemeSerializer(data=input_item)
        if serializer.is_valid():
            serializer.save()
            saved_entries += 1
            print("Saved (without previews): {0}".format(meme_to_save))
        else:
            print("We already have this item meme.")
    except Exception as ex:
        print(ex)
    return saved_entries


def leach_post(link_only=False):
    url = "https://meme-api.herokuapp.com/gimme/"
    result = requests.get(url).json()
    leach_save_if_new(result)

    if link_only:
        return result['url']
    else:
        return result


def leach_post_subreddit(subreddit, link_only=False):
    url = "https://meme-api.herokuapp.com/gimme/{0}".format(subreddit)
    result = requests.get(url).json()
    leach_save_if_new(result)

    if link_only:
        return result['url']
    else:
        return result
