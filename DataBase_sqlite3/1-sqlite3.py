# insert a data  into database.

import sqlite3

# /===============
# . cursor => all operation in sql Done by it not the connection itself.
# . commit => save all changes.


db = sqlite3.connect("1_sqbhbhblite3.db")  # - as we know creat db and connect it.

# - setting up the cursor.
cr = db.cursor()  #: now i have a variable inner it cursor to do my excution.

# - create Table and fields.
cr.execute("CREATE TABLE if not exists users (user_id int ,name text)")
cr.execute("CREATE TABLE if not exists skills (Name text , progress int , user_id int)")

# + inserting Data:
# cr.execute("insert into users(user_id ,name) values (1,'abdullah')")
# cr.execute("insert into users(user_id ,name) values (3,'zaki')")
# cr.execute("insert into users(user_id ,name) values (3,'ahmed')")

# cr.execute("insert into skills(Name , progress , user_id) values ('python', 90 , 1)")
# cr.execute("insert into skills(Name , progress , user_id) values ('js', 40 , 2)")
# cr.execute("insert into skills(Name , progress , user_id) values ('php', 69 , 3)")

name_l = ["abdullah", "ahmed", "saeed", "Ninja", "hero", "ali", "king"]

for key, user in enumerate(name_l):

    cr.execute(f"insert into users(user_id ,name) values ({key},'{user}')")


# commit => to save my changes.
db.commit()

# close db connection
db.close()
