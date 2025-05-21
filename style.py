style = """QMainWindow {
    background-color: #222222;
}

QLabel {
    color: #FFFFFF;
    font-size: 18px;
    font-weight: bold;
}

QTextEdit {
    color: #FFFFFF;
    background-color: #333333;
    border: none;
    border-radius: 5px;
    padding: 5px;
    font-size: 14px;
}

QPushButton {
    color: #FFFFFF;
    background-color: #0066CC;
    border: none;
    border-radius: 5px;
    padding: 10px;
}

QPushButton:hover {
    background-color: #0099FF;
}

#result_label {
    font-size: 20px;
    margin-top: 30px;
}

#result_text {
    color: #000000;
    background-color: #FFFFFF;
    border: none;
    border-radius: 5px;
    padding: 10px;
    font-family: fira code;
    font-size: 14px;
    line-height: 1.2;
}
"""


style = """
QWidget {
            background-color: #f0f2f5; /* Gris clair de fond */
            font-family: "Segoe UI", "Arial", sans-serif;
            font-size: 14px;
            color: #333333;
        }

        /* Styles pour les QFrame (utilisé comme conteneur de carte) */
        QFrame#cardFrame {
            background-color: white;
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Ombre légère */
            padding: 20px;
        }

        /* Styles pour les QLabel */
        QLabel {
            color: #333333;
            padding: 2px 0;
        }
        QLabel#titleLabel {
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50; /* Bleu foncé */
            margin-bottom: 15px;
        }
        QLabel#subtitleLabel {
            font-size: 16px;
            color: #7f8c8d; /* Gris moyen */
            margin-bottom: 20px;
        }

        /* Styles pour les QLineEdit (champs de saisie) */
        QLineEdit {
            border: 1px solid #cccccc;
            border-radius: 8px;
            padding: 10px 15px;
            background-color: #ffffff;
            color: #333333;
            selection-background-color: #a8d8ff;
            selection-color: #333333;
        }
        QLineEdit:focus {
            border: 1px solid #007bff; /* Bordure bleue au focus */
            box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25); /* Ombre de focus */
        }

        /* Styles pour les QPushButton */
        QPushButton {
            background-color: #007bff; /* Bleu primaire */
            color: white;
            border: none;
            border-radius: 8px;
            padding: 12px 25px;
            font-weight: bold;
            font-size: 15px;
            text-transform: uppercase; /* Texte en majuscules */
            min-width: 120px;
            transition: all 0.3s ease; /* Transition douce pour les effets */
        }
        QPushButton:hover {
            background-color: #0056b3; /* Bleu plus foncé au survol */
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); /* Ombre plus prononcée */
            transform: translateY(-2px); /* Léger déplacement vers le haut */
        }
        QPushButton:pressed {
            background-color: #004085; /* Bleu encore plus foncé au clic */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transform: translateY(0);
        }

        QPushButton#secondaryButton {
            background-color: #6c757d; /* Gris secondaire */
        }
        QPushButton#secondaryButton:hover {
            background-color: #5a6268;
        }
        QPushButton#secondaryButton:pressed {
            background-color: #495057;
        }

        /* Styles pour les QCheckBox */
        QCheckBox {
            spacing: 8px;
            color: #555555;
        }
        QCheckBox::indicator {
            width: 18px;
            height: 18px;
            border-radius: 4px;
            border: 1px solid #cccccc;
            background-color: #ffffff;
        }
        QCheckBox::indicator:checked {
            background-color: #28a745; /* Vert pour coché */
            border: 1px solid #28a745;
            image: url(check_icon.png); /* Vous pouvez utiliser une icône SVG/PNG ici */
        }
        QCheckBox::indicator:checked:hover {
            background-color: #218838;
        }
        QCheckBox::indicator:hover {
            border: 1px solid #007bff;
        }

        /* Styles pour QProgressBar */
        QProgressBar {
            border: 1px solid #cccccc;
            border-radius: 8px;
            text-align: center;
            background-color: #e9ecef; /* Fond de la barre */
            height: 25px;
            color: #333333;
        }
        QProgressBar::chunk {
            background-color: #28a745; /* Vert pour la progression */
            border-radius: 6px;
            margin: 1px; /* Petit espace entre les chunks si la barre est segmentée */
        }
"""