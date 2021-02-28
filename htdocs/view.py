import os

def get_list():
    files = os.listdir("data")
    list_str = ""
    for item in files:
        list_str = list_str + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return list_str