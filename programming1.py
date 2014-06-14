import os , urllib2 , urllib

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0')]
opener.addheaders.append(('Cookie', 'enigmafiedV4=my; PHPSESSID=mysession ; mission=yes'))

user = "rezk2ll"
myip = "ip"
values = {'ip':myip,'username':user}
post_data = urllib.urlencode(values)
response = opener.open('http://www.enigmagroup.org/missions/programming/1/', post_data)
file_handle = open('result.html', 'w')
file_handle.write(response.read())
file_handle.close