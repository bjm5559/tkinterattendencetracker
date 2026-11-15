import tkinter as tk
from ui.dashboard import Dashboard
from ui.students import StudentsView
from ui.attendance import AttendanceView
from ui.reports import ReportsView
from utils.data_manager import DataManager

class AttendanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Attendance Tracker")
        self.geometry("1150x720"); self.minsize(1000,650)
        self.configure(bg="#0f172a")
        self.data=DataManager(); self.current_view=None
        self.build_shell(); self.show_dashboard()

    def build_shell(self):
        h=tk.Frame(self,bg="#0f172a"); h.pack(fill="x",padx=25,pady=(20,10))
        tk.Label(h,text="Attendance Tracker",bg="#0f172a",fg="#f8fafc",font=("Segoe UI",24,"bold")).pack(anchor="w")
        tk.Label(h,text="Python • Tkinter • CSV | Biswa Jyoti Maity • Suyash Rusia • Amal Vinod",bg="#0f172a",fg="#94a3b8",font=("Segoe UI",10)).pack(anchor="w")
        body=tk.Frame(self,bg="#0f172a"); body.pack(fill="both",expand=True,padx=20,pady=10)
        self.sidebar=tk.Frame(body,bg="#111827",width=190); self.sidebar.pack(side="left",fill="y",padx=(0,12)); self.sidebar.pack_propagate(False)
        self.content=tk.Frame(body,bg="#111827"); self.content.pack(side="right",fill="both",expand=True)
        for text,cmd in [("Dashboard",self.show_dashboard),("Students",self.show_students),("Mark Attendance",self.show_attendance),("Reports",self.show_reports)]:
            tk.Button(self.sidebar,text=text,command=cmd,bg="#1e293b",fg="white",activebackground="#2563eb",relief="flat",anchor="w",font=("Segoe UI",10,"bold"),padx=16,pady=12).pack(fill="x",padx=12,pady=5)
        tk.Label(self.sidebar,text="Minimum Attendance\n75%",bg="#111827",fg="#60a5fa",font=("Segoe UI",10,"bold"),justify="left").pack(anchor="w",padx=18,pady=18)

    def clear(self):
        for w in self.content.winfo_children(): w.destroy()
    def show_dashboard(self):
        self.clear(); self.current_view=Dashboard(self.content,self.data); self.current_view.pack(fill="both",expand=True,padx=20,pady=20)
    def show_students(self):
        self.clear(); self.current_view=StudentsView(self.content,self.data,self.show_students); self.current_view.pack(fill="both",expand=True,padx=20,pady=20)
    def show_attendance(self):
        self.clear(); self.current_view=AttendanceView(self.content,self.data,self.show_attendance); self.current_view.pack(fill="both",expand=True,padx=20,pady=20)
    def show_reports(self):
        self.clear(); self.current_view=ReportsView(self.content,self.data); self.current_view.pack(fill="both",expand=True,padx=20,pady=20)

if __name__=="__main__": AttendanceApp().mainloop()
