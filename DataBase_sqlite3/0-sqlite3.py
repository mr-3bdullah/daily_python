# wellcome in to database lessones.
# /===============================

import sqlite3

# /============
# . Connect => used for => creat database file if not exeist , then connect to it.
# . Excute  => used for => excute sql command like (create table, fetch, ....)
# . Close   => for close database connection.
# /============

# + create Database and connect
db = sqlite3.connect("app.db")

# + creat Tables and fields
db.execute(
    "CREATE TABLE if not exists Skills (name text, progress integer, user_ID int)"
)

# + close database
db.close()
