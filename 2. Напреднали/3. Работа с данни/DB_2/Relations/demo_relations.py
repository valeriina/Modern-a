import sqlalchemy as db
import pandas as pd

engine = db.create_engine('sqlite:///employees.db') #Create people.db automatically
connection = engine.connect()
metadata = db.MetaData()

employees = db.Table('emp', metadata,
                     db.Column('Id', db.Integer()),
                     db.Column('name', db.String(255), nullable=False),
                     db.Column('salary', db.Float(), default=100.0),
                     db.Column('active', db.Boolean(), default=True)
                     )

metadata.create_all(engine) #Creates the table

#Inserting record one by one
query = db.insert(employees).values(Id=1, name='naveen', salary=60000.00, active=True)
ResultProxy = connection.execute(query)

#Inserting many records at ones
query = db.insert(employees)
values_list = [{'Id':'2', 'name':'ram', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'ramesh', 'salary':70000, 'active':True}]
ResultProxy = connection.execute(query,values_list)

results = connection.execute(db.select([employees])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
print(df.head(4))




