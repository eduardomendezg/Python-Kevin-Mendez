#Resuelve el problema de crear una lista de tareas que permita a 
# los usuarios agregar, eliminar y marcar como completadas las tareas. 
# La aplicación utiliza un campo de texto para ingresar nuevas tareas,
#  una lista de tareas para mostrar las tareas pendientes y completadas, y botones 
# para eliminar y marcar tareas como completadas.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem

class ListaTareas(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Lista de Tareas')

        layout = QVBoxLayout()

        # Campo de texto para ingresar nuevas tareas
        self.entradaTarea = QLineEdit()
        layout.addWidget(self.entradaTarea)

        # Botón para agregar nuevas tareas
        self.botonAgregar = QPushButton('Agregar Tarea')
        self.botonAgregar.clicked.connect(self.agregarTarea)
        layout.addWidget(self.botonAgregar)

        # Lista de tareas
        self.listaTareas = QListWidget()
        layout.addWidget(self.listaTareas)

        # Botón para eliminar tareas
        self.botonEliminar = QPushButton('Eliminar Tarea')
        self.botonEliminar.clicked.connect(self.eliminarTarea)
        layout.addWidget(self.botonEliminar)

        # Botón para marcar tareas como completadas
        self.botonCompletar = QPushButton('Completar Tarea')
        self.botonCompletar.clicked.connect(self.completarTarea)
        layout.addWidget(self.botonCompletar)

        self.setLayout(layout)

    def agregarTarea(self):
        tarea = self.entradaTarea.text()
        if tarea:
            self.listaTareas.addItem(tarea)
            self.entradaTarea.clear()

    def eliminarTarea(self):
        row = self.listaTareas.currentRow()
        if row != -1:
            self.listaTareas.takeItem(row)

    def completarTarea(self):
        row = self.listaTareas.currentRow()
        if row != -1:
            tarea = self.listaTareas.item(row)
            tarea.setText(tarea.text() + ' (Completada)')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    listaTareas = ListaTareas()
    listaTareas.show()
    sys.exit(app.exec_())