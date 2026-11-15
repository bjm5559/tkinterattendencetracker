import tkinter as tk
from tkinter import ttk,messagebox
from datetime import datetime
class AttendanceView(tk.Frame):
    SUBJECTS=["Data Structures","Computer Organization","Operating Systems","Object Oriented Programming","Advance Programming"]
    def __init__(self,p,d,refresh): super().__init__(p,bg="#111827"); self.d=d; self.refresh=refresh; self.date=tk.StringVar(value=datetime.now().strftime("%Y-%m-%d")); self.subject=tk.StringVar(value=self.SUBJECTS[0]); self.status={}; self.build()
    def build(self):
        tk.Label(self,text="Mark Attendance",bg="#111827",fg="white",font=("Segoe UI",20,"bold")).pack(anchor="w")
        c=tk.Frame(self,bg="#111827"); c.pack(fill="x",pady=18)
        tk.Label(c,text="Date",bg="#111827",fg="#cbd5e1").pack(side="left"); tk.Entry(c,textvariable=self.date,width=14,bg="#1e293b",fg="white",insertbackground="white",relief="flat").pack(side="left",padx=7,ipady=5)
        ttk.Combobox(c,textvariable=self.subject,values=self.SUBJECTS,state="readonly",width=25).pack(side="left",padx=10)
        for txt,cmd,col in [("All Present",lambda:self.setall("Present"),"#16a34a"),("All Absent",lambda:self.setall("Absent"),"#dc2626"),("Save Attendance",self.save,"#2563eb")]:
            tk.Button(c,text=txt,command=cmd,bg=col,fg="white",relief="flat",padx=10,pady=7).pack(side="left",padx=3)
        self.list=tk.Listbox(self,bg="#1e293b",fg="white",selectbackground="#2563eb",font=("Segoe UI",10),relief="flat"); self.list.pack(fill="both",expand=True); self.list.bind("<Double-1>",self.toggle); self.refresh_list()
    def refresh_list(self):
        self.list.delete(0,"end"); self.status={s["reg"]:"Present" for s in self.d.students}
        for s in self.d.students: self.list.insert("end",f'{s["name"]} | {s["reg"]} | Present')
    def redraw(self):
        self.list.delete(0,"end")
        for s in self.d.students: self.list.insert("end",f'{s["name"]} | {s["reg"]} | {self.status[s["reg"]]}')
    def setall(self,v):
        for r in self.status:self.status[r]=v
        self.redraw()
    def toggle(self,e=None):
        x=self.list.curselection()
        if x:
            r=self.d.students[x[0]]["reg"]; self.status[r]="Absent" if self.status[r]=="Present" else "Present"; self.redraw()
    def save(self):
        if not self.d.valid_date(self.date.get().strip()): messagebox.showerror("Invalid Date","Use YYYY-MM-DD."); return
        self.d.save_attendance(self.date.get().strip(),self.subject.get(),self.status); self.refresh(); messagebox.showinfo("Saved","Attendance saved.")
