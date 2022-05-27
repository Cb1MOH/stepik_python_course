import requests

# r = requests.get('http://example.com')
# print(r.text)

url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies)

print(r.text)
print(r.cookies[''])