import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file, delimiter=",") -> list[dict]:

    with open(file) as f:
        data = f.readlines()
        data = [line.rstrip() for line in data]

    lists = [val.split(delimiter) for val in data]
    headlines = lists[0]
    list_of_dicts = []

    for lines in lists[1:]:
        dict_ = {headlines[element]: lines[element] for element in range(len(headlines))}
        list_of_dicts.append(dict_)

    return list_of_dicts

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
