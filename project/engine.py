import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    victor = reconhece_face("./project/img/victor.jpg")
    if(victor[0]):
        rostos_conhecidos.append(victor[1][0])
        nomes_dos_rostos.append("victor")

    nanda = reconhece_face("./project/img/nanda.png")
    if(nanda[0]):
        rostos_conhecidos.append(nanda[1][0])
        nomes_dos_rostos.append("nanda")
    
    return rostos_conhecidos, nomes_dos_rostos