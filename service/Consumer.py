from time import sleep
import requests
from props.properties import PropsConfig


Properties = PropsConfig()

# Consumer Config
auto_offset_reset = Properties.auto_offset_reset
group_id = Properties.group_id
topic_name = Properties.topic_consumer_name

# Rest Consumer Props
instance =Properties.instance
format_data =Properties.format_data
url_ = Properties.url_consumer

# Security
auth_=(Properties.user,Properties.password)
path_ca_crt =Properties.ca_crt

headers = {
    'Content-Type': 'application/vnd.kafka.json.v2+json', # must include comma
    }

headers_consumer = {
    'Accept': 'application/vnd.kafka.json.v2+json',# must include comma
}

properties_consumer = '{"name": "%s", "format": "%s", "auto.offset.reset": "%s"}' %(instance ,format_data, auto_offset_reset)

# create consumer group (if group.id already exists a response will appear <Response [409]>)
create_consumer_group = requests.post(url_+group_id, headers=headers, data=properties_consumer, verify=path_ca_crt, auth=(auth_))


# Subscribe to the topic (if group.id already exists a response will appear <Response [204]>)
subscribe_topic = requests.post(url_+group_id+'/instances/%s/subscription' %instance, headers=headers, data='{"topics":["%s"]}' %topic_name, verify=path_ca_crt, auth=(auth_))

# Subcrribe message from topic
subscribe_msg = requests.get(url_+group_id+'/instances/%s/records'%instance, headers=headers_consumer, verify=path_ca_crt, auth=(auth_))
print(create_consumer_group)
print(subscribe_topic)
print(subscribe_msg)


# must sleep 10 seconds ref : https://github.com/confluentinc/kafka-rest/issues/432
sleep(10)
print("Consumer running")

# while(True): #<Response [202]>
#     subscribe_msg = requests.get(url_+group_id+'/instances/%s/records'%instance, headers=headers_consumer, verify=path_ca_crt, auth=(auth_))
#     data = dump.dump_all(subscribe_msg)
#     print(subscribe_msg.headers) # headers output from GET append to array

while(True):
    subscribe_msg = requests.get(url_+group_id+'/instances/%s/records'%instance, headers=headers_consumer, verify=path_ca_crt, auth=(auth_))
    if(subscribe_msg.json()==[]):
        None
    else:
        print(subscribe_msg.json())