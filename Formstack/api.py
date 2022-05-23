#from flask import Flask
import requests
import json
import pyodbc
from datetime import datetime 
import img2pdf
from PIL import Image
import os
import pprint

#app = Flask(__name__)
#app.config['JSON_SORT_KEYS'] = False

cwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(cwd)

#Formstack
form_id = "4685043"
oauth_token = "e98807a166042964e7eb626f84e81f03"

#DB connection
#conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
#                      'Server=localhost\SQLEXPRESS;'
#                      'Database=ReportsAutomation;'
#                      'Trusted_Connection=yes;')
                      
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=localhost;'
                      'Database=ImmilyticsReports;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
def change_format(date):
    #print('date', date)
    date = date.strip()
    
    if date:
        
        try:
            return datetime.strptime(date, "%b %d, %Y").strftime('%Y-%m-%d')
        except:
            try: 
                return datetime.strptime(date, "%d-%b-%Y").strftime('%Y-%m-%d')
            except: 
                try:
                    return datetime.strptime(date, "%m/%d/%Y").strftime('%Y-%m-%d')
                except: 
                    #return datetime.strptime("01/01/1900", "%m/%d/%Y").strftime('%Y-%m-%d')
                    return ''
    else:
        return date

def change_format2(date):
    #print('date', date)
    date = date.strip()
    
    if date:
        
        try:
            return datetime.strptime(date, "%b %d, %Y").strftime('%m%d%Y')
        except:
            try: 
                return datetime.strptime(date, "%d-%b-%Y").strftime('%m%d%Y')
            except: 
                try:
                    return datetime.strptime(date, "%m/%d/%Y").strftime('%m%d%Y')
                except: 
                    #return datetime.strptime("01/01/1900", "%m/%d/%Y").strftime('%Y-%m-%d')
                    return ''
    else:
        return date

