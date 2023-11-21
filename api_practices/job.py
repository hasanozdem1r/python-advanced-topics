import requests

HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Accept':
        'application/json, text/plain, */*',
    'accept-encoding':
        'gzip, deflate, br',
    'x-csrf-token':
        'x8H5xlPGncacH3uHcLZabdV9rA6i1FF2/n2nfnFPbxciMF8fxf0gHDgfzho9Yf0a+kcb/ViFiN9MtlP0/WcGnA==',
}

response = requests.get(url='https://justjoin.it/api/developers/me',
                        headers=HEADERS)
print(response)
