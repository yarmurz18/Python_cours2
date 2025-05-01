"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-13695.crce175.eu-north-1-1.ec2.redns.redis-cloud.com',
    port=13695,
    decode_responses=True,
    username="default",
    password="ewSjORoolIB7okIgfthyrWPHdFaog4sO",
)

#r.set("favorite model", "Toyota Camry")

#r.set("favorite pet", "dog", ex=3600)

#r.lpush("product list", "milk", "bread", "cheese")
#r.expire("product list", 7 * 24 * 60 * 60)

#r.hset("Cake", mapping={"flour": 250, "milk": 500})
#r.hset("Cake", mapping={"sugar": 300})
#r.hset("Cake", mapping={"sugar": 500})
#
#r.delete("Cake")
#
i = 1

while i != 0:
    msg = input("Введіть повідомлення для каналу 'school': ")
    r.publish("school", msg)
