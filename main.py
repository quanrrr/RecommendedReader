__metaclass__=type
import theoldreaderRss

rss = theoldreaderRss.TheoldreaderRss()
account = "qr2434061@gmail.com"
password = "theoldreader789456"
if rss.login(account,password) == True:
	rss.getAllUnreadContentFromWeb()

