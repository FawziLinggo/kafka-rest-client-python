##
## Change IP, 
## if don't use SSL, changet protocol to HTTP,
## and remove --cacert and -u 
curl "https://IP:8082/topics/rest-proxy-test" --cacert /var/ssl/private/ca.crt  -u user:pass | jq

curl -X POST -H "Content-Type: application/vnd.kafka.json.v2+json" \
          --data '{"records":[{"value":{"name": "testUser"}}]}' \
          "https://IP:8082/topics/rest-proxy-test" --cacert /var/ssl/private/ca.crt  -u user:pass | jq

curl -X POST -H "Content-Type: application/vnd.kafka.v2+json" -H "Accept: application/vnd.kafka.v2+json" \
    --data '{"name": "group-rest", "format": "json", "auto.offset.reset": "earliest"}' \
    https://IP:8082/consumers/rest-proxy-test --cacert /var/ssl/private/ca.crt  -u user:pass | jq


curl -X POST -H "Content-Type: application/vnd.kafka.v2+json" --data '{"topics":["rest-proxy-test"]}' \
    "https://IP:8082/consumers/rest-proxy-test/instances/group-rest/subscription" --cacert /var/ssl/private/ca.crt  -u user:pass | jq


curl -X GET -H "Accept: application/vnd.kafka.json.v2+json" \
    "https://IP:8082/consumers/rest-proxy-test/instances/group-rest/records" --cacert /var/ssl/private/ca.crt  -u user:pass | jq

# Create a consumer, starting at the beginning of the topic's log:
curl -X POST \
     -H "Content-Type: application/vnd.kafka.v2+json" \
     --data '{"name": "ci1", "format": "json", "auto.offset.reset": "earliest"}' \
     https://IP:8082/consumers/cg1 --cacert private/ca.crt  -u user:pass

# Subscribe to the topic purchases:
curl -X POST \
     -H "Content-Type: application/vnd.kafka.v2+json" \
     --data '{"topics":["rest-proxy-test"]}' \
     https://IP:8082/consumers/cg1/instances/ci1/subscription --cacert private/ca.crt  -u user:pass

curl -X GET \
     -H "Accept: application/vnd.kafka.json.v2+json" \
     https://IP:8082/consumers/cg1/instances/ci1/records --cacert private/ca.crt  -u user:pass