import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Simple Window")

    # Create a label widget
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack()

    # Run the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()
