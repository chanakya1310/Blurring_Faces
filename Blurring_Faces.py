import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('Enter you image here') #Enter the image.
img=cv2.resize(img,(960,1032))
print(img.shape)
cv2.imshow('image',img)
cv2.waitKey()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4)
face=[]
print(img.shape)
print(faces)
count=0
for i in range(0,len(faces)):
    if faces[i][2]>=80:
        face.append(faces[i])
        count+=1
for i in range(0,len(face)):
    curr=face[i]
    x=curr[0]
    y=curr[1]
    w=curr[2]
    h=curr[3]
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255))
    sub_image=img[y:y+h,x:x+w]
    (hh,ww)=sub_image.shape[:2]
    # print(sub_image.shape)
    kW=int(ww/3)
    kH=int(hh/3)
    if kW%2==0:
        kW-=1
    if kH%2==0:
        kH-=1
    # print(kW,kH)
    blur=cv2.GaussianBlur(sub_image,(kW,kH),0)
    #Uncomment the below code to see each blurred face.
    #cv2.imshow('imagew',blur)
    #cv2.waitKey()
    img[y:y+h,x:x+w]=blur
cv2.imwrite('image2_output.jpeg',img)
cv2.imshow('image1',img)
cv2.waitKey()
cv2.destroyAllWindows()
