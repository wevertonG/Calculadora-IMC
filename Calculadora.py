from typing import Optional, Tuple, Union
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox as msg
from calculos import calcular_imc

class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.janela()
        self.tema()
        self.frame()
        self.pesoealtura()
        self.buttoncalcular()

    def janela(self):
        self.geometry("700x400")
        self.title("Calculadora de IMC")
        self.resizable(False, False)
        self.iconbitmap(r'C:\Users\wever\OneDrive\Área de Trabalho\Python\Curso Python\calculadora.ico')

    def tema(self):
        self.img = PhotoImage(file=r'C:\Users\wever\OneDrive\Área de Trabalho\Python\Curso Python\Capa_Redimensionada.png')
        self.labelimg = ctk.CTkLabel(self, text=None, image=self.img)
        self.labelimg.grid(row=0, column = 0, padx = 10, pady = 10) #padx - espaço de 10px
        self._set_appearance_mode("Dark")
        #self.title = ctk.CTkLabel(self, text= "Faça Login ou Cadastra-se \npara ter acesso a nossa plataforma", font=("Century Gothic bold", 18), bg_color="black", text_color="white")
        #self.title.grid(row = 0, column = 0, padx = 10, pady = 10)
   
    def frame(self):
        self.frame = ctk.CTkFrame(self, width = 250, height = 10, fg_color="black", bg_color="black")
        self.frame.grid(row=1, column=0, padx=10, pady=10)

    def pesoealtura(self):
       self.grid_rowconfigure(0, weight=5)  # Linha vazia no topo
       self.grid_rowconfigure(3, weight=10)  # Linha vazia na parte inferior

       self.entry_altura = ctk.CTkEntry(self.frame, width=300, height = 10, placeholder_text="Altura Atual", font=("Roboto", 16), corner_radius=7, border_color="blue", fg_color="black", placeholder_text_color="white", text_color="white")
       self.entry_altura.grid(row=2, column=0, padx=230, pady=10, sticky="n")  # sticky="n" para alinhar ao topo

       self.entry_peso = ctk.CTkEntry(self.frame, width=300, height = 10, placeholder_text="Peso Atual", font=("Roboto", 16), corner_radius=7, border_color="blue", fg_color="black", placeholder_text_color="white", text_color="white")
       self.entry_peso.grid(row=3, column=0, padx=230, pady=10)
    
    def calcular(self):
      try:
            peso = float(self.entry_peso.get())
            altura = str(self.entry_altura.get())
            imc = calcular_imc(peso, altura)
            self.resultado.configure(state="normal")  # Permitir modificação
            self.resultado.delete(1.0, "end")  # Limpar conteúdo anterior
            self.resultado.insert("end", f"Seu IMC é: {imc:.2f}")
            self.resultado.configure(state="disabled")  # Tornar somente leitura novamente

            # Remover o cursor de barra vertical (|)
            self.resultado.focus()  # Coloca o foco no resultado (Remove o cursor)
      except ValueError:
            self.resultado.configure(state="normal")
            self.resultado.delete(1.0, "end")
            self.resultado.insert("end", "Insira um Valor Válido")
            self.resultado.configure(state="disabled")

    def buttoncalcular(self):
        self.calcular = ctk.CTkButton(self, width=200, text="Calcular".upper(), corner_radius=15, font=("Century Gothic bold", 16), fg_color="blue", hover_color="green", bg_color="black", command=self.calcular)
        self.calcular.place(x=285, y=250)

        self.resultado = ctk.CTkTextbox(self, height=1, width=200, font=("Roboto", 16), state="disabled", wrap="none", border_width=0, fg_color="yellow", border_color="black", bg_color="black", corner_radius=7)
        self.resultado.place(x=285, y=300)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()