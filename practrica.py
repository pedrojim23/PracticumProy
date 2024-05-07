import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime, timedelta

class Vista(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Horario Escolar")
        # Set window size
        self.geometry("800x500")  # Set a fixed size for the window

        # Definir las variables materias y profesores dentro de __init__
        self.materias = {}
        self.profesores = {}

        # Cargar datos de profesores desde el archivo CSV
        with open('profesores.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre_profesor = row['Nombre']
                self.profesores[nombre_profesor] = {
                    "Disponibilidad": row['Disponibilidad'],
                    "Tipo": row['Tipo']
                }

        # Cargar datos de materias desde el archivo CSV
        with open('materias.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.materias[row['Nombre']] = {
                    "Prioridad": int(row['Prioridad']),
                    "Prerrequisitos": row['Prerrequisitos'],
                    "Modulos": int(row['Modulos']),
                    "Profesores": row['Profesores'].split(", ")
                }

        # Vista 1
        self.frame_vista1 = tk.Frame(self, bg='#ff5900')
        self.frame_vista1.pack(expand=True, fill=tk.BOTH)
        tk.Label(self.frame_vista1, text="SISTEMA HORARIO", fg="white", bg='#ff5900', font=("Colibri", 30, "bold")).pack(pady=30)
        btn_frame = tk.Frame(self.frame_vista1,  bg='#ff5900')
        btn_frame.pack(expand=True, pady=(self.winfo_height() // 2, 0))
        btn_materia = tk.Button(btn_frame, text="Materia", command=self.mostrar_vista_materia)
        btn_materia.pack(side=tk.LEFT, padx=10)
        btn_profesor = tk.Button(btn_frame, text="Profesor", command=self.mostrar_vista_profesor)
        btn_profesor.pack(side=tk.LEFT, padx=10)
        btn_horario = tk.Button(btn_frame, text="Horario", command=self.mostrar_vista_horario)
        btn_horario.pack(side=tk.LEFT, padx=10)

        # Vista 2 (Materia)
        self.frame_vista_materia = tk.Frame(self, bg='#ff5900')
        tk.Label(self.frame_vista_materia, text="Nombre de la Materia:").pack()
        self.entry_nombre_materia = tk.Entry(self.frame_vista_materia)
        self.entry_nombre_materia.pack()
        tk.Label(self.frame_vista_materia, bg='#ff5900').pack()
        tk.Label(self.frame_vista_materia, text="Prioridad de la Materia:").pack()
        self.entry_prioridad_materia = tk.Entry(self.frame_vista_materia)
        self.entry_prioridad_materia.pack()
        tk.Label(self.frame_vista_materia, bg='#ff5900').pack()
        tk.Label(self.frame_vista_materia, text="Prerrequisitos de la Materia:").pack()
        self.entry_prerrequisitos_materia = tk.Entry(self.frame_vista_materia)
        self.entry_prerrequisitos_materia.pack()
        tk.Label(self.frame_vista_materia, bg='#ff5900').pack()
        tk.Label(self.frame_vista_materia, text="Módulos por Semana:").pack()
        self.entry_modulos_materia = tk.Entry(self.frame_vista_materia)
        self.entry_modulos_materia.pack()
        tk.Label(self.frame_vista_materia, bg='#ff5900').pack()
        tk.Label(self.frame_vista_materia, text="Profesores Candidatos:").pack()
        self.entry_profesores_materia = tk.Entry(self.frame_vista_materia)
        self.entry_profesores_materia.pack()
        tk.Label(self.frame_vista_materia, bg='#ff5900').pack()
        btn_agregar_materia = tk.Button(self.frame_vista_materia, text="Agregar Materia", command=self.agregar_materia)
        btn_agregar_materia.pack()

        btn_eliminar_materia = tk.Button(self.frame_vista_materia, text="Eliminar Materia", command=self.eliminar_materia)
        btn_eliminar_materia.pack()

        # Vista 3 (Profesor)
        self.frame_vista_profesor = tk.Frame(self, bg='#ff5900')
        tk.Label(self.frame_vista_profesor, text="Nombre del Profesor:").pack()
        self.entry_nombre_profesor = tk.Entry(self.frame_vista_profesor)
        self.entry_nombre_profesor.pack()
        tk.Label(self.frame_vista_profesor, bg='#ff5900').pack()
        tk.Label(self.frame_vista_profesor, text="Disponibilidad de Horario:").pack()
        self.frame_disponibilidad_profesor = tk.Frame(self.frame_vista_profesor)
        self.frame_disponibilidad_profesor.pack()
        self.checkboxes_dias = {}
        self.entry_horarios_inicio = {}
        self.entry_horarios_fin = {}
        for dia in ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']:
            self.checkboxes_dias[dia] = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.frame_disponibilidad_profesor, text=dia, variable=self.checkboxes_dias[dia])
            checkbox.pack(side=tk.LEFT)
            self.entry_horarios_inicio[dia] = tk.Entry(self.frame_disponibilidad_profesor, width=5)
            self.entry_horarios_inicio[dia].insert(tk.END, '07:30')
            self.entry_horarios_inicio[dia].pack(side=tk.LEFT)
            tk.Label(self.frame_disponibilidad_profesor, text="-").pack(side=tk.LEFT)
            self.entry_horarios_fin[dia] = tk.Entry(self.frame_disponibilidad_profesor, width=5)
            self.entry_horarios_fin[dia].insert(tk.END, '21:00')
            self.entry_horarios_fin[dia].pack(side=tk.LEFT)
        tk.Label(self.frame_vista_profesor, bg='#ff5900').pack()
        tk.Label(self.frame_vista_profesor, text="Tipo de Profesor:").pack()
        self.profesor_tiempo_completo = tk.BooleanVar()
        checkbox_tiempo_completo = tk.Checkbutton(self.frame_vista_profesor, text="Profesor de Tiempo Completo", variable=self.profesor_tiempo_completo)
        checkbox_tiempo_completo.pack()
        tk.Label(self.frame_vista_profesor, bg='#ff5900').pack()
        btn_agregar_profesor = tk.Button(self.frame_vista_profesor, text="Agregar Profesor", command=self.agregar_profesor)
        btn_agregar_profesor.pack()

        btn_eliminar_profesor = tk.Button(self.frame_vista_profesor, text="Eliminar Profesor", command=self.eliminar_profesor)
        btn_eliminar_profesor.pack()

        # Vista 4 (Horario)
        self.frame_vista4 = tk.Frame(self, bg='#ff5900')

        # Ensure asignaciones_anteriores is initialized with entries for each day of the week
        self.asignaciones_anteriores = {day: {} for day in range(5)}

        # Create pestañas for each day of the week
        self.tabs = ttk.Notebook(self.frame_vista4)
        for day in range(5):
            tab = ttk.Frame(self.tabs)
            self.tabs.add(tab, text=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'][day])

            # Asegurar que day esté dentro del rango esperado
            day = day % 5

            horario_semana = self.crear_horario_semana()
            self.asignar_materias_interactivo(horario_semana, self.materias, self.profesores, day, self.asignaciones_anteriores)
            self.mostrar_horario(tab, horario_semana)

        self.tabs.pack(expand=1, fill='both')
        self.frame_vista4.pack(expand=True, fill=tk.BOTH)

    def crear_horario_semana(self):
        horario = {}
        current_time = datetime.strptime("07:30", "%H:%M")
        while current_time < datetime.strptime("21:00", "%H:%M"):
            horario[current_time] = None
            current_time += timedelta(hours=1, minutes=30)
        return horario

    def parse_disponibilidad(self, disponibilidad_str):
        disponibilidad_dict = eval(disponibilidad_str.replace("'", '"'))
        return disponibilidad_dict

    def asignar_materias_interactivo(self, horario, materias, profesores, day, asignaciones_anteriores, seleccionados={}):
        profesores_asignados = asignaciones_anteriores.get(day, {})
        profesores_asignados_dia_anterior = asignaciones_anteriores.get(day - 1, {}) if day > 0 else {}

        for materia_nombre, materia in materias.items():
            # Verificar si la materia ya ha sido seleccionada anteriormente
            if materia_nombre in seleccionados:
                profesor_asignado = seleccionados[materia_nombre]
            else:
                profesor_anterior = profesores_asignados_dia_anterior.get(materia_nombre, None)
                if profesor_anterior:
                    profesor_asignado = profesor_anterior
                elif materia_nombre in profesores_asignados:
                    profesor_asignado = profesores_asignados[materia_nombre]
                else:
                    # Crear una nueva ventana para la selección del profesor
                    ventana_profesor = tk.Toplevel()
                    ventana_profesor.title(f"Seleccionar profesor para {materia_nombre}")

                    # Etiqueta para mostrar las opciones de profesores disponibles
                    label = tk.Label(ventana_profesor, text=f"Selecciona un profesor para {materia_nombre} entre los siguientes disponibles:")
                    label.pack()

                    # Función para confirmar la selección del profesor y cerrar la ventana
                    def confirmar_seleccion(profesor):
                        seleccionados[materia_nombre] = profesor
                        ventana_profesor.destroy()

                    # Opciones de profesores disponibles
                    opciones_profesores = materia["Profesores"]

                    # Crear botones para cada profesor disponible
                    for profesor in opciones_profesores:
                        boton_profesor = tk.Button(ventana_profesor, text=profesor, command=lambda p=profesor: confirmar_seleccion(p))
                        boton_profesor.pack()

                    # Esperar hasta que se cierre la ventana de selección del profesor
                    ventana_profesor.wait_window()

                    # Obtener la selección del profesor
                    profesor_asignado = seleccionados[materia_nombre]

            # Verificar la disponibilidad del profesor y realizar la asignación en el horario
            disponibilidad_profesor = self.parse_disponibilidad(profesores[profesor_asignado]["Disponibilidad"])
            for dia, horas in disponibilidad_profesor.items():
                if dia.lower() == ['lunes', 'martes', 'miércoles', 'jueves', 'viernes'][day].lower():
                    inicio = datetime.strptime(horas["inicio"], "%H:%M")
                    fin = datetime.strptime(horas["fin"], "%H:%M")
                    current_time = inicio
                    while current_time < fin:
                        if current_time in horario and horario[current_time] is None:
                            horario[current_time] = (materia_nombre, profesor_asignado)
                            profesores_asignados[materia_nombre] = profesor_asignado
                            break
                        current_time += timedelta(hours=1, minutes=30)

        # Actualizar las asignaciones anteriores
        asignaciones_anteriores[day].update(profesores_asignados)
        asignaciones_anteriores.update({materia_nombre: profesor_asignado for materia_nombre, profesor_asignado in profesores_asignados.items() if profesor_asignado is not None and day not in asignaciones_anteriores})

    def mostrar_horario(self, tab, horario):
        frame = ttk.Frame(tab)
        frame.pack(fill='both', expand=True)
        for time, clase in horario.items():
            label = tk.Label(frame, text=f"{time.strftime('%H:%M')}: {clase[0]} ({clase[1]})" if clase else f"{time.strftime('%H:%M')}: Libre")
            label.pack()

    def eliminar_materia(self):
        nombre = self.entry_nombre_materia.get()

        if not nombre:
            mensaje = "Por favor, ingrese el nombre de la materia a eliminar."
            self.mostrar_alerta(mensaje)
            return

        if self.verificar_nombre_repetido('materias.csv', nombre):
            # Remove the subject from the CSV file
            self.eliminar_fila('materias.csv', nombre)
            mensaje = f"Materia '{nombre}' eliminada exitosamente."
            self.mostrar_alerta(mensaje)
        else:
            mensaje = f"No se encontró la materia '{nombre}'."
            self.mostrar_alerta(mensaje)

    def eliminar_profesor(self):
        nombre = self.entry_nombre_profesor.get()

        if not nombre:
            mensaje = "Por favor, ingrese el nombre del profesor a eliminar."
            self.mostrar_alerta(mensaje)
            return

        if self.verificar_nombre_repetido('profesores.csv', nombre):
            # Remove the professor from the CSV file
            self.eliminar_fila('profesores.csv', nombre)
            mensaje = f"Profesor '{nombre}' eliminado exitosamente."
            self.mostrar_alerta(mensaje)
        else:
            mensaje = f"No se encontró el profesor '{nombre}'."
            self.mostrar_alerta(mensaje)

    def eliminar_fila(self, archivo, nombre):
        filas = []
        try:
            with open(archivo, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] != nombre:
                        filas.append(row)
        except FileNotFoundError:
            pass

        with open(archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(filas)
        
        # Hide other frames initially
        self.hide_all_frames()

    def hide_all_frames(self):
        self.frame_vista_materia.pack_forget()
        self.frame_vista_profesor.pack_forget()
        self.frame_vista4.pack_forget()

    def mostrar_vista_materia(self):
        self.hide_all_frames()
        self.frame_vista_materia.pack(expand=True, fill=tk.BOTH)

    def mostrar_vista_profesor(self):
        self.hide_all_frames()
        self.frame_vista_profesor.pack(expand=True, fill=tk.BOTH)

    def mostrar_vista_horario(self):
        self.hide_all_frames()
        self.frame_vista4.pack(expand=True, fill=tk.BOTH)

    def agregar_materia(self):
        nombre = self.entry_nombre_materia.get()
        prioridad = self.entry_prioridad_materia.get()
        modulos = self.entry_modulos_materia.get()
        profesores = self.entry_profesores_materia.get()

        # Check if any required field is empty
        if not all([nombre, prioridad, modulos, profesores]):
            mensaje = "Por favor, complete todos los campos obligatorios."
            self.mostrar_alerta(mensaje)
            return

        if self.verificar_nombre_repetido('materias.csv', nombre):
            mensaje = f"El nombre de la materia '{nombre}' ya existe."
            self.mostrar_alerta(mensaje)
        else:
            # Encabezados de columna
            encabezados = ['Nombre', 'Prioridad', 'Prerrequisitos', 'Modulos', 'Profesores']

            # Escribir encabezados en el archivo CSV si el archivo no existe
            with open('materias.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                if file.tell() == 0:
                    writer.writerow(encabezados)

                # Escribir datos de materia
                writer.writerow([nombre, prioridad, '', modulos, profesores])

            print("Materia agregada:", nombre, prioridad, modulos, profesores)


    def agregar_profesor(self):
        nombre = self.entry_nombre_profesor.get()
        disponibilidad = {}
        for dia, checkbox in self.checkboxes_dias.items():
            if checkbox.get():
                disponibilidad[dia] = {
                    'inicio': self.entry_horarios_inicio[dia].get(),
                    'fin': self.entry_horarios_fin[dia].get()
                }

        tipo_profesor = "Tiempo Completo" if self.profesor_tiempo_completo.get() else "Por Honorarios"

        # Check if any field is empty
        if not all([nombre, disponibilidad, tipo_profesor]):
            mensaje = "Por favor, complete todos los campos."
            self.mostrar_alerta(mensaje)
            return

        if self.verificar_nombre_repetido('profesores.csv', nombre):
            mensaje = f"El nombre del profesor '{nombre}' ya existe."
            self.mostrar_alerta(mensaje)
        else:
            # Encabezados de columna
            encabezados = ['Nombre', 'Disponibilidad', 'Tipo']

            # Escribir encabezados en el archivo CSV si el archivo no existe
            with open('profesores.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                if file.tell() == 0:
                    writer.writerow(encabezados)

                # Escribir datos del profesor
                writer.writerow([nombre, disponibilidad, tipo_profesor])

            print("Profesor agregado:", nombre, disponibilidad, tipo_profesor)



    def verificar_nombre_repetido(self, archivo, nombre):
        try:
            with open(archivo, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == nombre:
                        return True
        except FileNotFoundError:
            pass
        return False

    def mostrar_alerta(self, mensaje):
        messagebox.showerror("Error", mensaje)


if __name__ == "__main__":
    app = Vista()
    app.mainloop()


import os

print("Directorio actual de trabajo:", os.getcwd())
