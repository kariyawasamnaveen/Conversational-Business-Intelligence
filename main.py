from ttkbootstrap import Style
from ttkbootstrap.constants import *
from tkinter import StringVar
from tkinter.ttk import Frame, Treeview, Label, Combobox, Entry, Button
from ttkbootstrap.dialogs import Messagebox
from utils.translator import TranslatorUtility
from utils.calculator import DataCalculator


# Initialize utilities
translator = TranslatorUtility()
calculator = DataCalculator("data.csv")

# Translation mappings
column_translation_map = {
    "Sales": translator.translate_to_sinhala("Sales"),
    "Quantity": translator.translate_to_sinhala("Quantity")
}
inverse_column_translation_map = {v: k for k, v in column_translation_map.items()}


# Function to calculate results
def calculate_result(operation):
    selected_column_sinhala = column_selection.get()
    selected_column = inverse_column_translation_map.get(selected_column_sinhala, None)

    result_entry.delete(0, "end")
    if selected_column:
        if operation == "Average":
            result = calculator.calculate_average(selected_column)
        elif operation == "Maximum":
            result = calculator.calculate_maximum(selected_column)
        result_entry.insert(0, f"{result:.2f}")
    else:
        Messagebox.show_error(translator.translate_to_sinhala("Invalid Selection"))


# Create main window
style = Style(theme="flatly")  # Modern theme
root = style.master
root.title(translator.translate_to_sinhala("Conversational Business Intelligence"))
root.geometry("900x600")
root.resizable(False, False)

# Header Section
header_frame = Frame(root, padding=10)
header_frame.pack(fill=X)
header_label = Label(header_frame, text=translator.translate_to_sinhala("Conversational Business Intelligence"),
                     font=("Helvetica", 18, "bold"))
header_label.pack(pady=5)

# Table Section
table_frame = Frame(root, padding=10)
table_frame.pack(fill=BOTH, expand=True)

# Create Treeview table
columns = ["Product", "Category", "Sales", "Quantity"]
translated_columns = [
    translator.translate_to_sinhala(col) if col in column_translation_map else col for col in columns
]
tree = Treeview(table_frame, columns=columns, show="headings", height=10)

# Define column widths and headings
for col, translated_col in zip(columns, translated_columns):
    tree.heading(col, text=translated_col, anchor=CENTER)
    tree.column(col, anchor=CENTER, width=200)

# Add data to the table
for _, row in calculator.data.iterrows():
    tree.insert("", "end", values=(row["Product"], row["Category"], row["Sales"], row["Quantity"]))

tree.pack(fill=BOTH, expand=True)

# Input Section
input_frame = Frame(root, padding=10)
input_frame.pack(fill=X, pady=10)

Label(input_frame, text=translator.translate_to_sinhala("Select Column:"), font=("Helvetica", 12)).pack(side=LEFT, padx=5)
column_selection = StringVar(value=column_translation_map["Sales"])
Combobox(input_frame, textvariable=column_selection, values=list(column_translation_map.values()),
         font=("Helvetica", 12), width=20).pack(side=LEFT, padx=5)

Label(input_frame, text=translator.translate_to_sinhala("Result:"), font=("Helvetica", 12)).pack(side=LEFT, padx=5)
result_entry = Entry(input_frame, font=("Helvetica", 12), width=25)
result_entry.pack(side=LEFT, padx=5)

# Button Section
button_frame = Frame(root, padding=10)
button_frame.pack(fill=X)

Button(button_frame, text=translator.translate_to_sinhala("Show Average"),
       command=lambda: calculate_result("Average")).pack(side=LEFT, padx=10)

Button(button_frame, text=translator.translate_to_sinhala("Show Maximum"),
       command=lambda: calculate_result("Maximum")).pack(side=LEFT, padx=10)

Button(button_frame, text=translator.translate_to_sinhala("Exit"),
       command=root.destroy).pack(side=RIGHT, padx=10)

# Run the GUI
root.mainloop()
