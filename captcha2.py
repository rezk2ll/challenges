import urllib2 , urllib , re , Image , os
from PIL import Image
import ImageEnhance
import sys

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36')]
opener.addheaders.append(('Cookie', 'enigmafiedV4=thisismine; PHPSESSID=alsomine; __utma=115660889.2075853026.1402668604.1402668604.1402668604.1; __utmb=115660889.10.10.1402668604; __utmc=115660889; __utmz=115660889.1402668604.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'))
while( 1 < 10):
	response = opener.open('http://www.enigmagroup.org/missions/captcha/2/image.php')
	html = response.read()

	file_handle = open('captcha.png', 'wb')
	file_handle.write(html)
	file_handle.close
	file_handle = open('captcha.png', 'rb')
	im = Image.open("captcha.png")
	im = im.convert('L')
	im = im.point(lambda x:255 if x>43 or x < 37 else x)
	im = im.point(lambda x:0 if x<37 and x < 40 else x)
	im.save("bam.png")
	os.system("tesseract bam.png a")
	f = open("a.txt",'rb')
	xxx = f.read()
	f.close()
	xxx = xxx.replace('\n', '')
	xxx = xxx.replace(' ', '')
	xxx = xxx.replace(',', '')
	xxx = xxx.replace('_', '')
	xxx = xxx.replace('?', '')
	xxx = xxx.replace('-', '')
	xxx = xxx.replace('.', '')
	xxx = xxx.replace('\'', '')
	xxx = re.sub(r'\W+', '', xxx)
	print "[+] Captcha :" + xxx

	values = {'answer':xxx,'submit':'true'}
	post_data = urllib.urlencode(values)
	opener.addheaders.append(('Referer', 'http://www.enigmagroup.org/missions/captcha/2/image.php'))
	response = opener.open('http://www.enigmagroup.org/missions/captcha/2/image.php', post_data)

	fi = open('c1.html','w')
	fi.write(response.read())
	fi.close
