# we learn Retrive data from Database
# ===================================

# . fetchone => returns a single record or none if no more rows are available.
# . fetchall => fetches all the rows of query result (return all rows).

import sqlite3

db = sqlite3.connect("2-sqlite3.db")

cr = db.cursor()

cr.execute(
    "CREATE TABLE if not exists user (name txt, country txt ,age int ,user_id int  )"
)
cr.execute("CREATE TABLE if not exists skills (skill_name txt ,user_id int  )")


# cr.execute(
#     "insert into user(name ,country ,age ,user_id) values ('abdullah' ,'Eg' ,21 ,1 )"
# )
# cr.execute(
#     "insert into user(name ,country ,age ,user_id) values ('man_Z' ,'Eg' ,20 ,2 )"
# )
# cr.execute(
#     "insert into user(name ,country ,age ,user_id) values ('ninja' ,'Eg' ,24 ,3 )"
# )
# cr.execute(
#     "insert into user(name ,country ,age ,user_id) values ('ahmed' ,'Eg' ,31 ,4 )"
# )

# cr.execute("insert into skills (skill_name, user_id) values ('python', 1)")
# cr.execute("insert into skills (skill_name, user_id) values ('php', 2)")
# cr.execute("insert into skills (skill_name, user_id) values ('bash', 3)")
# cr.execute("insert into skills (skill_name, user_id) values ('rust', 4)")


# - fetch or data

cr.execute("select name from user")  # + now i select the colum name from user table.
# :note:
# -you can select many faildes.
# cr.execute("select name country from user")
# cr.execute("select * from user")  #- all


print(cr.fetchone())  # - return single record.
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())


db.commit()

db.close()
