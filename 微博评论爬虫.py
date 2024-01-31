import requests
#1.发送请求，模拟浏览器对url地址发送请求
headers={
    #cookie用户信息（登陆）
    'Cookie':'UOR=,weibo.com,www.baidu.com; SINAGLOBAL=8646238999630.371.1705507417158; XSRF-TOKEN=ZPiOdfotqxGdwR6niKXzbYzT; ALF=1709280675; SUB=_2A25IvnDzDeRhGeFL7lYY-C_NwjWIHXVrsow7rDV8PUJbkNB-LWjDkW1NfedCkAJyBoCWu7jvh75ZKH6-ZRD9WrOe; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5JUlXjS2dmsNbgSMQm.U6W5JpX5KzhUgL.FoMfSKB41h2p1K.2dJLoIX2LxKqLBoBL1-zLxK-LBonL12eLxKqL1--L1h2LxK.L1K.L1K5LxKBLBonL12Hb9CH8SEHFxC-RxCH8SCHWxFHWSntt; _s_tentry=weibo.com; Apache=8945079503755.469.1706688698551; ULV=1706688698583:2:2:1:8945079503755.469.1706688698551:1705507417161; WBPSESS=-57qIS9i0nbVi5SP-CpPMdHhx1HG7ewKG-lwz4nFXlMEYw-wo3_vdhSfs8hkNxWaVboj3Cd5ceGqWTAqv80bJLgY7E0C29cZ2pHcm-DIsWeN82tUs42W3Cg_KVV8gVngwMmGB3q8BKN6BjkLxBbwPg==',
    #Referer防盗链
    'Referer':'https://weibo.com/2283007510/MykJm7m5j',
    #用户代理
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}
#请求网址(拆分写)
url='https://weibo.com/ajax/statuses/buildComments'
data={
    'is_reload': '1',
    'id': '4881828441753193',
    'is_show_bulletin':' 2',
    'is_mix': '0',
    'count': '10',
    'uid': '2283007510',
    'fetch_level':'0',
    'locale': 'zh-CN'
}
#发送请求
response=requests.get(url=url,params=data,headers=headers)
#2.获取响应数据
json_data=response.json()
#3.解析数据
m=0
content_list=json_data['data']
for index in content_list:
    m+=1
    name=index['user']['screen_name']
    content=index['text_raw']
    time=index['created_at']
    print('第',m,'条评论')
    print(name)
    print(content)
    print(time)
    print()









