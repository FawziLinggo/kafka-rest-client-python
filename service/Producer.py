import requests
from props.properties import PropsConfig
Properties = PropsConfig()

# initialization from properties
url=Properties.url_producer
ca_crt=Properties.ca_crt
auth_=(Properties.user,Properties.password)
topic_name = Properties.topic_producer_name

# REST Header
headers = {
    'Content-Type': 'application/vnd.kafka.json.v2+json',
    'Accept': 'application/vnd.kafka.v2+json',
}

# REST Data
# Value is the message
# if not using "key" then we can remove "key" field
json_msg_1 ='{"name":"tis", "age":30, "city":"New York"}'
json_msg_2 ='{"name":"lala", "age":30, "city":"New York"}'
json_msg_3 ='{"name":"mama", "age":30, "city":"New York"}'
message = '{"records":[' \
          '{"key":"key_tes_1","value":%s},' \
          '{"key":"key_tes_2","value":%s},' \
          '{"value":%s}' \
          ']}' %(json_msg_1,json_msg_2,json_msg_3)

response = requests.post(url+topic_name,
                         headers=headers,
                         data=message,
                         verify=ca_crt,
                         auth=(auth_))
print(response)