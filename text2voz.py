""""
Autor: Diego
FechaTermino: 08/11/2020
Descripcion: Este programa Traduce de voz a texto 
Agradecimiento a https://www.texttomp3.online que no sabe que uso el servicio de su web de forma automatizada
"""

from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests
#arreglar import urllib2 es para el GET si hacemos esta listo todo

def tex2file(text, archivo = "Audio"):
    """
    tex2voz(texto = [texto a ingresar], archivo = [Nombre de archivo])

    Esta funcion dvuelve en un archivo mp3 el texto ingresado.

    Sintaxis: 

    Ingrese el texto de la siguinte manera:
        - tex2file("texto de prueba")                    => crea .mp3 con mombre Audio.mp3
        - tex2file("texto de prueba", "nombre")          => crea .mp3 con mombre nombre.mp3 
        - tex2file("texto de prueba", "ubicacion/nombre")=> crea .mp3 con mombre nombre.mp3 en [ubicacion]
    
    """

    try:
        url = "https://www.texttomp3.online/php/logic/textToSpeech.php" 
        post_fields = {'backmusicFile': "", "backmusicvolume": "", "msg": str(text), "usebackmusic": "0", "voice": "3"}   

        request = Request(url, urlencode(post_fields).encode())
        json = urlopen(request).read().decode()
        #print(json)

        url2 =  "https://www.texttomp3.online/audio_tmp/" + json 
        r = requests.get(url2)  

        with open(archivo + ".mp3", "wb") as f:
            f.write(r.content)
        r.close()
    except:
        print("Error no podemos realizar la peticion")

#speechnotes.com/es
