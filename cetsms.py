from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import urllib2
import re
import sets
import sys
import cookielib
import datetime


from urllib import urlencode
import cgi
import urllib
import wsgiref.handlers
from google.appengine.ext import db
from google.appengine.api import users

class  Registration(db.Model):
  code = db.StringProperty()
  name = db.StringProperty()
  mobno = db.StringProperty()
  pwd = db.StringProperty()
  pro = db.StringProperty()
  #count = db.StringProperty()
class Code(db.Model):
  current = db.StringProperty()
  
def registration_key():
  return db.Key.from_path('RegistrationTable', 'registration_record')

def code_key():
  return db.Key.from_path('CodeTable', 'lastcode')

name = None  #user name
mobno = None #user mobile no
pro = None  #provider eg 160by2,site2sms
pswd = None #provider password
key = None  # send s or regiser r
code = None  #user registerd unique code
msg = None
urltosend = None
tono = None
TOTAL = 260

CONNECTION_ERROR = -1
SUCCESS = 1
class MainPage(webapp.RequestHandler): 
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'
    message=self.request.get_all('message' or '00')
    if message is None:
      sys.exit(1)    
    data=[]
    data=message[-1].split(' ') 
    a =1
    if a == 1 :
      uid =data[0]
      psw = data[1]
      code= data[1]
      cj = cookielib.CookieJar()
      opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
      opener.addheaders = [('User-Agent','Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:8.0) Gecko/20100101 Firefox/8.0')]
      url = 'http://117.211.100.44:8080/index.php'
      url_data = urlencode({'username':uid,'pswd':psw,'cmd':code})
      try:
	usock = opener.open(url, url_data) 
	   
      except IOError:      
	sys.exit(1)
          
	    	    
application = webapp.WSGIApplication(
    [('/', MainPage)],
    debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
	main()		                       
                        
