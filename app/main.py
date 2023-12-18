from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox

from bin import AOCRunner, DataHandler
from .widgets import WidgetCollection


class MainGUI:
    def __init__(self):
        self.data_handler = DataHandler(self)
        self.app = QApplication([])
        self._main_window = QWidget()

        self._main_window.setWindowTitle('Advent of Code')

        self._layout = QVBoxLayout()
        self.widgets = WidgetCollection(self._layout)
        self.widgets.prerender()
        self.widgets['date_confirm'].propagate(self.run_aoc)

        self._main_window.setLayout(self._layout)

    def run(self):
        self.app.exec()

    def render(self):
        self._main_window.show()

    def show_message_and_copy(self, message):
        self.widgets['result_box'].widget.setText(message)
        self.widgets['result_box'].widget.exec()
        if self.widgets['result_box'].widget.clickedButton():
            clipboard = QApplication.clipboard()
            clipboard.setText(message)

    def run_aoc(self):
        try:
            self.widgets.hide_current()
            year = self.widgets['year_selector'].value
            day = self.widgets['day_selector'].value
            runner = AOCRunner(self, year, day)
            runner.prepare()
            result = runner.run()
            self.show_message_and_copy(result)
            self.widgets.show_main()
        except Exception as e:
            QMessageBox.critical(self._main_window, "Error", str(e))
            self.widgets.show_main()
