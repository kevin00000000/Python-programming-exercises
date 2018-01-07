import re
email = 'username@companyname.com'
match = re.search(r'\b(\w+)@(\w+)\.com', email)
username = ''
companyname = ''
if match != None:
    username = match.group(1)
    companyname = match.group(2)

print('username:{0:s}\ncompanyname:{1:s}'.format(username, companyname))