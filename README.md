# Python Calculator with Tkinter

## Overview
This is a **simple Python calculator** application built using the **Tkinter** library. It provides a graphical user interface (GUI) for performing basic arithmetic operations (addition, subtraction, multiplication, and division) along with more advanced functionality like percentage calculations. The calculator is user-friendly and ideal for beginners learning Python and GUI development.

## Features
* **Basic Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
* **Percentage Calculations**: Calculate percentages and apply them to existing equations.
* **Clear Functionality**: Clear the current entry with the `C` button.
* **Responsive UI**: Designed using Tkinter for a clean, intuitive interface.
* **Error Handling**: Proper error handling for invalid operations.

## Installation
Follow these steps to install and run the calculator:

1. **Clone the Repository:**
   First, clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/calculator-python-tkinter.git
   ```

2. **Navigate to the Project Directory:**
   Change to the project folder:
   ```bash
   cd calculator-python-tkinter
   ```

3. **Install Tkinter (if not already installed):**
   Tkinter is often bundled with Python, but if it's not available, you can install it using:
   * For **Ubuntu/Debian**:
     ```bash
     sudo apt-get install python3-tk
     ```
   * For **Windows**, Tkinter is included by default, so no installation is needed.

4. **Install Dependencies (if any):**
   You can install dependencies (if any) using pip:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: This project does not have any additional dependencies beyond Tkinter.*

## Usage
Running the Calculator:
1. Open the project folder.
2. Run the calculator script:
   ```bash
   python calculator.py
   ```

Interface Overview:
* The **Entry** at the top shows the current equation.
* **Buttons** for numbers, operators, and functions are laid out below the entry.
* **Clear (C)**: Clears the current input.
* **Percentage (%)**: Applies percentage to the last operand in the equation.
* **Equal (=)**: Evaluates the equation and displays the result.

Example Usage:
* To calculate `200 + 50`, type `200`, press the `+` button, type `50`, and then press `=`.
* To calculate a percentage, like `50% of 200`, input `200 + 50`, press `%`, and the equation will show `200 + 100.0`.

## Code Structure
`calculator.py`
This script contains the main calculator application code.
* **GUI Setup**: Uses Tkinter to create the user interface, including an entry for input and buttons for numbers and operations.
* **Functions**:
   * `show(value)`: Displays the clicked button value in the entry field.
   * `clear()`: Clears the current equation.
   * `solve()`: Evaluates the equation and displays the result.
   * `percentage()`: Handles percentage operations and updates the equation.

Example:
Let's say you want to calculate 20% of 200:
1. Input: `200 + 20`
2. Press `%` to apply the percentage.
3. The display will show: `200 + 40.0`.
4. Press `=` to evaluate the expression, which will give the result `240.0`.

## Contribution
Feel free to contribute to this project! Here's how you can contribute:
1. **Fork** the repository and clone it to your local machine.
2. Create a **new branch** for your feature or bug fix.
3. Make your changes and **commit** them with descriptive messages.
4. Push your changes to your fork and create a **pull request**.

## License
This project is licensed under the **MIT License**. See the LICENSE file for more details.

## Acknowledgements
* **Tkinter**: For building the GUI of the calculator.
* **Python**: The primary language used to build this project.
* The **Python community** for continuous learning resources and support.

## Contact
If you have any questions or suggestions, feel free to open an issue on the GitHub repository or contact me directly.

---
**Notes:**
* Replace `your-username` with your actual GitHub username in the clone link.
* Ensure to provide a `LICENSE` file if you include the MIT License or another license for the project.
