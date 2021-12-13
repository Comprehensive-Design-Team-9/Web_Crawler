import requests
from bs4 import BeautifulSoup
import urllib.request
import os, re, sys
from time import sleep


def mkdir_img(dir_path, dir_name):

    if not (os.path.isdir(dir_path + dir_name)):
        os.makedirs(os.path.join(dir_path + dir_name))


def get_post_img(url, bin_str, img_save_path):
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit'
                      '/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    hs_n_b = "https://blog.naver.com"
    response = requests.get(url, headers=header)

    if response.status_code == 200:

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        post = soup.find('iframe')
        new_url = post.get('src')
        real_html = requests.get(hs_n_b + new_url).text
        #print("real html : ", real_html)
        real_soup = BeautifulSoup(real_html, 'html.parser')
        #print("real soup : ", real_soup)
        if real_soup.find_all('div', {'class': 'se-section se-section-image se-l-default se-section-align-center'}) != []:
            img_tag = real_soup.find_all('div', {'class': 'se-section se-section-image se-l-default se-section-align-center'})

            try:
                cnt = 1
                for get_imgUrl in img_tag:
                    #print(get_imgUrl)
                    a = 0
                    uuu = ""

                    # img_url = get_imgUrl.find("a")["img"]
                    # urllib.request.urlretrieve(img_url, img_save_path + url + '/' + str(cnt) + '.jpg')
                    # print(img_url)
                    # ---------------------------------------
                    img_url = get_imgUrl.find("img")["data-lazy-src"]#["data-linkdata"]
                    print(img_url)
                    # for i in img_url:
                    #     if i == "\"":
                    #         a += 1
                    #     if a == 7:
                    #         uuu = uuu + i
                    #     elif a == 8:
                    #         break
                    # uuu = uuu[1:]
                    #print(uuu)
                    mkdir_img(img_save_path, url)
                    #'[^0-9a-zA-Zㄱ-힗]'
                    #uuu = re.sub('[\(\)ㄱ-힗]', '', uuu)
                    #uuu = uuu.replace("\\ufeff", "")
                    #print(uuu)
                    #---------------------------------------
                    # try:
                    #     imgUrl = urllib.request.urlopen(header).read()  # 웹 페이지 상의 이미지를 불러옴
                    #     with open(uuu, "wb") as f:  # 디렉토리 오픈
                    #         f.write(imgUrl)  # 파일 저장
                    #     cnt += 1
                    #     print("images download")
                    # except urllib.error.HTTPError:
                    #     print('에러')
                    #     sys.exit(0)
                    urllib.request.urlretrieve(img_url, img_save_path + url + '/' + str(cnt) + '.jpg')
                    sleep(0.1)
                    cnt = cnt + 1
                bin_str = "1"
                return bin_str

            except:
                bin_str = "1"
                return bin_str
                print(error)
                pass

        else:
            print("fail")
            bin_str = "0"
            return bin_str

    else:
        print(response.status_code)

