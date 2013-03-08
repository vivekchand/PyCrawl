PyCrawl
=======

 Run as 
	python pycrawl.py <url>

 Eg:
  python pycrawl.py http://www.google.com

 Implementaion Notes:
 ====================
 1. Finds hyperlinks based on a regular expression
    <a\s*href=[\'|"](.*?)[\'"].*?>
 2. tovisit is the data structure used to store the links to be visited.
 3. visited stores the links that have been visited.
 4. 
   for link in (links.pop(0) for _ in xrange(len(links))): # Make link based on what it startswith from all links
    if link.startswith('/'):
      link = 'http://' + url[1] + link
    elif link.startswith('#'):
      link = 'http://' + url[1] + url[2] + link
    elif not link.startswith('http'):
      link = 'http://' + url[1] + '/' + link

   Iterates through all the links and check if it starts with '/' or '#' or 'http' and make an absolute link

	5.  
    if link not in visited:   # add to the list of visited if not visited
      tovisit.add(link)

		Add the tovisit only if the link is not already visited


  Exception Handling:
  ===================
  1.   
		try:
  	  visiting = tovisit.pop()  # Pop the top most unvisited link
	    print visiting            # Print it!
	  except KeyError:            # if the stack (tovisit) was empty
	    raise StopIteration       # time to stop Crawling!

   It raises an StopIteration when a KeyError occurs, specifically when tovisit is empty or no more pages to be visited
  
  2.
	  try:
  	  response = urllib2.urlopen(visiting) # Try open the visiting page
	  except urllib2.HTTPError, e:
	    print('EXCEPTION: HTTPError = ' + str(e.code))
	    continue
	  except urllib2.URLError, e:
	    print('EXCEPTION: URLError = ' + str(e.reason))
	    continue
	  except httplib.HTTPException, e:
	    print('EXCEPTION: HTTPException')
	    continue
	  except Exception:
	    import traceback
	    print('EXCEPTION: generic exception: ' + traceback.format_exc())
	    continue
 
 
