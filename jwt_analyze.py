#! /usr/bin/python3
'''
Usage: python3 jwt_analyze.py -t eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiI.eyJ1c2VyIjoiYWRtaW4ifQ.6efk2VpsnN_
'''

import argparse
import base64
import json

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--token', help='Input JWT token')
args = parser.parse_args()

if not args.token:
    print("Invalid operation, try -h or --help")
    exit(1)

jwt_token = args.token

def analyze_jwt():
    header, payload, signature = jwt_token.split('.')
    header_decoded = base64.b64decode(header + "==").decode('utf-8')
    payload_decoded = base64.b64decode(payload + "==").decode('utf-8')

    print(f"Header - Raw: \n\033[92m{header_decoded}\033[0m")
    print("\n")
    print(f"Header - Pretty: \n\033[92m{json.dumps(json.loads(header_decoded), indent=4)}\033[0m")

    print("*" * 50)

    print(f"Payload - Raw: \n\033[92m{payload_decoded}\033[0m")
    print("\n")
    print(f"Payload - Pretty: \n\033[92m{json.dumps(json.loads(payload_decoded), indent=4)}\033[0m")

analyze_jwt()
