#pylint:disable=E0001
import json
import requests

def get_hash(data):
    url = "https://my.telegram.org/auth/send_password"
    data = "%2B91"+data
    headers = {"Host: my.telegram.org","Connection: keep-alive","Content-Length: 21",'sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',"Accept: application/json, text/javascript, */*; q=0.01","X-Requested-With: XMLHttpRequest","sec-ch-ua-mobile: ?1","Save-Data: on","User-Agent: Mozilla/5.0 (Linux; Android 7.0; Micromax C1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type: application/x-www-form-urlencoded; charset=UTF-8","Origin: https://my.telegram.org","Sec-Fetch-Site: same-origin","Sec-Fetch-Mode: cors","Sec-Fetch-Dest: empty","Referer: https://my.telegram.org/auth?to=apps"}
    response = requests.post(url, data=data, headers=headers, timeout=5)
    j=json.loads(response)
    hash=j["random_hash"]
    return hash
    
    mo=str(input("Enter Mo=>"))
    print(get_hash(mo))