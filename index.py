#!python
print("content-type: text/html; charset=euc-kr")
print()
import cgi, os, view

form = cgi.FieldStorage()

print('''
<!DOCTYPE html>
<html>
  <body>
    Hi
  </body>
</html>
''')
