import re
import json
import os
import requests

from bs4 import BeautifulSoup as bs
from django.conf import settings

TAG_LOCATION = os.path.join(settings.BASE_DIR, 'taggie/tags.json')


def valid_tag(tag):
    """checks if a tag is valid with respect to tags.json"""
    with open(TAG_LOCATION) as json_file:
        data = json.load(json_file)

    return tag in data['tags']

# to be used for testing or from shell
def total_tags():
    """returns the total number of tags present in tags.json"""
    with open(TAG_LOCATION) as json_file:
        data = json.load(json_file)

    return f'{len(data["tags"])}'


def tokenize_tutorial(title, description, generated_tags):
    """tokenizes the tutorial"""
    pattern = re.compile(r'\W+^[\+.]')

    title_list = list(re.sub(pattern, '', title).lower().split(" "))
    meta_list = list(re.sub(pattern, '', description).lower().split(" "))

    generated_tags += list(filter(valid_tag, list(title_list + meta_list)))

    if len(generated_tags) == 0:
        generated_tags.append('other')

    generated_tags = ' '.join(generated_tags).split()

    return list(set(generated_tags))


def parse_tutorial(res):
    """parses the tutorial page"""
    temporary_tags = []

    html = bs(res.text, "lxml")

    og_description = html.find('meta', property="og:description")
    description = html.find('meta', property="description")
    keywords = html.find(attrs={'name': 'keywords'})
    twitter_title = html.find('meta', property="twitter:title")

    tutorial_title = str(html.title.text).strip()

    for tag in html.find_all('meta', property="article:tag"):
        if tag is not None:
            temporary_tags.append(str(tag.get("content")).lower())

    temporary_tags = list(filter(valid_tag, temporary_tags))

    if og_description is None and description is not None:
        tutorial_description = str(description.get("content"))
    if description is None and og_description is not None:
        tutorial_description = str(og_description.get("content"))
    if og_description is None and description is None:
        tutorial_description = "null"
    if keywords is not None:
        keywords = keywords.get("content").replace(',', ' ')
        tutorial_description = f'{tutorial_description}{" "}{keywords}'
    if twitter_title is not None:
        twitter_title = twitter_title.get("content")
        tutorial_description = f'{tutorial_description}{" "}{twitter_title}'

    return tutorial_title, tutorial_description, temporary_tags


def get_tutorial(link):
    """get request to the tutorial link"""
    res = None
    try:
        res = requests.get(link, headers={
            'User-Agent': 
                'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36'
                + '(KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36'
        })
        if res.status_code == 200:
            return res
        elif res.status_code == 403:
            raise Exception('Unautorized Access')
        elif res.status_code == 404:
            raise Exception('{} Not Found'.format(link))

    except requests.exceptions.InvalidURL as e:
        raise Exception(e)
    except requests.exceptions.MissingSchema as e:
        raise Exception(e)
    except requests.exceptions.ConnectionError as e:
        raise Exception(e)


def generate_tags(link):
    """generates tutorial tags"""
    response = get_tutorial(link)
    tutorial_title, tutorial_description, temporary_tags = parse_tutorial(
        response)
    tutorial_tags = tokenize_tutorial(
        tutorial_title, tutorial_description, temporary_tags)

    if 'ci/cd' in tutorial_tags:
        tutorial_tags[tutorial_tags.index('ci/cd')] = 'ci-cd'

    return tutorial_tags, tutorial_title
