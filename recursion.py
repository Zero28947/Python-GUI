import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *  
import os
import sys

# --- Configuration ---
BG_COLOR = "#0D1B2A"  # Dark Blue
FG_COLOR = "#E0E1DD"  # Light Gray
BTN_COLOR = "#E76F51" # Red/Orange
BTN_FG = "#FFFFFF"
INPUT_BG = "#1B263B"
TEXT_BG = "#1B263B"

# --- MODIFIED: Global Style Setup ---
# This function now takes your 'root' window as an argument
def setup_styles(root):
    s = ttk.Style()
    s.theme_use('clam')
    s.configure('.', background=BG_COLOR, foreground=FG_COLOR, fieldbackground=INPUT_BG, bordercolor="#888")
    s.map('.', 
          foreground=[('disabled', '#777'), ('active', FG_COLOR)], 
          background=[('disabled', '#444'), ('active', INPUT_BG)], 
          fieldbackground=[('disabled', '#444')])
    
    s.configure('TButton', background=BTN_COLOR, foreground=BTN_FG, font=('Helvetica', 11, 'bold'), padding=5, borderwidth=0)
    s.map('TButton', 
          background=[('active', '#F4A261')], 
          foreground=[('active', BTN_FG)])
    
    s.configure('Large.TButton', font=('Helvetica', 14, 'bold'), padding=10)
    
    s.configure('TCombobox', font=('Helvetica', 11), padding=5)
    # These settings now apply to the 'root' window you pass in
    root.option_add('*TCombobox*Listbox.background', INPUT_BG)
    root.option_add('*TCombobox*Listbox.foreground', FG_COLOR)
    root.option_add('*TCombobox*Listbox.selectBackground', BTN_COLOR)
    
    s.configure('TLabel', font=('Helvetica', 11), padding=2)
    s.configure('TEntry', font=('Helvetica', 11), padding=5, borderwidth=1, relief="solid", foreground=FG_COLOR, insertcolor=FG_COLOR)
    s.configure('TCheckbutton', font=('Helvetica', 10), padding=5)
    s.map('TCheckbutton', 
          indicatorbackground=[('selected', BTN_COLOR), ('!selected', INPUT_BG)], 
          indicatorforeground=[('selected', FG_COLOR), ('!selected', FG_COLOR)])


