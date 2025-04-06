import tkinter as tk
from tkinter import ttk, messagebox
from scheduler import fcfs

process_list = []

def add_process():
    try:
        pid = entry_pid.get()
        arrival = int(entry_arrival.get())
        burst = int(entry_burst.get())

        process_list.append({'pid': pid, 'arrival': arrival, 'burst': burst})
        listbox.insert(tk.END, f"P{pid} - Arrival: {arrival}, Burst: {burst}")
        
        entry_pid.delete(0, tk.END)
        entry_arrival.delete(0, tk.END)
        entry_burst.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer values.")

def run_simulation():
    algorithm = algorithm_var.get()

    if algorithm == "FCFS":
        result = fcfs(process_list)
        output_text.delete('1.0', tk.END)
        
        total_wt = 0
        total_tat = 0
        for r in result:
            output_text.insert(tk.END, f"{r['pid']} -> CT: {r['completion']} | TAT: {r['turnaround']} | WT: {r['waiting']}\n")
            total_wt += r['waiting']
            total_tat += r['turnaround']
        
        avg_wt = total_wt / len(result)
        avg_tat = total_tat / len(result)
        output_text.insert(tk.END, f"\nAverage Waiting Time: {avg_wt:.2f}")
        output_text.insert(tk.END, f"\nAverage Turnaround Time: {avg_tat:.2f}")
    else:
        messagebox.showinfo("Coming Soon", f"{algorithm} not implemented yet.")

# GUI setup
root = tk.Tk()
root.title("CPU Scheduler Simulator")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Process ID").grid(row=0, column=0)
tk.Label(frame_input, text="Arrival Time").grid(row=0, column=1)
tk.Label(frame_input, text="Burst Time").grid(row=0, column=2)

entry_pid = tk.Entry(frame_input, width=5)
entry_pid.grid(row=1, column=0)
entry_arrival = tk.Entry(frame_input, width=5)
entry_arrival.grid(row=1, column=1)
entry_burst = tk.Entry(frame_input, width=5)
entry_burst.grid(row=1, column=2)

btn_add = tk.Button(frame_input, text="Add Process", command=add_process)
btn_add.grid(row=1, column=3, padx=10)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=5)

algorithm_var = tk.StringVar()
algorithm_dropdown = ttk.Combobox(root, textvariable=algorithm_var, values=["FCFS", "SJF", "Round Robin", "Priority"])
algorithm_dropdown.current(0)
algorithm_dropdown.pack(pady=5)

btn_run = tk.Button(root, text="Run Simulation", command=run_simulation)
btn_run.pack(pady=5)

output_text = tk.Text(root, height=10, width=60)
output_text.pack(pady=5)

root.mainloop()
