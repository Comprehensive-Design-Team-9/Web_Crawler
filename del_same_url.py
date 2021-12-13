import pandas as pd

url_csv01 = "./data/all_url_title_text.csv"
url_csv02 = "./data/all_url_bin.csv"


def del_same_url_and_save(new_sub_csv, url_bin):
    post = pd.read_csv(new_sub_csv)
    img_bin = pd.read_csv(url_bin)
    print(len(post))
    print(len(img_bin))
    post.drop_duplicates(['url'], keep='first', inplace=True, ignore_index=True)
    #post.dropna(axis=0)
    img_bin.drop_duplicates(['url'], keep='first', inplace=True, ignore_index=True)
    #img_bin.dropna(axis=0)
    print(len(post))
    print(len(img_bin))
    post.to_csv(new_sub_csv)
    img_bin.to_csv(url_bin)


#del_same_url_and_save(url_csv01, url_csv02)
