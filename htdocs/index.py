#!C:/Users/Administrator/AppData/Local/Programs/Python/Python39-32/python.exe
print("content-type: text/html; charset=euc-kr")
print()
import cgi, os, view

form = cgi.FieldStorage()
if "id" in form:
    pageId = form["id"].value
    description = open("data/"+pageId, "r").read()
    description = description.replace(">", "&lt;")
    description = description.replace("<", "&gt;")
    create_link = ""
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
      <form action="process_delete.py" method="post">
        <input type="hidden" name="pageId" value="{}">
        <input type="submit" value="delete">
      </form>
    '''.format(pageId)
else:
    pageId = "welcome"
    description = "Hello, web"
    create_link = '<a href="create.py">create</a>'
    update_link = ""
    delete_action = ""
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
    {create_link}
    {update_link}
    {delete_action}
        <h2>{title}</h2>
        <p>{desc}</p>
      </div>
    </div>
  </body>
</html>
'''.format(title=pageId, desc=description, list_str=view.get_list(), 
create_link=create_link, update_link=update_link, delete_action=delete_action))