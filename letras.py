from PIL import Image # Importando o módulo Pillow para abrir a imagem no script
import cv2
import img2pdf
import pytesseract # Módulo para a utilização da tecnologia OCR

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Caminho do Tesseract MUITO IMPORTANTE sem isso não funciona

for i in range(39):

    ind = i+1
    img_path = r'F:\Documentos\(OpenCV)\Aula\ilovepdf_pages-to-jpg\img ('+str(ind)+').jpg'
    image = cv2.imread(img_path)

    roi = image[200: 260, 390: 550]
    cv2.imwrite("out.jpg",roi)
    file_name = pytesseract.image_to_string( Image.open("out.jpg") )  # imagem de amostra

    pdf_path = r"C:/Users/pedro/Desktop/PDF/" + str(file_name)+ ".pdf"

    image = Image.open(img_path)
    pdf_bytes = img2pdf.convert(image.filename)
    file = open(pdf_path, "wb")
    file.write(pdf_bytes)
    image.close()
    file.close()

print("Todas imagens convertidas")