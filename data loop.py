student=[{"name": "Joseph","score": 85},
{"name": "James","score": 70},
{"name": "Mary","score": 90},
{"name" :"tony","score": 65},
{"name" :"Tuu","score": 49},
{"name" :"Pom","score": 51}]

for x in student:
    if x["score"] >= 80:
        for key,vale in x.items():
            print(key,vale,"grade 4")
    elif x["score"] >= 70:
        for key,vale in x.items():
            print(key,vale,"grade 3")
    elif x["score"] >= 60:
        for key,vale in x.items():
            print(key,vale,"grade 2")
    elif x["score"] >= 50:
        for key,vale in x.items():
            print(key,vale,"grade 1")
    elif x["score"] < 50:
        for key,vale in x.items():
            print(key,vale,"grade 0")
#นายรัฐธีร์ ชัยจันทร์ ม.6/14 เลขที่32