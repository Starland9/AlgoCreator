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
                model=g4f.models.gpt_35_turbo,
                messages=[
                    {"role": "user",
                     "content": f"Grace a ce que je vais de demander . stp donne moi un algorithme avec un style "
                                f"comme dans aglobox en francais avec les indentation et tout et aussi la coloration "
                                f"syntaxique."
                                f"utilise le html pour representer cela"
                                f": {self.source_text}"}
                ],
                provider=g4f.Provider.Aichat,
            )

            self.signals.algoCreated.emit(result)
        except Exception as e:
            print("Error:", e)
            self.signals.algoCreated.emit("Une erreur est survenue : \n" + str(e))
