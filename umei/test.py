import requests


testurl = "http://www.umei.cc/meinvtupian/xingganmeinv/3.htm"
headers = {
    'USER_AGENT':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"


}
response = requests.get(url=testurl,headers=headers)
print response.text
