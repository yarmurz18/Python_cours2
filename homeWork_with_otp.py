import datetime
import time

import jwt

secret1 = "wokfa4ajsv9223098423JDH"
secret2 = "wokfa4a9223098423JDH"
secret3 = "wa4a9223098423JDH"

payload1 = {
    "The_name_of_my_favorite_city": "Kharkiv",
    "my_name": "Yaroslav",
    "age": 14,
    "exp": datetime.datetime.now(datetime.timezone.utc)
    + datetime.timedelta(seconds=1000),
}

encode_jwt1 = jwt.encode(payload=payload1, key=secret1, algorithm="HS256")
print(encode_jwt1)

decoded1 = jwt.decode(
    encode_jwt1,
    secret1,
    algorithms=["HS256"],
)
print(decoded1)

payload2 = {
    "The_name_of_my_favorite_city": "Kyiv",
    "my_name": "Yaroslav",
    "age": 14,
    "exp": datetime.datetime.now(datetime.timezone.utc)
    + datetime.timedelta(seconds=10),
}

encode_jwt2 = jwt.encode(payload=payload2, key=secret2, algorithm="HS256")
time.sleep(15)

decoded2 = jwt.decode(
    encode_jwt2,
    secret2,
    algorithms=["HS256"],
)
print(decoded2)

payload3 = {
    "The_name_of_my_favorite_city": "Lviv",
    "my_name": "Yaroslav",
    "age": 14,
    "exp": datetime.datetime.now(datetime.timezone.utc)
    + datetime.timedelta(seconds=500),
}

encode_jwt3 = jwt.encode(payload=payload3, key=secret3, algorithm="HS256")

decoded2 = jwt.decode(
    encode_jwt3,
    secret1,
    algorithms=["HS256"],
)
print(decoded2)
