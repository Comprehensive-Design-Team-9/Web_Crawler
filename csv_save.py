import csv


def make_csv(data, csv_path):
    with open(csv_path, 'a', encoding='utf-8-sig', newline='') as new_csv:
        write_csv = csv.writer(new_csv)
        write_csv.writerow(data)
    new_csv.close()


def save_to_csv(url, title, text, csv_path):
    with open(csv_path, 'a', encoding='utf-8-sig', newline='') as csv_f:
        write_csv = csv.writer(csv_f)
        write_csv.writerow([url,title,text])
    csv_f.close()


def img_have_none(url, bin_str, csv_path):
    with open(csv_path, 'a', encoding='utf-8-sig', newline='') as ihn:
        write_csv = csv.writer(ihn)
        write_csv.writerow([url, bin_str])
    ihn.close()

