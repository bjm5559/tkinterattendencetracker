import tkinter as tk
class Dashboard(tk.Frame):
    def __init__(self,p,d): super().__init__(p,bg="#111827"); self.d=d; self.build()
    def build(self):
        tk.Label(self,text="Dashboard",bg="#111827",fg="white",font=("Segoe UI",20,"bold")).pack(anchor="w")
        cards=tk.Frame(self,bg="#111827"); cards.pack(fill="x",pady=25)
        for title,val in [("Total Students",len(self.d.students)),("Attendance Records",len(self.d.attendance)),("Low Attendance",self.d.low_count())]:
            f=tk.Frame(cards,bg="#1e293b"); f.pack(side="left",fill="both",expand=True,padx=7)
            tk.Label(f,text=title,bg="#1e293b",fg="#94a3b8",font=("Segoe UI",10)).pack(anchor="w",padx=16,pady=(18,4))
            tk.Label(f,text=str(val),bg="#1e293b",fg="white",font=("Segoe UI",25,"bold")).pack(anchor="w",padx=16,pady=(0,18))
        tk.Label(self,text="Python Tkinter desktop Attendance Management System. Attendance below 75% is marked LOW.",bg="#111827",fg="#cbd5e1",font=("Segoe UI",10)).pack(anchor="w")
