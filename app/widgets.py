from PyQt6.QtWidgets import QSpinBox, QComboBox, QLabel, QPushButton, QMessageBox

from bin import YEARS


class Widget:
    def __init__(self, label, widget, preenabled=False):
        self.label = label
        self.widget = widget
        self.type = type(widget)
        self.preenabled = preenabled
        self.enabled = preenabled
        self.visible = preenabled

    def render(self, layout):
        layout.addWidget(self.label)
        layout.addWidget(self.widget)

    def remove(self, layout):
        layout.removeWidget(self.label)
        layout.removeWidget(self.widget)

    def show(self):
        if not self.enabled:
            return
        if self.visible:
            return
        if self.label:
            self.label.show()
        self.widget.show()
        self.visible = True

    def hide(self):
        if not self.enabled:
            return
        if not self.visible:
            return
        if self.label:
            self.label.hide()
        self.widget.hide()
        self.visible = False

    def enable(self):
        if self.enabled:
            return
        self.widget.setEnabled(True)
        self.enabled = True

    def disable(self):
        if not self.enabled:
            return
        self.widget.setEnabled(False)
        self.enabled = False

    @property
    def value(self):
        match self.widget:
            case QSpinBox():
                return self.widget.value()
            case QComboBox():
                return self.widget.currentText()
            case QComboBox():
                return self.widget.currentText()
            case QMessageBox():
                return self.widget.currentText()
            case _:
                return None

    def propagate(self, method):
        match self.widget:
            case QSpinBox():
                self.widget.valueChanged.connect(method)
            case QComboBox():
                self.widget.currentTextChanged.connect(method)
            case QPushButton():
                self.widget.clicked.connect(method)

    def __repr__(self):
        return f"<Widget {type(self.widget)}>"

    def __str__(self):
        return f"<Widget: {self.label.text()}>"


class WidgetCollection:
    widgets = {}
    layout = None

    def __init__(self, layout):
        self.prepare_widgets()
        self.layout = layout

    def prepare_widgets(self):
        year_label = QLabel("Select Year:")
        year_combo = QComboBox()
        year_combo.addItems(YEARS)
        self.widgets['year_selector'] = Widget(year_label, year_combo, preenabled=True)

        day_label = QLabel("Select Day:")
        day_spin = QSpinBox()
        day_spin.setRange(1, 25)
        self.widgets['day_selector'] = Widget(day_label, day_spin, preenabled=True)

        confirm_label = QLabel("Confirm Selection:")
        confirm_button = QPushButton("Confirm")
        self.widgets['date_confirm'] = Widget(confirm_label, confirm_button, preenabled=True)

        result_box = QMessageBox()
        result_box.setWindowTitle("Result")
        result_box.addButton(
            "Copy to clipboard", QMessageBox.ButtonRole.ActionRole
        )
        self.widgets['result_box'] = Widget(None, result_box, preenabled=False)

    def __getitem__(self, key):
        return self.widgets.get(key, None)

    def prerender(self):
        for key, widget in self.widgets.items():
            if not widget.preenabled:
                continue
            widget.render(self.layout)

    def hide_current(self):
        for key, widget in self.widgets.items():
            if widget.visible:
                widget.hide()

    def show_main(self):
        for key, widget in self.widgets.items():
            if widget.preenabled:
                widget.enable()
                widget.show()
