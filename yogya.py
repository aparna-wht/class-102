import cv2
import dropbox
import time 
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    VideoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = VideoCaptureObject.read()
        image_name = "img" +str(number) +".png"

        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False
        
    return image_name
    
    print("SnapShot Taken")

    VideoCaptureObject.release()

    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BKFYU95WkHZs2Dr4kl9vXC3F2BPi-Ozc3bj0PXm6LTzgRbxLTRgSaGzSq1bjDq5r9m0QZAmaX1y-5yGpGgB1Wp0szwCTfwaqJ61rEHCuqObCHRVng1Ba6kSEiulY7Uu8JwnaOoagIzcw"
    file = img_name

    file_from = file
    file_to = "/Snap1/" + (img_name)
    
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("filesupload")
def main():
    while(True):
        if((time.time() - start_time) >= 300 ):
            name = take_snapshot()
            upload_file(name)

main()
