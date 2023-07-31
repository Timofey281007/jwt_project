import jwt
import datetime
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import config


def encode_jwt(payload: dict) -> str:
    encoded_jwt = jwt.encode(payload, config.JWT_SECRET, algorithm='HS256')
    return encoded_jwt


def decode_jwt(encoded_jwt: str) -> dict:
    try:
        decoded_jwt = jwt.decode(encoded_jwt,
                                 config.JWT_SECRET,
                                 algorithms=['HS256'])
        return decoded_jwt
    except ExpiredSignatureError:
        raise ValueError("Token has expired")
    except InvalidTokenError:
        raise ValueError("Invalid Token")


user_payload = {
    'my_name': 'Tim',
    'password': 'MichaelJordan23',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
    'iat': datetime.datetime.utcnow()
}

# my_jwt = encode_jwt(user_payload)
# print(my_jwt)
# print(decode_jwt(my_jwt))
