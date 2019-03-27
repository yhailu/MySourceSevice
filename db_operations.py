from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
meta = MetaData()

engine = create_engine('sqlite:///college.db', echo = True)



class db_operations:
    students = Table(
        'students', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('lastname', String),
    )
    con = engine.connect()

    def insert_student(self, firstname, lastname):
        ins  = self.students.insert()
        ins  = self.students.insertins = self.students.insert().values(name = firstname, lastname = lastname)


    def get_student(self, userid):
        gs = self.students.select().where(self.students.c.id == userid)
        result = engine.execute(gs)
        return result.fetchall()


db = db_operations()
db.get_student(1)
