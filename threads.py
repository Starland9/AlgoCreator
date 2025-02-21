from PyQt6.QtCore import QRunnable, pyqtSlot, QObject, pyqtSignal

import g4f


class IntelliSignals(QObject):
    algoCreated = pyqtSignal(str)


# noinspection PyUnresolvedReferences
class AlgoWorker(QRunnable):
    def __init__(self, source_text: str):
        super(AlgoWorker, self).__init__()
        self.source_text = source_text
        self.signals = IntelliSignals()

    @pyqtSlot()
    def run(self) -> None:
        try:
            result = g4f.ChatCompletion.create(
                model=g4f.models.qwen_2_72b,
                messages=[
                    {
                        "role": "user",
                        "content": (
                            "Grâce à ce que je vais te demander, s'il te plaît, fournis-moi un algorithme "
                            "écrit en français avec un style similaire à celui utilisé dans Aglobox. "
                            "Assure-toi d'inclure une indentation correcte et une coloration syntaxique. "
                            "Représente le tout en utilisant du HTML. Voici le texte source :\n\n et tu peux laisser les comodité et donner juste l'algorithme stp"
                            f"{self.source_text}"
                        ),
                    }
                ],
            )

            self.signals.algoCreated.emit(result)
        except Exception as e:
            print("Error:", e)
            self.signals.algoCreated.emit("Une erreur est survenue : \n" + str(e))
