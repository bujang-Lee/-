#!C:/Users/Administrator/AppData/Local/Programs/Python/Python39-32/python.exe
print("content-type: text/html; charset=euc-kr")
print()
import cgi, os, view

form = cgi.FieldStorage()
if "id" in form:
    pageId = form["id"].value
    description = open("data/"+pageId, "r").read()
else:
    pageId = "welcome"
    description = "Hello, web"
print('''
<!DOCTYPE html>
<html>
  <head>
    <title>WEB1 - Welcome</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        {list_str}
    </ol>
    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
      </div>
    </div>
  </body>
</html>
'''.format(title=pageId, desc=description, list_str=view.get_list()))