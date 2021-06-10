import requests
from bs4 import BeautifulSoup
import urllib.request
import os, re


def mkdir_img(dir_path, dir_name):

    if not (os.path.isdir(dir_path + dir_name)):
        os.makedirs(os.path.join(dir_path + dir_name))


def get_post_img(url, bin_str, img_save_path):
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    hs_n_b = "https://blog.naver.com"
    response = requests.get(url, headers=header)

    if response.status_code == 200:

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        post = soup.find('iframe')
        new_url = post.get('src')
        real_html = requests.get(hs_n_b + new_url).text
        real_soup = BeautifulSoup(real_html, 'html.parser')
        if real_soup.find_all('div', {'class': 'se-component se-image se-l-default'}) != []:
            img_tag = real_soup.find_all('div', {'class': 'se-component se-image se-l-default'})

            try:
                cnt = 1
                for get_imgUrl in img_tag:
                    a = 0
                    uuu = ""
                    img_url = get_imgUrl.find("a")["data-linkdata"]
                    #print(img_url)
                    for i in img_url:
                        if i == "\"":
                            a += 1
                        if a == 7:
                            uuu = uuu + i
                        elif a == 8:
                            break
                    uuu = uuu[1:]
                    print(uuu)

                    mkdir_img(img_save_path, url)
                    #'[^0-9a-zA-Zㄱ-힗]'
                    uuu = re.sub('[\(\)ㄱ-힗]', '', uuu)
                    uuu = uuu.replace("\\ufeff", "")
                    urllib.request.urlretrieve(uuu, img_save_path + url + '/' + str(cnt) + '.jpg')
                    cnt = cnt + 1
                bin_str = "1"
                return bin_str
            except:
                bin_str = "1"
                return bin_str
                pass

        else:
            bin_str = "0"
            return bin_str

    else:
        print(response.status_code)

