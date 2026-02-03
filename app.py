import sys
import requests
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chemical Visualizer - Desktop')

        self.setStyleSheet("""
            background:#1a001a;
            color:#e6ccff;
        """)

        self.btn = QtWidgets.QPushButton('Upload CSV')
        self.btn.setStyleSheet('background:#8000ff; color: white; padding:6px; border-radius:6px;')

        self.btn.clicked.connect(self.upload)

        self.fig = Figure(figsize=(5, 3))
        self.canvas = FigureCanvasQTAgg(self.fig)

        lay = QtWidgets.QVBoxLayout()
        lay.addWidget(self.btn)
        lay.addWidget(self.canvas)

        self.setLayout(lay)

    def upload(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open CSV', '', 'CSV Files (*.csv)')
        if not path:
            return

        files = {'file': open(path, 'rb')}
        try:
            r = requests.post('http://127.0.0.1:8000/api/upload/', files=files)
            r.raise_for_status()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Error', f'Upload failed: {e}')
            return

        d = r.json()

        ax = self.fig.add_subplot(111)
        ax.clear()
        ax.bar(
          ['Flow', 'Pressure', 'Temp'],
          [d.get('avg_flow'), d.get('avg_pressure'), d.get('avg_temp')],
          color='#b366ff'
        )

        self.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())
