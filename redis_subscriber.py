import redis

r = redis.Redis(
    host='redis-13695.crce175.eu-north-1-1.ec2.redns.redis-cloud.com',
    port=13695,
    decode_responses=True,
    username="default",
    password="ewSjORoolIB7okIgfthyrWPHdFaog4sO",
)

pubsub = r.pubsub()
pubsub.subscribe("school")
for message in pubsub.listen():
    print(message)
    if message["type"] == "message":
        data = message["data"]
        if isinstance(data, str) and "контрольна робота" in data:
            with open("message.txt", mode="a", encoding="utf-8") as f:
                f.write(data + "\n")
