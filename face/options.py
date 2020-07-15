import base64
from face.face_field import face_field


image = "8.jpg"
#将图片编码成base64
def images(image):
    with open(image,"rb")as f:
        date=base64.b64encode(f.read())
        b64_date=date.decode(encoding="utf-8")
        # print(date)
        # print(b64_date)
        return b64_date



#人脸识别可选参数
def options(facecodename):
    options = {}
    options["face_field"] =facecodename
    # options["face_field"] = face_field()
    options["max_face_num"] = 1
    options["face_type"] = "LIVE"
    options["liveness_control"] = "LOW"
    #print(options)
    return options




if __name__ == '__main__':

    images(image)
    options()