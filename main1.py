import tkinter as tk
from tkinter import messagebox

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time

def fcfs_scheduling(processes):
    time = 0
    result = "Process Execution Order:\n"
    for process in processes:
        result += f"Process {process.pid} starts at time {time}\n"
        time += process.burst_time
        result += f"Process {process.pid} ends at time {time}\n"
    return result

def add_process():
    try:
        pid = int(entry_pid.get())
        burst_time = int(entry_burst.get())
        processes.append(Process(pid, burst_time))
        listbox.insert(tk.END, f"Process {pid} - Burst Time: {burst_time}")
        entry_pid.delete(0, tk.END)
        entry_burst.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def schedule_processes():
    if not processes:
        messagebox.showerror("Error", "No processes added")
        return
    result = fcfs_scheduling(processes)
    text_output.config(state=tk.NORMAL)
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, result)
    text_output.config(state=tk.DISABLED)

def clear_all():
    processes.clear()
    listbox.delete(0, tk.END)
    text_output.config(state=tk.NORMAL)
    text_output.delete(1.0, tk.END)
    text_output.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("CPU Scheduler (FCFS)")
root.geometry("400x400")

processes = []

# Input Fields
tk.Label(root, text="Process ID:").pack()
entry_pid = tk.Entry(root)
entry_pid.pack()

tk.Label(root, text="Burst Time:").pack()
entry_burst = tk.Entry(root)
entry_burst.pack()

# Buttons
tk.Button(root, text="Add Process", command=add_process).pack()
tk.Button(root, text="Schedule", command=schedule_processes).pack()
tk.Button(root, text="Clear", command=clear_all).pack()

# Process List
listbox = tk.Listbox(root)
listbox.pack()

# Output Area
text_output = tk.Text(root, height=10, state=tk.DISABLED)
text_output.pack()

root.mainloop()
