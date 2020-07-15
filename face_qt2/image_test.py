from face_qt2.apptesting import imgName
from face.auth import auth
from face.options import options,images

def cilent():
    cilent=auth()


    cilent.detect(images(imgName))