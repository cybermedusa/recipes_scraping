import json

files = ["preparation_h4.json", "preparation_p.json", "preparation_ul.json"]


def merge_json(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open("preparation.json", "w") as output_file:
        json.dump(result, output_file, indent=4)


merge = merge_json(files)
