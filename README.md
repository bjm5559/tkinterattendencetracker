# Attendance Tracker — Python Tkinter

**Team:** Biswa Jyoti Maity, Suyash Rusia, Amal Vinod

A modular desktop Attendance Management System built with Python, Tkinter/ttk and CSV.

## Features
- Dashboard
- Student management
- Attendance marking by date and subject
- Present/Absent controls
- Attendance percentage
- Automatic LOW status below 75%
- Search and subject filtering
- CSV persistence
- Modular OOP architecture

## Structure
```text
main.py
students.csv
attendance.csv
ui/
  dashboard.py
  students.py
  attendance.py
  reports.py
utils/
  data_manager.py
```

## Run
```bash
python main.py
```
Windows alternative:
```bash
py main.py
```

No third-party packages are required.

## Formula
Attendance % = (Present Classes / Total Classes) × 100

## Future Scope
SQLite/MySQL database, login system, PDF/Excel export, analytics and notifications.
