from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QVBoxLayout, QTabWidget
from PyQt5.QtCore import Qt, QDate
from expenses import ExpensesSheet
from incomes import IncomesSheet
from data_processing import DataProcessingSheet

class EconomicsGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout
        self.layout = QVBoxLayout()

        # Create the Year and Month selection
        self.year_month_label = QLabel("Select Year and Month:")
        self.year_month_combobox = QComboBox()

        # Add the current month and future months to the combo box
        current_date = QDate.currentDate()
        for i in range(0, 12):  
            month_date = current_date.addMonths(i)
            month_text = month_date.toString("yyyy MMMM")
            self.year_month_combobox.addItem(month_text)

        self.layout.addWidget(self.year_month_label)
        self.layout.addWidget(self.year_month_combobox)

        # Create the tab widget
        self.tab_widget = QTabWidget()

        # Create the expense sheet
        self.expenses_tab = ExpensesSheet()
        self.tab_widget.addTab(self.expenses_tab, "Expenses")

        # Create the income sheet
        self.incomes_tab = IncomesSheet()
        self.tab_widget.addTab(self.incomes_tab, "Incomes")

        # Create the data processing sheet
        self.data_processing_tab = DataProcessingSheet(self.expenses_tab, self.incomes_tab)
        self.tab_widget.addTab(self.data_processing_tab, "Data Processing")

        self.layout.addWidget(self.tab_widget)

        # Set up the main layout
        self.setLayout(self.layout)

        # Connect signals to update data processing result
        self.expenses_tab.update_button.clicked.connect(self.data_processing_tab.calculate_and_display_result)
        self.incomes_tab.update_income_button.clicked.connect(self.data_processing_tab.calculate_and_display_result)
