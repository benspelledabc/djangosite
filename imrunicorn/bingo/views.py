from django.shortcuts import render
from announcements.get_news import get_version_json, get_page_blurb_override
from imrunicorn.functions import step_hit_count_by_page
from content_collection.functions import leach_buzzword
from datetime import datetime
from .functions import get_bingo_card_buzz_words


def page_home(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Bingo: Home",
        "blurb": get_page_blurb_override('bingo/home/'),
    }
    return render(request, "bingo/home.html", context)


def page_buzz_words_or_phrases(request):
    step_hit_count_by_page(request.path)
    # lets hit the leach every time this page loads
    leach_buzzword()
    values = get_bingo_card_buzz_words()
    print(values)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Bingo: Buzz Words (or Phrases)",
        "values": values,
        "card_intent": "Take this buzz word card with you to your next meeting and play a game of Bingo instead of "
                       "sleeping.",
        "blurb": get_page_blurb_override('bingo/buzz_word/'),
    }
    return render(request, "bingo/bingo_card.html", context)
