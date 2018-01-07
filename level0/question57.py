import re
email = 'username@companyname.com'
match = re.search(r'\b(\w+)@', email)
username = ''
companyname = ''
if match != None:
    username = match.group(1)
match = re.search(r'@(\w+)\.com', email)
if match != None:
    companyname = match.group(1)
print('username:{0:s}\ncompanyname:{1:s}'.format(username, companyname))