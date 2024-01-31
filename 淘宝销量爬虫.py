from DrissionPage import ChromiumPage
from account import USER_NAME,PASSWORD
import time
import re
import json


page=ChromiumPage()
page.listen.start('h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/')
#1.打开一个窗口
page.get("https://login.taobao.com/member/login.jhtml")
#2.匹配账号输入框并且输入账号信息
page.ele('xpath://input[@id="fm-login-id"]').input(USER_NAME)
#3.匹配密码输入框并且输密码信息
page.ele('xpath://input[@id="fm-login-password"]').input(PASSWORD)
#4.点击登录
page.ele('xpath://button[@class="fm-button fm-submit password-login"]').click()
time.sleep(2)
#打开商品页
page.get('https://s.taobao.com/search?area=c2c&commend=all&q=%E5%87%8F%E7%B3%96%E7%83%98%E7%84%99&search_type=mall&sourceId=tb.index&spm=a1z02.1.6856637.d4910789&ssid=s5-e')
m=0;
for i in range(5):
    page.ele('xpath://button[@class="next-btn next-small next-btn-normal next-pagination-item next-next"]').click()
    pack=page.listen.wait()
    mtopjsonp=re.findall('mtopjsonp\d+\((.*)\)',pack.response.body)[0]
    mtopdict=json.loads(mtopjsonp)
    itemsArray=mtopdict['data']['itemsArray']
    for item in itemsArray:
        title=item['title']
        price=item['price']
        realSales=item['realSales']
        procity=item['procity']
        shop_name=item['shopInfo']['title']
        m+=1
        print('第',m,'条数据')
        print('商品名:'+title)
        print('价格:',price)
        print('销量:',realSales)
        print('产地:',procity)
        print('店铺名:',shop_name)
        print()
    time.sleep(2)