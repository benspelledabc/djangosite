from django.shortcuts import render
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page
from datetime import datetime
from content_collection.functions import get_all_videos, get_latest_video, get_video_by_pk, \
    get_recent_pictures_for_carousel, get_all_pictures_for_carousel, get_all_dnd5e, get_all_fantasy_grounds
from django.shortcuts import render
from imrunicorn.decorators import allowed_groups
from .functions import get_shooting_challenges


def page_home(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Shooting Challenge: Blank",
        "blurb": get_page_blurb_override('shooting_challenge/home/'),
    }
    return render(request, "shooting_challenge/home.html", context)


# we'll make this a model update later.. for now its just hard coded... shhhhh
def page_shooting_challenges_list(request):
    step_hit_count_by_page(request.path)
    challenges = get_shooting_challenges(request)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Shooting Challenge",
        "blurb": get_page_blurb_override('shooting_challenge/list/'),
        "challenges": challenges,
    }
    return render(request, "shooting_challenge/challenge_list.html", context)


def page_2021_520y_egg_challenge_lkg(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Shooting Challenge",
        "blurb": "2021 520y Egg Challenge",
        "simple_info": "I've found that shooting shotgun clays that have been set on the ground is fun and challenging "
                       "it has a flaw. The flaw is sometimes the bullet just POKES through instead of causing it to "
                       "shatter. The shooter ends up putting several rounds in it and it never 'shatters'. Those repeat"
                       " hits ended up costing points in the scoring process because it was a 'missed shot'. It was "
                       "okay if we went to go look at them and CLEARLY saw 2 holes but if it has 1 hole THEN fractures,"
                       " sadly we could only count it as 1 hit and 1 miss.<br /><br /> "
                       "The plan THIS year.. is to get a piece of 2x4 and cut it into 5 inch slabs. Cut/mill holes in"
                       "the wood to form a cup in each piece. Line this cup lightly with some thing soft but not bulky "
                       "(t-shirt cloth perhaps). Finally put eggs on there! You end up with a piece of 2x4, lined with "
                       "padding topped with an egg. They are all separate from each other so a hit from one can't cause"
                       " the others to fall and fracture/break. Shots will be recorded using a slow motion video "
                       "hooked up to a spotting scope. This way we will know if you hit the target or hit the wood "
                       "and caused it to fall/break. To be analyzed after the set. "
                       "<br /><br /><strong>Challenge: Hit your 5 eggs at 520 yards. Fastest time wins, misses count "
                       "as 15 second penalty. Max of 10 rounds.</strong> "
                       "<br /><br />"
                       "Someone on a website pointed out that we could try eggs propped on a golf tee. Perhaps glued "
                       "to the egg to prevent it from falling off in the mostly gentle winds in the field."
                       "<br /><br />"
                       "A quick/small $10 entry fee will get you into the competition. The winner takes home 100% of "
                       "pot after event materials cost, I'm guessing this will be about $4-10 for the eggs, the rest "
                       "goes to the winner!",
        # "blurb": get_page_blurb_override('shooting_challenge/2021_520y_egg_challenge/'),
    }
    return render(request, "shooting_challenge/home.html", context)

