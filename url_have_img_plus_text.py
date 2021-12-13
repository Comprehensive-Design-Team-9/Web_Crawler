import csv

import csv_save


#final_list = []

def load_csv(csv_path, get_data):
    with open(csv_path, 'r', encoding='utf-8-sig') as read:
        read_csv = csv.reader(read)
        for i in read_csv:
            get_data.append(i)
        return get_data


def save_final_csv(list, csv_path):
    with open(csv_path, 'a', encoding='utf-8-sig', newline='') as csv_f:
        write_csv = csv.writer(csv_f)
        write_csv.writerow(list)
    csv_f.close()


def make_new_csv(text_csv, img_bin_csv, get_data_text, get_data_img_bin, final_save_path):
    text = load_csv(text_csv, get_data_text)
    img_bin = load_csv(img_bin_csv, get_data_img_bin)
    save_final_csv(text[0], final_save_path)

    j = 0
    for i in range(len(img_bin)):
        print(i)
        print(img_bin[i][2])
        if img_bin[i][2] == "1":
            print("have")
            save_final_csv([j, text[i][1], text[i][2],text[i][3]], final_save_path)
            j = j + 1
        else:
            print("None")




