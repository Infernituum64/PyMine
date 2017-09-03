import requests

def download(url):
  return requests.get(url)
  
print (download("http://octopus-world.com").text())
