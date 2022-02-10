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
#     "apikey": "4e63991d70fe408d3278700cc0d0abe9",
#     "chat_id": "2a01:4f8:c17:ac8:3::16",
#     "chat_key": "4e63991d70fe408d3278700cc0d0abe9",
#     "chat_token": "tpUvBBfrqDegSyny",
#     "date_add": 1644480795,
#     "date_pay": 0,
#     "date_subscription": 0,
#     "date_trial": "null",
#     "id": 27,
#     "instanceId": "2a01:4f8:c17:ac8:3::16",
#     "is_premium": 0,
#     "md": 0,
#     "name": "",
#     "phone": "",
#     "platform": "",
#     "status": 0,
#     "token": "tpUvBBfrqDegSyny"
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

