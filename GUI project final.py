import tkinter as tk
from tkinter import messagebox, ttk

class CakeOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cake Order System")
        self.root.geometry("800x600")
        
        # Initialize customer selection variables
        self.cake_type = tk.StringVar()
        self.cake_size = tk.StringVar()
        self.cake_flavor = tk.StringVar()
        self.customer_name = tk.StringVar()
        self.customer_phone = tk.StringVar()
        
        # Create and show the main window
        self.create_main_window()
    
    def create_main_window(self):
        # Clear previous content
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header
        header_label = tk.Label(self.root, text="Sweet Delights Cake Shop", font=("Arial", 20, "bold"))
        header_label.pack(pady=20)
        
        # Create frame for cake selection
        selection_frame = tk.Frame(self.root)
        selection_frame.pack(pady=20)
        
        # Chocolate cake option
        chocolate_frame = tk.Frame(selection_frame)
        chocolate_frame.pack(side=tk.LEFT, padx=20)
        
        # Create chocolate cake image using Canvas
        chocolate_canvas = tk.Canvas(chocolate_frame, width=200, height=150, bg="#F5F5F5")
        chocolate_canvas.create_oval(50, 30, 150, 130, fill="#4A2C2A", outline="#4A2C2A")
        chocolate_canvas.create_rectangle(40, 80, 160, 130, fill="#4A2C2A", outline="#4A2C2A")
        chocolate_canvas.create_line(50, 80, 150, 80, fill="#7B3F00", width=2)
        chocolate_canvas.pack()
        
        # Add alt text as tooltip
        chocolate_canvas.bind("<Enter>", lambda e: self.show_tooltip(e, "Image of chocolate cake"))
        chocolate_canvas.bind("<Leave>", self.hide_tooltip)
        
        chocolate_label = tk.Label(chocolate_frame, text="Chocolate Cake", font=("Arial", 12))
        chocolate_label.pack(pady=5)
        
        chocolate_button = tk.Button(chocolate_frame, text="Select", command=lambda: self.select_cake("Chocolate"))
        chocolate_button.pack(pady=5)
        
        # Vanilla cake option
        vanilla_frame = tk.Frame(selection_frame)
        vanilla_frame.pack(side=tk.LEFT, padx=20)
        
        # Create vanilla cake image using Canvas
        vanilla_canvas = tk.Canvas(vanilla_frame, width=200, height=150, bg="#F5F5F5")
        vanilla_canvas.create_oval(50, 30, 150, 130, fill="#FFF8E7", outline="#FFF8E7")
        vanilla_canvas.create_rectangle(40, 80, 160, 130, fill="#FFF8E7", outline="#FFF8E7")
        vanilla_canvas.create_line(50, 80, 150, 80, fill="#FFE4B5", width=2)
        vanilla_canvas.pack()
        
        # Add alt text as tooltip
        vanilla_canvas.bind("<Enter>", lambda e: self.show_tooltip(e, "Image of vanilla cake"))
        vanilla_canvas.bind("<Leave>", self.hide_tooltip)
        
        vanilla_label = tk.Label(vanilla_frame, text="Vanilla Cake", font=("Arial", 12))
        vanilla_label.pack(pady=5)
        
        vanilla_button = tk.Button(vanilla_frame, text="Select", command=lambda: self.select_cake("Vanilla"))
        vanilla_button.pack(pady=5)
        
        # Exit button
        exit_button = tk.Button(self.root, text="Exit", command=self.exit_application)
        exit_button.pack(side=tk.BOTTOM, pady=20)
    
    def select_cake(self, cake_type):
        """Callback function for selecting a cake type"""
        self.cake_type.set(cake_type)
        self.open_customization_window()
    
    def open_customization_window(self):
        """Create and show the customization window"""
        # Clear previous content
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header
        header_label = tk.Label(self.root, text=f"Customize Your {self.cake_type.get()} Cake", font=("Arial", 18, "bold"))
        header_label.pack(pady=20)
        
        # Create frame for customization options
        customize_frame = tk.Frame(self.root)
        customize_frame.pack(pady=20)
        
        # Size selection
        size_label = tk.Label(customize_frame, text="Select Size:", font=("Arial", 12))
        size_label.grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)
        
        size_options = ["Small (6-inch)", "Medium (8-inch)", "Large (10-inch)"]
        size_menu = ttk.Combobox(customize_frame, textvariable=self.cake_size, values=size_options, width=20)
        size_menu.grid(row=0, column=1, pady=10, padx=10)
        size_menu.current(0)
        
        # Flavor selection
        flavor_label = tk.Label(customize_frame, text="Select Flavor:", font=("Arial", 12))
        flavor_label.grid(row=1, column=0, sticky=tk.W, pady=10, padx=10)
        
        if self.cake_type.get() == "Chocolate":
            flavor_options = ["Dark Chocolate", "Milk Chocolate", "White Chocolate"]
        else:
            flavor_options = ["Classic Vanilla", "French Vanilla", "Vanilla Bean"]
        
        flavor_menu = ttk.Combobox(customize_frame, textvariable=self.cake_flavor, values=flavor_options, width=20)
        flavor_menu.grid(row=1, column=1, pady=10, padx=10)
        flavor_menu.current(0)
        
        # Customer information
        info_frame = tk.Frame(self.root)
        info_frame.pack(pady=20)
        
        name_label = tk.Label(info_frame, text="Your Name:", font=("Arial", 12))
        name_label.grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)
        
        name_entry = tk.Entry(info_frame, textvariable=self.customer_name, width=30)
        name_entry.grid(row=0, column=1, pady=10, padx=10)
        
        phone_label = tk.Label(info_frame, text="Phone Number:", font=("Arial", 12))
        phone_label.grid(row=1, column=0, sticky=tk.W, pady=10, padx=10)
        
        phone_entry = tk.Entry(info_frame, textvariable=self.customer_phone, width=30)
        phone_entry.grid(row=1, column=1, pady=10, padx=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)
        
        back_button = tk.Button(buttons_frame, text="Back", command=self.create_main_window)
        back_button.grid(row=0, column=0, padx=10)
        
        order_button = tk.Button(buttons_frame, text="Place Order", command=self.confirm_order)
        order_button.grid(row=0, column=1, padx=10)
        
        exit_button = tk.Button(buttons_frame, text="Exit", command=self.exit_application)
        exit_button.grid(row=0, column=2, padx=10)
    
    def confirm_order(self):
        """Callback function to confirm and process the order"""
        # Validate input
        if not self.customer_name.get() or not self.customer_phone.get():
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        # Open confirmation window
        self.open_confirmation_window()
    
    def open_confirmation_window(self):
        """Create and show the order confirmation window"""
        # Clear previous content
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header
        header_label = tk.Label(self.root, text="Order Confirmation", font=("Arial", 18, "bold"))
        header_label.pack(pady=20)
        
        # Order details
        details_frame = tk.Frame(self.root)
        details_frame.pack(pady=20)
        
        # Calculate price (just for demonstration)
        size_prices = {"Small (6-inch)": 25, "Medium (8-inch)": 35, "Large (10-inch)": 45}
        price = size_prices.get(self.cake_size.get(), 25)
        
        details = [
            f"Customer: {self.customer_name.get()}",
            f"Phone: {self.customer_phone.get()}",
            f"Cake Type: {self.cake_type.get()}",
            f"Size: {self.cake_size.get()}",
            f"Flavor: {self.cake_flavor.get()}",
            f"Price: ${price}"
        ]
        
        for i, detail in enumerate(details):
            label = tk.Label(details_frame, text=detail, font=("Arial", 12))
            label.pack(anchor=tk.W, pady=5)
        
        # Thank you message
        thank_label = tk.Label(self.root, text="Thank you for your order!", font=("Arial", 14, "bold"))
        thank_label.pack(pady=20)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)
        
        new_order_button = tk.Button(buttons_frame, text="New Order", command=self.create_main_window)
        new_order_button.grid(row=0, column=0, padx=10)
        
        exit_button = tk.Button(buttons_frame, text="Exit", command=self.exit_application)
        exit_button.grid(row=0, column=1, padx=10)
    
    def show_tooltip(self, event, text):
        """Show tooltip with alt text for images"""
        x, y, _, _ = event.widget.bbox("insert")
        x += event.widget.winfo_rootx() + 25
        y += event.widget.winfo_rooty() + 25
        
        # Create a toplevel window
        self.tooltip = tk.Toplevel(event.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        label = tk.Label(self.tooltip, text=text, background="#ffffe0", relief=tk.SOLID, borderwidth=1)
        label.pack()
    
    def hide_tooltip(self, event):
        """Hide the tooltip"""
        if hasattr(self, "tooltip"):
            self.tooltip.destroy()
    
    def exit_application(self):
        """Callback function to exit the application"""
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

# Main function to start the application
def main():
    root = tk.Tk()
    app = CakeOrderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
