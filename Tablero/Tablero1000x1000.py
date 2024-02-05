from tkinter import *



class Tablero(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title("Tablero 1000x1000")
        self.geometry("1000x1000+500+150")
        self.tablero = Canvas(self)
        self.tablero.pack(fill="both", expand = 1)
        self.cuadrado()

#En esta funcion cuadrado es donde identifico si el componente de la matriz es par o impar
    def cuadrado(self):
        for i in range(1000): 
            for j in range(1000): # cambiando el rango de i y j se cambia el tamaño de la matriz
                if(i+j)%2 == 0:
                    self.tablero.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="blue") #componente par
                else:
                    self.tablero.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="red") # componente impar



if __name__== "__main__":
    app = Tablero()
    app.mainloop()

# Hecho por Alejo Hidalgo. 
# Perfil de linkedin: https://www.linkedin.com/in/alejo-rom%C3%A1n-hidalgo/
