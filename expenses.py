from PyQt5.QtWidgets import QScrollArea, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class ExpensesSheet(QWidget):
    def __init__(self):
        super().__init__()

        # Create the expense list scroll area
        self.expense_list_scroll_area = QScrollArea()
        self.expense_list_widget = QWidget()
        self.expense_list_widget_layout = QVBoxLayout()

        self.expenses = [
            "Rent", "Mortgage", "Homeowners Association", "Electricity", "Water", "Property Tax",
            "Car loan", "Mandatory insurance for all vehicles", "Comprehensive insurance for all vehicles",
            "Annual vehicle inspection for all vehicles", "Maintenance costs for all vehicles", "Home phone", "Mobile phone",
            "Cables/Subscription", "Gardener", "Alarm system", "Security service", "Subscription to a daily newspaper",
            "Subscription to a magazine", "Daycare payment", "School payment", "Health insurance", "Medications",
            "Luxury indulgences", "Helper/maid", "Babysitter", "Taxis and buses", "National insurance", "Life insurance",
            "Hobbies", "Travel abroad", "Music lessons", "Internet", "Fuel", "Gym membership", "Pocket money for children",
            "Home maintenance", "Babysitter", "Subscription/Tickets to theater/movies", "Books/CDs", "Clothing purchases",
            "Regular/irregular medication expenses", "Eyeglasses/contact lenses expenses", "Dental care expenses",
            "Special medical treatments", "Food and care for pets", "Parking fees and fines",
            "Monthly family entertainment expenses", "Annual vacation", "Memberships in various clubs",
            "Bank account management fees", "Average monthly spending on gifts for events",
            "Contributions to the family savings plan", "Contributions to provident funds", "Cosmetics and perfumes",
            "Average monthly spending on food products", "Average monthly spending on cleaning products", "Cigarettes",
            "Average visits of family members to a salon/cosmetician", "Vacation home",
            "Renting movies from the library or cable", "Assistance to a family member: student/parent", "Groceries",
            "Interest", "Restaurants", "Shoe expenses for all family members", "Hosting expenses for family and friends",
            "Expenses for baby - diapers/creams/special food/bottles", "Hobbies", "Legal expenses",
            "Tutoring expenses for children", "Lotteries - Toto/Lotto", "Jewelry and watches",
            "Gifts for colleagues, birthdays", "School supplies", "Expenses on computers and games",
            "Meals outside the home that are not part of leisure activities", "Coffee expenses from"
        ]

        self.expense_entries = {}
        for expense in self.expenses:
            entry = QLineEdit()
            self.expense_entries[expense] = entry
            expense_label = QLabel(expense)
            expense_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            row_layout = QHBoxLayout()
            row_layout.addWidget(expense_label)
            row_layout.addWidget(entry)
            row_layout.setSpacing(0)  
            self.expense_list_widget_layout.addLayout(row_layout)

        self.expense_list_widget.setLayout(self.expense_list_widget_layout)
        self.expense_list_scroll_area.setWidget(self.expense_list_widget)
        self.expense_list_scroll_area.setWidgetResizable(True)

        # Create the update button
        self.update_button = QPushButton("Update Expenses")
        self.update_button.clicked.connect(self.update_expenses_graph)

        # Create the matplotlib plot for expenses
        self.expense_figure, self.expense_ax = plt.subplots(figsize=(8, 8))
        self.expense_canvas = FigureCanvas(self.expense_figure)
        self.expense_toolbar = NavigationToolbar(self.expense_canvas, self)
        self.expense_layout = QVBoxLayout()
        self.expense_layout.addWidget(self.expense_toolbar)
        self.expense_layout.addWidget(self.expense_list_scroll_area)
        self.expense_layout.addWidget(self.expense_canvas)
        self.expense_layout.addWidget(self.update_button)
        self.setLayout(self.expense_layout)

        # Customize the expense pie chart appearance
        self.customize_expense_pie_chart()

    def update_expenses_graph(self):
        named_expenses = [expense for expense in self.expenses if self.expense_entries[expense].text()]
        monthly_amounts = [float(self.expense_entries[expense].text()) for expense in named_expenses]

        self.expense_ax.clear()
        self.expense_ax.pie(monthly_amounts, labels=named_expenses, autopct='%1.1f%%', startangle=90)
        self.expense_ax.axis('equal')
        self.customize_expense_pie_chart()
        self.expense_canvas.draw()

        # Update the title
        selected_month_year = self.window().year_month_combobox.currentText()
        self.expense_ax.set_title(f"Expenses Distribution - {selected_month_year}")
        self.expense_canvas.draw()

    def customize_expense_pie_chart(self):
        for text in self.expense_ax.texts:
            text.set_fontsize(10)
            text.set_fontweight('bold')
