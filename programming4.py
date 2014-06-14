import urllib2 , urllib , re 

import Image

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36')]
opener.addheaders.append(('Cookie', 'enigmafiedV4=my; PHPSESSID=mysession; __utma=115660889.2075853026.1402668604.1402668604.1402668604.1; __utmb=115660889.10.10.1402668604; __utmc=115660889; __utmz=115660889.1402668604.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'))
response = opener.open('http://www.enigmagroup.org/missions/programming/4/image.php')
html = response.read()

file_handle = open('pixel.jpg', 'wb')
file_handle.write(html)
file_handle.close

file_handle = open('pixel.jpg', 'rb')
img = Image.open(file_handle)
pix = img.load()
string = ""
x, y = img.size
 
for i in range(15, y): 
        for j in range(0, x):
                string += str(pix[j,i])
answer = ""
 
for i in range(0, string.__len__()/8):
        answer += str(chr(int(string[:8], 2)))
        string = string[8:]

print answer

values = {'answer':answer}
post_data = urllib.urlencode(values)
opener.addheaders.append(('Referer', 'http://www.enigmagroup.org/missions/programming/4/index.php'))
response = opener.open('http://www.enigmagroup.org/missions/programming/4/image.php', post_data)
fi = open('4.html' ,'w')
fi.write(response.read())
fi.close