from PyQt5.QtWidgets import QScrollArea, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class IncomesSheet(QWidget):
    def __init__(self):
        super().__init__()

        # Create the income list scroll area
        self.income_list_scroll_area = QScrollArea()
        self.income_list_widget = QWidget()
        self.income_list_widget_layout = QVBoxLayout()

        self.incomes = [
            "Salary 1", "Salary 2", "Child Allowances", "Additional Allowances", "Rental Income",
            "Pension from Previous Job", "Bonuses", "13th Salary", "Opportunistic Income", "Other Business Income",
            "Disability Allowance", "National Insurance", "Income from Investments", "Food Allowance",
            "Insurance Compensation due to Accident or Event", "One-Time Incomes"
        ]

        self.income_entries = {}
        for income_category in self.incomes:
            entry = QLineEdit()
            self.income_entries[income_category] = entry
            income_label = QLabel(income_category)
            income_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            row_layout = QHBoxLayout()
            row_layout.addWidget(income_label)
            row_layout.addWidget(entry)
            row_layout.setSpacing(0)  
            self.income_list_widget_layout.addLayout(row_layout)

        self.income_list_widget.setLayout(self.income_list_widget_layout)
        self.income_list_scroll_area.setWidget(self.income_list_widget)
        self.income_list_scroll_area.setWidgetResizable(True)

        # Create the update button
        self.update_income_button = QPushButton("Update Incomes")
        self.update_income_button.clicked.connect(self.update_incomes_graph)

        # Create the matplotlib plot for incomes
        self.income_figure, self.income_ax = plt.subplots(figsize=(8, 8))
        self.income_canvas = FigureCanvas(self.income_figure)
        self.income_toolbar = NavigationToolbar(self.income_canvas, self)
        self.income_layout = QVBoxLayout()
        self.income_layout.addWidget(self.income_toolbar)
        self.income_layout.addWidget(self.income_list_scroll_area)
        self.income_layout.addWidget(self.income_canvas)
        self.income_layout.addWidget(self.update_income_button)
        self.setLayout(self.income_layout)

        # Customize the income pie chart appearance
        self.customize_income_pie_chart()

    def update_incomes_graph(self):
        named_incomes = [income for income in self.incomes if self.income_entries[income].text()]
        monthly_amounts = [float(self.income_entries[income].text()) for income in named_incomes]

        self.income_ax.clear()
        self.income_ax.pie(monthly_amounts, labels=named_incomes, autopct='%1.1f%%', startangle=90)
        self.income_ax.axis('equal')
        self.customize_income_pie_chart()
        self.income_canvas.draw()

        # Update the title
        selected_month_year = self.window().year_month_combobox.currentText()
        self.income_ax.set_title(f"Incomes Distribution - {selected_month_year}")
        self.income_canvas.draw()

    def customize_income_pie_chart(self):
        for text in self.income_ax.texts:
            text.set_fontsize(10)
            text.set_fontweight('bold')
