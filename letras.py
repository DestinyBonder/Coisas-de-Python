from PIL import Image # Importando o módulo Pillow para abrir a imagem no script
import cv2
import img2pdf
import pytesseract # Módulo para a utilização da tecnologia OCR

n = 168
vet = [n]
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Path do Tesseract MUITO IMPORTANTE sem isso não funciona

for i in range(n):

    ind = i+1
    img_path = r'C:\Users\pedro\Desktop\IMG\img ('+str(ind)+').jpg'
    image = cv2.imread(img_path)

    roi = image[380: 500, 800: 1100]
    cv2.imwrite("out.jpg",roi)
    file_name = pytesseract.image_to_string( Image.open("out.jpg") )  # imagem de amostra
    file_name = file_name.replace('>', '').replace('<', '').replace('/', '').replace( '\n' , '').replace(':', ''
                                ).replace('?','').replace('*', '').replace('|', '').replace('\\','')


    #if file_name == '':
     #   file_name = str(ind)

    vet.append(file_name)

    j = 0
    while j <= i:
        if file_name == vet[j]:
            file_name = file_name+'_'
            j = 0
            n =+1
        else:
            j += 1

    vet[i] = file_name

    pdf_path = r"C:/Users/pedro/Desktop/PDF/" + str(file_name)+ ".pdf"

    image = Image.open(img_path)
    pdf_bytes = img2pdf.convert(image.filename)


    file=open(pdf_path, "wb+")
    file.write(pdf_bytes)
    image.close()
    file.close()

print("Todas imagens convertidas")