import tkinter as tk

def button_click():
    input_text1 = left_text1.get("1.0", "end-1c")
    input_text2 = left_text2.get("1.0", "end-1c")
    result_label.config(text=f"You entered:\nText Box 1: {input_text1}\nText Box 2: {input_text2}")

root = tk.Tk()
root.title("Playfair cipher")

# Set the background color to dark green
root.configure(bg="black")

# Create and place the left text boxes
left_text1 = tk.Text(root, width=20, height=5)
left_text1.grid(row=0, column=0, padx=10, pady=5)

left_text2 = tk.Text(root, width=20, height=5)
left_text2.grid(row=1, column=0, padx=10, pady=5)

left_text3 = tk.Text(root, width=20, height=5)
left_text3.grid(row=2, column=0, padx=10, pady=5)

# Insert the text into the left text boxes
left_text1.insert("1.0", "Text to encrypt ")
left_text2.insert("1.0", "Filtered text")
left_text3.insert("1.0", "Encrypted text")

# Create and place the middle text boxes
middle_text1 = tk.Text(root, width=20, height=5)
middle_text1.grid(row=0, column=1, padx=10, pady=5)

middle_text2 = tk.Text(root, width=20, height=5)
middle_text2.grid(row=1, column=1, padx=10, pady=5)

middle_text1.insert("1.0", "Keyword ")

# Create and place the right text boxes
right_text1 = tk.Text(root, width=20, height=5)
right_text1.grid(row=0, column=2, padx=10, pady=5)

right_text2 = tk.Text(root, width=20, height=5)
right_text2.grid(row=1, column=2, padx=10, pady=5)

right_text3 = tk.Text(root, width=20, height=5)
right_text3.grid(row=2, column=2, padx=10, pady=5)

right_text1.insert("1.0", "Text to decrypt ")
right_text2.insert("1.0", "Filtered text")
right_text3.insert("1.0", "Decrypted text")

# Create and place the buttons
left_button = tk.Button(root, text="Left Button", command=button_click)
left_button.grid(row=3, column=0, padx=10, pady=5)

middle_button = tk.Button(root, text="Middle Button", command=button_click)
middle_button.grid(row=3, column=1, padx=10, pady=5)

right_button = tk.Button(root, text="Right Button", command=button_click)
right_button.grid(row=3, column=2, padx=10, pady=5)

# Create a label for displaying the result
result_label = tk.Label(root, text="", width=40)
result_label.grid(row=4, column=1, padx=10, pady=5)

root.mainloop()
