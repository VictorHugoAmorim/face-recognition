import dlib
import face_recognition as fr
import numpy as np
import cv2

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if (len(rostos) > 0):
        return True, rostos
    else:
        False,rostos

def get_rostos():
    #lista dos rostos
    rostos_conhecidos = []
    nomes_dos_rostos = []
    nanda = reconhece_face("./project/img/nanda.png.png")
    if(nanda[0]):
        rostos_conhecidos.append(nanda[1][0])
        nomes_dos_rostos.append('Nanda')

    victor = reconhece_face("./project/img/victor.pngr.png")
    if(victor[0]):
        rostos_conhecidos.append(nanda[1][0])
        nomes_dos_rostos.append('victor')
    return rostos_conhecidos, nomes_dos_rostos
