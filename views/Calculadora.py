import tkinter as tk
from config import config
import ttkbootstrap as ttk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Cargar configuracion y demas
        self.Configuracion()
        self.UI()
        self.Buttons()
    
    def Configuracion(self):
        self.title('Calculadora Py')
        self.attributes('-alpha', 0.90)
        self.configure(bg=config.ColorBase)
        self.resizable(False, False)
        self.style = ttk.Style(theme="vapor")
        
    def UI(self):
        
        # Configuracion de columnas
        for Columna in range(4):
            self.grid_columnconfigure(Columna, weight=1)
        
        self.LabelOperaciones = tk.Label(self, text="", font="Arial, 15", justify="right", bd=1, height=2)
        self.LabelOperaciones.grid(row=0, column=0, columnspan=4, sticky='ew')
        
        # Contenedor operacion
        self.ContenedorOperaciones = tk.Entry(self, font="Arial 20", justify="right", bd=1)
        self.ContenedorOperaciones.grid(row=1, column=0, columnspan=4, sticky='ew')
        
    
    def Buttons(self):
        
        # Lista Bottones
        Buttones = [
            '(', ')', 'CE', 'C',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', '/',
        ]
        
        Fila = 2
        Columna = 0
        
        for Botton in Buttones:
            Button_ = tk.Button(self, text=Botton, command=lambda ValorB=Botton: self.ButtonClick(ValorB), width=2, height=2)
            # Button_ = tk.Button(self,text=Botton , width=2, height=2, command=lambda ValorB=Botton: self.ButtonClick(ValorB))
            Button_.grid(row=Fila, column=Columna, sticky='nsew')

            Columna += 1
            if Columna > 3:
                Columna = 0
                Fila += 1
                
    def ButtonClick(self, Valor):
        if Valor == 'C':
            ContenidoActual = self.ContenedorOperaciones.get()
            if ContenidoActual:
                Contenido_1 = ContenidoActual[:-1]                
                self.ContenedorOperaciones.delete(0, tk.END)
                self.ContenedorOperaciones.insert(tk.END, Contenido_1)
                self.LabelOperaciones.config(text=Contenido_1)
        elif Valor == 'CE':
            self.ContenedorOperaciones.delete(0, tk.END)
            self.LabelOperaciones.config(text="")
        elif Valor == '=':
            try:
                Expresion = self.ContenedorOperaciones.get().replace('%', '/100')
                Resultado = eval(Expresion)
                self.ContenedorOperaciones.delete(0, tk.END)
                self.ContenedorOperaciones.insert(tk.END, str(Resultado))
                Opracion = Expresion
                self.LabelOperaciones.config(text=Opracion)
            except Exception as Error:
                self.ContenedorOperaciones.delete(0, tk.END)
                self.ContenedorOperaciones.insert(tk.END, "Error")
                self.LabelOperaciones.config(text="")
        else:
            ContenidoActual = self.ContenedorOperaciones.get()
            self.ContenedorOperaciones.delete(0, tk.END)
            self.ContenedorOperaciones.insert(tk.END, ContenidoActual + Valor)
            if Valor == '=':
                self.LabelOperaciones.configure(text="")