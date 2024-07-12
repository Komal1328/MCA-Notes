import glob 
import cv2
import sys
while True:
    #filename = input("Enter the file name in which images are present = ")
    for img in glob.glob(r'C:\Users\ASUS\Desktop\Emergency-Vehicle-Detection-master\images'+'/*.*'):
        try :
            var_img = cv2.imread(img)
            cv2.imshow(str(img) , var_img)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
        
        except Exception as e:
            print (e)
    user_input = raw_input("do you want to read another folder = ")
    if user_input == 'no':
        break
