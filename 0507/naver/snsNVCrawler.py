import datetime
import json
import urllib.request
from config import *

#[CODE 1]
def get_request_url(url):

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    try:
        response = urllib.request.urlopen(req)
        print('******************************************************')
        print(response)
        print('******************************************************')
        if response.getcode() == 200:
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(),
                                          url))
        return None

#[CODE 2]
def getNaverSearchResult(sNode, search_text, page_start, display):

    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % sNode
    parameters = "?query=%s&start=%s&display=%s" %(urllib.parse.quote(search_text),
                                                   page_start, display)
    url = base + node + parameters
    print("==========================================================")
    print("url =", url)
    print("==========================================================")

    retData = get_request_url(url)
    print("retData =", retData)

    if (retData == None):
        return None
    else:
        print(retData)
        return json.loads(str(retData))

# [CODE 3]
def getPostData(post, jsonResult):
    print()
    title = post['title']
    description = post['description']
    #org_link= post['originallink']
    org_link = post['bloggerlink']
    link = post['link']
    pDate = post['postdate']
    bloggername = post['bloggername']

    jsonResult.append({'title':title, 'description':description,
                       'org_link':org_link, 'link': link,
                       'pDate':pDate, 'bloggername':bloggername})
    return

def main():

    jsonResult =[]

    # 'news', 'blog', 'cafearticle'
    sNode = 'blog'
    search_text = '코로나'
    display_count = 5

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)
    print("jsonSearch =",jsonSearch)
    print('----------------------------------------------------------------------------------------')
    while ((jsonSearch !=None) and (jsonSearch['display'] != 0)):
        for post in jsonSearch['items']: # 'items' key에 기사가 저장되어 있음
            print("################################################################################")
            print(post)
            print("################################################################################")
            getPostData(post, jsonResult)

        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)

    with open('%s_naver_%s.json' %(search_text, sNode), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,
                             indent=4, sort_keys=True,
                             ensure_ascii=False)
        outfile.write(retJson)

    print('%s_naver_%s.json SAVED' %(search_text, sNode))

if __name__ == '__main__':
    main()