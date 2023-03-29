import json
def getter(roi):
    with open("API.json", "r") as r:
        data = json.load(r)
        r.close()
    print(data[roi])
    return data[roi]

def setter(roi, value):
    with open("API.json", "r") as r:
        data = json.load(r)
        r.close()

    data[roi] = value.replace("'", " ")
    data = str(data)
    data = data.replace("'", '"')
    with open("API.json", "w") as r:
        r.write(data)
        r.close()
