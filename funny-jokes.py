import tkinter as tk
import pyjokes

def get_joke():
    """Retrieves a random programming joke from the pyjokes library.

    Returns:
        str: A string containing a randomly selected programming joke.
    """
    joke = pyjokes.get_joke()
    return joke

# Create the main window
root = tk.Tk()
root.title("Py Joke")

# Generate and display the joke label
# The get_joke() function is called here to get the joke text
label = tk.Label(root, text=get_joke(), wraplength=400)
label.pack(pady=20, padx=20)

# Start the Tkinter event loop
root.mainloop()
