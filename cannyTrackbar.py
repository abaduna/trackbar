import cv2

def nada():
    pass


img = cv2.imread(r'C:\Users\Abadu\js\python\trackBars\imagenes\guisantes.jpg')
# reducimos la imagen
filas,columnes, _ =img.shape
img = cv2.resize(img,(columnes//10,columnes//10))
#Usar blur

img = cv2.blur(img,(5,5))

#creamos la ventana y barras deslizantes
cv2.namedWindow("canny")
cv2.createTrackbar("Umbral1","canny",0,500,nada)
cv2.createTrackbar("Umbral2","canny",0,500,nada)
while True:
    img2 = img.copy()
    a = cv2.getTrackbarPos("Umbral1","canny")
    b = cv2.getTrackbarPos("Umbral2","canny")
    imgCanny =cv2.Canny(img,a,b)
    #encrontrar y dibujar contornos
    contornos, _    = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img2, contornos,-1,(0,255,0),3)

    cv2.imshow("canny",imgCanny)
    cv2.imshow("contornos",img2)   
    if cv2.waitKey(1) == ord("s"):
        break
cv2.destroyAllWindows()