# --- Logic for all Recursion Algorithms ---
# This class is unchanged
class RecursionLogic:
    def __init__(self):
        self.steps = []
        self.memo = {}

    # --- 1. Linear Recursion (e.g., Sum of n) ---
    def _linear_recursion(self, n):
        if n == 1:
            self.steps.append("Base: 1")
            return 1
        else:
            result = n + self._linear_recursion(n - 1)
            self.steps.append(f"{n} + {result - n} = {result}")
            return result

    # --- 2. Tail Recursion (e.g., Factorial with accumulator) ---
    def _tail_recursion(self, n, acc):
        if n == 0:
            self.steps.append(f"Final Value: {acc}")
            return acc
        else:
            self.steps.append(f"acc = {acc} * {n}  ->  {n * acc}")
            return self._tail_recursion(n - 1, n * acc)

    # --- 3. Tree Recursion (e.g., Fibonacci) ---
    def _tree_recursion(self, n):
        if n <= 1:
            self.steps.append(f"fib({n}) = {n}")
            return n
        else:
            res1 = self._tree_recursion(n - 1)
            res2 = self._tree_recursion(n - 2)
            result = res1 + res2
            self.steps.append(f"fib({n}) = {res1} + {res2}")
            return result
            
    # --- 4. Nested Recursion (SAFE & MEMOIZED) ---
    def _nested_subtract(self, n):
        """A simple nested function: f(n) = n - f(f(n-1))"""
        if n in self.memo:
            self.steps.append(f"f({n}) -> (from memory): {self.memo[n]}")
            return self.memo[n]

        self.steps.append(f"f({n}):")
        if n < 3:
            self.steps.append(f"   Base case is 1")
            self.memo[n] = 1
            return 1
        else:
            self.steps.append(f"   Inner call: f({n-1})")
            inner_result = self._nested_subtract(n - 1)
            
            self.steps.append(f"   Outer call: f({inner_result})")
            outer_result = self._nested_subtract(inner_result)
            
            final_result = n - outer_result
            self.steps.append(f"   Result: {n} - {outer_result} = {final_result}")
            self.memo[n] = final_result
            return final_result

    # --- 5. Mutual Recursion (e.g., IsEven/IsOdd) ---
    def _mutual_is_even(self, n):
        if n == 0:
            self.steps.append("is_even(0) = True")
            return True
        else:
            self.steps.append(f"is_even({n}) -> is_odd({n-1})")
            return self._mutual_is_odd(n - 1)

    def _mutual_is_odd(self, n):
        if n == 0:
            self.steps.append("is_odd(0) = False")
            return False
        else:
            self.steps.append(f"is_odd({n}) -> is_even({n-1})")
            return self._mutual_is_even(n - 1)

    # --- 6. Indirect Recursion (e.g., A -> B -> C -> A) ---
    def _indirect_A(self, n):
        if n > 0:
            self.steps.append(f"A({n}) -> B({n-1})")
            self._indirect_B(n - 1)
        else:
            self.steps.append("A(0)")

    def _indirect_B(self, n):
        if n > 0:
            self.steps.append(f"B({n}) -> C({n-1})")
            self._indirect_C(n - 1)
        else:
            self.steps.append("B(0)")

    def _indirect_C(self, n):
        if n > 0:
            self.steps.append(f"C({n}) -> A({n-1})")
            self._indirect_A(n - 1)
        else:
            self.steps.append("C(0)")

    # --- 7. Head Recursion (e.g., Print 1-to-n) ---
    def _head_recursion(self, n):
        if n == 0:
            self.steps.append("Base: head(0)")
            return
        else:
            self.steps.append(f"head({n}) -> head({n-1})")
            self._head_recursion(n - 1)
            self.steps.append(f"Process: {n}") # Process after call returns
            
    # --- Main Compute Function (Tracing) ---
    def compute(self, algo, val1):
        self.steps = []
        self.memo = {} # Reset memoization for each run
        try:
            if algo == "Linear":
                if val1 < 1: self.steps.append("Input must be >= 1"); return self.steps
                result = self._linear_recursion(val1)
            
            elif algo == "Tail":
                if val1 < 0: self.steps.append("Input must be >= 0"); return self.steps
                result = self._tail_recursion(val1, 1)

            elif algo == "Tree":
                if val1 < 0: self.steps.append("Input must be >= 0"); return self.steps
                result = self._tree_recursion(val1)

            elif algo == "Nested":
                if val1 < 0: self.steps.append("Input must be >= 0"); return self.steps
                result = self._nested_subtract(val1)

            elif algo == "Mutual":
                if val1 < 0: self.steps.append("Input must be >= 0"); return self.steps
                result = self._mutual_is_even(val1)

            elif algo == "Indirect":
                if val1 < 0: self.steps.append("Input must be >= 0"); return self.steps
                self._indirect_A(val1)
                result = "Complete"

            elif algo == "Head":
                if val1 < 0: self.steps.append("Input must be >= 0"); return self.steps
                self._head_recursion(val1)
                result = "Complete"
            else:
                self.steps.append("Error: Please select an algorithm.")
                return self.steps
                
            self.steps.append(f"\nFinal Result: {result}")
                
        except RecursionError:
            self.steps.append("\n---!! STACK OVERFLOW !!---")
            self.steps.append(f"Input '{val1}' is too large for tracing.")
        except Exception as e:
            self.steps.append(f"\nAn error occurred: {e}")
            
        return self.steps


