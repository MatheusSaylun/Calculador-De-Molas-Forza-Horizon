import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def CalculoRigidezRetorno(numero: float) -> float:
    
    num_str = str(float(numero))
    primeiro = int(num_str[0]) + 1
    segundo = num_str[1]
    
    valor = float(f"{primeiro}.{segundo}")
    return valor

def Calcular():
    try:
        pesoCarro = float(entry_peso.get())
        porcentagemPesoDianteira = float(entry_dianteira.get())
        porcentagemPesoTraseira = 100 - porcentagemPesoDianteira

        molaDianteira = (pesoCarro - (pesoCarro * porcentagemPesoDianteira / 100)) / 2
        molaTraseira = (pesoCarro - (pesoCarro * porcentagemPesoTraseira / 100)) / 2

        rigidezRetornoDianteira = CalculoRigidezRetorno(molaDianteira)
        rigidezRetornoTraseira = CalculoRigidezRetorno(molaTraseira)

        rigidezCompressaoDianteira = rigidezRetornoDianteira * 1.5
        rigidezCompressaoTraseira = rigidezRetornoTraseira * 1.5

        resultado.set(
            f"Mola dianteira: {molaDianteira:.2f}\n"
            f"Mola traseira: {molaTraseira:.2f}\n"
            f"Rigidez retorno dianteiro: {rigidezRetornoDianteira:.2f}\n"
            f"Rigidez retorno traseiro: {rigidezRetornoTraseira:.2f}\n"
            f"Rigidez compressão dianteira: {rigidezCompressaoDianteira:.2f}\n"
            f"Rigidez compressão traseira: {rigidezCompressaoTraseira:.2f}"
        )
    except ValueError:
        resultado.set("Insira valores válidos!")

menuPrincipal = ttk.Window(themename="darkly")
menuPrincipal.title("Cálculo de Molas do Carro")
menuPrincipal.geometry("500x400")

ttk.Label(menuPrincipal, text="Peso do carro (libras):", font=("Segoe UI", 11)).pack(pady=5)
entry_peso = ttk.Entry(menuPrincipal, bootstyle="info")
entry_peso.pack(pady=5)

ttk.Label(menuPrincipal, text="Porcentagem do peso da dianteira (%):", font=("Segoe UI", 11)).pack(pady=5)
entry_dianteira = ttk.Entry(menuPrincipal, bootstyle="info")
entry_dianteira.pack(pady=5)

btn = ttk.Button(menuPrincipal, text="calcular", command=Calcular, bootstyle="success")
btn.pack(pady=15)

resultado = tk.StringVar()
label_result = ttk.Label(menuPrincipal, textvariable=resultado, font=("Consolas",11),justify="left")
label_result.pack(pady=10)

menuPrincipal.mainloop()












