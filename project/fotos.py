import face_recognition as fr
from engine import reconhece_face, get_rostos

desconhecido = reconhece_face("./project/img/desconhecido.png")

if(desconhecido[0]):
    rosto_desconhecido = desconhecido[1]
    rostos_conhecidos, nomes_dos_rostos = get_rostos()
    resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    print(resultados)




else:
    print('Rosto não encontrado')