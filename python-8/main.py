import jwt
from pprint import pprint

def create_token(data, secret):
    return jwt.encode(data, secret, algorithm='HS256')


def verify_signature(token):
    try:
        info = jwt.decode(token,'acelera', algorithm='HS256')
    except:
        return {"error": 2}
    else:
        return info

pprint(create_token({'language':'Python'},'acelera'))
pprint(verify_signature(b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsYW5ndWFnZSI6IlB5dGhvbiJ9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M'))