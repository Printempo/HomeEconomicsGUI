# Home Economics GUI

Home Economics GUI is a PyQt5-based application that helps users manage and visualize their monthly expenses and incomes. The GUI provides an interactive interface with three main tabs: Expenses, Incomes, and Data Processing.

## Features

- **Expense Tracking:** The Expenses tab allows users to input various expense categories along with their respective amounts. The provided pie chart visually represents the distribution of expenses for the selected month.

- **Income Management:** The Incomes tab enables users to enter different sources of income and their corresponding amounts. An income pie chart is generated to illustrate the income distribution for the chosen month.

- **Data Processing:** The Data Processing tab displays the result of the financial data processing. It calculates the difference between total incomes and total expenses, providing users with an overview of their financial situation. The result is displayed in a dynamic label with color-coded formatting based on the calculated difference.

- **Legend Table:** The Legend table helps users interpret the color codes used in the result display, categorizing the financial situation as Positive (Excellent, Good, Needs improvement, Reasonable) or Negative (Dangerous, Concerning).

- **Save as Figure:** Users can save the entire Data Processing sheet, including the pie charts and legend, as an image file (PNG format). The Save Figure button prompts the user to choose a destination and filename for the saved figure.

## How to Use

1. Run the `main.py` script.
2. Select the desired year and month using the combo box.
3. Navigate between the Expenses, Incomes, and Data Processing tabs to manage and visualize your financial data.
4. Click the "Update Expenses" and "Update Incomes" buttons to refresh the pie charts.
5. Explore the Legend table to understand the color-coded financial result.
6. Use the "Save Figure" button to save the entire Data Processing sheet as an image.

## Requirements

- Python 3.x
- PyQt5
- Matplotlib

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using the following command:

   ```
   pip install PyQt5 matplotlib
   ```

3. Run the `main.py` script to launch the Home Economics GUI.
![GUI_homeEconomics_expeneses](https://github.com/Printempo/HomeEconomicsGUI/assets/97199103/31022dd6-5a00-4f4f-9290-6546e8eb3732)

![GUI_homeEconomics_example](https://github.com/Printempo/HomeEconomicsGUI/assets/97199103/e907084c-5173-4122-b64f-690d950d3201)

Feel free to customize the expense and income categories based on your specific financial needs.

**Note:** Make sure to adjust file paths and organize your project structure as needed.
