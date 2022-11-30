import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}')
    return res


def pwned_api_check(password):
    sha1_hash_password = hashlib.sha1(password.encode('utf-8'))
    # check api res for password
