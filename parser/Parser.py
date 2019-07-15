import requests
from bs4 import BeautifulSoup as bs
import re
import time
import json


def validTag(tag):
    with open('tags.json') as json_file:
        data = json.load(json_file)
    if tag in data['tags']: return True
    else: return False


def totalTags():
    with open('tags.json') as json_file:
        data = json.load(json_file)

    return f'{len(data["tags"])}'


def tokenizeTutorial(title, description, generated_tags):
    pattern = re.compile(r'\W+^[\+.]')

    titleList = list(re.sub(pattern, '', title).lower().split(" "))
    metaList = list(re.sub(pattern, '', description).lower().split(" "))

    [generated_tags.append(tag)
     for tag in list(titleList + metaList) if validTag(tag)]

    if len(generated_tags) == 0:
        generated_tags.append('other')

    #[generated_tags.append(tag) for elem in generated_tags if elem not in generated_tags]
    generated_tags = ' '.join(generated_tags).split()
    return list(set(generated_tags))


def parseTutorial(res):
    temporaryTags = []

    html = bs(res.text, "lxml")

    ogDescription = html.find('meta', property="og:description")
    description = html.find('meta', property="description")
    keywords = html.find(attrs={'name': 'keywords'})
    twitterTitle = html.find('meta', property="twitter:title")

    tutorialTitle = str(html.title.text).strip()

    [temporaryTags.append(str(tag.get("content")).lower()) for tag in html.find_all(
        'meta', property="article:tag") if tag != None]

    temporaryTags = list(filter(lambda x: validTag(x), temporaryTags))

    if ogDescription == None and description != None:
        tutorialDescription = str(description.get("content"))
    if description == None and ogDescription != None:
        tutorialDescription = str(ogDescription.get("content"))
    if ogDescription == None and description == None:
        tutorialDescription = "null"
    if keywords != None:
        keywords = keywords.get("content").replace(',', ' ')
        tutorialDescription = f'{tutorialDescription}{" "}{keywords}'
    if twitterTitle != None:
        twitterTitle = twitterTitle.get("content")
        tutorialDescription = f'{tutorialDescription}{" "}{twitterTitle}'

    return tutorialTitle, tutorialDescription, temporaryTags


def getTutorial(link):
    try:
        res = requests.get(link, headers={
                           'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36'})
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


def generateTags(link):
    response = getTutorial(link)
    tutorialTitle, tutorialDescription, temporaryTags = parseTutorial(response)
    tutorialTags = tokenizeTutorial(
        tutorialTitle, tutorialDescription, temporaryTags)

    return tutorialTags, tutorialTitle
