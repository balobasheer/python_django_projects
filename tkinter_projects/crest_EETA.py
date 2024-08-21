import tkinter as tk
import tkinter.messagebox as msgbox

import sqlite3

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome To EETA")
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        print(self.creat_db())
        print(self.save_data_to_db())
        print(self.retrieve_data())
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(fill=tk.BOTH, expand=1, padx=100, pady=244)

        self.password_entry = tk.Entry(self)
        self.password_entry.pack(fill=tk.BOTH, expand=1, padx=244, pady=22)

    def creat_db(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS STAFF")
        sql ='''CREATE TABLE STAFF( 
                FIRST_NAME  CHAR(20) NOT NULL, 
                LAST_NAME  CHAR(20), 
                AGE INT,
                SEX CHAR(1), 
                INCOME FLOAT)''' 
        cursor.execute(sql) 
        print("Table created successfully........")
        conn.commit()
        conn.close()
        # return cursor

    def save_data_to_db(self, *args, **kwargs):
        # data = kwargs
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        # cursor = self.creat_db()
        cursor.execute('''INSERT INTO STAFF(FIRST_NAME, LAST_NAME, AGE, SEX,  
        INCOME) VALUES ('Ramya', 'Rama Priya', 27, 'F', 9000)''') 
 
        cursor.execute('''INSERT INTO STAFF(FIRST_NAME, LAST_NAME, AGE, SEX,  
        INCOME) VALUES ('Vinay', 'Battacharya', 20, 'M', 6000)''') 
   
        cursor.execute('''INSERT INTO STAFF(FIRST_NAME, LAST_NAME, AGE, SEX,  
        INCOME) VALUES ('Sharukh', 'Sheik', 25, 'M', 8300)''') 
   
        cursor.execute('''INSERT INTO STAFF(FIRST_NAME, LAST_NAME, AGE, SEX,  
        INCOME) VALUES ('Sarmista', 'Sharma', 26, 'F', 10000)''') 
 
        cursor.execute('''INSERT INTO STAFF(FIRST_NAME, LAST_NAME, AGE, SEX,  
        INCOME) VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)''') 
   
        # Commit your changes in the database 
        conn.commit() 
 
        print("Records inserted........") 
 
        # Closing the connection 
        conn.close()

    def retrieve_data(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor() 
 
        #Retrieving data 
        cursor.execute('''SELECT * from STAFF''') 
        
        #Fetching 1st row from the table 
        result = cursor.fetchone(); 
        print(result) 
        
        #Fetching 1st row from the table 
        result = cursor.fetchall(); 
        print(result) 
        
        #Commit your changes in the database 
        conn.commit() 
        
        #Closing the connection 
        conn.close()

    def update_db(self):
        sql = '''UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX = 'M' ''' 
        cursor.execute(sql)

    def delete_db(self):
        cursor.execute('''DELETE FROM EMPLOYEE WHERE AGE > 25''')

if __name__ == "__main__":
    window = Window()
    window.mainloop()