import requests

print("check the site exist!!!")
print("enter your url(website): ")
target = input()
#parse text to know if https:// are wrote
first_part = target.split("/")
if first_part[0] != "https:":
    target = "https://" + target

try:
    x = requests.get(target)     
    if x.status_code == 200:
        print("the url(website) is a live")
        
    if x.status_code != 200:
        print("Error, the url(website) is a  NOt live!!!")
except:
    print("please enter a url correctly!")    
