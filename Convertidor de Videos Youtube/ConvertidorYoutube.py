from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import re

root = Tk()
#Tamaño de la ventana en pixeles
root.geometry('500x300')
#Se desabilita la opcion de cambiar el tamaño.
root.resizable(0, 0)
#Se Coloca el titulo de la aplicacion
root.title('Convertidor de Youtube (CR8A)')
#Color de fondo
root.configure(bg='#AACDE2')
#Etiquetas de Texto en la que se  mostraran los mensajes del usuario.
Label(root, text='Descargador de Videos', 
      font='arial 20 bold', bg='#AACDE2').place(x=90, y=30)
#Se guarda la url  introducida por el usuario.
link = StringVar()
#Creamos un texto que nos proporciona informacion.
Label(root, text='Pega el link aquí:', font='arial 12', bg='#AACDE2').place(x=190, y=90)

#Creamos un  cuadro de entrada para escribir la URL.
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=120)

#Funcion para descargar el video
def download_video():
    #Comprobamos que la  url no este vacia.
    if link.get() == "":
        #Si lo esta nos saldra este mensaje con su color y fondo.
        label = Label(root, text='Ingresa una URL válida', font='arial 13 bold', bg='#AACDE2', fg='red')
        #El lugar en la pantalla donde aparecera
        label.place(x=150, y=150)
        #Cuanto tiempo estara visible, en este caso 1000 milisegundos ( 1 segundo )
        root.after(1000, lambda: label.destroy())
    else:
        #Si no esta vacia la URL realizará estas acciones.
        #Intentara
        try:
            #Guardar la url
            url = YouTube(str(link.get()))
            #Llama a la funcion extract_video_id para asegurarse que la URL es una URL valida.
            video_id = extract_video_id(str(link.get()))
            #Guarda dentro de Video el video en maxima resolución
            video = url.streams.get_highest_resolution()
            # Ventana de diálogo para seleccionar la carpeta de destino
            folder_path = filedialog.askdirectory()
            # Si ha seleccionado una carpeta el Usuario
            if folder_path:
                #Descargara el video con el nombre del mismo y terminado en .mp4 
                    #(Esto tambien podria servir para añadir mas botones y mas formatos de guardado)
                video.download(output_path=folder_path, filename = f"{video_id}.mp4")
                #Creamos un nuevo texto el cual aparecera durante 2,5 segundos y nos indicara que se ha descargado con exito el video
                label = Label(root, text='DESCARGADO', font='arial 13 bold', bg='#AACDE2', fg='#B57199')
                label.place(x=180, y=150)
                root.after(2500, lambda: label.destroy())
            #Si el usuario no selecciona una carpeta
            else:
                #Nos saldra un mensaje que nos indicara que hemos cancelado la accion y se destruye en 1 seg.
                label = Label(root, text='Selección cancelada', font='arial 13 bold', bg='#AACDE2', fg='red')
                label.place(x=150, y=150)
                root.after(1000, lambda: label.destroy())
        # Si surgiera algún error lo controlaria para que no crashee la app y mostraria el error a traves de un mensaje
        except ValueError as e:
            print(f"Error: {e}")

# Funcion para extraer el audio del video
def download_audio():
    # Identico a la funcion download_video
    if link.get() == "":
        label = Label(root, text='Ingresa una URL válida', font='arial 13 bold', bg='#AACDE2', fg='red')
        label.place(x=150, y=150)
        root.after(1000, lambda: label.destroy())  # Label will disappear after 5 seconds
    else:
        try:
            url = YouTube(str(link.get()))
            # Lo unico que nos quedamos es con el audio solamente
            audio = url.streams.filter(only_audio=True).first()
            
            # Igual que en la funcion download_video
            # Ventana de diálogo para seleccionar la carpeta de destino
            folder_path = filedialog.askdirectory()
            if folder_path:
                # Guardamos como .mp3 es la unica diferencia a la funcion download_video
                audio.download(output_path=folder_path, filename=f"{url.title}.mp3") 
                label = Label(root, text='DESCARGADO', font='arial 13 bold', bg='#AACDE2', fg='#B57199')
                label.place(x=180, y=150)
                root.after(2500, lambda: label.destroy())
            else:
                label = Label(root, text='Selección cancelada', font='arial 13 bold', bg='#AACDE2', fg='red')
                label.place(x=150, y=150)
                root.after(1000, lambda: label.destroy())
        except ValueError as e:
            print(f"Error: {e}")

# Función para extraer el Id del video
def extract_video_id(url):
    # Expresion Regular para obtener la ID de una URL de Youtube.
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    # Si esto es verdadero
    if match:
        # Devolvemos solo los caracteres entre las  llaves (entre v= y & o al final de la cadena)
        return match.group(1)
    # Si no
    else:
        # Mostramos el siguiente error.
        raise ValueError("Invalid YouTube URL. Please provide a valid YouTube video URL.")


#Boton para descargar el Video (MP4)
Button(root, text='DESCARGAR VIDEO', font='arial 13 bold italic', 
       bg='#B57199', padx=2, command=download_video).place(x=150, y=180)

# Botón para descargar audio (MP3)
Button(root, text='DESCARGAR AUDIO (MP3)', font='arial 13 bold italic',
       bg='#B57199', padx=2, command=download_audio).place(x=120, y=220)

# Mantiene en bucle la interfaz para que no se cierre hasta que el usuario le de a cerrar.
root.mainloop()
