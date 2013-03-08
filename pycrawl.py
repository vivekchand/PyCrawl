import sys
import re
import urllib2
import urlparse
tovisit = set([sys.argv[1]])
visited = set([])
linkregex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')

while 1:  # Repeat Forever
	try:
		visiting = tovisit.pop()  # Pop the top most unvisited link
		print visiting            # Print it!
	except KeyError:            # if the stack (tovisit) was empty
		raise StopIteration       # time to stop Crawling!
	url = urlparse.urlparse(visiting) # Parse the URL 
	try:
		response = urllib2.urlopen(visiting) # Try open the visiting page
	except urllib2.HTTPError, e:
		print('EXCEPTION: HTTPError = ' + str(e.code))
		continue		 # If there is an exceptyion, continue with the next tovisit page
	except urllib2.URLError, e:
		print('EXCEPTION: URLError = ' + str(e.reason))
		continue		 # If there is an exceptyion, continue with the next tovisit page
	except httplib.HTTPException, e:
		print('EXCEPTION: HTTPException')
		continue		 # If there is an exceptyion, continue with the next tovisit page
	except Exception:
		import traceback
		print('EXCEPTION: generic exception: ' + traceback.format_exc())
		continue		 # If there is an exceptyion, continue with the next tovisit page
		
	page = response.read() # read the page
	links = linkregex.findall(page) # get all the links in the page matching with linkregex pattern
	visited.add(visiting) # add the visiting page to the list of visited page
	for link in (links.pop(0) for _ in xrange(len(links))): # Make link based on what it startswith from all links
		if link.startswith('/'):
			link = 'http://' + url[1] + link
		elif link.startswith('#'):
			link = 'http://' + url[1] + url[2] + link
		elif not link.startswith('http'):
			link = 'http://' + url[1] + '/' + link

		if link not in visited:   # add to the list of visited if not visited
			tovisit.add(link)

