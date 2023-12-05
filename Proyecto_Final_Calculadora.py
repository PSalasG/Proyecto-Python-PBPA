import tkinter as tk
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Interfaz():
    """Representa la interfaz con la que interactúa el usuario.

    Atributos:
        window (TK)
        texto (str)
        funcion (str)
        lower_limit_var (float)
        upper_limit_var (float)
    """
    def __init__(self):
        """Crea un objeto de tipo Interfaz.
        """
        self.window = tk.Tk()
        self.texto = ""
        self.funcion = tk.StringVar()  
        self.lower_limit_var = tk.DoubleVar()
        self.upper_limit_var = tk.DoubleVar()    
    
    def labels(self):   
        """Crea los títulos que se ven en la interfaz. 
        """
        label_calcular = tk.Label(self.window, text="Ingresar Expresión", font=('consolas', 14))
        label_calcular.pack()
        
        entry_calcular = tk.Entry(self.window, textvariable=self.funcion, font=('consolas', 14))
        entry_calcular.pack()

        label_lower_limit = tk.Label(self.window, text="Limite inferior:", font=('consolas', 14))
        label_lower_limit.pack()

        entry_lower_limit = tk.Entry(self.window, textvariable=self.lower_limit_var, font=('consolas', 14))
        entry_lower_limit.pack()

        label_upper_limit = tk.Label(self.window, text="Limite superior:", font=('consolas', 14))
        label_upper_limit.pack()

        entry_upper_limit = tk.Entry(self.window, textvariable=self.upper_limit_var, font=('consolas', 14))
        entry_upper_limit.pack()

        self.frame = tk.Frame(self.window)
        self.frame.pack()

        self.button_place(self.frame)
        
        self.window.protocol("WM_DELETE_WINDOW", self.cerrar_Matplotlib)
        self.window.mainloop()

    def button_press(self, texto):
        """Realiza la función correspondiente al presionar cada botón.

        Argumentos:
         texto (str)
        """
        if texto == "Clear":
            self.funcion.set('')
            self.texto = ""
            
        elif texto == "=":
            self.texto = ""
            calculo = Calcular(self.funcion)
            calculo.calcular_resultado()
            
        elif texto == "Graph":
            self.texto = ""
            lower_limit = self.lower_limit_var.get()
            upper_limit = self.upper_limit_var.get()
            
            if upper_limit == 0 and lower_limit == 0:
                self.upper_limit_var.set(10.0)
                upper_limit = 10
            
            grafica = Graficar(self.funcion, self.eje, lower_limit, upper_limit)
            grafica.generar_grafico()
            self.canvas.draw()
            
        else:
            self.texto = self.texto + str(texto)
            self.funcion.set(self.texto)

    def button_place(self, frame):
        """Define la posición de cada uno de los botones.

        Argumentos:
         frame (TK)
        """
        button_list = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),('sin', 1, 4), ('x', 1, 5),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),('cos', 2, 4), ('(', 2, 5),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),('tan', 3, 4), (')', 3, 5),
            ('0', 4, 0), ('Clear', 4, 1), ('=', 4, 2), ('+', 4, 3), ('exp', 4, 4), ('Graph', 4, 5)  
        ]

        for i in button_list:
            texto = i[0]
            fila = i[1]
            columna = i[2]

            button = tk.Button(frame, text=texto, height=4, width=9, font=('consolas', 14), bd=2, relief="sunken", bg="light gray" ,command=lambda text=texto: self.button_press(text))
            button.grid(row=fila, column=columna)

    def Matplotlib_insert(self):
        """Se encarga de crear el espacio para las gráficas.
        """
        self.figura = plt.figure(figsize=(6, 4), dpi=100)
        self.eje = self.figura.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figura, master= self.window)
        self.canvas_widget = self.canvas.get_tk_widget()        
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def cerrar_Matplotlib(self):
        """Se encarga de cerrar Matplotlib.
        """
        plt.close(self.figura)
        self.window.destroy()
        
class Graficar():
    """Permite realizar la graficación de una función introducida por el usuario.

    Atributos:
        funcion (str) 
        ax (plt.subplot)
        lower_limit (float)
        upper_limit (float)
    """
    def __init__(self, funcion, axis, lower_limit, upper_limit):
        """Crea un objeto de tipo Graficar.

        Argumentos:
        funcion (str)
        axis (plt.subplot)
        lower_limit (float)
        upper_limit (float)
        """
        self.funcion = funcion
        self.ax = axis
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def generar_grafico(self):
        """Se encarga de desplegar el gráfico de la función.

        Excepción:
        Manejo de cualquier excepción al graficar.
        """
        try:
            self.ax.clear()

            expresion_str = self.funcion.get()
            expresion = sp.sympify(expresion_str)

            x = sp.symbols("x")
            f = sp.lambdify(x, expresion, 'numpy')
            x_vals = np.linspace(self.lower_limit, self.upper_limit, 1000)
            y_vals = f(x_vals)

            self.ax.plot(x_vals, y_vals, label=expresion_str)
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.ax.legend()
            self.ax.grid(True)

        except:
            self.funcion.set('Error al graficar')

class Calcular():
    """Realiza el cálculo de las operaciones matemáticas.

    Atributos:
        funcion (str) 
    """
    def __init__(self, funcion):
        """Crea un objeto de tipo Calcular.

            Argumentos:
            funcion (str)
        """
        self.funcion = funcion

    def calcular_resultado(self):
        """Se encarga de resolver las operaciones matemáticas.

        Excepciones:
        Maneja excepciones al cálcular operaciones.
        """
        try:
            expresion_str = self.funcion.get()
            expresion = sp.sympify(expresion_str)
            resultado = round(expresion.evalf(), 2)
            self.funcion.set(str(resultado))
        except:
            self.funcion.set('Error')

if __name__ == "__main__":
    calculadora = Interfaz()
    calculadora.window.title("Calculadora Grafica")
    calculadora.window.geometry("900x750")
    calculadora.Matplotlib_insert()
    calculadora.labels()