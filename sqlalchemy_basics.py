# sqlalchemy basics
from sqlalchemy import create_engine
from blogger.conf.settings import DATABASE_LOCATION

# to understand the basics of sqlalchemy

# First to create the engine to connect to a database
engine = create_engine("sqlite:///{}".format(DATABASE_LOCATION), pool_recycle=3600, echo=True)
print("The engine is : {} ".format(engine))
connection = engine.connect()
print("The connection to the database is : {}".format(connection))

#  Metadata : To tie together information about the table objects and the engine and connection information together.
#  Metadata needs to be imported and initialized before objects can be tied to it.
from sqlalchemy import MetaData
metadata = MetaData()
print("The metadata object initialized is : {} ".format(metadata))


#  Table creation with columns
from sqlalchemy import Table, Column
from sqlalchemy import (String, DateTime, Integer, Boolean, ForeignKey)
import datetime


# users table definition
user_id = Column("user_id", Integer(), primary_key=True)
username = Column("username", String(30), unique=True,nullable=False, index=True)
password = Column("password", String(255), nullable=False)
email_address = Column("email_address", String(255), nullable=False)
phone = Column("phone", String(20), nullable=False)
user_created_time = Column("created_time", DateTime(), default=datetime.datetime.now)
user_modified_time = Column("modified_time", DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)
user_status = Column("status", Boolean(), default=False)
users = Table("users", metadata, user_id, username, password, email_address, phone,
                     user_created_time, user_modified_time, user_status)
print("Users table defined is : {} ".format(users))

#  articles table definition
article_id = Column("article_id", Integer(), primary_key=True)
article_author = Column("author", ForeignKey("users.user_id"))
article_info = Column("author", String(50), index=True)
article_created_time = Column("created_time", DateTime(), default=datetime.datetime.now)
article_modified_time = Column("modified_time", DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)
articles = Table("articles", metadata, article_id, article_author, article_info, article_created_time, article_modified_time)
print("articles table defined is : {} ".format(articles))

#  sessions table definition
_id = Column("id", Integer(), autoincrement=True, primary_key=True)
session_id = Column("session_id", String(60), index=True)
session_user_id = Column("user_id", ForeignKey("users.user_id"))
session_modified_time = Column("modified_time", DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)
sessions = Table("sessions",metadata, _id, session_id, session_user_id, session_modified_time)
print("sessions table defined is : {} ".format(articles))

resp = metadata.create_all(bind=engine)
print("Creation of table response is : {} ".format(resp))
"""
2020-11-22 20:41:22,122 INFO sqlalchemy.engine.base.Engine ()
2020-11-22 20:41:22,122 INFO sqlalchemy.engine.base.Engine PRAGMA main.table_info("sessions")
2020-11-22 20:41:22,122 INFO sqlalchemy.engine.base.Engine ()
2020-11-22 20:41:22,122 INFO sqlalchemy.engine.base.Engine PRAGMA temp.table_info("sessions")
2020-11-22 20:41:22,122 INFO sqlalchemy.engine.base.Engine ()
2020-11-22 20:41:22,123 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE users (
        user_id INTEGER NOT NULL, 
        username VARCHAR(30) NOT NULL, 
        password VARCHAR(255) NOT NULL, 
        email_address VARCHAR(255) NOT NULL, 
        phone VARCHAR(20) NOT NULL, 
        created_time DATETIME, 
        modified_time DATETIME, 
        status BOOLEAN, 
        PRIMARY KEY (user_id), 
        CHECK (status IN (0, 1))
)
2020-11-22 20:41:22,123 INFO sqlalchemy.engine.base.Engine ()
2020-11-22 20:41:22,152 INFO sqlalchemy.engine.base.Engine COMMIT
2020-11-22 20:41:22,152 INFO sqlalchemy.engine.base.Engine CREATE UNIQUE INDEX ix_users_username ON users (username)
2020-11-22 20:41:22,153 INFO sqlalchemy.engine.base.Engine ()
2020-11-22 20:41:22,177 INFO sqlalchemy.engine.base.Engine COMMIT
2020-11-22 20:41:22,178 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE articles (
        article_id INTEGER NOT NULL, 
        author VARCHAR(50), 
        created_time DATETIME, 
        modified_time DATETIME, 
        PRIMARY KEY (article_id)
)
2020-11-22 20:41:22,178 INFO sqlalchemy.engine.base.Engine ()
2020-11-22 20:41:22,194 INFO sqlalchemy.engine.base.Engine COMMIT
2020-11-22 20:41:22,194 INFO sqlalchemy.engine.base.Engine CREATE INDEX ix_articles_author ON articles (author)
2020-11-22 20:41:22,195 INFO sqlalchemy.engine.base.Engine ()
2020-11-22 20:41:22,210 INFO sqlalchemy.engine.base.Engine COMMIT
2020-11-22 20:41:22,211 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE sessions (
        id INTEGER NOT NULL, 
        session_id VARCHAR(60), 
        user_id INTEGER, 
        modified_time DATETIME, 
        PRIMARY KEY (id), 
        FOREIGN KEY(user_id) REFERENCES users (user_id)
)
2020-11-22 20:41:22,211 INFO sqlalchemy.engine.base.Engine ()
2020-11-22 20:41:22,225 INFO sqlalchemy.engine.base.Engine COMMIT
2020-11-22 20:41:22,225 INFO sqlalchemy.engine.base.Engine CREATE INDEX ix_sessions_session_id ON sessions (session_id)
2020-11-22 20:41:22,225 INFO sqlalchemy.engine.base.Engine ()
2020-11-22 20:41:22,239 INFO sqlalchemy.engine.base.Engine COMMIT
Creation of table response is : None
"""
from sqlalchemy import insert
def insert_func():
    #  Creation and inserting data into the tables
    new_user = users.insert().values(username="token", password="token", email_address="token@gmail.com", phone="0909090909009")
    print("User Information prepared is : {} ".format(new_user))
    new_user.compile()
    print("User Information compiled is : {} ".format(new_user.compile().params))
    #  to insert we can execute the command
    res = connection.execute(new_user)
    print("Primary key is {} ".format(res.inserted_primary_key))
    # inserting multiple values
    insert_statement = insert(users)
    user_list = [
        dict(username="stan", password="stan", email_address="stan@gmail.com", phone="0909090909009"),
        dict(username="eric", password="eric", email_address="eric@gmail.com", phone="0909090909009"),
        dict(username="kenny", password="kenny", email_address="kenny@gmail.com", phone="0909090909009"),
        dict(username="randy", password="randy", email_address="randy@gmail.com", phone="0909090909009"),
        dict(username="butters", password="butters", email_address="butters@gmail.com", phone="0909090909009"),

    ]
    res = connection.execute(insert_statement, user_list)
    print("Insertion result of multiple users is : {} ".format(res))
    return

