from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import validators

root = Tk()
#Tamaño de la ventana en pixeles
root.geometry('500x300')
#Se desabilita la opcion de cambiar el tamaño.
root.resizable(0, 0)
#Titulo de la aplicacion.
root.title('Convertidor de Youtube (CR8A)')
#Color de fondo
root.configure(bg='#AACDE2')
#Etiquetas de Texto en la que se  mostraran los mensajes del usuario.
Label(root, text='Descargador de Videos', 
      font='arial 20 bold', bg='#AACDE2').place(x=90, y=30)
#Se guarda la url  introducida por el usuario.
link = StringVar()
#Etiquetas de Texto en la que se  mostraran los mensajes del usuario.
Label(root, text='Pega el link aquí:', font='arial 12',
      bg='#AACDE2').place(x=190, y=90)
#Se crea un campo donde se puede pegar la url que quieres descargar.
link_enter = Entry(root, width=70,
                   textvariable=link).place(x=32, y=120)

#Descarga el video de Youtube en la calidad mas alta.
def download_video():
        url = YouTube(str(link.get()))
        video = url.streams.get_highest_resolution()
#Muestra una ventana emergente para elegir el directorio destino.
    # Ventana de diálogo para seleccionar la carpeta de destino
        folder_path = filedialog.askdirectory()
        if folder_path:
            video.download(output_path=folder_path)  # Guarda en la carpeta seleccionada
            Label(root, text='DESCARGADO', font='arial 13 bold', 
                bg='#AACDE2', fg='#B57199').place(x=180, y=150)
        else:
            Label(root, text='Selección cancelada', font='arial 13 bold', 
                bg='#AACDE2', fg='red').place(x=150, y=150)
        
#Descarga el video de youtube en formato .mp3
def download_audio():
    url = YouTube(str(link.get()))
    audio = url.streams.filter(only_audio=True).first()
    # Ventana de diálogo para seleccionar la carpeta de destino
    folder_path = filedialog.askdirectory()
    if folder_path:
        audio.download(output_path=folder_path)  # Guarda en la carpeta seleccionada
        Label(root, text='DESCARGADO', font='arial 13 bold', 
              bg='#AACDE2', fg='#B57199').place(x=180, y=150)
    else:
        Label(root, text='Selección cancelada', font='arial 13 bold', 
              bg='#AACDE2', fg='red').place(x=150, y=150)



#Boton para descargar el Video (MP4)
Button(root, text='DESCARGAR VIDEO', font='arial 13 bold italic',
       bg='#B57199', padx=2, command=download_video).place(x=150, y=180)

# Botón para descargar audio (MP3)
Button(root, text='DESCARGAR AUDIO (MP3)', font='arial 13 bold italic',
       bg='#B57199', padx=2, command=download_audio).place(x=120, y=220)
#El programa entra en un bucle principal que mantiene la ventana abierta y responde a las interacciones del usuario.
root.mainloop()