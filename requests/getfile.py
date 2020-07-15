import requests
from bs4 import BeautifulSoup


params={
    "User-Agent":"Mozilla/5.0 (Linux; Android 10; LYA-AL00 Build/HUAWEILYA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/11.16 SP-engine/2.12.5 baiduboxapp/11.16.5.10 (Baidu; P1 10)"
}
url="http://60k.cn/read/13416/"
for i in range(1,1181):

    repon=requests.get(url+str(i),params=params)
    print(repon)
    soup=BeautifulSoup(repon.text,"html.parser")
    soup.encode("gbk")
    #print(soup)
    z=(soup.h3)
    zhangj=z.get_text()
    print(zhangj)
    w=soup.find('div', class_="read-content").get_text()

    with open('xs.txt','a')as f:
        f.write(zhangj)
        f.write("\n")
        f.write(str(w))
        f.write('\n')

