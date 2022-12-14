# Requirement
We can use jproperties module to read properties file in Python. A properties file contains key-value pairs in each line. The equals (=) works as the delimiter between the key and value. A line that starts with # is treated as a comment.
```bash
  pip install jproperties
```
# how to run this code
this is just a simple program from producers and consumers using python, where the kafka cluster built already uses the HTTPS protocol, for settings can be completed in the [config.properties](config.properties) file
# Kafka REST Proxy
Kafka REST Proxy provides a RESTful interface to the Kafka cluster. That makes it easy to generate and deploy messages, view cluster status, and perform administrative actions without using Kafka's native protocols or clients. in this repository using the python programming language by creating a simple producer and consumer

# Quickstart
I took this part directly from the official documentation, you can check it out [here](https://github.com/confluentinc/kafka-rest)


```bash
    # Get a list of topics
    $ curl "http://localhost:8082/topics"
      
      ["__consumer_offsets","jsontest"]

    # Get info about one topic
    $ curl "http://localhost:8082/topics/jsontest"
    
      {"name":"jsontest","configs":{},"partitions":[{"partition":0,"leader":0,"replicas":[{"broker":0,"leader":true,"in_sync":true}]}]}

    # Produce a message with JSON data
    $ curl -X POST -H "Content-Type: application/vnd.kafka.json.v2+json" \
          --data '{"records":[{"value":{"name": "testUser"}}]}' \
          "http://localhost:8082/topics/jsontest"
          
      {"offsets":[{"partition":0,"offset":3,"error_code":null,"error":null}],"key_schema_id":null,"value_schema_id":null}

    # Create a consumer for JSON data, starting at the beginning of the topic's
    # log. The consumer group is called "my_json_consumer" and the instance is "my_consumer_instance".
    
    $ curl -X POST -H "Content-Type: application/vnd.kafka.v2+json" -H "Accept: application/vnd.kafka.v2+json" \
    --data '{"name": "my_consumer_instance", "format": "json", "auto.offset.reset": "earliest"}' \
    http://localhost:8082/consumers/my_json_consumer
          
      {"instance_id":"my_consumer_instance","base_uri":"http://localhost:8082/consumers/my_json_consumer/instances/my_consumer_instance"}
      
    # Subscribe the consumer to a topic
    
    $ curl -X POST -H "Content-Type: application/vnd.kafka.v2+json" --data '{"topics":["jsontest"]}' \
    http://localhost:8082/consumers/my_json_consumer/instances/my_consumer_instance/subscription
    # No content in response
      
    # Then consume some data from a topic using the base URL in the first response.

    $ curl -X GET -H "Accept: application/vnd.kafka.json.v2+json" \
    http://localhost:8082/consumers/my_json_consumer/instances/my_consumer_instance/records
      
      [{"key":null,"value":{"name":"testUser"},"partition":0,"offset":3,"topic":"jsontest"}]
   
    # Finally, close the consumer with a DELETE to make it leave the group and clean up
    # its resources.  
    
    $ curl -X DELETE -H "Accept: application/vnd.kafka.v2+json" \
          http://localhost:8082/consumers/my_json_consumer/instances/my_consumer_instance
      # No content in response
```

Contribute
----------

- Source Code: https://github.com/confluentinc/kafka-rest
- Issue Tracker: https://github.com/confluentinc/kafka-rest/issues