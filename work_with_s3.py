import boto3

ACCESS_KEY = '4dd66d398a44366b982d6cad83defb3a'
SECRET_KEY = '4a14200736eeee6bfc4080630c872bc445f66a6464f149dbca4c6e5bd0b2c880'
BUCKET_NAME = 'firstbucket'
ENDPOINT = 'https://89c70d9f1a1abb774afba96c5fad59cb.r2.cloudflarestorage.com/firstbucket'
# ---------------------------------------------------------------------------


PUBLIC_URL = 'https://pub-59ffd09ba4df4dd9a01518c311e944c2.r2.dev'

s3client = boto3.client(
    's3',
    endpoint_url=ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name='EEUR'
)

# UPLOAD FILE

target_file_name = 'Yaroslav,jpg'
s3client.upload_file('spring.jpeg', BUCKET_NAME, target_file_name)
print(f'{PUBLIC_URL}/{BUCKET_NAME}/{target_file_name}')