# --- Main Application Window (Toplevel) ---
# This class is the one your friend will import and call.
# It now includes a built-in animated welcome screen.
class RecursionTool(tk.Toplevel):
    def __init__(self, parent):
        # --- Setup the new window ---
        super().__init__(parent)
        self.title("CC 2103 Project")
        self.configure(bg=BG_COLOR)
        icon = PhotoImage(file='image/hacker06.png')
        self.iconphoto(True, icon)
        self.state("zoomed")
        
        # This stops the window from shrinking to fit the widgets
        self.pack_propagate(False) 

        # Set recursion limit for this tool
        sys.setrecursionlimit(2000)

        self.logic = RecursionLogic()
        
        # Animation IDs
        self.intro_animation_id = None
        self.step_animation_id = None 
        
        self.current_steps = []
        self.current_step_index = 0
        self.is_fullscreen = False 

        self.descriptions = {
            "Linear": "One recursive call. Processing happens after the call returns (on the way 'up').\nExample: Sum(n) = n + Sum(n-1)",
            "Tail": "One recursive call, which is the VERY last action. All processing happens *before* the call.\nExample: Fact(n, acc) = Fact(n-1, n*acc)",
            "Tree": "Multiple recursive calls (e.g., two or more). Creates a branching, tree-like structure of calls.\nExample: Fib(n) = Fib(n-1) + Fib(n-2)",
            "Nested": "A recursive call is passed as an argument to another recursive call.\nExample: f(n) = n - f( f(n-1) )",
            "Mutual": "Two or more functions call each other in a cycle.\nExample: is_even(n) calls is_odd(n-1)",
            "Indirect": "A function calls another... eventually leading back to the first function.",
            "Head": "The recursive call is the first operation. All processing happens *after* the call returns.\nExample: print_1_to_n(n)"
        }

        # --- NEW: Animated Welcome Screen ---
        # Start the window as fully transparent
        self.attributes("-alpha", 0.0)
        
        # Create the welcome frame
        self.welcome_frame = tk.Frame(self, bg=BG_COLOR)
        self.welcome_frame.pack(fill="both", expand=True)
        
        tk.Label(self.welcome_frame, text="Welcome to the",
                 font=("Helvetica", 24, "bold"), 
                 bg=BG_COLOR, fg=FG_COLOR).place(relx=0.5, rely=0.4, anchor="center")
        
        tk.Label(self.welcome_frame, text="Recursion Learning Tool",
                 font=("Helvetica", 32, "bold"), 
                 bg=BG_COLOR, fg=FG_COLOR).place(relx=0.5, rely=0.5, anchor="center")

        # --- Make this window modal ---
        self.grab_set()
        
        # --- NEW: Handle window closing ---
        # This will properly close the app when run directly
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Start the fade-in animation
        self.fade_in()
        
    def on_close(self):
        """Handles window close event."""
        # Cancel any pending animations to prevent errors
        try:
            if self.intro_animation_id:
                self.after_cancel(self.intro_animation_id)
                self.intro_animation_id = None
            if self.step_animation_id:
                self.after_cancel(self.step_animation_id)
                self.step_animation_id = None
        except Exception as e:
            print(f"Error cancelling animations: {e}") # Handle errors if window closes fast

        # Destroy this window
        self.destroy()
        
        # NEW: Check if the parent window is hidden (withdrawn)
        # If it is, that means we are in test mode, so close the root app.
        # self.master is the 'parent' window passed to __init__
        if self.master.winfo_ismapped() == 0:
            self.master.destroy()

    def fade_in(self, alpha=0.0):
        """Animates the window fading in."""
        new_alpha = alpha + 0.05
        try:
            if new_alpha < 1.0:
                self.attributes("-alpha", new_alpha)
                self.intro_animation_id = self.after(25, lambda: self.fade_in(new_alpha))
            else:
                # Fade-in complete
                self.attributes("-alpha", 1.0)
                # Wait 1.5 seconds, then show the main tool
                self.intro_animation_id = self.after(1500, self.show_main_tool)
        except tk.TclError:
            # Window was closed during fade-in
            pass

    def show_main_tool(self):
        """Destroys the welcome screen and builds the main tool UI."""
        if self.intro_animation_id:
            self.after_cancel(self.intro_animation_id)
            self.intro_animation_id = None
            
        # Remove the welcome screen
        self.welcome_frame.destroy()

        # --- Build the Main Tool UI ---
        self.columnconfigure(0, weight=1, minsize=300)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        self.control_frame = tk.Frame(self, bg=BG_COLOR, bd=10)
        self.control_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.control_frame.columnconfigure(0, weight=1)

        tk.Label(self.control_frame, text="Recursion Learning", font=("Helvetica", 20, "bold"), bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, pady=10, sticky="w")
        tk.Label(self.control_frame, text="Recursion is a process where a function calls itself to solve a smaller version of the problem.", font=("Helvetica", 10), bg=BG_COLOR, fg=FG_COLOR, wraplength=280, justify="left").grid(row=1, column=0, pady=(0, 20), sticky="w")
        
        ttk.Label(self.control_frame, text="Choose a recursion type:").grid(row=2, column=0, sticky="w", pady=(10,0))
        self.algo_list = ["Linear", "Tail", "Tree", "Nested", "Mutual", "Indirect", "Head"]
        self.algo_var = tk.StringVar()
        self.dropdown = ttk.Combobox(self.control_frame, textvariable=self.algo_var, values=self.algo_list, state="readonly", width=30)
        self.dropdown.grid(row=3, column=0, sticky="ew", pady=5)
        self.dropdown.bind("<<ComboboxSelected>>", self.on_algo_select)
        
        self.description_label = tk.Message(self.control_frame, text="Select a recursion type to see its definition.", width=280, font=("Helvetica", 10, "italic"), bg=BG_COLOR, fg=FG_COLOR, justify="left")
        self.description_label.grid(row=4, column=0, sticky="ew", pady=(5, 10))

        ttk.Label(self.control_frame, text="Enter integer 'n':").grid(row=5, column=0, sticky="w", pady=(10,0))
        self.entry1_var = tk.StringVar()
        self.entry1 = ttk.Entry(self.control_frame, textvariable=self.entry1_var, width=33)
        self.entry1.grid(row=6, column=0, sticky="ew", pady=5)

        self.show_animation_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.control_frame, text="Show step-by-step animation", variable=self.show_animation_var, style="TCheckbutton").grid(row=9, column=0, sticky="w", pady=5)

        self.compute_button = ttk.Button(self.control_frame, text="Compute", command=self.start_computation, style="Large.TButton")
        self.compute_button.grid(row=10, column=0, sticky="ew", pady=20)

        self.back_button = ttk.Button(self.control_frame, text="Back", command=self.back, style="Large.TButton")
        self.back_button.grid(row=15, column=0, sticky="ew", pady=20)

        
        self.output_frame = tk.Frame(self, bg=BG_COLOR, bd=10)
        self.output_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.output_frame.rowconfigure(1, weight=1)    # Text area row
        self.output_frame.columnconfigure(0, weight=1) # Label/Text col
        self.output_frame.columnconfigure(1, weight=0) # Button col
        self.output_frame.columnconfigure(2, weight=0) # Scrollbar col

        ttk.Label(self.output_frame, text="Computation Process:", font=("Helvetica", 16, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        
        self.fullscreen_button = ttk.Button(self.output_frame, text="Full Screen", command=self.toggle_fullscreen, style="TButton")
        self.fullscreen_button.grid(row=0, column=1, sticky="e", padx=5)

        self.process_text = tk.Text(self.output_frame, height=20, width=60, font=("Consolas", 12), bg=TEXT_BG, fg=FG_COLOR, wrap=tk.NONE, state='disabled', relief="solid", bd=1)
        yscroll = ttk.Scrollbar(self.output_frame, orient=tk.VERTICAL, command=self.process_text.yview)
        xscroll = ttk.Scrollbar(self.output_frame, orient=tk.HORIZONTAL, command=self.process_text.xview)
        self.process_text.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        
        self.process_text.grid(row=1, column=0, columnspan=2, sticky="nsew")
        yscroll.grid(row=1, column=2, sticky="ns")
        xscroll.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.on_algo_select(None)
    
    def back(self):
        self.withdraw()
        os.system("python project.py")
        self.destroy()
        
    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen # Toggle the state

        if self.is_fullscreen:
            # Go Full Screen
            self.control_frame.grid_remove()
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=1)
            self.output_frame.grid_configure(padx=0, pady=0, bd=0)
            self.fullscreen_button.config(text="Exit Full Screen")
            
        else:
            # Exit Full Screen
            self.control_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
            self.columnconfigure(0, weight=1, minsize=300)
            self.columnconfigure(1, weight=3)
            self.output_frame.grid_configure(padx=10, pady=10, bd=10)
            self.fullscreen_button.config(text="Full Screen")

    def on_algo_select(self, event):
        algo = self.algo_var.get()
        description = self.descriptions.get(algo, "Select a recursion type to see its definition.")
        # Need to check if description_label exists yet
        if hasattr(self, 'description_label'):
            self.description_label.config(text=description)

    def start_computation(self):
        self.finish_computation()
            
        self.process_text.config(state='normal')
        self.process_text.delete('1.0', tk.END)
        self.process_text.config(state='disabled')
        
        algo = self.algo_var.get()
        val1_str = self.entry1_var.get()
        
        if not algo:
            # Use messagebox *from this window*
            messagebox.showerror("Input Error", "Please select an algorithm.", parent=self)
            return
        
        try:
            val1 = int(val1_str)
        except ValueError:
            messagebox.showerror("Input Error", f"Invalid input: '{val1_str}'. Must be an integer.", parent=self)
            return

        limit_message = ""
        
        if algo == "Tree" and val1 > 18: 
            limit_message = (
                f"Input n > 18 for Tree (Fibonacci) is too large to animate.\n\n"
                f"This algorithm is O(2^n) and generates too many steps.\n"
                f"Please choose a smaller number (e.g., 10)."
            )
        
        elif algo == "Nested" and val1 > 15: 
             limit_message = (
                f"Input n > 15 for Nested recursion is too large to animate.\n\n"
                f"Even with memoization, the call trace becomes very large.\n"
                f"Please choose a smaller number (e.g., 12)."
            )

        if limit_message:
            self.process_text.config(state='normal')
            self.process_text.insert(tk.END, "--- INPUT LIMIT REACHED ---\n\n")
            self.process_text.insert(tk.END, limit_message)
            self.process_text.config(state='disabled')
            return

        steps = self.logic.compute(algo, val1)
        
        if self.show_animation_var.get():
            self.current_steps = steps
            self.current_step_index = 0
            self.compute_button.config(text="Stop & Show Result", command=self.stop_and_finish_computation)
            self.animate_steps(steps, 0)
        else:
            self.process_text.config(state='normal')
            for step in steps:
                self.process_text.insert(tk.END, step + "\n")
            self.process_text.see(tk.END)
            self.process_text.config(state='disabled')

    def animate_steps(self, steps, index):
        if index < len(steps):
            self.current_step_index = index
            self.process_text.config(state='normal')
            self.process_text.insert(tk.END, steps[index] + "\n")
            self.process_text.see(tk.END)
            self.process_text.config(state='disabled')
            
            delay = 50 # Standard delay
            try:
                self.step_animation_id = self.after(delay, self.animate_steps, steps, index + 1)
            except tk.TclError:
                # Window was closed during animation
                pass
        else:
            self.finish_computation()

    def stop_and_finish_computation(self):
        if self.step_animation_id:
            self.after_cancel(self.step_animation_id)
            self.step_animation_id = None
            
        self.process_text.config(state='normal')
        for i in range(self.current_step_index + 1, len(self.current_steps)):
            self.process_text.insert(tk.END, self.current_steps[i] + "\n")
        self.process_text.see(tk.END)
        self.process_text.config(state='disabled')
        self.finish_computation()

    def finish_computation(self):
        if hasattr(self, 'compute_button'): # Check if button exists yet
            self.compute_button.config(text="Compute", command=self.start_computation)
        if self.step_animation_id:
            try:
                self.after_cancel(self.step_animation_id)
            except tk.TclError:
                pass # Window already closed
            self.step_animation_id = None
        self.current_steps = []
        self.current_step_index = 0


# --- NEW: Main execution block (for testing) ---
# This part only runs when you execute THIS file directly
# to test the animated welcome screen.
# Your friend's code (which imports this file) will NOT run this.
if __name__ == "__main__":
    
    # 1. Create a root window
    root = tk.Tk()
    
    # 2. Hide the root window so only the tool is visible
    root.withdraw()

    # 3. Apply the styles to this root window
    setup_styles(root)

    # 4. Create the tool window (it's now the "main" window)
    app = RecursionTool(root)

    # 5. Run the main loop
    root.mainloop()