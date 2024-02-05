from tkinter import *



class Tablero(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title("Tablero 8x8")
        self.geometry("640x640+500+150")
        self.tablero = Canvas(self)
        self.tablero.pack(fill="both", expand = 1)
        self.cuadrado()


    def cuadrado(self):
        for i in range(8):
            for j in range(8):
                if(i+j)%2 == 0:
                    self.tablero.create_rectangle(i*80, j*80, (i+1)*80, (j+1)*80, fill="blue")
                else:
                    self.tablero.create_rectangle(i*80, j*80, (i+1)*80, (j+1)*80, fill="red")



if __name__== "__main__":
    app = Tablero()
    app.mainloop()
