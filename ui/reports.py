import tkinter as tk
from tkinter import ttk
class ReportsView(tk.Frame):
    SUBJECTS=["All Subjects","Data Structures","Computer Organization","Operating Systems","Object Oriented Programming","Advance Programming"]
    def __init__(self,p,d): super().__init__(p,bg="#111827"); self.d=d; self.subject=tk.StringVar(value="All Subjects"); self.search=tk.StringVar(); self.build()
    def build(self):
        tk.Label(self,text="Attendance Reports",bg="#111827",fg="white",font=("Segoe UI",20,"bold")).pack(anchor="w")
        c=tk.Frame(self,bg="#111827"); c.pack(fill="x",pady=18)
        ttk.Combobox(c,textvariable=self.subject,values=self.SUBJECTS,state="readonly",width=25).pack(side="left"); self.search.trace_add("write",lambda *_:self.refresh())
        tk.Entry(c,textvariable=self.search,width=25,bg="#1e293b",fg="white",insertbackground="white",relief="flat").pack(side="left",padx=15,ipady=5)
        self.tree=ttk.Treeview(self,columns=("name","reg","classes","present","absent","percent","status"),show="headings")
        for col,title,w in [("name","Name",200),("reg","Registration",160),("classes","Classes",80),("present","Present",80),("absent","Absent",80),("percent","Attendance %",110),("status","Status",90)]: self.tree.heading(col,text=title); self.tree.column(col,width=w,anchor="center")
        self.tree.pack(fill="both",expand=True); self.subject.trace_add("write",lambda *_:self.refresh()); self.refresh()
    def refresh(self):
        for x in self.tree.get_children(): self.tree.delete(x)
        q=self.search.get().lower()
        for s in self.d.students:
            if q and q not in s["name"].lower() and q not in s["reg"].lower(): continue
            total,present,absent,pct,status=self.d.calculate(s["reg"],self.subject.get())
            self.tree.insert("","end",values=(s["name"],s["reg"],total,present,absent,f"{pct:.1f}%",status))
