import json

INPUT_FILE = "input.csv"
JEVSON = "result.json"


def csv_to_list_dict(dd) -> list[dict]:
    with open(INPUT_FILE, "r") as input_file:
        with open(JEVSON, "w") as output_file:
            list_dict_ = []
            stroki = input_file.readlines()
            zagolovki = stroki[0]
            zagolovki_otd = zagolovki.split(",")
            for i in range(1, 5):
                line_i = stroki[i]
                line_i = line_i.split(",")
                dict_i = {zagolovki_otd[k]: line_i[k] for k in range(0, 9)}
                list_dict_.append(dict_i)
            output_file.write(str(list_dict_))
    return list_dict_

            #for line in input_file:
                #tt = line.split(",")
                #output_file.write(str(tt))
                #output_file.write('\n')
    ...  # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
