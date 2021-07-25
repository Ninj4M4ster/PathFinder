from PyQt6 import QtCore


class Worker(QtCore.QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    def run(self):
        try:
            self.fn(*self.args, **self.kwargs)
        except Exception as e:
            print(e.args)
        finally:
            self.signals.finished.emit()


class WorkerSignals(QtCore.QObject):

    finished = QtCore.pyqtSignal()