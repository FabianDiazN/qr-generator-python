import qrcode
import cv2


convertir = input('Ingrese la cadena a converir a Qr: ')

img = qrcode.make(convertir)


img_file = open('qr_img.png', 'wb')


img.save(img_file)
img_file.close()
imagen=cv2.imread('qr_img.png')
cv2.imshow('Codigo QR generado',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
