import requests
from bs4 import BeautifulSoup


def get_post_text(url, post_text):
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    hs_n_b = "https://blog.naver.com"
    response = requests.get(url, headers = header)
    if response.status_code == 200:

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        post = soup.find('iframe')
        new_url = post.get('src')
        real_html = requests.get(hs_n_b + new_url).text
        real_soup = BeautifulSoup(real_html, 'html.parser')
        if real_soup.find_all('div', {'class': 'se-main-container'}) != []:
            real_post = real_soup.find_all('div', {'class': 'se-main-container'})
            # print(real_post.get_text())
            for name in real_post:
                post_text.append(name.text)
                # print(len(name.text))
        else:
            post_text.append(None)
            # print(None)
        return post_text

    else:
        print(response.status_code)
