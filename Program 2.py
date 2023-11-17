import tkinter as tk
from tkinter import messagebox

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Program 2 :)")

        # Left Side of the Window
        self.left_frame = tk.Frame(self, bg="#CAE1FF", width=200, height=200)
        self.left_frame.pack(side="left", fill="both", expand=True)

        # Right Side of the Window
        self.right_frame = tk.Frame(self, bg="#CAE1FF", width=200, height=100)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Widgets
        
        # Input Label and Entry
        self.input_label = tk.Label(self.left_frame, text="Input:", bg="white", font=("20"))
        self.input_label.pack(padx=10, pady=10)
        
        self.name_label = tk.Label(self.left_frame, bg="white", text="Name:")
        self.name_label.pack(padx=10, pady=10)
        
        self.name_entry = tk.Entry(self.left_frame)
        self.name_entry.pack(padx=10, pady=10)

        self.age_label = tk.Label(self.left_frame, bg="white", text="Age:")
        self.age_label.pack(padx=10, pady=10)

        self.age_entry = tk.Entry(self.left_frame)
        self.age_entry.pack(padx=10, pady=10)
        
        self.address_label = tk.Label(self.left_frame, bg="white", text="Address:")
        self.address_label.pack(padx=10, pady=10)
        
        self.address_entry = tk.Entry(self.left_frame)
        self.address_entry.pack(padx=10, pady=10)

        # Button 
        self.submit_button = tk.Button(self.left_frame, text="Submit", command=self.update_output)
        self.submit_button.pack(padx=10, pady=10)
        
        # Output Label
        self.output_label = tk.Label(self.right_frame, bg="white", text="Output:", font=("20"))
        self.output_label.pack(padx=10, pady=10)

        self.output_text = tk.Text(self.right_frame, wrap="word")
        self.output_text.pack(padx=10, pady=10)

    # Validation of no inputs and wrong inputs
    def is_valid(self):
        if self.name_entry.get() == "" or self.age_entry.get() == "" or self.address_entry.get() == "" or self.name_entry.get().isdigit() or self.age_entry.get().isalpha():
            return False
        return True

    def update_output(self):
        if not self.is_valid():
            tk.messagebox.showwarning("Invalid Input", "Please enter all the required and correct information.")
            return
        self.output_text.delete(1.0, "end")
        self.output_text.insert("end", "Name: " + self.name_entry.get() + "\n")
        self.output_text.insert("end", "Age: " + self.age_entry.get() + "\n")
        self.output_text.insert("end", "Address: " + self.address_entry.get() + "\n")
        
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()