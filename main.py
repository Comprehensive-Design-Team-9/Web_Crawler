import requests
from bs4 import BeautifulSoup
import json
import naver_blog_post_url
import naver_blog_post_text
import naver_blog_post_img
import pandas as pd
import json_save
import csv_save
import time
from datetime import datetime
import search_keyword
import del_same_url
import url_have_img_plus_text

url_list = []
post_text = []
post_title_list = []
data = {}
today_hour = datetime.today().strftime("%Y%m%d%H%M%S")
#저장하고자 하는 위치
save_path = "./data/"
#rep_path = save_path + "uni_url_title_text.json"
csv_path = save_path + "all_url_title_text_{}.csv".format(today_hour)
img_csv_path = save_path + "all_url_bin_{}.csv".format(today_hour)
img_path = save_path + "naver_blog_post_img/"
index_text = ["url", "title", "text"]
index_img = ["url", "bin"]
get_data_text = []
get_data_img_bin = []
final_save = f"./final_{today_hour}.csv"


real_search_keyword_list = search_keyword.all_search_keyword_list #mini_yu_search_keyword_list

if __name__ == "__main__":
    start_time = time.time()
    print("make csv file")
    csv_save.make_csv(index_text, csv_path)
    csv_save.make_csv(index_img, img_csv_path)

    print("Working add 맛집")

    a = 0
    for i in real_search_keyword_list:
        real_search_keyword_list[a] = i + ' 맛집'
        a += 1
    print("Working get url")
    for i in real_search_keyword_list:
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

    del_same_url.del_same_url_and_save(csv_path, img_csv_path)

    url_have_img_plus_text.make_new_csv(csv_path, img_csv_path, get_data_text, get_data_img_bin, final_save)

    finish_time = time.time() - start_time
    print(finish_time/60)
    print("Finish !")