#  insert_func()

#  query_func
from sqlalchemy import select, desc

def query_func():
    select_query = select([users])
    result_proxy = connection.execute(select_query)
    results = result_proxy.fetchall()
    print("Results of the query is : {} ".format(results))
    # parsing the result object
    user_info = results[0]
    print("Accessing by index ::: User id is : {} ".format(user_info[0]))
    print("Accessing by name :::User email is : {} ".format(user_info.email_address))
    print("Accessing by column name or column object ::: User name is : {} ".format(user_info["username"]))

    #  accessing the results via the rowcount
    select_query = select([users])
    result_proxy = connection.execute(select_query)
    # print("Total number of users are : {} ".format(result_proxy.rowcount))
    print("Keys available in the result proxy is : {} ".format(result_proxy.keys()))
    for user in result_proxy:
        print("User being iterated over is : {} ".format(user.username))

    #  selecting only specific columns
    select_query = select([users.c.username])
    result_proxy = connection.execute(select_query)
    # print("Total number of users are : {} ".format(result_proxy.rowcount))
    print("Keys available in the result proxy is : {} ".format(result_proxy.keys()))
    for user in result_proxy:
        print("User being iterated over is : {} ".format(user.username))

    #  order by the username
    select_query = select([users.c.username]).order_by(users.c.username)
    result_proxy = connection.execute(select_query)
    # print("Total number of users are : {} ".format(result_proxy.rowcount))
    print("Keys available in the result proxy is : {} ".format(result_proxy.keys()))
    for user in result_proxy:
        print("User being iterated over is : {} ".format(user.username))

    #  order by the username descending
    select_query = select([users.c.username]).order_by(desc(users.c.username))
    result_proxy = connection.execute(select_query)
    # print("Total number of users are : {} ".format(result_proxy.rowcount))
    print("Keys available in the result proxy is : {} ".format(result_proxy.keys()))
    for user in result_proxy:
        print("User being iterated over is : {} ".format(user.username))

    #  limiting the number of records
    select_query = select([users.c.username]).order_by(users.c.username).limit(3)
    result_proxy = connection.execute(select_query)
    # print("Total number of users are : {} ".format(result_proxy.rowcount))
    print("Keys available in the result proxy is : {} ".format(result_proxy.keys()))
    for user in result_proxy:
        print("User being iterated over is : {} ".format(user.username))

    pass

# query_func()

from sqlalchemy.sql import func
def advanced_query():
    #  to perform the count query
    s = select([func.count(users.c.username)])
    result_proxy = connection.execute(s)
    record = result_proxy.first() # note that after the first call, the connection is closed.
    print("The keys in the record are :: {} ".format(record.keys()))
    print("The total number of items are : {} ".format(record["count_1"]))
    # the count_1 tells us that the count was done on the column 1

    #  to perform the count query nad give it a label
    s = select([func.count(users.c.username).label("user_count")])
    result_proxy = connection.execute(s)
    record = result_proxy.first()  # note that after the first call, the connection is closed.
    print("The keys in the record are :: {} ".format(record.keys()))
    print("The total number of items are : {} ".format(record["user_count"]))


    # filter the query
    s = select([users.c.username]).where(users.c.username == 'token')
    result_proxy = connection.execute(s)
    record = result_proxy.first()  # note that after the first call, the connection is closed.
    print("The keys in the record are :: {} ".format(record.keys()))
    # print("The keys in the record are :: {} ".format(record.items()))
    # for user in record.items():
    #     print("user matching the filter is :: {}".format(user.username))
    print("The total number of items are : {} ".format(record["username"]))

    s = select([users.c.username]).where(users.c.username.like('%an%'))
    result_proxy = connection.execute(s)
    # record = result_proxy.first()  # note that after the first call, the connection is closed.
    # print("The keys in the record are :: {} ".format(record.keys()))
    # print("The keys in the record are :: {} ".format(record.items()))
    for user in result_proxy:
         print("user matching the filter is :: {}".format(user.username))
    return

advanced_query()
