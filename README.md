# JWT-Scripts

## Analyze JWT Token
### Usage:
```
$ python3 jwt_analyze.py -h
usage: jwt_analyze.py [-h] [-t TOKEN]

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Input JWT token
```
```bash
$ python3 jwt_analyze.py -t '<JWT Token>'
```
<img src=assets/analyze_demo.png alt="JWT Analyze"></img>

## Generate JWT Token
### Usage:
```
$ python3 jwt_generate.py -h      
usage: jwt_generate.py [-h] [-H HEADER] [-P PAYLOAD] [-sk SECRET_KEY]

optional arguments:
  -h, --help            show this help message and exit
  -H HEADER, --header HEADER
                        jwt raw header
  -P PAYLOAD, --payload PAYLOAD
                        jwt raw payload
  -sk SECRET_KEY, --secret_key SECRET_KEY
                        secret key
```
```bash
$ python3 jwt_generate.py -H '<Header>' -P '<Payload>' -sk '<Secret>'
$ python3 jwt_generate.py -H '<Header>' -P '<Payload>'
```
<img src=assets/generate_demo.png alt="JWT Generate"></img>
