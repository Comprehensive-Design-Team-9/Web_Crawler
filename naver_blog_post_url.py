import requests
from bs4 import BeautifulSoup


def crawling_naver_blog_post_url(search_keyword, url_list, post_title_list):


    url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query={}".format(search_keyword)

    response = requests.get(url)
    try:
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            for i in range(1, 31):
                post_url = soup.select_one(
                    '#main_pack > section > div > div._list > panel-list > div:nth-child(1) > more-contents > div > ul > li:nth-child({}) > div.total_wrap.api_ani_send > div > a'.format(
                        i))

                #print(title.get("href"))
                will_use_url = post_url.get(("href"))
                if will_use_url[8] == "b" and will_use_url[13] == "n":
                    url_list.append(will_use_url)
                    #print(post_url.get_text())
                    post_title_list.append(post_url.get_text())

                else:
                    pass
            return url_list, post_title_list
    except:
        pass
    else:
        print(response.status_code)
