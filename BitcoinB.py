import os
import pandas as pd
from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import datetime

path = os.path.abspath(os.path.dirname(__file__))
df = pd.read_csv(path+"/BTCUSD_day.csv", encoding="utf-8", parse_dates= True)


# Funciones:
def actualizar():
    """Actualiza los valores entre las fechas elegidas por el usuario"""
    fecha_min = fecha_desde.get()
    fecha_max = fecha_hasta.get()
    df_filtrado = df[(fecha_min<df["Date"]) & (df["Date"]<fecha_max)]
    lbl15 =Label(text= (df_filtrado["Close"].shape), font=("Arial Bold", 10)) # Cantidad de días analizados
    lbl15.grid(column=1, row=9)
    lbl16 =Label(text=(df_filtrado["Close"].max()), font=("Arial Bold", 10)) #Maximo valor de cierre
    lbl16.grid(column=1, row=10)
    lbl17 =Label(text=(df_filtrado["Close"].mean()), font=("Arial Bold", 10)) #Promedio valor de cierre
    lbl17.grid(column=1, row=11)
    lbl18 =Label(text=(df_filtrado["Close"].min()), font=("Arial Bold", 10)) # Minimo valor de cierre
    lbl18.grid(column=1, row=12)
    lbl19 =Label(text=(df_filtrado["High"].max()), font=("Arial Bold", 10)) # Valor maximo alcanzado
    lbl19.grid(column=1, row=13)
    lbl20=Label(text=(df_filtrado["Low"].min()), font=("Arial Bold", 10)) # Valor minimo alcanzado
    lbl20.grid(column=1, row=14)


def grafico_1():
    """Gráfico histórico de valor del bitcoin"""
    plt.close("all")
    seleccion = df[["Date","Close"]]
    seleccion.plot.line()
    plt.show()


def grafico_2():
    """Gráfico entre las fechas elegidas por el usuario"""
    fecha_min = fecha_desde.get()
    fecha_max = fecha_hasta.get()
    df_filtrado = df[(fecha_min<df["Date"]) & (df["Date"]<fecha_max)]
    plt.close("all")
    frecuencias = df_filtrado["Close"]
    frecuencias.plot.line()
    plt.show()

def guardar():
    """Guarda un .csv con los datos entre las fechas elegidas"""
    fecha_min = fecha_desde.get()
    fecha_max = fecha_hasta.get()
    df_filtrado = df[(fecha_min<df["Date"]) & (df["Date"]<fecha_max)]
    now = datetime.datetime.now()
    fechaTexto = pd.to_datetime(now).strftime("%Y_%m_%d__%H_%M_%S ")
    df_filtrado.to_csv(path+"/"+fechaTexto+".csv", encoding="utf-8", decimal=",")

window = Tk()
window.title("Bienvenidos al proyecto final")
window.geometry('600x500')

# Labels
lbl1 = Label(text="Análisis del valor de Bitcoin histórico (Se toma el valor de cierre del mercado).", font=("Arial Bold", 10))
lbl2 = Label(text="Seleccione la fecha inicial:", font=("Arial Bold", 10))
lbl3 = Label(text="Seleccione la fecha final:", font=("Arial Bold", 10))
lbl6 = Label(text="Total de días analizado:", font=("Arial Bold", 10))
lbl7 = Label(text="Valor máximo:", font=("Arial Bold", 10))
lbl8 = Label(text="Promedio de valor:", font=("Arial Bold", 10))
lbl9 = Label(text="Valor mínimo:", font=("Arial Bold", 10))
lbl10 = Label(text="Valor máximo alcanzado (Fuera de cierre):", font=("Arial Bold", 10))
lbl11= Label(text="Valor mínimo alcanzado (Fuera de cierre):", font=("Arial Bold", 10))
lbl12 = Label(text="Graficos de valor histórico:", font=("Arial Bold", 10))
lbl13 = Label(text="Graficos de valor entre las fechas seleccionadas:", font=("Arial Bold", 10))

lbl1.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
lbl3.grid(column=0, row=3)
lbl6.grid(column=0, row=9)
lbl7.grid(column=0, row=10)
lbl8.grid(column=0, row=11)
lbl9.grid(column=0, row=12)
lbl10.grid(column=0, row=13)
lbl11.grid(column=0, row=14)
lbl12.grid(column=0, row=15)
lbl13.grid(column=0, row=17)

# Botones:
btn_act = Button(window, text="Actualizar", command=actualizar)
btn_gr1 = Button(window, text="Graficar", command=grafico_1)
btn_gr2 = Button(window, text="Graficar", command=grafico_2)
btn_gua = Button(window, text="Guarde su archivo analizado", command=guardar)

btn_act.grid(column=0, row=7)
btn_gr1.grid(column=0, row=16)
btn_gr2.grid(column=0, row=18)
btn_gua.grid(column=0, row=20)

#Fechas:
fechas = list(df["Date"].unique())
fechas.sort()
fecha_desde = tk.StringVar(window)
menu1 = tk.OptionMenu(window, fecha_desde, *fechas)
menu1.grid(column=0, row=2)

fechas_1 = list(df["Date"].unique())
fechas_1.sort()
fecha_hasta = tk.StringVar(window)
menu2 = tk.OptionMenu(window, fecha_hasta, *fechas_1)
menu2.grid(column=0, row=4)

window.mainloop()