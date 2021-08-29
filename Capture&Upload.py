import cv2
import dropbox
import time
import random

sTime = time.time()

def take_snapshot():
    # start camera
    takePics = cv2.VideoCapture(0)
    result = True
    while(result):
        # taking one picture saved as img(random number).png if result is true
        ret,frame = takePics.read()
        number = random.randint(0,100)
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        sTime = time.time
        result = False
    return img_name
    # stop camera
    takePics.release()
    # close all camera windows
    cv2.destroyAllWindows()



def upload_file(img_name):
    access_token = "XYQkbTiSQ4YAAAAAAAAAAfmEFWs2lizNVP6pEWXSKiuVkPVwS-enpL_yid35jrtG"
    file = img_name
    file_from = file
    file_to = "/securityFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded!")


def main():
    while(True):
        if ((time.time() - sTime) >= 5):
            name = take_snapshot()
            upload_file(name)

main()