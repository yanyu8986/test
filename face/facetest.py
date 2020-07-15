from face.auth import auth
from face.options import images ,options

def face():
    client=auth()
    face_date=client.detect(images('8.jpg'),"BASE64",options())
    print(face_date)
    with open("facedate.txt",'a')as f:
        f.write(str(face_date))


if __name__ == '__main__':
    face()