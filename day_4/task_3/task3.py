# Task 3: Create a tool to parse the news feed and print them. You can choose any rss feed. These feeds are in XML and you need to print them as String.

import requests, xmltodict, json

def loadRSS():
    request  = "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
    response = requests.get(request)
    return response

def parseXML(response):
    data = xmltodict.parse(response.text)
    return data

def main():
    response = loadRSS()
    newsitems = json.dumps(parseXML(response), indent=4)
    print(newsitems, type(newsitems))

if __name__ == "__main__":
    main()