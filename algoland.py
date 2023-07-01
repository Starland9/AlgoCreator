from PyQt6.QtCore import QThreadPool
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QTextEdit, QPushButton, \
    QTextBrowser

from style import style
from threads import AlgoWorker


class Algoland(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AlgoLand")
        self.setMinimumSize(800, 600)

        # Widget principal
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        self.threadPool = QThreadPool()

        # Layout principal
        layout = QVBoxLayout(main_widget)

        # Étiquette pour le titre
        title_label = QLabel("Génère ton Algorithme grace a ton idée", self)
        title_label.setObjectName("title")
        layout.addWidget(title_label)

        # Zone de texte pour le texte d'entrée
        self.input_text_edit = QTextEdit(self)
        self.input_text_edit.setObjectName("input_text")
        self.input_text_edit.setMaximumHeight(50)
        layout.addWidget(self.input_text_edit)

        # Bouton pour convertir
        self.convert_button = QPushButton("Lancer la machine", self)
        self.convert_button.setObjectName("convert_button")
        layout.addWidget(self.convert_button)

        # Étiquette pour afficher le résultat
        self.result_label = QLabel("Resultat:", self)
        self.result_label.setObjectName("result_label")
        layout.addWidget(self.result_label)

        # Zone de texte pour le résultat de l'algorithme
        self.result_text_edit = QTextBrowser(self)
        self.result_text_edit.setObjectName("result_text")
        self.result_text_edit.setReadOnly(True)
        layout.addWidget(self.result_text_edit)

        # Appliquer les styles CSS
        self.setStyleSheet(style)

        # Connecter le bouton à la fonction de conversion
        self.convert_button.clicked.connect(self.convert_text_to_algorithm)

    def convert_text_to_algorithm(self):
        input_text = self.input_text_edit.toPlainText()
        algo_worker = AlgoWorker(input_text)
        self.threadPool.start(algo_worker)
        algo_worker.signals.algoCreated.connect(self.algo_created)
        self.convert_button.setEnabled(False)
        self.convert_button.setStyleSheet("background-color: #336633")
        self.convert_button.setText("La machine est en train de convertir ...")
        # Résultat de l'algorithme

    def algo_created(self, result):
        self.result_text_edit.setHtml(result)
        self.convert_button.setStyleSheet("background-color: #0066CC;")
        self.convert_button.setEnabled(True)
        self.convert_button.setText("Lancer la machine")


