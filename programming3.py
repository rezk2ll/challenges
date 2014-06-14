import urllib2 , urllib , re 
import Image

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36')]
opener.addheaders.append(('Cookie', 'enigmafiedV4=my; PHPSESSID=mysession; __utma=115660889.2075853026.1402668604.1402668604.1402668604.1; __utmb=115660889.10.10.1402668604; __utmc=115660889; __utmz=115660889.1402668604.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'))
response = opener.open('http://www.enigmagroup.org/missions/programming/3/image.php')
html = response.read()

file_handle = open('captcha.jpg', 'wb')
file_handle.write(html)
file_handle.close

file_handle = open('captcha.jpg', 'rb')
img = Image.open(file_handle)
rgb_im = img.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))
file_handle.close

colors = str(r)+";"+str(g)+";"+str(b)
print "sending "+colors
values = {'color':colors,'submit':1}
post_data = urllib.urlencode(values)
opener.addheaders.append(('Referer', 'http://www.enigmagroup.org/missions/programming/3/image.php'))
response = opener.open('http://www.enigmagroup.org/missions/programming/3/image.php', post_data)
fi = open('3.html' ,'w')
fi.write(response.read())
fi.close