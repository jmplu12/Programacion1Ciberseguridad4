#5. Diseña una interfaz con un Canvas donde el usuario pueda dibujar líneas 
# manteniendo presionado el botón del mouse.
import tkinter as tk
class AplicacionDibujo:
    def __init__(self, master):
        self.master = master
        self.master.title("Dibuja con el mouse")
        self.canvas = tk.Canvas(self.master, bg="white", width=600, height=400)
        self.canvas.pack()

        # Panel de botones debajo del canvas
        self.panel_botones = tk.Frame(self.master)
        self.panel_botones.pack(pady=6)

        # Botón para borrar el contenido del canvas
        self.boton_borrar = tk.Button(self.panel_botones, text="Borrar", command=self.borrar_canvas)
        self.boton_borrar.pack(side=tk.LEFT, padx=4)

        # Variables para almacenar la posición inicial del mouse
        self.x_inicial = None
        self.y_inicial = None

        # Vincular eventos del mouse
        self.canvas.bind("<ButtonPress-1>", self.iniciar_dibujo)
        self.canvas.bind("<B1-Motion>", self.dibujar_linea)

    def iniciar_dibujo(self, event):
        """Captura la posición inicial cuando se presiona el botón del mouse."""
        self.x_inicial = event.x
        self.y_inicial = event.y

    def dibujar_linea(self, event):
        """Dibuja una línea desde la posición inicial hasta la posición actual del mouse."""
        if self.x_inicial is not None and self.y_inicial is not None:
            # Dibujar línea
            self.canvas.create_line(self.x_inicial, self.y_inicial, event.x, event.y, fill="black")
            # Actualizar la posición inicial para la siguiente línea
            self.x_inicial = event.x
            self.y_inicial = event.y    

    def borrar_canvas(self):
        """Borra todo lo dibujado en el canvas y reinicia la posición inicial."""
        self.canvas.delete("all")
        self.x_inicial = None
        self.y_inicial = None
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionDibujo(root)
    root.mainloop()