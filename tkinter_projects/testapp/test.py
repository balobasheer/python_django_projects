import time, sys
import random, shutil
import tkinter as tk

from csv import DictReader, DictWriter
from tempfile import NamedTemporaryFile


class TestApp(tk.Tk):

    def __init__(self):
        super(TestApp, self).__init__()
        self.header = ['Question', 'Option_1', 'Option_2', 'Option_3', 'Option_4', 'Answer']
        self.response = 'Transaction in progress...'
        self.wait = time.sleep(2)
        self.data = self.read_record_from_db()
        # self.frame = tk.Frame(self, relief='flat', borderwidth=5, background='white',
        #         width=10, height=10)
        # self.frame.pack(side='bottom', padx=5, pady=5)
        self.title('CrestHive | TestIT')
        tk.Label(self, text='Welcome To CrestHive 2022/2023 ' + 'Entrance Examination', 
        font='Arial 29', foreground='black', background='green', height=10
        ).pack(fill='both')

        for i, question in enumerate(self.data):
            for key,value in question.items():
                if not key == 'Question' :
                    continue
                # tk.Label(frame, text=x).pack()
                if not key == 'Question' :
                    tk.Label(self, text=value, font='Arial 12', foreground='black').pack()
                else:
                    tk.Label(self, text=f'{i+1}. '+ value, font='Arial 12', foreground='black').pack()

                self.Label(root, text='foreground=red', foreground='red').pack()

    def read_record_from_db(self):
        with open('testapp/users.csv') as file:
            csv_reader = DictReader(file)
            data = list(csv_reader)
            return data
    
    def user_registration(self):
            user_data = {}
            user_data['Question'] = input('Enter your question: ')
            user_data['Option_1'] = input('Enter option 1: ')
            user_data['Option_2'] = input('Enter option 2: ')
            user_data['Option_3'] = input('Enter option 3: ')
            user_data['Option_4'] = input('Enter option 4: ')
            user_data['Answer']   = input('Enter currect option A,B,C or D ?: ')
            self.response
            self.wait
            empty_string = 'Application submitted successfully'
            print(empty_string)
            return self.record_db_form(user_data)

    def record_db_form(self, application):
        with open('testapp/users.csv', 'a') as file:
                csv_writer = DictWriter(
                    file,
                    fieldnames=self.header,
                    lineterminator='\n'
                    )
                # csv_writer.writeheader()
                csv_writer.writerow(application)
                # return self.dashboard()

    def wallet_funder(self, amount):
            data = self.get_credential()
            print(data)
            print(amount)
            with NamedTemporaryFile(mode='w', delete=False) as temp_file:
                second = DictWriter(
                        temp_file,
                        fieldnames=self.header,
                        lineterminator='\n'
                        )
                second.writeheader()

                if data['First Name'] == 'Basheer':
                    data['Balance'] = amount
                second.writerow(data)
            shutil.move(temp_file.name, 'files/users.csv')
            self.response
            self.wait
            print('Data saved successfully')
            return self.dashboard()


if __name__ == '__main__':
    test = TestApp()
    test.mainloop()
