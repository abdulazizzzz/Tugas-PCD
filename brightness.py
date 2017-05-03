import numpy as np
import cv2

cap = cv2.VideoCapture(0) #ntuk melakukan inisialisasi pada webcam. angka "0" menunjukkan bahwa yang digunakan adalah webcam internal pada pc.
print(cap.isOpened())


while(True): #untuk looping imshow, sehingga camera akan menangkap objek video secara realtime.
    ret, frame = cap.read() #untuk menangkap gambar dengan format berwarna /BGR
    bright = cv2.addWeighted(frame,1.5, np.zeros(frame.shape, frame.dtype), 0, 25) #untuk meningkatkan nilai kecerahan gambar
    cv2.imshow('webcam',bright) #untuk menampilkan gambar yang tellah diubah tingkat kecerahannya.
    if cv2.waitKey(1) & 0xFF == ord('q'): #perintah untuk menghentikan program dengan menekan tombol q pada keyboard
        break


cap.realease()
cv2.destroyAllwindows()
