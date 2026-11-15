import csv
from pathlib import Path
from datetime import datetime
BASE=Path(__file__).resolve().parent.parent
STUDENTS=BASE/"students.csv"; ATTENDANCE=BASE/"attendance.csv"; MIN_PERCENT=75.0

class DataManager:
    def __init__(self): self.load()
    def load(self):
        self.students=self.read(STUDENTS); self.attendance=self.read(ATTENDANCE)
    @staticmethod
    def read(path):
        if not path.exists(): return []
        with open(path,newline="",encoding="utf-8") as f: return list(csv.DictReader(f))
    @staticmethod
    def write(path,fields,rows):
        with open(path,"w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
    def save(self):
        self.write(STUDENTS,["name","reg","course"],self.students)
        self.write(ATTENDANCE,["date","subject","reg","status"],self.attendance)
    def student_exists(self,reg): return any(s["reg"].lower()==reg.lower() for s in self.students)
    def add_student(self,name,reg,course):
        self.students.append({"name":name,"reg":reg,"course":course}); self.save()
    def delete_student(self,reg):
        self.students=[s for s in self.students if s["reg"]!=reg]
        self.attendance=[a for a in self.attendance if a["reg"]!=reg]; self.save()
    def save_attendance(self,date,subject,statuses):
        self.attendance=[a for a in self.attendance if not(a["date"]==date and a["subject"]==subject)]
        for s in self.students:
            self.attendance.append({"date":date,"subject":subject,"reg":s["reg"],"status":statuses.get(s["reg"],"Present")})
        self.save()
    def calculate(self,reg,subject="All Subjects"):
        r=[a for a in self.attendance if a["reg"]==reg and (subject=="All Subjects" or a["subject"]==subject)]
        total=len(r); present=sum(a["status"]=="Present" for a in r); pct=present/total*100 if total else 0
        return total,present,total-present,pct,("N/A" if not total else "LOW" if pct<MIN_PERCENT else "OK")
    def low_count(self): return sum(self.calculate(s["reg"])[4]=="LOW" for s in self.students)
    @staticmethod
    def valid_date(v):
        try: datetime.strptime(v,"%Y-%m-%d"); return True
        except ValueError: return False
