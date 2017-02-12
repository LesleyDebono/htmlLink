import urllib
from lxml import html

url = "http://www.canberratimes.com.au"
page = html.fromstring(urllib.urlopen(url).read())

for link in page.xpath("//a"):
    print "Name", link.text, "URL", link.get("href")
