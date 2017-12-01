def get_names(empl):
    names = []
    for e in empl:
        for ch in e["children"]:
            if ch["age"] >= 18:
                names.append(e["name"])
    return names

ivan = {
    "name": "ivan",
    "age": 34,
    "children":[
        {
            "name": "vasja",
            "age": 12
        },
        {
            "name": "petja",
            "age": 10
        }
    ]
}

darja = {
    "name": "darja",
    "age": 41,
    "children":[
        {
            "name": "kirill",
            "age": 21
        },
        {
            "name": "pavel",
            "age": 15
        }
    ]
}

emps = [ivan, darja]
names = get_names(emps)
print(names)