#field codes
def process():
    beneficiary_id_field = "120635895"
    case_id_field = "120635899"
    beneficiary_name_field = "120633442"
    beneficiary_other_name_field = "120633443"
    birth_certificate_file_field = "120647341"
    city_of_birth_field = "120651559"
    country_of_birth_field = "120651622"
    country_of_citizenship_field = "120651641"
    marital_status_field = "120651788"
    passport_file_field = "120747496"
    passport_no_field = "120746526"
    passport_issuing_country_field = "120747281"
    passport_issue_date_field = "120747445"
    passport_expiration_date_field = "120747452"
    visa_file_field = "120747501"
    visa_type_field = "120747502"
    visa_issue_date_field = "120747504"
    visa_expiration_date_field = "120747505"
    ped_field = "120747503"



    url = "https://www.formstack.com/api/v2/form/"+str(form_id)+"/submission.json?oauth_token="+str(oauth_token)

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers)
    x = response.text
    y = json.loads(x)
    list_data = y['submissions']

    results_read = cursor.execute("SELECT last_processed_form_id FROM dbo.processed_form_details where id=1").fetchone()
    read_id = results_read[0]

    for submission_data in list_data:
        submission_id = submission_data['id']
        print(submission_id)
        if int(submission_id) > int(read_id):
            url2 = "https://www.formstack.com/api/v2/submission/"+str(submission_id)+".json?oauth_token="+str(oauth_token)
            response_data = requests.request("GET", url2, headers=headers)
            x2 = response_data.text
            y2 = json.loads(x2)
            #print(y2["data"])

            beneficiary_id = ""
            case_id = ""
            beneficiary_first_name = ""
            beneficiary_middle_name = ""
            beneficiary_last_name = ""
            beneficiary_other_first_name = ""
            beneficiary_other_middle_name = ""
            beneficiary_other_last_name = ""
            birth_certificate_file = ""
            city_of_birth = ""
            country_of_birth = ""
            country_of_citizenship = ""
            marital_status = ""
            passport_file = ""
            passport_no = ""
            passport_issuing_country = ""
            passport_issue_date = ""
            passport_expiration_date = ""
            visa_file = ""
            visa_type = ""
            visa_issue_date = ""
            visa_expiration_date = ""
            ped = ""
            passport_expiration_date_mmddyy = ""
            visa_expiration_date_mmddyy = ""

            for field in y2["data"]:
                field_id = str(field['field'])
                field_value = str(field['value'])
                if field_id == beneficiary_id_field:
                    beneficiary_id = field_value

                elif field_id == case_id_field:
                    case_id = field_value

                elif field_id == beneficiary_name_field:
                    chk1 = field_value.split('\n')
                    #print(chk1)
                    for chk in chk1:
                        
                        chk2 = (chk.strip()).split('=')
                        #print(chk2)
                        if chk2[0].strip() == "first":
                            beneficiary_first_name = chk2[1].strip()
                            #print(beneficiary_first_name)
                        elif chk2[0].strip() == "last":
                            beneficiary_last_name = chk2[1].strip()
                        elif chk2[0].strip() == "middle":
                            beneficiary_middle_name = chk2[1].strip()

                elif field_id == beneficiary_other_name_field:
                    chk1 = field_value.split('\n')
                    for chk in chk1:
                        chk2 = (chk.strip()).split('=')
                        if chk2[0].strip() == "first":
                            beneficiary_other_first_name = chk2[1].strip()
                        elif chk2[0].strip() == "last":
                            beneficiary_other_last_name = chk2[1].strip()
                        elif chk2[0].strip() == "middle":
                            beneficiary_other_middle_name = chk2[1].strip()

                elif field_id == birth_certificate_file_field:
                    birth_certificate_file = field_value
                
                elif field_id == city_of_birth_field:
                    city_of_birth = field_value
                
                elif field_id == country_of_birth_field:
                    country_of_birth = field_value
                
                elif field_id == country_of_citizenship_field:
                    country_of_citizenship = field_value
                
                elif field_id == marital_status_field:
                    marital_status = field_value

                elif field_id == passport_file_field:
                    passport_file = field_value

                elif field_id == passport_no_field:
                    passport_no = field_value

                elif field_id == passport_issuing_country_field:
                    passport_issuing_country = field_value
                
                elif field_id == passport_issue_date_field:
                    passport_issue_date = change_format(field_value)

                elif field_id == passport_expiration_date_field:
                    passport_expiration_date = change_format(field_value)
                    passport_expiration_date_mmddyy = change_format2(field_value)

                elif field_id == visa_file_field:
                    visa_file = field_value

                elif field_id == visa_type_field:
                    visa_type = field_value

                elif field_id == visa_issue_date_field:
                    visa_issue_date = change_format(field_value)

                elif field_id == visa_expiration_date_field:
                    visa_expiration_date = change_format(field_value)
                    visa_expiration_date_mmddyy = change_format2(field_value)

                elif field_id == ped_field:
                    ped = change_format(field_value)

            if beneficiary_id:     
                results = cursor.execute("SELECT * FROM dbo.Beneficiary where BeneficiaryXref='{}'".format(beneficiary_id)).fetchall()
                length = len(results)
                if length <= 0:
                    
                    cursor.execute("INSERT INTO dbo.Beneficiary(BeneficiaryXref, LastName, FirstName, MiddleName, OtherLastName, OtherFirstName, OtherMiddleName, BirthCity, BirthCountry, CitizenshipCountry, MaritalStatus, MostRecentPassportNumber, MostRecentPassportIssuingCountry, MostRecentPassportValidFromDate, MostRecentPassportExpirationDate, VisaType, VisaValidFromDate, VisaExpirationDate, VisaPedDate) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(beneficiary_id, beneficiary_last_name, beneficiary_first_name, beneficiary_middle_name, beneficiary_other_last_name, beneficiary_other_first_name, beneficiary_other_middle_name, city_of_birth, country_of_birth, country_of_citizenship, marital_status, passport_no, passport_issuing_country, passport_issue_date, passport_expiration_date, visa_type, visa_issue_date,  visa_expiration_date, ped))

                    cursor.execute("SELECT @@IDENTITY AS ID;")
                    beneficiary_inserted_id = cursor.fetchone()[0]
                    cursor.commit()
                else:
                    beneficiary_inserted_id = results[0].BeneficiaryId
                    cursor.execute("Update dbo.Beneficiary SET BeneficiaryXref='{}', LastName='{}', FirstName='{}', MiddleName='{}', OtherLastName='{}', OtherFirstName='{}', OtherMiddleName='{}', BirthCity='{}', BirthCountry='{}', CitizenshipCountry='{}', MaritalStatus='{}', MostRecentPassportNumber='{}', MostRecentPassportIssuingCountry='{}', MostRecentPassportValidFromDate='{}', MostRecentPassportExpirationDate='{}', VisaType='{}', VisaValidFromDate='{}', VisaExpirationDate='{}', VisaPedDate='{}' WHERE BeneficiaryXref='{}'".format(beneficiary_id, beneficiary_last_name, beneficiary_first_name, beneficiary_middle_name, beneficiary_other_last_name, beneficiary_other_first_name, beneficiary_other_middle_name, city_of_birth, country_of_birth, country_of_citizenship, marital_status, passport_no, passport_issuing_country, passport_issue_date, passport_expiration_date, visa_type, visa_issue_date,  visa_expiration_date, ped, beneficiary_id))
                    cursor.commit()
            
            if case_id and  beneficiary_inserted_id:
                results = cursor.execute("SELECT * FROM dbo.[Case] where BeneficiaryId='{}' and CaseXref='{}'".format(beneficiary_inserted_id, case_id)).fetchall()
                length = len(results)
                if length <= 0:
                    cursor.execute("INSERT INTO dbo.[Case](BeneficiaryId, CaseXref) VALUES ('{}', '{}')".format(beneficiary_inserted_id, case_id))
                    cursor.commit()
                else:
                    case_inserted_id = results[0].CaseId
                    cursor.execute("Update dbo.[Case] SET BeneficiaryId='{}', CaseXref='{}' WHERE CaseId='{}'".format(beneficiary_inserted_id, case_id, case_inserted_id))
                    cursor.commit()
                    
                    
                
            cursor.execute("UPDATE dbo.processed_form_details SET last_processed_form_id='{}' where id=1".format(str(submission_id)))
            cursor.commit()
            
            if birth_certificate_file:
                response = requests.get("https://www.formstack.com/api/v2/download/"+str(submission_id)+"/"+str(birth_certificate_file_field)+"?oauth_token="+oauth_token)
                img_file_name = "birth_certificate_image_"+str(submission_id)+".png"
                file = open("Downloaded/"+str(img_file_name), "wb")
                file.write(response.content)
                file.close()
                pdf_file_name = str(beneficiary_id)+', '+str(beneficiary_last_name)+', '+str(beneficiary_first_name)+' - Birth Certificate.pdf'
                img_path = os.path.join("Downloaded", img_file_name)
                
                pdf_path = os.path.join("Downloaded", pdf_file_name)
                image = Image.open(img_path)
                pdf_bytes = img2pdf.convert(image.filename)
                file = open(pdf_path, "wb")
                file.write(pdf_bytes)
                image.close()
                file.close()
                os.remove(img_path)

                
                
            if passport_file:
                response = requests.get("https://www.formstack.com/api/v2/download/"+str(submission_id)+"/"+str(passport_file_field)+"?oauth_token="+oauth_token)
                img_file_name = "passport_image_"+str(submission_id)+".png"
                file = open("Downloaded/"+str(img_file_name), "wb")
                file.write(response.content)
                file.close()
                pdf_file_name = str(beneficiary_id)+', '+str(beneficiary_last_name)+', '+str(beneficiary_first_name)+' - Passport'+' - '+str(passport_expiration_date_mmddyy)+'.pdf'
                img_path = os.path.join("Downloaded", img_file_name)
                pdf_path = os.path.join("Downloaded", pdf_file_name)
                image = Image.open(img_path)
                pdf_bytes = img2pdf.convert(image.filename)
                file = open(pdf_path, "wb")
                file.write(pdf_bytes)
                image.close()
                file.close()
                os.remove(img_path)

                

            if visa_file:
                response = requests.get("https://www.formstack.com/api/v2/download/"+str(submission_id)+"/"+str(visa_file_field)+"?oauth_token="+oauth_token)
                img_file_name = "visa_image_"+str(submission_id)+".png"
                file = open("Downloaded/"+str(img_file_name), "wb")
                file.write(response.content)
                file.close()
                pdf_file_name = str(beneficiary_id)+', '+str(beneficiary_last_name)+', '+str(beneficiary_first_name)+' - Visa Stamp'+' - '+str(visa_type)+str(visa_expiration_date_mmddyy)+'.pdf'
                img_path = os.path.join("Downloaded", img_file_name)
                pdf_path = os.path.join("Downloaded", pdf_file_name)
                image = Image.open(img_path)
                pdf_bytes = img2pdf.convert(image.filename)
                file = open(pdf_path, "wb")
                file.write(pdf_bytes)
                image.close()
                file.close()
                os.remove(img_path)

                

            

    print('All Forms Read.')

if __name__ == "__main__":
#    app.run(debug=True)
    process()
    