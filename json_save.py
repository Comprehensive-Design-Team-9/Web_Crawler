import json




def save_to_json(data, url, title, text, rep_path):
    # with open(rep_path, 'r') as json_file:
    #     data = json.load(json_file)
    data[url] = []
    data[url].append({"{}".format(title): "{}".format(text)})
    with open(rep_path, 'w', encoding='utf-8') as make_file:
        json.dump(data, make_file, ensure_ascii=False, indent=4)


