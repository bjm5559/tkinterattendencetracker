import tkinter as tk
from tkinter import messagebox
class StudentsView(tk.Frame):
    def __init__(self,p,d,refresh): super().__init__(p,bg="#111827"); self.d=d; self.refresh=refresh; self.name=tk.StringVar(); self.reg=tk.StringVar(); self.course=tk.StringVar(value="B.Tech CSE"); self.build()
    def build(self):
        tk.Label(self,text="Student Management",bg="#111827",fg="white",font=("Segoe UI",20,"bold")).pack(anchor="w")
        form=tk.Frame(self,bg="#111827"); form.pack(fill="x",pady=18)
        for label,var,width in [("Name",self.name,22),("Registration No.",self.reg,20),("Course",self.course,18)]:
            b=tk.Frame(form,bg="#111827"); b.pack(side="left",padx=(0,12)); tk.Label(b,text=label,bg="#111827",fg="#cbd5e1").pack(anchor="w"); tk.Entry(b,textvariable=var,width=width,bg="#1e293b",fg="white",insertbackground="white",relief="flat").pack(pady=4,ipady=5)
        tk.Button(form,text="Add Student",command=self.add,bg="#2563eb",fg="white",relief="flat",padx=12,pady=7).pack(side="left",pady=17)
        tk.Button(form,text="Delete Selected",command=self.delete,bg="#dc2626",fg="white",relief="flat",padx=12,pady=7).pack(side="left",padx=5,pady=17)
        self.list=tk.Listbox(self,bg="#1e293b",fg="white",selectbackground="#2563eb",font=("Segoe UI",10),relief="flat"); self.list.pack(fill="both",expand=True); self.refresh_list()
    def refresh_list(self):
        self.list.delete(0,"end")
        for s in self.d.students: self.list.insert("end",f'{s["name"]} | {s["reg"]} | {s["course"]}')
    def add(self):
        n,r,c=self.name.get().strip(),self.reg.get().strip(),self.course.get().strip()
        if not n or not r: messagebox.showwarning("Missing Data","Enter name and registration number."); return
        if self.d.student_exists(r): messagebox.showerror("Duplicate","Registration number already exists."); return
        self.d.add_student(n,r,c); self.refresh(); messagebox.showinfo("Success","Student added successfully.")
    def delete(self):
        x=self.list.curselection()
        if not x: messagebox.showwarning("Select Student","Select a student first."); return
        r=self.list.get(x[0]).split("|")[1].strip()
        if messagebox.askyesno("Confirm",f"Delete {r}?"): self.d.delete_student(r); self.refresh()
