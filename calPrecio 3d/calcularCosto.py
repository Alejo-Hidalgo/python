from tkinter import *


root = Tk()
root.geometry("400x400")
root.title("Calcular costo")


def calCostoSD():
    horas = float(horas_entry.get())
    minutos = float(minutos_entry.get())
    kwhPrecio = float(kwhPrecio_entry.get())
    cantMaterial = float(cantMaterial_entry.get())
    precioKg = float(precioKg_entry.get())
    
    horasImp = ((horas * 60) + minutos) / 60

    costeElectrico = (horasImp * 1.5) * kwhPrecio
    costeMaterial = cantMaterial * (precioKg / 1000)
    costeSD = costeElectrico + costeMaterial

    Label(text=f"Costo S/D: {costeSD}", font=("arial", 15, "bold")).grid(row=9, column=0, padx=5)
    
#def calCostoCD():
#    horas = float(horas_entry.get())
#   minutos = float(minutos_entry.get())
#    kwhPrecio = float(kwhPrecio_entry.get())
#    cantMaterial = float(cantMaterial_entry.get())
#    precioKg = float(precioKg_entry.get())
    
#    horasImp = ((horas * 60) + minutos) / 60

#    costeElectrico = (horasImp * 1.5) * kwhPrecio
#   costeMaterial = cantMaterial * (precioKg / 1000)
#    costeSD = costeElectrico + costeMaterial
    
#    hsDiseno = float(hsDiseno_entry.get())
#    precioDiseno = float(precioDiseno_entry.get())
#    costeCD = costeSD + (hsDiseno * precioDiseno)

#    Label(text=f"Costo C/D: {costeCD}", font=("arial", 15, "bold")).grid(row=10, column=0, padx=5)

    
Label(text="Horas", font=("arial", 15, "bold")).grid(row=1,column=0, padx=50)
Label(text="Minutos", font=("arial", 15, "bold")).grid(row=2,column=0, )
Label(text="kw/h precio", font=("arial", 15, "bold")).grid(row=3,column=0)
Label(text="Cant. material", font=("arial", 15, "bold")).grid(row=4,column=0)
Label(text="Precio kg", font=("arial", 15, "bold")).grid(row=5,column=0)
#Label(text="Horas Diseño", font=("arial", 15, "bold")).grid(row=6,column=0)
#Label(text="Precio x hs diseño", font=("arial", 15, "bold")).grid(row=7,column=0,padx=30)

horas_entry = StringVar()
minutos_entry = StringVar()
kwhPrecio_entry = StringVar()
cantMaterial_entry = StringVar()
precioKg_entry = StringVar()
#hsDiseno_entry = StringVar()
#precioDiseno_entry = StringVar()

horas_entry = Entry(root, textvariable=horas_entry)
minutos_entry = Entry(root, textvariable=minutos_entry)
kwhPrecio_entry = Entry(root, textvariable=kwhPrecio_entry)
cantMaterial_entry = Entry(root, textvariable=cantMaterial_entry)
precioKg_entry = Entry(root, textvariable=precioKg_entry)
#hsDiseno_entry = Entry(root, textvariable=hsDiseno_entry)
#precioDiseno_entry = Entry(root, textvariable=precioDiseno_entry)

horas_entry.grid(row=1, column=1, pady=5)
minutos_entry.grid(row=2, column=1, pady=5)
kwhPrecio_entry.grid(row=3, column=1, pady=5)
cantMaterial_entry.grid(row=4, column=1, pady=5)
precioKg_entry.grid(row=5, column=1, pady=5)
#hsDiseno_entry.grid(row=6, column=1, pady=5)
#precioDiseno_entry.grid(row=7, column=1, pady=5)

costoSinD = Button(text="Calcular costo S/D", font=("arial", 15, "bold"), fg="white", bg="#21130d", command=calCostoSD)
costoSinD.grid(row=8, column=1, pady=5)

#costoConD = Button(text="Calcular costo C/D", font=("arial", 15, "bold"), fg="white", bg="#21130d", command=calCostoCD)
#costoConD.grid(row=8, column=1, pady=5)


root.mainloop()
