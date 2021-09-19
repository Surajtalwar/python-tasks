##Task 1: Convert a dictionary object to JSON and then convert it back to JSON. Do the same with XML.


# json.dumps() - This method allows you to convert a python object into a serialized JSON object.
# json.dump() - This method allows you to convert a python object into JSON and additionally allows you to store the information into a file (text file)


a_dict = [
    {
        "name": "gara",
        "power": "some sand related jutsu",
        "powerlevel": 199,
        "frieds": [
            {
                "name": "Naruto",
                "friend_points": 28,
                "enemies": ["Saitama"] 
            },
            {
                "name": "Boruto",
                "friend_points": 18,
                "enemies": ["Saitama"]
            }
        ]
    },
    {
        "name": "Alex",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Soniya",
            "friend_points": 128,
            "enemies": ["Saitama"] 
            }
        ]
    },
    {
        "name": "King",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Saitama",
            "friend_points": 128,
            "enemies": ["Naruto", "gara", "boruto"] 
            }
        ]
    }
    
]
print("########### Converted to json ##########")
print()

# json.dumps() - This method allows you to convert a python object into a serialized JSON object.
# json.dump() - This method allows you to convert a python object into JSON and additionally allows you to store the information into a file (text file)

import json
json_object = json.dumps(a_dict, indent=4)
print(json_object)
print()

print("########### Converted to dict ##########")
print()

# json.loads() - Deserializes a JSON object to a standard python object.
# json.load() - Deserializes a JSON file object into a standard python object.

json_objects = json.loads(json_object)
print(json_objects, end="\n")
print()

print("########### Converting to XML ##########")
print()
import xmltodict

def convert_dict_xml(b):
    items = {'user': a_dict}
    main_root = {'users': items}
    return xmltodict.unparse(main_root, pretty=True)

print("########### Converting Back to DICT ##########")
print()
def convert_xml_dict(my_xml):
    return xmltodict.parse(my_xml)

new_xml = convert_dict_xml(a_dict)
print(f"Result of converting a dictionary to XML:\n{new_xml}\nType of the result is a JSON string format: {type(new_xml)}\n")

new_dict = convert_xml_dict(new_xml)
new_dict = new_dict['users']['user']
print(f"Result of converting a XML to dictionary:\n{json.dumps(new_dict, indent=4)}\nType of the result is a dictionary: {type(new_dict)}")


# dict_object=xmltodict.parse(xml_object)
# print(dict_object)
# print()
# Task 3: Given below logs try to parse them and get unique IP from where the requests are coming.
print("############## Unique IP's ##################")
print()
log = '''
TLSv1.2 AES128-SHA 1.1.1.1 "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 2.2.2.2 "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 3.3.3.3 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0"
TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 4.4.4.4 "Mozilla/5.0 (Android 4.4.2; Tablet; rv:65.0) Gecko/65.0 Firefox/65.0"
TLSv1 AES128-SHA 5.5.5.5 "Mozilla/5.0 (Android 4.4.2; Tablet; rv:65.0) Gecko/65.0 Firefox/65.0"
TLSv1.2 ECDHE-RSA-CHACHA20-POLY1305 6.6.6.6 "Mozilla/5.0 (Linux; U; Android 5.0.2; en-US; XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.2.1164 Mobile Safari/537.36"
TLSv1.2 AES128-SHA 1.1.1.1 "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 2.21.2.2 "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 3.31.3.3 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0"
TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 2.4.4.4 "Mozilla/5.0 (Android 4.4.2; Tablet; rv:65.0) Gecko/65.0 Firefox/65.0"
TLSv1 AES128-SHA 5.5.5.51 "Mozilla/5.0 (Android 4.4.2; Tablet; rv:65.0) Gecko/65.0 Firefox/65.0"
TLSv1.2 ECDHE-RSA-CHACHA20-POLY1305 6.6.6.6 "Mozilla/5.0 (Linux; U; Android 5.0.2; en-US; XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.2.1164 Mobile Safari/537.36"
'''


import re
compiling_values = re.compile(r'(\d{0,5}\.\d{0,5}\.\d{0,5}\.\d{0,5})')
matched_values = compiling_values.findall(log)
unique=set(matched_values)
for i in unique:
    print(i)