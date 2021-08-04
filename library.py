import sqlite3
import datetime

database_connection = sqlite3.connect("librarydatabase.db")
curs = database_connection.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS library(
    book_id INTEGER NOT NULL PRIMARY KEY,
    book_name TEXT,
    edition_year INTEGER,
    author TEXT,
    owner_name TEXT,
    category TEXT,
    translator TEXT,
    date_time TEXT
    );""")

curs.execute("""CREATE TABLE IF NOT EXISTS log_info(
    book_id_log INTEGER NOT NULL PRIMARY KEY,
    date_time TEXT,
    process TEXT,
    lib_id INTEGER,
    FOREIGN KEY(lib_id) REFERENCES library(book_id)
);""")

database_connection.commit()
database_connection.close()

now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")
def updateRecordLibLog():
    try:
        database_connection = sqlite3.connect("librarydatabase.db")
        curs = database_connection.cursor()

        idNum = int(input("Please enter a book id for update: "))
        entry = int(input("Please enter a number 1-7 for record to change,\n1: for book name changes,\n2: for edition year changes,\n3: for author changes,\n\
4: for owner name changes,\n5: for category changes,\n6: for translator name changes,\n7: for all data changes for one book: "))

        if entry==1:
            name = input ("Please enter a new book name: ")
            result = curs.execute("SELECT book_name, owner_name FROM library WHERE book_id='{}'".format(idNum)).fetchall()
            owner = result[0][1]
            old_book_name = result[0][0]
            update_data = ("""UPDATE library SET book_name='{}'
                            WHERE book_id='{}' """.format(name,idNum))
            curs.execute(update_data)
            update = 'Updated, owner name is {}, book name {}, new book name {}'.format(owner,old_book_name,name)
            curs.execute("INSERT INTO log_info (lib_id,date_time,process) VALUES('{}','{}','{}')".format(idNum,time,update))

        elif entry==2:
            year = input ("Please enter new edition year: ")
            result = curs.execute("SELECT book_name, owner_name FROM library WHERE book_id='{}'".format(idNum)).fetchall()
            owner = result[0][1]
            old_book_name = result[0][0]
            update_data = ("""UPDATE library SET edition_year='{}'
                            WHERE book_id='{}'""".format(year,idNum))
            curs.execute(update_data)
            update = 'Updated,owner name is {}, book name {}, new edition year {}'.format(owner,old_book_name,year)
            curs.execute("INSERT INTO log_info (lib_id,date_time,process) VALUES('{}','{}','{}')".format(idNum,time,update))

        elif entry==3:
            aut = input ("Please enter new author: ")
            result = curs.execute("SELECT book_name, owner_name FROM library WHERE book_id='{}'".format(idNum)).fetchall()
            owner = result[0][1]
            old_book_name = result[0][0]
            update_data = ("""UPDATE library SET author='{}'
                            WHERE book_id='{}'""".format(aut,idNum))
            curs.execute(update_data)
            update = 'Updated, owner name is {}, book name {}, new author {}'.format(owner,old_book_name,aut)
            curs.execute("INSERT INTO log_info (lib_id,date_time,process) VALUES('{}','{}','{}')".format(idNum,time,update))

        elif entry==4:
            new_owner = input ("Please enter new owner name: ")
            result = curs.execute("SELECT book_name, owner_name FROM library WHERE book_id='{}'".format(idNum)).fetchall()
            owner = result[0][1]
            old_book_name = result[0][0]
            update_data = ("""UPDATE library SET owner_name='{}'
                            WHERE book_id='{}'""".format(new_owner,idNum))
            curs.execute(update_data)
            update = 'Updated, owner name is {}, book name is {}, new owner name {}'.format(owner,old_book_name,new_owner)
            curs.execute("INSERT INTO log_info (lib_id,date_time,process) VALUES('{}','{}','{}')".format(idNum,time,update))

        elif entry==5:
            cat = input ("Please enter new category name: ")
            result = curs.execute("SELECT book_name, owner_name FROM library WHERE book_id='{}'".format(idNum)).fetchall()
            owner = result[0][1]
            old_book_name = result[0][0]
            update_data = ("""UPDATE library SET category='{}'
                            WHERE book_id='{}' """.format(cat,idNum))
            curs.execute(update_data)
            update = 'Updated, owner name is {}, book name is {}, new category name {}'.format(owner,old_book_name,cat)
            curs.execute("INSERT INTO log_info (lib_id,date_time,process) VALUES('{}','{}','{}')".format(idNum,time,update))

        elif entry==6:
            translatorName = input ("Please enter new translator name: ")
            result = curs.execute("SELECT book_name, owner_name FROM library WHERE book_id='{}'".format(idNum)).fetchall()
            owner = result[0][1]
            old_book_name = result[0][0]
            update_data = ("""UPDATE library SET translator='{}'
                            WHERE book_id='{}'""".format(translatorName,idNum))
            curs.execute(update_data)
            update = 'Updated, owner name is {}, book name is {}, new translator name {}'.format(owner,old_book_name,translatorName)
            curs.execute("INSERT INTO log_info (lib_id,date_time,process) VALUES('{}','{}','{}')".format(idNum,time,update))

        elif entry==7:
            bookN = input("Please enter a book name: ")
            edition = input("Please enter an edition: ")
            author = input("Please enter author name: ")
            owner = input("Please enter owner name: ")
            category = input("Please enter a category: ")
            translator = input("Please enter a translator name: ")
            date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            update_data = ("""UPDATE library SET book_name=?, edition_year=?,author=?,owner_name=?,category=?,translator=?,date_time=?
                            WHERE book_id='{}' """.format(idNum))
            data_list = [bookN,edition,author,owner,category,translator,date_time]
            curs.execute(update_data,data_list)
            update = "Updated one book"
            curs.execute("INSERT INTO log_info (lib_id,date_time,process) VALUES('{}','{}','{}')".format(idNum,time,update))

    except Exception as e:
        print("Failed to update row of sqlite table", e)
    finally:
        database_connection.commit()
        database_connection.close()

def deleteRecordLib():
    try:
        database_connection = sqlite3.connect("librarydatabase.db")
        curs = database_connection.cursor()
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S")

        delete = input("Would you like to delete all records or one record? all/one: ")

        if delete == 'all' or delete=='ALL':
            curs.execute("DROP TABLE library")
            deleted = "library table is deleted"
            curs.execute("INSERT INTO log_info (date_time,process) VALUES ('{}','{}')".format(time,deleted))

        elif delete == 'one' or delete=='ONE':
            idNum = int(input("Please enter a book id for delete: "))
            result = curs.execute("SELECT book_name, owner_name FROM library WHERE book_id='{}'".format(idNum)).fetchall()
            curs.execute("DELETE FROM library WHERE book_id='{}';".format(idNum))
            owner = result[0][1]
            old_book_name = result[0][0]
            deletion = "Deleted {}.book, owner name is {} book name is {}".format(idNum,owner,old_book_name)
            curs.execute("INSERT INTO log_info (lib_id,date_time,process) VALUES('{}','{}','{}')".format(idNum,time,deletion))
            database_connection.commit()
        else:
            print("Please JUST write 'one' or 'all'")         
    except Exception as e:
        print("Failed to delete record from a table", e)
    finally:
        if database_connection:
            database_connection.close()


def insertRecordLib(book_name,edition_year,author,owner_name,category,translator,date_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
    try:
        database_connection = sqlite3.connect("librarydatabase.db")
        curs = database_connection.cursor()

        insert_data = ("""INSERT INTO library(book_name,edition_year,author,owner_name,category,translator,date_time)
                        VALUES(?,?,?,?,?,?,?)""")

        data_list = [book_name,edition_year,author,owner_name,category,translator,date_time]
        curs.execute(insert_data,data_list)

        database_connection.commit()  

    except Exception as e:
        print("Failed to insert Python variable into sqlite table", e)
    finally:
        if database_connection:
            database_connection.close()

def show_all():
    database_connection = sqlite3.connect("librarydatabase.db")
    curs = database_connection.cursor()
    print ("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format('Book Id','Book Name','Edition Year','Author','Owner Name','Category','Translator'))
    curs.execute("SELECT * FROM library")
    results = curs.fetchall()
    for item in results:
        print ("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(item[0],item[1],item[2],item[3],item[4],item[5],item[6]))
    database_connection.close()

# insertRecordLib("Alamut Kalesi",1938,"Vladimir Bartol","Aybuke","History","Ayşe")
# insertRecordLib("Ayni Yildizin Altinda",2012,"John Green","Ahmet","Romantic","Ece")
# insertRecordLib("Twillight",2005,"Stephenie Meyer","Göknur","Romantic","Ece")

# deleteRecordLib()
# updateRecordLibLog()
# show_all()
