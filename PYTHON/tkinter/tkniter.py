import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")
etiqueta = tkinter.Label(ventana, text= "hola mundo") # aca utilizo label para poner algo dentro de la ventana

etiqueta.pack() #con esto pego en pantalla  los obejtos,  esto lo pega automaticamente

etiqueta2 = tkinter.Label(ventana, text = "ahora estoy en otro lado", bg = "red")
etiqueta2.pack(side= tkinter.BOTTOM, fill= tkinter.X) # con esto lo pongo abajo, y con FILL lo que hago esq estiro todo el bg o background en el eje que decida yo en este cas oe es el x


def hola():
    print ("hoal , funciono")








escribir = tkinter.Button(ventana, text= "algo", padx= 40, pady= 30, command= hola)
escribir.pack()
ventana.mainloop()