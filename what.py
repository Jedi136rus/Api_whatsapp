import requests
import json
import  base64

dict_head = {"X-Tasktest-Token": "f62cdf1e83bc324ba23aee3b113c6249",}
dict_params = {"full": 1,}

api = "https://dev.wapp.im/v3/"
method_chat = "chat/spare?crm=TEST&domain=test"
other_method = 'instance{ID}/{METHOD}?token={TOKEN}'

res = requests.get("https://dev.wapp.im/v3/chat/spare?crm=TEST&domain=test", headers=dict_head)
print(res.status_code)
print(json.dumps(res.json(), sort_keys=True, indent=4))
params = json.dumps(res.json(), sort_keys=True, indent=4)
params = json.loads(params)

# params = {
#     "apikey":
#     "chat_id": 
#     "chat_key": 
#     "chat_token": 
#     "date_add": 
#     "date_pay": 
#     "date_subscription": 
#     "date_trial":
#     "id":
#     "instanceId": 
#     "is_premium": 
#     "md": 
#     "name": 
#     "phone": 
#     "platform": 
#     "status":
#     "token": 
# }

res_status = api + other_method.format(ID=params["id"], METHOD="status", TOKEN=params['token'])  #Формирование qrCode
res_status = requests.get(res_status, headers=dict_head, params=dict_params)
print(res_status.status_code)

img_data = res_status.content
img_value = json.loads(img_data)
base64_img = img_value['qrCode']
base64_img = base64_img[base64_img.find(',')+1:]
with open("qrCode.png", "wb") as file:
    file.write(base64.b64decode(base64_img))
print(res_status.content)


url = "https://dev.whatsapp.sipteco.ru/v3/instance{ID}/sendMessage?token={TOKEN}".format(ID=params["id"], TOKEN=params['token']) #сообщение по API

payload={
"phone" : "79872745052",
"chat_id": params["chat_id"],
'body': 'Сообщение от Петр',
'sendSeen': '0',
'typeMsg': 'text',
}


response = requests.request("POST", url, headers=dict_head, data=payload)

print(response.text)
print(response.status_code)

