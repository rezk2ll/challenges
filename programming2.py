import urllib2 , urllib , re

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36')]
opener.addheaders.append(('Cookie', 'enigmafiedV4=my; PHPSESSID=mysession; __utma=115660889.2075853026.1402668604.1402668604.1402668604.1; __utmb=115660889.10.10.1402668604; __utmc=115660889; __utmz=115660889.1402668604.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'))
response = opener.open('http://www.enigmagroup.org/missions/programming/2/','')
html = response.read()
fi = open('fi.html','w')
fi.write(html)
fi.close

num1 = re.search(r'number (.*) by' , html)
enum = re.search(r'ber]" value="(.*)"',html)
etime = re.search(r'me]" value="(.*)"',html)
ehash = re.search(r'sh" value="(.*)"',html)


x = int(num1.group(1))*4

values = {'answer':x,'E[number]':enum.group(1),'E[time]':etime.group(1),'hash':ehash.group(1),'submit':'Submit Answer'}
post_data = urllib.urlencode(values)
response = opener.open('http://www.enigmagroup.org/missions/programming/2/', post_data)
file_handle = open('result2.html', 'w')
file_handle.write(response.read())
file_handle.close