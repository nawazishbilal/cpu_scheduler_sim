# 🧠 Intelligent CPU Scheduler Simulator

An interactive desktop application built using Python and Tkinter to simulate various CPU scheduling algorithms. It provides **animated Gantt chart visualizations**, process metrics (Completion Time, Turnaround Time, Waiting Time), and a sleek user interface for learning and demonstration purposes.

## 🚀 Features

- Supports multiple scheduling algorithms:
  - First-Come-First-Serve (FCFS)
  - Shortest Job First (SJF) - Non-Preemptive
  - Priority Scheduling - Non-Preemptive
  - Round Robin (with custom time quantum)
  - Shortest Remaining Time First (SRTF)
  - Preemptive Priority Scheduling
- Animated Gantt chart timeline (optional toggle)
- Real-time visualization of process execution
- Displays average waiting and turnaround time
- Easy-to-use GUI with input validation

## 🧩 Modules

- `main.py`: GUI, event handling, simulation logic, Gantt chart rendering
- `scheduler.py`: Contains all CPU scheduling algorithms
- `README.md`: Project overview and usage

## 🛠️ Technologies Used

- **Programming Language:** Python 3.10+
- **Libraries:**
  - `Tkinter` – GUI development
  - `Matplotlib` – Gantt chart visualization
  - `random` – Unique color generation for processes
- **Other Tools:**
  - Git & GitHub – Version control and collaboration

## 📈 Flow Diagram

```
User Input
   ↓
Select Scheduling Algorithm
   ↓
Run Simulation
   ↓
→ Algorithm Execution
→ Timeline & Metrics Calculation
   ↓
Gantt Chart + Output Display
```

## 📚 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/intelligent-cpu-scheduler
   ```
2. Install required dependencies:
   ```bash
   pip install matplotlib
   ```
3. Run the app:
   ```bash
   python main.py
   ```

## ✅ Future Scope

- Add support for Multilevel and Multilevel Feedback Queue Scheduling
- Export reports in CSV/PDF format
- Add memory and I/O simulation
- Enhance UI with themes and dark mode
- Package as a standalone desktop executable
