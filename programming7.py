import re , urllib , urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0')]
opener.addheaders.append(('Cookie', 'enigmafiedV4=mine; PHPSESSID=mine'))

resp = opener.open("http://www.enigmagroup.org/missions/programming/7/")
html = resp.read()

print "[+] EnigmaGroup.org :: Programming 7 \n"


depar = re.search(r'the (.*) department.',html)
department = str(depar.group(1))
comp = re.search(r'Company:  (.*)<br /><br />D',html)
companie = str(comp.group(1))

print "[+] Department : "+department
print "[+] abbreviation :"+companie

ss = re.search(r'<br />D(.*)<br />',html)
sx = ss.group(1)
text = sx.split('epartment: ')
x = 0

for z in text:
	if department in z:
		x1 = z.find('$')
		x2 = z.find(' ',x1)
		amount = z[x1+1:x2]
		x = x + int(amount)

print "[+] Amount :"+str(x)
aa = str(x)

values = {'company':companie,'department':department,'total': aa}
post_data = urllib.urlencode(values)
link = "http://www.enigmagroup.org/missions/programming/7/submit.php"
resp2 = opener.open(link,post_data)
html2 = resp2.read()

f = open('8.html','wb')
f.write(html2)
f.close

print "[+] Done !"
