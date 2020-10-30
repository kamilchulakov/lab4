import time
import json
import xmltodict


def doit():
    start_time = time.time()

    with open("Friday.xml", 'r', encoding="UTF-8") as f:
        xmlString = f.read()

    jsonString = json.dumps(xmltodict.parse(xmlString), indent=4, ensure_ascii=False)

    with open("Result2.json", 'w', encoding="UTF-8") as f:
        f.write(jsonString)

    print(time.time() - start_time)
