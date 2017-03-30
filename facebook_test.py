import os
import urllib2
import urllib
import subprocess
import pandas as pd
import requests
import csv
import xmllib
import cookielib 
import mechanize

def login_facebook():
	# Browser 
	br = mechanize.Browser() 

	# Enable cookie support for urllib2 
	cookiejar = cookielib.LWPCookieJar() 
	br.set_cookiejar( cookiejar ) 

	# Broser options 
	br.set_handle_equiv( True ) 
	br.set_handle_gzip( True ) 
	br.set_handle_redirect( True ) 
	br.set_handle_referer( True ) 
	br.set_handle_robots( False ) 

	# ?? 
	br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 ) 

	br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ] 

	# authenticate 
	br.open( 'https://www.facebook.com/' ) 
	# br.select_form( name="the name of the form from above" )
	br.select_form(nr=0)
	# these two come from the code you posted
	# where you would normally put in your username and password
	br[ "email" ] = 'USER HERE'
	br[ "pass" ] = 'PASSWORD'
	res = br.submit() 

	print "Success!\n"

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

print '_______________________________________________________________'
print 'Welcome to my scrapper'
print '_______________________________________________________________'
login_facebook()

text_to_search = 'Days N Daze'
text_to_search = urllib.quote(text_to_search)
search_page = requests.get('https://www.facebook.com/search/pages/?q=' + text_to_search)
tree_text = search_page.text

X=xmllib.XMLParser()
possible_names = {}
possible_links = {}
index = 0
for text_portion in tree_text.split('<div class="_3u1 _gli _5und"'):
	if '<div class="_5d-5">' in text_portion:
		potential_name = text_portion.split('<div class="_5d-5">')[1].split('</div>')[0]
		# possible_names.append(X.translate_references(potential_name))
		possible_names[index] = X.translate_references(potential_name)
		print text_portion.split('<div class="_5d-5">')[1].split('</div>')[0]
	if 'data-testid="serp_result_link' in text_portion:
		possible_links[index] = text_portion.split('<div><a href="')[1].split('" data-testid="serp_result_link')[0]
		print text_portion.split('<div><a href="')[1].split('" data-testid="serp_result_link')[0]

	index = index + 1

print possible_names
print possible_links







