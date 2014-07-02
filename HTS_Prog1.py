import urllib , urllib2 , re

bot = urllib2.build_opener()
bot.addheaders = [('User-agent' , 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36')]
bot.addheaders.append(('Cookie' , 'PHPSESSID=bomdates'))


f = open('wordlist.txt','rb')
lines = [line for line in f]
f.close()

def solveit(var,lt):
	for alt in lt:
		k = alt
		k = k.replace("\n",'')
		k = k.replace("\r",'')
		k = ' '.join(k.split())
		if sorted(var) == sorted(k):
			return k


resp = bot.open("https://www.hackthissite.org/missions/prog/1/")
html = resp.read()

words = re.findall(r'<td><li>(.*)</li>',html)
answers = []
for word in words:
	aa = word.replace("\n","")
	answers.append(solveit(aa , lines))
ch = ','.join(answers)
print ch
values = {"solution":ch}
post = urllib.urlencode(values)
bot.addheaders.append(('Referer', 'https://www.hackthissite.org/missions/prog/1/'))
send = bot.open("https://www.hackthissite.org/missions/prog/1/index.php",post)
html2 = send.read()
fk = open("hts.html", 'wb')
fk.write(html2)
fk.close()
