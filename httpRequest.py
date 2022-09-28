import requests
url = 'https://www.ibm.com/'
r = requests.get(url) # get request

# print(r.status_code) # 200
# print(r.headers)
# print(r.request.body) # no body in the request | none
# print(r.headers['date']) # date of the request
# print(r.headers['Content-Type'])

#----------------------------------------------------

url_get = 'http://httpbin.org/get'
payload = {'name':'Joseph','ID':'123'}

req = requests.get(url_get, params=payload)
print(req.url) # http://httpbin.org/get?name=Joseph&ID=123
print(req.json())

#----------------------------------------------------

# POST request

url_post = 'http://httpbin.org/post'
payload = {'name':'Joseph','ID':'123'}
                                # data instead of params
req_post = requests.post(url_post, data=payload)

print(req_post.url) # http://httpbin.org/post

#----------------------------------------------------

