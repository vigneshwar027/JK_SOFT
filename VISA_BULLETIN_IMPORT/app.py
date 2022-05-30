from concurrent.futures import process
from multiprocessing import connection
from openpyxl import Workbook
import pandas as pd
import glob
# from xlsxwriter import Workbook
import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-GLMUIDH\SQLEXPRESS;'
                      'Database=VISA_BULLETIN_IMPORT;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

def truncate_full_db():
    cursor.execute('''
                EXEC sp_MSforeachtable 'TRUNCATE TABLE ?' 
                ''')
    cursor.commit()
    # quit()

def import_data_to_db(file):

    file_sheets = ['Visa Bulletin Formatted_2021','Visa Bulletin Formatted_2020','Visa Bulletin Formatted_2014','Visa Bulletin Formatted_2013','Visa Bulletin Formatted_2012','Visa Bulletin Formatted_2011']
    
    for sheet in file_sheets:
        df = pd.read_excel(file,sheet_name=sheet)
        
        # column_list = list(df.columns) not required

        # you need to use index in for loop to access by name else it wont work
        for index, row in df.iterrows(): 
            Visa_Bulletin_Month_and_Year=''
            if 'Visa Bulletin Month and Year' in df.columns:
                Visa_Bulletin_Month_and_Year = row['Visa Bulletin Month and Year']

            Priority_Category=''
            if 'Priority Category' in df.columns:
                Priority_Category = row['Priority Category']

            Priority_Country=''
            if 'Priority Country' in df.columns:
                Priority_Country = row['Priority Country']

            Priority_Type=''
            if 'Priority Type' in df.columns:
                Priority_Type = row['Priority Type']

            Priority_Date=''
            if 'Priority Date' in df.columns:
                Priority_Date = row['Priority Date']

            Priority_Processing_Category=''
            if 'Priority Processing Category' in df.columns:
                Priority_Processing_Category = row['Priority Processing Category']
            
            USCIS_Filing_Cut_off=''
            if 'USCIS - Filing Cut-off ' in df.columns:
                USCIS_Filing_Cut_off  = row['USCIS - Filing Cut-off ']

            cursor.execute('''
            insert into VisaBulletinData (Visa_Bulletin_Month_and_Year,Priority_Category,Priority_Country,Priority_Type,Priority_Date,Priority_Processing_Category,USCIS_Filing_Cut_off)
            values ('{}','{}','{}','{}','{}','{}','{}')
            '''.format(Visa_Bulletin_Month_and_Year,Priority_Category,Priority_Country,Priority_Type,Priority_Date,Priority_Processing_Category,USCIS_Filing_Cut_off))

            cursor.commit()
               
    print('All data imported into DB')   

def changes_to_db_tables():

    tables = ['VisaBulletinData']
    for  table in tables:
        table_columns = cursor.execute('''
        SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('{}')
        '''.format(table)).fetchall()
        # the above query gives the list of columns as a queryset

        for i in range(len(table_columns)):     
            try:      
                cursor.execute('''UPDATE {}
                SET {} = REPLACE({}, 'nan & .0','')'''.format(table,table_columns[i].name,table_columns[i].name))
                cursor.commit()
            except:
                pass

            
def export_to_excel():
    query = '''select * from VisaBulletinData'''
    df = pd.read_sql(query,conn)
    for d_h in list(df.columns):
        # if d_h =='Visa_Bulletin_Month_and_Year' or d_h =='Priority_Date':
        if 'Year' in d_h or 'Date' in d_h:
            if "1900-01-01" in df[d_h]:
                        df[d_h] = ""
            else:
                df[d_h] = pd.to_datetime(df[d_h], format='%Y-%m-%d', errors='coerce').dt.date
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter',date_format='m/d/yyyy')
    df.to_excel(writer,'first',index=False)
    writer.save()

def start():
    truncate_full_db()
    # quit()
    for file in glob.glob('source_file/*'):
        
        import_data_to_db(file)


start()
changes_to_db_tables()
#export_to_excel()