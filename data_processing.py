from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QFileDialog, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PyQt5.QtGui import QColor, QFont, QPixmap
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtWidgets


class DataProcessingSheet(QWidget):
    def __init__(self, expenses_tab, incomes_tab):
        super().__init__()

        self.expenses_tab = expenses_tab
        self.incomes_tab = incomes_tab

        self.layout = QVBoxLayout()

        # Create labels and widgets for displaying the result
        self.result_label = QLabel("Result of Data Processing:")
        self.result_display = QLabel()
        self.result_display.setFont(QFont("Arial", 12))

        # Create the legend table
        self.legend_table_label = QLabel("Legend:")
        self.legend_table = QTableWidget()
        self.legend_table.setColumnCount(5)
        self.legend_table.setRowCount(2)
        self.legend_table.setHorizontalHeaderLabels(["Difference", "4 digits", "3 digits", "2 digits", "Balanced"])
        self.legend_table.setEditTriggers(QTableWidget.NoEditTriggers)  # Make the table read-only

        # Create a canvas for the expenses pie chart
        self.expense_figure, self.expense_ax = plt.subplots(figsize=(4, 4))
        self.expense_canvas = FigureCanvas(self.expense_figure)

        # Create a canvas for the incomes pie chart
        self.income_figure, self.income_ax = plt.subplots(figsize=(4, 4))
        self.income_canvas = FigureCanvas(self.income_figure)

        # Create a button to display pie charts
        self.display_pie_charts_button = QPushButton("Display Pie Charts")
        self.display_pie_charts_button.clicked.connect(self.update_pie_charts)

        # Create a button to save the sheet as a figure
        self.save_as_figure_button = QPushButton("Save as Figure")
        self.save_as_figure_button.clicked.connect(self.save_as_figure)

        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.result_display)
        self.layout.addWidget(self.legend_table_label)
        self.layout.addWidget(self.legend_table)
        self.layout.addWidget(self.display_pie_charts_button)
        self.layout.addWidget(self.expense_canvas)
        self.layout.addWidget(self.income_canvas)
        self.layout.addWidget(self.save_as_figure_button)
        self.setLayout(self.layout)

        # Calculate and display the result on initialization
        self.calculate_and_display_result()
        # Populate the legend table
        self.populate_legend_table()

    def calculate_and_display_result(self):
        last_expenses_sum = sum(float(entry.text()) if entry.text() else 0 for entry in self.expenses_tab.expense_entries.values())
        last_incomes_sum = sum(float(entry.text()) if entry.text() else 0 for entry in self.incomes_tab.income_entries.values())

        result = last_incomes_sum - last_expenses_sum

        # Set the result label and color based on the conditions
        if result >= 1000:
            color = QColor(0, 128, 0)  # Bold green
        elif 100 <= result < 1000:
            color = QColor(0, 128, 0)  # Green
        elif -999 <= result <= -100:
            color = QColor(255, 0, 0)  # Red
        elif result < -999:
            color = QColor(255, 0, 0)  # Bold red
        else:
            color = QColor(0, 0, 0)  # Default color

        self.result_display.setText(f"Result: {result:.2f}")
        self.result_display.setStyleSheet(f"color: rgb({color.red()}, {color.green()}, {color.blue()}); font-weight: {'bold' if abs(result) >= 1000 else 'normal'}")

    def populate_legend_table(self):
        legend_data = [
            ("Positive", "Excellent", "Good", "Needs improvement", "Reasonable"), ("Negative",
            "Dangerous", "Concerning")
        ]

        for row, data in enumerate(legend_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(value)
                if row == 0 and col == 1:
                    item.setForeground(QColor(0, 128, 0))  # Bold green
                    item.setFont(QFont("Arial", 10, weight=QFont.Bold))
                elif row == 0 and col == 2:
                    item.setForeground(QColor(0, 128, 0))  # Green
                elif row == 1 and col == 1:
                    item.setForeground(QColor(255, 0, 0))  # Bold red
                    item.setFont(QFont("Arial", 10, weight=QFont.Bold))
                elif row == 1 and col == 2:
                    item.setForeground(QColor(255, 0, 0))  # Red
                elif row == 0 and col >= 3:
                    item.setForeground(QColor(0, 0, 0))  # Black
                self.legend_table.setItem(row, col, item)

        # Merge cells in the last two columns of both rows
        self.legend_table.setSpan(0, 3, 2, 1)
        self.legend_table.setSpan(0, 4, 2, 1)

    def update_pie_charts(self):
        # Update the expenses pie chart
        named_expenses = [expense for expense in self.expenses_tab.expenses if self.expenses_tab.expense_entries[expense].text()]
        monthly_expense_amounts = [float(self.expenses_tab.expense_entries[expense].text()) for expense in named_expenses]

        self.expense_ax.clear()
        self.expense_ax.pie(monthly_expense_amounts, labels=named_expenses, autopct='%1.1f%%', startangle=90)
        self.expense_ax.axis('equal')
        self.expense_canvas.draw()

        # Update the incomes pie chart
        named_incomes = [income for income in self.incomes_tab.incomes if self.incomes_tab.income_entries[income].text()]
        monthly_income_amounts = [float(self.incomes_tab.income_entries[income].text()) for income in named_incomes]

        self.income_ax.clear()
        self.income_ax.pie(monthly_income_amounts, labels=named_incomes, autopct='%1.1f%%', startangle=90)
        self.income_ax.axis('equal')
        self.income_canvas.draw()
    
    def save_as_figure(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Figure", "", "PNG Files (*.png);;All Files (*)")
        if filename:
            pixmap = QPixmap(self.size())
            self.render(pixmap)
            pixmap.save(filename)

