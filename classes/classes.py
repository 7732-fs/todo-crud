import db.crud as db

class Task:
    categories=['Home', 'Car', 'Work', 'Dog']
    def __init__(self, tid:int=0, category:str="default", description:str="default", date="") -> None:
        self.tid=tid
        self.category=category
        self.description=description
        self.date=date

    def add(self):
        db.add(self)    

