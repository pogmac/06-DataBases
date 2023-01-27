from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

# sqlalchemy_ex_02.py
from alchemy_ex_02 import students, engine

### INSERT BEGIN ###
#Insert is similar to CREATE (from CRUD)

ins = students.insert()
print(repr(ins)) # Shows us object details
print(str(ins)) # casting on string shows us SQL

print(ins.compile().params)

ins = students.insert().values(firstname ='Eric', lastname = 'Clapton')
print(ins.compile().params)

### INSERT END ###

### UPDATE BEGIN ###
#Update is same as UPDATE (from CRUD)

upd = students.update()
print(repr(upd))
print(str(upd))
print(upd.compile().params)

upd = students.update().values(id = 2, firstname ='Mark',)
print(upd.compile().params)

### INSERT END ###

## select() and delete() are missing ##



#########################################
#####       END OF THE PROGRAM      #####
#########################################


#(5,"czarna","mamba")