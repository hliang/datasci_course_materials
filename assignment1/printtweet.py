
import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=pizza")

pyresponse = json.load(response)

results = pyresponse["results"]

for i in range(10):
  print "### tweet", i, "###"
  # print results[i]
  print results[i]["from_user"], results[i]["from_user_name"]
  print results[i]["text"]
