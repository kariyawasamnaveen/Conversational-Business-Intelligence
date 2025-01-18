from tkinter import Tk, Label, Frame, StringVar, OptionMenu, Button, Entry
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

# GUI Functions
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
        result_entry.insert(0, translator.translate_to_sinhala("Invalid Selection"))

# GUI Setup
root = Tk()
root.title(translator.translate_to_sinhala("Data Analysis"))
root.geometry("600x400")

# Table Display
table_frame = Frame(root)
table_frame.pack(pady=10)

headers = ["Product", "Category", "Sales", "Quantity"]
translated_headers = [
    translator.translate_to_sinhala(header) if header in column_translation_map else header for header in headers
]
for j, col in enumerate(translated_headers):
    Label(table_frame, text=col, borderwidth=1, relief="solid", width=15).grid(row=0, column=j)

for i, row in calculator.data.iterrows():
    Label(table_frame, text=row.get("Product", ""), borderwidth=1, relief="solid", width=15).grid(row=i + 1, column=0)
    Label(table_frame, text=row.get("Category", ""), borderwidth=1, relief="solid", width=15).grid(row=i + 1, column=1)
    Label(table_frame, text=row.get("Sales", ""), borderwidth=1, relief="solid", width=15).grid(row=i + 1, column=2)
    Label(table_frame, text=row.get("Quantity", ""), borderwidth=1, relief="solid", width=15).grid(row=i + 1, column=3)

# Dropdown for Column Selection
input_frame = Frame(root)
input_frame.pack(pady=20)

column_selection = StringVar()
column_selection.set(column_translation_map["Sales"])  # Default selection
OptionMenu(input_frame, column_selection, *column_translation_map.values()).grid(row=0, column=1, padx=5)

# Entry for Result
Label(input_frame, text=translator.translate_to_sinhala("Result:")).grid(row=0, column=2, padx=5)
result_entry = Entry(input_frame, width=20)
result_entry.grid(row=0, column=3, padx=5)

# Buttons for Calculations
Button(input_frame, text=translator.translate_to_sinhala("Show Average"), command=lambda: calculate_result("Average")).grid(row=1, column=1, pady=10)
Button(input_frame, text=translator.translate_to_sinhala("Show Maximum"), command=lambda: calculate_result("Maximum")).grid(row=1, column=3, pady=10)

# Run GUI
root.mainloop()
