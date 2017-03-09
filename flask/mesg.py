import requests
url = "http://api.onehop.co/v1/sms/send/"
payload = "mobile_number=9011855886&sms_text=hey how are you&label=PYTHON&sender_id=ONEHOP"
headers = {
   'apikey': "sm90d8df498024415d8f23347beb132c64",
   'content-type': "application/x-www-form-urlencoded",
   }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
