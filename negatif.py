import numpy as np
import cv2

cap = cv2.VideoCapture(0) #ntuk melakukan inisialisasi pada webcam. angka "0" menunjukkan bahwa yang digunakan adalah webcam internal pada pc.
print(cap.isOpened())

while(True): #untuk looping imshow, sehingga camera akan menangkap objek video secara realtime.
    ret, frame = cap.read() #untuk menangkap gambar dengan format berwarna /BGR
    abu=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #untuk mengkonversi objek video dari yang sebelumnya berwarna menjadi grayscale sebelum diubah menjadi gambar negatif.
    cv2.imshow('webcam', 255-abu) #untuk mengubah gambar dari skala keabuan menjadi gambar dengan skala negatif. 
    if cv2.waitKey(1) & 0xFF == ord('q'): #perintah untuk menghentikan program dengan menekan tombol q pada keyboard
        break


cap.realease()
cv2.destroyAllwindows()
