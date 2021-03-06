import sqlite3
from pandas import DataFrame

conn = sqlite3.connect('./data.db',check_same_thread=False)

class DataBase():

    cursor = conn.cursor()
    
    def __init__(self):
        self.createTable()
        
    def createTable(self):
        '''
        Creates A Table If it Doesnt Exist
        '''
        conn.execute("""CREATE TABLE IF NOT EXISTS MeetingData (Name text,ID text,Password text, DateTime text,Audio text,Video Text)""")
    
    def enterData(self,meetingData):
        '''
        Enters Data From The UI Table To The DataBase
        '''
        meetingData.to_sql('MeetingData', con = conn, if_exists='replace', index = False)
    
    def readData(self):
        '''
        Reads Data From The SQL DataBase
        '''
        self.cursor.execute('''SELECT * FROM MeetingData''')
        retVal = DataFrame(self.cursor.fetchall(),columns=['Name','ID','Password','DateTime','Audio','Video'])
        return retVal                