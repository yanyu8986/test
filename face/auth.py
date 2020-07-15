from aip import AipFace
import random

#随机先择api-id 认证
def auth():

    authlists=[{"APP_ID":"18839808","API_KEY":'QV2LvbW6g9e4zyc6mkK5EKhg',"SECRET_KEY":'XZGoi4RxZFtavbA7WXFfM5nEbYungG64'},

    {"APP_ID": "16077854", "API_KEY": 'dwq1n1Zd7hGVcnxEBrcxz0dy', "SECRET_KEY": 'QyAvxWG7qNHfkMix8jCQ1ahhiqaCsNTG'}]

    authlist=random.choice(authlists)
    # print(authlist)
    # print(type(authlist))

    client = AipFace(authlist["APP_ID"], authlist["API_KEY"], authlist["SECRET_KEY"])
    #print(client)
    return client

if __name__ == '__main__':

        print(auth())

