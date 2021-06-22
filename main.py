import requests
from bs4 import BeautifulSoup
import json
import naver_blog_post_url
import naver_blog_post_text
import naver_blog_post_img
import json_save
import csv_save
import time
from datetime import datetime

url_list = []
post_text = []
post_title_list = []
data = {}
today_hour = datetime.today().strftime("%Y%m%d%H%M%S")
#저장하고자 하는 위치
save_path = "저장하고자 하는 위치"
#rep_path = save_path + "uni_url_title_text.json"
csv_path = save_path + "all_url_title_text_{}.csv".format(today_hour)
img_csv_path = save_path + "all_url_bin_{}.csv".format(today_hour)
img_path = save_path + "naver_blog_post_img/"
index_text = ["url", "title", "text"]
index_img = ["url", "bin"]

#yu_search_keyword_list = ["대전 맛집", "유성구 맛집", "봉명동 맛집", "궁동 맛집", "죽동 맛집", "어은동 맛집", "장대동 맛집", "노은동 맛집"]

yu_search_keyword_list = ["가정동","갑동","계산동","관평동","교촌동","구룡동","구성동","구암동","궁동","금고동",
                         "금탄동","노은동","대동","대정동","덕명동","덕진동","도룡동","둔곡동","문지동","반석동",
                         "방동","방현동","복룡동","봉명동","봉산동", "상대동","성북동","세동","송강동","송정동",
                          "수남동","신동","신봉동","신성동","안산동","어은동","외삼동","용계동","용산동","원내동",
                          "원신흥동","원촌동","자운동","장대동","장동","전민동","죽동","지족동","추목동","탑립동",
                          "하기동","학하동","화암동"]


dae_search_keyword_list = ["갈전동","대화동","덕암동","목상동","문평동","미호동","법동","부수동","비래동","삼정동",
                           "상서동","석봉동","송촌동","신대동","신일동","신탄진동","연축동","오정동","와동","용호동",
                           "읍내동","이현동","장동","중리동","평촌동","황호동"]

dong_search_keyword_list = ["양동","가오동","구도동","낭월동","내탑동","대동","대별동","대성동","마산동","비룡동","사성동","삼괴동","삼성동","삼정동","상소동",
                            "성남동","세천동","소제동","소호동","신상동","신안동","신촌동","신하동","신흥동","오동","용계동","용운동","용전동","원동","이사동",
                            "인동","자양동","장척동","정동","주산동","주촌동","중동","직동","천동","추동","판암동","하소동","홍도동","효동","효평동"]

seo_search_keyword_list = ["가수원동","가장동","갈마동","관저동","괴곡동","괴정동","내동","도마동","도안동","둔산동","만년동","매로동","변동","복수동","봉곡동",
                           "산직동","삼천동","오동","용문동","용촌동","우명동","원정동","월평동","장안동","정림동","탄방동","평촌동","흑석동"]

zung_search_keyword_list = ["구완동","금동","대사동","대흥동","목달동","목동","무수동","문창동","문화동","부사동","사정동","산성동","석교동","선화동","안영동",
                            "어남동","오류동","옥계동","용두동","유천동","은행동","정생동","중촌동","침산동","태평동","호동"]

subway_search_keyword_list = ["반석역", "지족역", "노은역", "월드컵경기장역", "현충원역", "구암역", "유성온천역", "갑천역", "월평역", "갈마역",
                              "정부청사역", "시청역", "탄방역", "용문역", "오룡역", "서대전네거리역", "중구청역", "중앙로역", "대전역", "대동역",
                              "신흥역", "판암역"]

uni_search_keyword_list = ["충남대", "카이스트","한남대", "한밭대", "배재대", "목원대", "우송대", "건양대", "대전대", "국군간호사관학교",
                           "대덕대", "대전과기대", "대전보건대", "우송정보"]

city_search_keyword_list = ["대전"]

town_search_keyword_list = yu_search_keyword_list + dae_search_keyword_list + dong_search_keyword_list + seo_search_keyword_list + zung_search_keyword_list

all_search_keyword_list = uni_search_keyword_list + city_search_keyword_list + town_search_keyword_list


if __name__ == "__main__":
    start_time = time.time()
    print("make csv file")
    csv_save.make_csv(index_text, csv_path)
    csv_save.make_csv(index_img, img_csv_path)

    print("Working add 맛집")

    a = 0
    for i in all_search_keyword_list:
        all_search_keyword_list[a] = i + ' 맛집'
        a += 1
    print("Working get url")
    for i in all_search_keyword_list:
        naver_blog_post_url.crawling_naver_blog_post_url(i, url_list, post_title_list)

    #print(len(url_list))
    print(len(url_list))
    print(len(post_title_list))
    print("Working get post_text")

    num = 0
    bin_str = ""
    for url_data in url_list:
        naver_blog_post_text.get_post_text(url_data, post_text)
        csv_save.save_to_csv(url_data, post_title_list[num], post_text[num], csv_path)
        bin_str = naver_blog_post_img.get_post_img(url_data, bin_str, img_path)
        csv_save.img_have_none(url_data, bin_str, img_csv_path)
        num = num + 1
        print(num)


    finish_time = time.time() - start_time
    print(finish_time/60)
    print("Finish !")




