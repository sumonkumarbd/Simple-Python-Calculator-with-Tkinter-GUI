from tkinter import Tk, Entry, Button, StringVar

class calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry("360x450+0+0")
        master.config(bg="gray")
        master.resizable(False,False)


        self.equation = StringVar()
        self.entry_value = ""
        Entry(width=17,bg="#ccddff",font=("Arial Bold",28),textvariable=self.equation).place(x=0,y=0)
        
        button_config = {"width": 11, "height": 4, "relief": "flat", "anchor": "center","padx":5, "pady":5}
        Button(**button_config, text="(", bg="white", command=lambda: self.show("(")).place(x=0, y=50)
        Button(**button_config, text=")", bg="white", command=lambda: self.show(")")).place(x=90, y=50)
        Button(**button_config, text="%", bg="white", command=lambda: self.percentage()).place(x=180, y=50)
        Button(**button_config, text="/", bg="white", command=lambda: self.show("/")).place(x=270, y=50)

        Button(**button_config, text="7", bg="white", command=lambda: self.show(7)).place(x=0, y=125)
        Button(**button_config, text="8", bg="white", command=lambda: self.show(8)).place(x=90, y=125)
        Button(**button_config, text="9", bg="white", command=lambda: self.show(9)).place(x=180, y=125)
        Button(**button_config, text="x", bg="white", command=lambda: self.show("*")).place(x=270, y=125)

        Button(**button_config, text="4", bg="white", command=lambda: self.show(4)).place(x=0, y=200)
        Button(**button_config, text="5", bg="white", command=lambda: self.show(5)).place(x=90, y=200)
        Button(**button_config, text="6", bg="white", command=lambda: self.show(6)).place(x=180, y=200)
        Button(**button_config, text="-", bg="white", command=lambda: self.show("-")).place(x=270, y=200)

        Button(**button_config, text="1", bg="white", command=lambda: self.show(1)).place(x=0, y=275)
        Button(**button_config, text="2", bg="white", command=lambda: self.show(2)).place(x=90, y=275)
        Button(**button_config, text="3", bg="white", command=lambda: self.show(3)).place(x=180, y=275)
        Button(**button_config, text="+", bg="white", command=lambda: self.show("+")).place(x=270, y=275)

        Button(**button_config, text="C", bg="white", command=self.clear).place(x=0, y=350)
        Button(**button_config, text="0", bg="white", command=lambda: self.show(0)).place(x=90, y=350)
        Button(**button_config, text=".", bg="white", command=lambda: self.show(".")).place(x=180, y=350)
        Button(**button_config, text="=", bg="lightblue", command=self.solve).place(x=270, y=350)


    def show(self,value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    
    def clear(self):
        self.entry_value=""
        self.equation.set(self.entry_value)


    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)



    def percentage(self):
        try:
            if self.entry_value:
                expression = self.entry_value.strip()

                # Check if an operator exists
                for op in "+-*/":
                    if op in expression:
                        # Split expression from the operator
                        parts = expression.rsplit(op, 1)
                        if len(parts) == 2 and parts[1].strip():
                            # Get the base value (before the operator) and percentage value (after operator)
                            base_number = float(parts[0].strip())  
                            percent_value = float(parts[1].strip())  # Second number, e.g., 50 for 50%

                            # Apply percentage calculation: Calculate percent_value of base_number
                            percentage_result = (percent_value / 100) * base_number

                            # Update the equation to show the percentage calculation
                            self.entry_value = f"{parts[0]}{op}{percentage_result:.1f}"  # Keep equation format
                            break
                else:
                    # If no operator, treat it as a percentage of the entire number
                    self.entry_value = str(float(expression) / 100)

                self.equation.set(self.entry_value)  # Update the display
        except Exception:
            self.equation.set("Error")  # Display error if something goes wrong
            self.entry_value = ""




root = Tk()
calculator = calculator(root)
root.mainloop()






