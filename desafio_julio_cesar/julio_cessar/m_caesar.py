import sys
import json
import hashlib
import requests

with open("answer.json", "r") as json_file:
    get = json.load(json_file)

#DECRIPT
alpha =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

c_array_msg = get['cifrado']

def func_decode(string):
    new_string = []
    for char in range(len(string)):
        new_string.append(string[char])
    return new_string

arr = func_decode(c_array_msg)

#FUNCTION 
def func_cripOrDescrip(number):
    msg = '' 
    for letter in arr:
        if letter in alpha:
            index = alpha.index(letter)                           
            i = index - number
            new_letter = alpha[i]
            new_index = alpha.index(str(new_letter))
            msg += new_letter
        elif letter == ' ':
                msg += ' '
        else:
             msg+= letter

    return msg

#Decript word and SH1
decript = func_cripOrDescrip(int(get['numero_casas']))
resumo = hashlib.sha1(decript.encode('UTF-8')).hexdigest()

#CREATE NEW DIC 
data = {}
data["numero_casas"] = get['numero_casas']
data["token"] = get["token"]
data["cifrado"] = get["cifrado"]  
data["decifrado"] = func_cripOrDescrip(data["numero_casas"])
data["resumo_criptografico"] = resumo

#WRITE FILE WITH NEW INFORMATION
file_new = open('answer.txt', 'w')
file_new.write(str(data))
file_new.close()

#REQUEST POST API WITH FILE TXT
url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=badb1909babde99888c15847aec2a54f17f61880'
files = {'answer': open('answer.txt', 'rb')}
newHeaders = {'Content-type': 'multipart/form-data'}
response = requests.post(url,files=files)
print(response.text.encode('utf8'))





