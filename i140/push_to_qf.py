import os
import sys, fitz
import pandas as pd
import csv 
import re
import pdfrw
from pdfrw import PdfReader, PdfWriter, PdfName
import shutil
from PyPDF2 import PdfFileMerger
import glob
import pyodbc
import requests
import json
from datetime import datetime
import base64

cwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(cwd)

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=localhost;'
                      'Database=immilyticsi140;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


username = "ImmilyticsLLC_AdminUser"
password = "wcqs9HscgI8StxrWBBeMTq"

api_url = "https://websvcs.quikforms.com/rest_authentication/token"
headersAuth = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
data = {"grant_type": "password", "username": username, "password": password}
response = requests.post(api_url, headers=headersAuth, data=data, verify=True)
response_auth = response.json()
#print(response_auth)
headersAPI = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer '+response_auth['access_token'],
}

source_dir = os.path.join(cwd, 'immiLytics/Certified PERMs')
processed_dir = os.path.join(cwd, 'processed')


def initf():
    
    file_names = os.listdir(source_dir)
    
    for file_name in file_names:
        print('Processing - '+file_name)
        case_number = ''.join(file_name.split('_')[:-1])
        print(case_number)
        get_from_DW(case_number, file_name)
    print('Finished')
def get_from_DW(case_number, file_name):
    
    results = cursor.execute("SELECT c.*,l.BarNumber,pas.LastName, pas.FirstName,pas.MiddleName,p.PetitionerName,\
            pas.Address1, pas.AddressType, pas.AddressTypeNumber, pas.City, pas.State, pas.ZipCode,\
            pas.Country, pas.JobTitle, pas.PhoneNumber, pas.MobilePhone, pas.Email, p.FederalEmployerId,\
            b.LastName as b_lastname, b.FirstName as b_firstname, b.MiddleName as b_middlename, b.BirthDate,\
            b.BirthCity, b.BirthStateProvince, b.BirthCountry, b.CitizenshipCountry,\
            ba.Address1 as ba_address1, ba.AddressType as ba_addresstype, ba.AddressUnitType as ba_addressunittype, ba.City as ba_city,\
            ba.StateProvince as ba_state, ba.ZipCode as ba_zipcode, ba.Country as ba_country,\
            b.AlienNumber, b.SsnNumber, b.MostRecentUSEntryDate, b.I94Number, b.I94ExpirationDate, b.I94Status,\
            b.MostRecentPassportNumber, b.MostRecentPassportIssuingCountry, b.MostRecentPassportExpirationDate,\
             p.BusinessType, p.YearEstablished, p.USEmployeeCount, p.GrossAnnualIncome, p.NetAnnualIncome, p.NaicsCode,\
            l.LastName as l_lastname, l.FirstName as l_firstname, l.MiddleName as l_middlename, l.FirmName as l_firmname, \
            l.Address1 as l_address1, l.AddressType as l_addresstype,\
            l.AddressTypeNumber as l_addresstypenumber, l.City as l_city, l.StateProvince as l_state, l.Country as l_country,\
            l.ZipCode as l_zipcode, l.BarNumber as l_barnumber,\
            l.PhoneNumber as l_phonenumber, l.MobileNumber as l_mobilenumber, l.Email as l_email,\
            o.OrganizationName, o.OrganizationXref, p.PetitionerXref, p.PetitionerName, b.BeneficiaryXref\
            FROM dbo.[Case] as c \
                LEFT JOIN dbo.Beneficiary b ON c.BeneficiaryId = b.BeneficiaryId \
                LEFT JOIN dbo.BeneficiaryAddress ba ON c.BeneficiaryId = ba.BeneficiaryId \
                LEFT JOIN dbo.Petitioner p ON p.PetitionerId=b.PetitionerId \
                LEFT JOIN dbo.Organization o ON o.OrganizationId =p.OrganizationId \
                LEFT JOIN dbo.PetitionerAuthorizedSignatory pas ON pas.PetitionerId=p.PetitionerId \
                LEFT JOIN dbo.LegalResource l ON l.EmployeeId=c.AttorneyPrimaryEMPId\
                WHERE c.ReceiptNumber='{}' and c.CasePetitionName like '%140%'".format(case_number)).fetchall()
    
    
    results2 = cursor.execute("Select * from CaseETA9089 Where PERMDOLCaseNumber='{}'".format(case_number)).fetchone()
    if results2 is None:
        results2_arr = []
        for i in range(0,75):
            results2_arr.append('')
        results2 = tuple(results2_arr)

    length = len(results)
    if results is not None and len(results) > 0:
        pass
        for result in results:
            #print(result)
            #print(result.BirthDate.strftime('%m/%d/%Y'))
            #return False

            address_type_chkbox_val = ''
            #print(result.AddressType, len(result.AddressType))
            if result.AddressType and len(result.AddressType) > 0: 
                if str(result.AddressType)[0]=='A':
                    address_type_chkbox_val = 1
                elif str(result.AddressType)[0]=='S':
                    address_type_chkbox_val = 2
                elif str(result.AddressType)[0]=='F':
                    address_type_chkbox_val = 3
            #print(address_type_chkbox_val)
            result_priority_category_chkbox_val = ''
            if str(result.PriorityCategory) in ["EB2", "EB-2", "Employment-Based 2nd", "Employment Based 2nd", "203(b)(2)"]:
                result_priority_category_chkbox_val = 4
            if str(result.PriorityCategory) in ["EB2", "EB-2", "Employment-Based 3rd", "Employment Based 3rd", "203(b)(3)(A)(ii)"]:
                result_priority_category_chkbox_val = 5

            
            result_ba_addressunittype_chkbox_val = ''
            if result.ba_addressunittype and len(result.ba_addressunittype) > 0:
                if str(result.ba_addressunittype)[0]=='A':
                    result_ba_addressunittype_chkbox_val = 1
                elif str(result.ba_addressunittype)[0]=='S':
                    result_ba_addressunittype_chkbox_val = 2
                elif str(result.ba_addressunittype)[0]=='F':
                    result_ba_addressunittype_chkbox_val = 3
            
            
            result_l_address1_chkbox_val = ''
            if result.l_address1 and len(result.l_address1) > 0:
                if str(result.l_address1)[0]=='A':
                    result_l_address1_chkbox_val = 1
                elif str(result.l_address1)[0]=='S':
                    result_l_address1_chkbox_val = 2
                elif str(result.l_address1)[0]=='F':
                    result_l_address1_chkbox_val = 3
            data_dict = [
                
                {
                    "FieldName":"1lawyer.G28Attached",
                    "FieldValue":1 
                },
                {
                    "FieldName":"1lawyer.LicNum",
                    "FieldValue":result.BarNumber 
                },
                {
                    "FieldName":"1petitioner.LName",
                    "FieldValue":result.LastName if result.LastName is not None else results2[18] 
                },
                {
                    "FieldName":"1petitioner.FName",
                    "FieldValue":result.FirstName if result.FirstName is not None else results2[19] 
                },
                {
                    "FieldName":"1petitioner.MName",
                    "FieldValue":result.MiddleName if result.MiddleName is not None else results2[20] 
                },
                {
                    "FieldName":"1contact.SEmp.Company",
                    "FieldValue":result.PetitionerName if result.PetitionerName is not None else (str(results2[18])+', '+str(results2[19])+' '+str(results2[20])).strip()
                },
                {
                    "FieldName":"1contact.EO.Attn",
                    "FieldValue":(str(result.FirstName if result.FirstName is not None else results2[19])+' '+str(result.LastName if result.LastName is not None else results2[18] )).strip()
                },
                {
                    "FieldName":"1contact.EO.Addr123",
                    "FieldValue":result.Address1 if result.Address1 is not None else results2[21] 
                },
                {
                    "FieldName":"1contact.EO.AddrUnitType",
                    "FieldValue":address_type_chkbox_val
                },  
                {
                    "FieldName":"1contact.EO.Addr4",
                    "FieldValue":result.AddressTypeNumber if result.AddressTypeNumber is not None else results2[22] 
                },
                {
                    "FieldName":"1contact.EO.City",
                    "FieldValue":result.City if result.City is not None else results2[23] 
                },
                {
                    "FieldName":"1contact.EO.State",
                    "FieldValue":result.State if result.State is not None else results2[24] 
                },
                {
                    "FieldName":"1contact.EO.Zip",
                    "FieldValue":result.ZipCode if result.ZipCode is not None else results2[25] 
                }, 
                {
                    "FieldName":"1contact.EO.Country",
                    "FieldValue":result.Country if result.Country is not None else results2[26] 
                },
                {
                    "FieldName":"1contact.SEmp.TaxIDComb",
                    "FieldValue":result.FederalEmployerId if result.FederalEmployerId is not None else results2[16] 
                },
                {
                    "FieldName":"IMMLY80315.chk1.04",
                    "FieldValue":result_priority_category_chkbox_val
                },
                {
                    "FieldName":"1ben.LName",
                    "FieldValue":result.b_lastname if result.b_lastname is not None else results2[55]
                },
                {
                    "FieldName":"1ben.FName",
                    "FieldValue":result.b_firstname  if result.b_firstname is not None else results2[56]
                },
                {
                    "FieldName":"1ben.MName",
                    "FieldValue":result.b_middlename if result.b_middlename is not None else results2[57]
                },
                {
                    "FieldName":"1ben.M.Attn",
                    "FieldValue":(str(result.b_firstname if result.b_firstname is not None else results2[56])+' '+str(result.b_lastname if result.b_lastname is not None else results2[55])).strip()
                },
                {
                    "FieldName":"1ben.M.Addr123",
                    "FieldValue":result.ba_address1 if result.ba_address1 is not None else results2[58]
                }, 
                {
                    "FieldName":"1ben.M.AddrUnitType",
                    "FieldValue":result_ba_addressunittype_chkbox_val
                },
                {
                    "FieldName":"1ben.M.Addr4",
                    "FieldValue":result.ba_addresstype if result.ba_addresstype is not None else results2[59]
                },
                {
                    "FieldName":"1ben.M.City",
                    "FieldValue":result.ba_city if result.ba_city is not None else results2[60]
                },
                {
                    "FieldName":"1ben.M.State",
                    "FieldValue":result.ba_state if result.ba_state is not None else results2[61]
                },
                {
                    "FieldName":"1ben.M.Zip",
                    "FieldValue":result.ba_zipcode if result.ba_zipcode is not None else results2[62]
                },
                {
                    "FieldName":"1ben.M.Country",
                    "FieldValue":result.ba_country if result.ba_country is not None else results2[63]
                },
                {
                    "FieldName":"1ben.DOB",
                    "FieldValue":result.BirthDate.strftime('%m/%d/%Y') if result.BirthDate is not None else results2[64].strftime('%m/%d/%Y')
                },
                {
                    "FieldName":"1ben.BP.City",
                    "FieldValue":result.BirthCity 
                },
                {
                    "FieldName":"1ben.BP.State",
                    "FieldValue":result.BirthStateProvince
                },
                {
                    "FieldName":"1ben.BP.Country",
                    "FieldValue":result.BirthCountry if result.BirthCountry is not None else results2[65] 
                },
                {
                    "FieldName":"1ben.Citizenship",
                    "FieldValue":result.CitizenshipCountry if result.CitizenshipCountry is not None else results2[66] 
                },
                {
                    "FieldName":"1ben.AlienRegNumComb",
                    "FieldValue":result.AlienNumber if result.AlienNumber is not None else results2[67] 
                },
                {
                    "FieldName":"1ben.SSNComb",
                    "FieldValue":result.SsnNumber
                },
                {
                    "FieldName":"1ben.I94.ArrivalDate",
                    "FieldValue":(result.MostRecentUSEntryDate).strftime('%m/%d/%Y') if result.MostRecentUSEntryDate is not None else ''
                },
                {
                    "FieldName":"1ben.I94.IDComb",
                    "FieldValue":result.I94Number  if result.I94Number is not None else results2[69] 
                },
                {
                    "FieldName":"1ben.I94.IDExpire",
                    "FieldValue":(result.I94ExpirationDate).strftime('%m/%d/%Y') if result.I94ExpirationDate is not None else ''
                },
                {
                    "FieldName":"1ben.I94.IDStatus",
                    "FieldValue":result.I94Status
                },
                {
                    "FieldName":"1ben.GOV.ID",
                    "FieldValue":result.MostRecentPassportNumber
                },
                {
                    "FieldName":"1ben.GOV.IDCountry",
                    "FieldValue":result.MostRecentPassportIssuingCountry
                },
                {
                    "FieldName":"1ben.GOV.IDExpire",
                    "FieldValue":(result.MostRecentPassportExpirationDate).strftime('%m/%d/%Y') if result.MostRecentPassportExpirationDate is not None else ''
                },
                {
                    "FieldName":"IMMLY80315.txt3.19.1",
                    "FieldValue":(str(result.b_firstname if result.b_firstname is not None else results2[56])+' '+str(result.b_lastname if result.b_lastname is not None else results2[55])).strip()
                },
                {
                    "FieldName":"IMMLY80315.txt3.19.0",
                    "FieldValue":result.ba_address1 if result.ba_address1 is not None else results2[58]
                },
                {
                    "FieldName":"IMMLY80315.txt3.24.0",
                    "FieldValue":result.ba_addressunittype if result.ba_addressunittype is not None else results2[59]
                },
                {
                    "FieldName":"IMMLY80315.txt3.29.0",
                    "FieldValue":result.ba_city if result.ba_city is not None else results2[60]
                },
                {
                    "FieldName":"IMMLY80315.txt3.29.2",
                    "FieldValue":result.ba_state if result.ba_state is not None else results2[61]
                },
                {
                    "FieldName":"IMMLY80315.txt3.29.3",
                    "FieldValue":result.ba_zipcode if result.ba_zipcode is not None else results2[62]
                },
                {
                    "FieldName":"IMMLY80315.txt3.34",
                    "FieldValue":result.ba_country if result.ba_country is not None else results2[63]
                },
                {
                    "FieldName":"1contact.SEmp.BusType",
                    "FieldValue":result.BusinessType 
                },
                {
                    "FieldName":"1contact.SEmp.YearEst",
                    "FieldValue":result.YearEstablished if result.YearEstablished is not None else results2[15]
                },
                {
                    "FieldName":"User.D1272.1contact.SEmp.NumEmployeesUS",
                    "FieldValue":result.USEmployeeCount if result.USEmployeeCount is not None else results2[14]
                },
                {
                    "FieldName":"1contact.SEmp.GrossIncome",
                    "FieldValue":result.GrossAnnualIncome 
                },
                {
                    "FieldName":"1contact.SEmp.NetIncome",
                    "FieldValue":result.NetAnnualIncome
                },
                {
                    "FieldName":"1contact.SEmp.NAICSComb",
                    "FieldValue":result.NaicsCode if result.NaicsCode is not None else results2[17]
                },
                {
                    "FieldName":"IMMLY80315.txt3.01.1",
                    "FieldValue":(str(result.l_firstname)+' '+str(result.l_lastname)).strip()
                },
                {
                    "FieldName":"1authind.LName",
                    "FieldValue":result.LastName if result.LastName is not None else results2[18] 
                },
                {
                    "FieldName":"1authind.FName",
                    "FieldValue":result.FirstName if result.FirstName is not None else results2[19] 
                },
                {
                    "FieldName":"1authind.SignTitle",
                    "FieldValue":result.JobTitle if result.JobTitle is not None else results2[45]
                },
                {
                    "FieldName":"1authind.O.Phone",
                    "FieldValue":result.PhoneNumber if result.PhoneNumber is not None else results2[27]
                },
                {
                    "FieldName":"IMMLY80315.txt3.525",
                    "FieldValue":result.MobilePhone if result.MobilePhone is not None else results2[28]
                },
                {
                    "FieldName":"1authind.O.Email",
                    "FieldValue":result.Email if result.Email is not None else results2[29]
                },
                {
                    "FieldName":"1lawyer.LName",
                    "FieldValue":result.l_lastname if result.l_lastname is not None else results2[30]
                },
                {
                    "FieldName":"1lawyer.FName",
                    "FieldValue":result.l_firstname if result.l_firstname is not None else results2[31]
                },
                {
                    "FieldName":"1lawfirm.Company",
                    "FieldValue":result.l_firmname if result.l_firmname is not None else results2[33]
                },
                {
                    "FieldName":"1lawfirm.O.Addr123",
                    "FieldValue":result.l_address1 if result.l_address1 is not None else results2[35]
                },
                {
                    "FieldName":"1lawfirm.O.AddrUnitType",
                    "FieldValue":result_l_address1_chkbox_val 
                },
                {
                    "FieldName":"1lawfirm.O.Addr4",
                    "FieldValue":result.l_addresstypenumber if result.l_addresstypenumber is not None else results2[36]
                },
                {
                    "FieldName":"1lawfirm.O.City",
                    "FieldValue":result.l_city if result.l_city is not None else results2[37]
                },
                {
                    "FieldName":"1lawfirm.O.State",
                    "FieldValue":result.l_state if result.l_state is not None else results2[38]
                },
                {
                    "FieldName":"1lawfirm.O.Zip",
                    "FieldValue":result.l_zipcode if result.l_zipcode is not None else results2[39]
                },
                {
                    "FieldName":"1lawfirm.O.Country",
                    "FieldValue":result.l_country if result.l_country is not None else results2[40]
                },
                {
                    "FieldName":"1lawyer.O.Phone",
                    "FieldValue":result.l_phonenumber if result.l_phonenumber is not None else results2[41]
                },
                {
                    "FieldName":"1lawyer.O.Mobile",
                    "FieldValue":result.l_mobilenumber if result.l_mobilenumber is not None else results2[42]
                },
                {
                    "FieldName":"1lawyer.O.Email",
                    "FieldValue":result.l_email if result.l_email is not None else results2[43]
                }
            ]

            #print(data_dict)
            params = {
                "HostFormOnQuik":True,
                "FormFields":data_dict,
                "QuikFormID":"80315",
                "PrintEditablePDF":True
                }

            #print(params)
            #return False
            data_json = json.dumps(params)

            response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf', headers=headersAPI, data=data_json)
            api_response = response.json()
            #print(api_response)
            pdf_base64 = api_response['ResultData']['PDF']
            #print()
            with open('Form I-140.pdf', 'wb') as pdf:
                pdf.write(base64.b64decode(pdf_base64))
            #print(api_response['ResultData']['FormIDs'])
            data_dict2 = [
                {
                    "FieldName":"1lawyer.LName",
                    "FieldValue":result.l_lastname if result.l_lastname is not None else results2[30]
                },
                {
                    "FieldName":"1lawyer.FName",
                    "FieldValue":result.l_firstname if result.l_firstname is not None else results2[31]
                },
                {
                    "FieldName":"1lawyer.MName",
                    "FieldValue":result.l_middlename if result.l_middlename is not None else results2[32]
                },
                {
                    "FieldName":"1lawfirm.O.Addr123",
                    "FieldValue":result.l_address1  if result.l_address1 is not None else results2[35]
                },
                {
                    "FieldName":"1lawfirm.O.AddrUnitType",
                    "FieldValue":result_l_address1_chkbox_val
                },
                {
                    "FieldName":"1lawfirm.O.Addr4",
                    "FieldValue":result.l_addresstypenumber if result.l_addresstypenumber is not None else results2[36]
                },
                {
                    "FieldName":"1lawfirm.O.City",
                    "FieldValue":result.l_city if result.l_city is not None else results2[37]
                },
                {
                    "FieldName":"1lawfirm.O.State",
                    "FieldValue":result.l_state if result.l_state is not None else results2[38]
                },
                {
                    "FieldName":"1lawfirm.O.Zip",
                    "FieldValue":result.l_zipcode if result.l_zipcode is not None else results2[39]
                },
                {
                    "FieldName":"1lawfirm.O.Country",
                    "FieldValue":result.l_country if result.l_country is not None else results2[40]
                },
                {
                    "FieldName":"1lawyer.O.Phone",
                    "FieldValue":result.l_phonenumber if result.l_phonenumber is not None else results2[41]
                },
                {
                    "FieldName":"1lawyer.O.Mobile",
                    "FieldValue":result.l_mobilenumber if result.l_mobilenumber is not None else results2[42]
                },
                {
                    "FieldName":"1lawyer.O.Email",
                    "FieldValue":result.l_email if result.l_email is not None else results2[43]
                },
                {
                    "FieldName":"1lawyer.LicNum",
                    "FieldValue":result.l_barnumber
                },
                {
                    "FieldName":"1lawfirm.Company",
                    "FieldValue":result.l_firmname if result.l_firmname is not None else results2[33]
                },
                {
                    "FieldName":"IMMLY80314.txt1.21.0",
                    "FieldValue":(str(result.b_lastname if result.b_lastname is not None else results2[55])+', '+str(result.b_firstname if result.b_firstname is not None else results2[56])+' '+str(result.b_middlename if result.b_middlename is not None else results2[57])).strip()
                },
                {
                    "FieldName":"1ben.LName",
                    "FieldValue":result.LastName  
                },
                {
                    "FieldName":"1ben.FName",
                    "FieldValue":result.FirstName 
                },
                {
                    "FieldName":"1ben.MName",
                    "FieldValue":result.MiddleName
                },
                {
                    "FieldName":"1ben.SEmp.Company",
                    "FieldValue":result.PetitionerName if result.PetitionerName is not None else results2[5]
                },
                {
                    "FieldName":"1ben.SignTitle",
                    "FieldValue":result.JobTitle if result.JobTitle is not None else results2[45]
                },
                {
                    "FieldName":"1ben.EO.Phone",
                    "FieldValue":result.PhoneNumber  if result.PhoneNumber is not None else results2[12]
                },
                {
                    "FieldName":"1ben.EO.Mobile",
                    "FieldValue":result.MobilePhone if result.MobilePhone is not None else results2[13]
                },
                {
                    "FieldName":"1ben.EO.Email",
                    "FieldValue":result.Email 
                },
                {
                    "FieldName":"1ben.EO.Addr123",
                    "FieldValue":result.Address1 if result.Address1 is not None else results2[7]
                },
                {
                    "FieldName":"1ben.EO.Addr4",
                    "FieldValue":result.AddressTypeNumber if result.AddressTypeNumber is not None else results2[8]
                },
                {
                    "FieldName":"1ben.EO.City",
                    "FieldValue":result.City if result.City is not None else results2[9]
                },
                {
                    "FieldName":"1ben.EO.State",
                    "FieldValue":result.State if result.State is not None else results2[10]
                },
                {
                    "FieldName":"1ben.EO.Zip",
                    "FieldValue":result.ZipCode if result.ZipCode is not None else results2[11]
                },
                {
                    "FieldName":"1ben.EO.Country",
                    "FieldValue":result.Country if result.Country is not None else results2[12]
                },
                {
                    "FieldName":"1ben.LName",
                    "FieldValue":result.LastName
                },
                {
                    "FieldName":"1ben.FName",
                    "FieldValue":result.FirstName
                },
                {
                    "FieldName":"1ben.MName",
                    "FieldValue":result.MiddleName
                },
                {
                    "FieldName":"User.D1272.AttorneyEligiblePracticeLawIn",
                    "FieldValue":1
                },
                {
                    "FieldName":"User.D1272.AmNotAmSubjectToAnyOrder",
                    "FieldValue":1
                }, 
                {
                    "FieldName":"IMMLY80314.chk1.02",
                    "FieldValue":1
                },
                {
                    "FieldName":"IMMLY80314.chk1.03",
                    "FieldValue":2
                },
                {
                    "FieldName":"1ben.EO.AddrUnitType",
                    "FieldValue":address_type_chkbox_val
                },
                {
                    "FieldName":"IMMLY80314.chk1.25",
                    "FieldValue":1
                }
            ]

            params = {
                "HostFormOnQuik":True,
                "FormFields":data_dict2,
                "QuikFormID":"80314",
                "PrintEditablePDF":True
                }

            data_json = json.dumps(params)

            response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf', headers=headersAPI, data=data_json)
            api_response = response.json()
            #print(api_response)
            pdf_base64 = api_response['ResultData']['PDF']
            #print()
            with open('Form G-28.pdf', 'wb') as pdf:
                pdf.write(base64.b64decode(pdf_base64))
            
            doc_details = {
                'organization_xref' :result.OrganizationXref,
                'organization_name' :result.OrganizationName,
                'petitioner_xref' :result.PetitionerXref,
                'petitioner_name' :result.PetitionerName,
                'beneficiary_xref' :result.BeneficiaryXref,
                'last_name' :result.b_lastname,
                'first_name' :result.b_firstname,

            }
        
    else:
        #print('else')
        results2 = cursor.execute("Select * from CaseETA9089 Where PERMDOLCaseNumber='{}'".format(case_number)).fetchone()

        length = len(results2)
        if length > 0:
        
            data_dict = [
                {
                    "FieldName":"1lawyer.G28Attached",
                    "FieldValue":1 
                },
                {
                    "FieldName":"1lawyer.LicNum",
                    "FieldValue":''
                },
                {
                    "FieldName":"1petitioner.LName",
                    "FieldValue":results2[18] 
                },
                {
                    "FieldName":"1petitioner.FName",
                    "FieldValue":results2[19] 
                },
                {
                    "FieldName":"1petitioner.MName",
                    "FieldValue":results2[20] 
                },
                {
                    "FieldName":"1contact.SEmp.Company",
                    "FieldValue": (str(results2[18])+', '+str(results2[19])+' '+str(results2[20])).strip()
                },
                {
                    "FieldName":"1contact.EO.Attn",
                    "FieldValue":(str(results2[19])+' '+str(results2[18] )).strip()
                },
                {
                    "FieldName":"1contact.EO.Addr123",
                    "FieldValue":results2[21] 
                },
                {
                    "FieldName":"1contact.EO.Addr123****",
                    "FieldValue":''
                },  
                {
                    "FieldName":"1contact.EO.Addr4",
                    "FieldValue":results2[22] 
                },
                {
                    "FieldName":"1contact.EO.City",
                    "FieldValue":results2[23] 
                },
                {
                    "FieldName":"1contact.EO.State",
                    "FieldValue":results2[24] 
                },
                {
                    "FieldName":"1contact.EO.Zip",
                    "FieldValue":results2[25] 
                }, 
                {
                    "FieldName":"1contact.EO.Country",
                    "FieldValue":results2[26] 
                },
                {
                    "FieldName":"1contact.SEmp.TaxIDComb",
                    "FieldValue":results2[16] 
                },
                {
                    "FieldName":"QuikRadio80315.IMMLY80315.chk1.04",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.LName",
                    "FieldValue":results2[55]
                },
                {
                    "FieldName":"1ben.FName",
                    "FieldValue":results2[56]
                },
                {
                    "FieldName":"1ben.MName",
                    "FieldValue":results2[57]
                },
                {
                    "FieldName":"1ben.M.Attn",
                    "FieldValue":(str(results2[56])+' '+str(results2[55])).strip()
                },
                {
                    "FieldName":"1ben.M.Addr123",
                    "FieldValue":results2[58]
                }, 
                {
                    "FieldName":"1ben.M.Addr4",
                    "FieldValue":results2[59]
                },
                {
                    "FieldName":"1ben.M.City",
                    "FieldValue":results2[60]
                },
                {
                    "FieldName":"1ben.M.State",
                    "FieldValue":results2[61]
                },
                {
                    "FieldName":"1ben.M.Zip",
                    "FieldValue":results2[62]
                },
                {
                    "FieldName":"1ben.M.Country",
                    "FieldValue":results2[63]
                },
                {
                    "FieldName":"1ben.DOB",
                    "FieldValue":results2[64].strftime('%m/%d/%Y')
                },
                {
                    "FieldName":"1ben.BP.City",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.BP.State",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.BP.Country",
                    "FieldValue":results2[65] 
                },
                {
                    "FieldName":"1ben.Citizenship",
                    "FieldValue":results2[66] 
                },
                {
                    "FieldName":"1ben.AlienRegNumComb",
                    "FieldValue":results2[67] 
                },
                {
                    "FieldName":"1ben.SSNComb",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.I94.ArrivalDate",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.I94.IDComb",
                    "FieldValue":results2[69] 
                },
                {
                    "FieldName":"1ben.I94.IDExpire",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.I94.IDStatus",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.GOV.ID",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.GOV.IDCountry",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.GOV.IDExpire",
                    "FieldValue":''
                },
                {
                    "FieldName":"IMMLY80315.txt3.19.1",
                    "FieldValue":(str(results2[56])+' '+str(results2[55])).strip()
                },
                {
                    "FieldName":"IMMLY80315.txt3.19.0",
                    "FieldValue":results2[58]
                },
                {
                    "FieldName":"IMMLY80315.txt3.24.0",
                    "FieldValue":results2[59]
                },
                {
                    "FieldName":"IMMLY80315.txt3.29.0",
                    "FieldValue":results2[60]
                },
                {
                    "FieldName":"IMMLY80315.txt3.29.2",
                    "FieldValue":results2[61]
                },
                {
                    "FieldName":"IMMLY80315.txt3.29.3",
                    "FieldValue":results2[62]
                },
                {
                    "FieldName":"IMMLY80315.txt3.34",
                    "FieldValue":results2[63]
                },
                {
                    "FieldName":"1contact.SEmp.BusType",
                    "FieldValue":''
                },
                {
                    "FieldName":"1contact.SEmp.YearEst",
                    "FieldValue":results2[15]
                },
                {
                    "FieldName":"User.D1272.1contact.SEmp.NumEmployeesUS",
                    "FieldValue":results2[14]
                },
                {
                    "FieldName":"1contact.SEmp.GrossIncome",
                    "FieldValue":'' 
                },
                {
                    "FieldName":"1contact.SEmp.NetIncome",
                    "FieldValue":''
                },
                {
                    "FieldName":"1contact.SEmp.NAICSComb",
                    "FieldValue":results2[17]
                },
                {
                    "FieldName":"IMMLY80315.txt3.01.1",
                    "FieldValue":''
                },
                {
                    "FieldName":"1authind.LName",
                    "FieldValue":results2[18] 
                },
                {
                    "FieldName":"1authind.FName",
                    "FieldValue":results2[19] 
                },
                {
                    "FieldName":"1authind.SignTitle",
                    "FieldValue":results2[45]
                },
                {
                    "FieldName":"1authind.O.Phone",
                    "FieldValue":results2[27]
                },
                {
                    "FieldName":"IMMLY80315.txt3.525",
                    "FieldValue":results2[28]
                },
                {
                    "FieldName":"1authind.O.Email",
                    "FieldValue":results2[29]
                },
                {
                    "FieldName":"1lawyer.LName",
                    "FieldValue":results2[30]
                },
                {
                    "FieldName":"1lawyer.FName",
                    "FieldValue":results2[31]
                },
                {
                    "FieldName":"1lawfirm.Company",
                    "FieldValue":results2[33]
                },
                {
                    "FieldName":"1lawfirm.O.Addr123",
                    "FieldValue":results2[35]
                },
                {
                    "FieldName":"1lawfirm.O.Addr4",
                    "FieldValue":results2[36]
                },
                {
                    "FieldName":"1lawfirm.O.City",
                    "FieldValue":results2[37]
                },
                {
                    "FieldName":"1lawfirm.O.State",
                    "FieldValue":results2[38]
                },
                {
                    "FieldName":"1lawfirm.O.Zip",
                    "FieldValue":results2[39]
                },
                {
                    "FieldName":"1lawfirm.O.Country",
                    "FieldValue":results2[40]
                },
                {
                    "FieldName":"1lawyer.O.Phone",
                    "FieldValue":results2[41]
                },
                {
                    "FieldName":"1lawyer.O.Mobile",
                    "FieldValue":results2[42]
                },
                {
                    "FieldName":"1lawyer.O.Email",
                    "FieldValue":results2[43]
                }
            ]

            #print(data_dict)
            params = {
                "HostFormOnQuik":True,
                "FormFields":data_dict,
                "QuikFormID":"80315",
                "PrintEditablePDF":True
                }


            data_json = json.dumps(params)

            response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf', headers=headersAPI, data=data_json)
            api_response = response.json()
            #print(api_response)
            pdf_base64 = api_response['ResultData']['PDF']
            print()
            with open('Form I-140.pdf', 'wb') as pdf:
                pdf.write(base64.b64decode(pdf_base64))
            #print(api_response['ResultData']['FormIDs'])
            data_dict2 = [
                {
                    "FieldName":"1lawyer.LName",
                    "FieldValue":results2[30]
                },
                {
                    "FieldName":"1lawyer.FName",
                    "FieldValue":results2[31]
                },
                {
                    "FieldName":"1lawyer.MName",
                    "FieldValue":results2[32]
                },
                {
                    "FieldName":"1lawfirm.O.Addr123",
                    "FieldValue":results2[35]
                },
                {
                    "FieldName":"1lawfirm.O.Addr4",
                    "FieldValue":results2[36]
                },
                {
                    "FieldName":"1lawfirm.O.City",
                    "FieldValue":results2[37]
                },
                {
                    "FieldName":"1lawfirm.O.State",
                    "FieldValue":results2[38]
                },
                {
                    "FieldName":"1lawfirm.O.Zip",
                    "FieldValue":results2[39]
                },
                {
                    "FieldName":"1lawfirm.O.Country",
                    "FieldValue":results2[40]
                },
                {
                    "FieldName":"1lawyer.O.Phone",
                    "FieldValue":results2[41]
                },
                {
                    "FieldName":"1lawyer.O.Mobile",
                    "FieldValue":results2[42]
                },
                {
                    "FieldName":"1lawyer.O.Email",
                    "FieldValue":results2[43]
                },
                {
                    "FieldName":"1lawyer.LicNum",
                    "FieldValue":''
                },
                {
                    "FieldName":"1lawfirm.Company",
                    "FieldValue":results2[33]
                },
                {
                    "FieldName":"IMMLY80314.txt1.21.0",
                    "FieldValue":(str(results2[55])+', '+str(results2[56])+' '+str(results2[57])).strip()
                },
                {
                    "FieldName":"1ben.LName",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.FName",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.MName",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.SEmp.Company",
                    "FieldValue":results2[5]
                },
                {
                    "FieldName":"1ben.SignTitle",
                    "FieldValue":results2[45]
                },
                {
                    "FieldName":"1ben.EO.Phone",
                    "FieldValue":results2[12]
                },
                {
                    "FieldName":"1ben.EO.Mobile",
                    "FieldValue":results2[13]
                },
                {
                    "FieldName":"1ben.EO.Email",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.EO.Addr123",
                    "FieldValue":results2[7]
                },
                {
                    "FieldName":"1ben.EO.Addr4",
                    "FieldValue":results2[8]
                },
                {
                    "FieldName":"1ben.EO.City",
                    "FieldValue":results2[9]
                },
                {
                    "FieldName":"1ben.EO.State",
                    "FieldValue":results2[10]
                },
                {
                    "FieldName":"1ben.EO.Zip",
                    "FieldValue":results2[11]
                },
                {
                    "FieldName":"1ben.EO.Country",
                    "FieldValue":results2[12]
                },
                {
                    "FieldName":"1ben.LName",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.FName",
                    "FieldValue":''
                },
                {
                    "FieldName":"1ben.MName",
                    "FieldValue":''
                },
                {
                    "FieldName":"User.D1272.AttorneyEligiblePracticeLawIn",
                    "FieldValue":1
                }, 
                {
                    "FieldName":"IMMLY80314.chk1.02",
                    "FieldValue":1
                },
                {
                    "FieldName":"IMMLY80314.chk1.03",
                    "FieldValue":2
                },
                {
                    "FieldName":"IMMLY80314.chk1.25",
                    "FieldValue":1
                }
            ]

            params = {
                "HostFormOnQuik":True,
                "FormFields":data_dict2,
                "QuikFormID":"80314",
                "PrintEditablePDF":True
                }

            data_json = json.dumps(params)

            response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf', headers=headersAPI, data=data_json)
            api_response = response.json()
            #print(api_response)
            pdf_base64 = api_response['ResultData']['PDF']
            #print()
            with open('Form G-28.pdf', 'wb') as pdf:
                pdf.write(base64.b64decode(pdf_base64))
            
            doc_details = {
                'organization_xref' :result.OrganizationXref,
                'organization_name' :result.OrganizationName,
                'petitioner_xref' :result.PetitionerXref,
                'petitioner_name' :result.PetitionerName,
                'beneficiary_xref' :result.BeneficiaryXref,
                'last_name' :result.b_lastname,
                'first_name' :result.b_firstname,

            }

            
    shutil.move(os.path.join(source_dir, file_name), os.path.join(processed_dir, file_name))
    pdf_merge_sequence(doc_details, file_name)
    
def pdf_merge_sequence(data_dict, file_name):
    #print(data_dict)
    chk_by = None
    folder_name = None
    if data_dict['organization_xref'] and data_dict['organization_name']:
        folder_name = str(data_dict['organization_xref'])+' - '+str(data_dict['organization_name'])
        chk_by = "Organization"

    if folder_name is None:
        if data_dict['petitioner_xref'] and data_dict['petitioner_name']:
            folder_name = str(data_dict['petitioner_xref'])+' - '+str(data_dict['petitioner_name'])
            chk_by = "Petitioner"
    
    #print(chk_by, folder_name)
    os.chdir(cwd)
    if os.path.exists(os.path.join('ImmiLytics', folder_name)):
        folder_path = os.path.join(cwd, 'ImmiLytics', folder_name)
        if chk_by =="Organization":
            if data_dict['petitioner_xref'] and data_dict['petitioner_name']:
                folder_name2 = str(data_dict['petitioner_xref'])+' - '+str(data_dict['petitioner_name'])
                #print(folder_name2)
                folder_path2 = os.path.join(folder_path, folder_name2)
        else:
            folder_path2 = folder_path
    
    #print('chk2', folder_path2)
    beneficiary_xref = ''
    beneficiary_lname = ''
    beneficiary_fname = ''
    beneficiary_name = ''
    folder_name4 = ''
    folder_path4 = ''
    beneficiary_xref = data_dict['beneficiary_xref']
    beneficiary_lname = str(data_dict["last_name"]).strip()
    beneficiary_fname = str(data_dict["first_name"]).strip()
    
    #print(folder_path2)
    beneficiary_name = str(beneficiary_xref)+' - '+beneficiary_lname+', '+beneficiary_fname
    if folder_path2:
        if os.path.exists(os.path.join(folder_path2, beneficiary_name)):
            folder_name3 = beneficiary_name
            folder_path3 = os.path.join(folder_path2, folder_name3)
    
    #print('chk3', folder_path3)
    #print(folder_path3)
    #print(os.path.join(folder_path3, "Supporting Docs"))
    if folder_path3:
        if os.path.exists(os.path.join(folder_path3, "Supporting Docs")):
            folder_path4 = os.path.join(folder_path3, "Supporting Docs")

    #print(folder_path4)
    pdfs = []
    if folder_path4:
        os.chdir(folder_path4)
        sequence = ["Masters Degree", "Masters Transcripts", "Bachelors Degree", "Bachelors Transcripts",
        "EVL", "Additional Supporting Docs", "Misc. Docs", "Passport", "I-94", "Pay Stub", "PR Sponsorship Letter"]

        sequence_multiple = ["Additional Supporting Docs", "Misc. Docs", "Pay Stubs"]
        pdf_files = glob.glob("*.pdf")
        
        shutil.move(os.path.join(cwd, 'Form G-28.pdf'), os.path.join(folder_path3, 'Form G-28.pdf'))
        shutil.move(os.path.join(cwd, 'Form I-140.pdf'), os.path.join(folder_path3, 'Form I-140.pdf'))
        pdfs.append(os.path.join(folder_path3, 'Form G-28.pdf'))
        pdfs.append(os.path.join(folder_path3, 'Form I-140.pdf'))
        pdfs.append(os.path.join(processed_dir, file_name))
        for seq in sequence:
            for pdf_f in glob.glob(seq+"*"):
                #print(pdf_f)
                #pdfs.append(pdf_f)
                pdfs.append(os.path.join(folder_path4, pdf_f))
        
        os.chdir(cwd)
        os.chdir(folder_path)
        latest_annual_report = 0
        latest_annual_report_file = ''
        for pdf_f in glob.glob("*.pdf"):
            if "Annual Report" in pdf_f:
                file_name_annual = os.path.splitext(os.path.basename(pdf_f))
                file_name_split = (str(file_name_annual[0]).strip()).split(' ')
                #print(file_name_split)
                if int(file_name_split[-1]) > latest_annual_report:
                    latest_annual_report = int(file_name_split[-1])
                    latest_annual_report_file = pdf_f
            elif "Tax Docs" in pdf_f:
                pdfs.append(os.path.join(folder_path, pdf_f))


        if latest_annual_report_file:    
            pdfs.append(os.path.join(folder_path, latest_annual_report_file))
        #print(pdfs)
        #pdfdocs(pdfs, folder_path3)
        merger = PdfFileMerger()
        
        for pdf in pdfs:
            merger.append(pdf)
        os.chdir(cwd)
        merger.write(os.path.join(folder_path3, "final.pdf"))
        merger.close()

def pdfdocs(inputfiles, folder_path):
    #merger = PdfFileMerger()
    #merger.write(os.path.join(folder_path, "final.pdf"))
    os.chdir(cwd)
    output = PdfWriter()
    num = 0
    output_acroform = None
    for inpfn in inputfiles:
        try:
            if os.path.exists(inpfn):
                input = PdfReader(inpfn, verbose=False)
                output.addpages(input.pages)
                if PdfName('AcroForm') in input[PdfName('Root')].keys():
                    source_acroform = input[PdfName(
                        'Root')][PdfName('AcroForm')]
                    if PdfName('Fields') in source_acroform:
                        output_formfields = source_acroform[PdfName('Fields')]
                    else:
                        output_formfields = []
                    num2 = 0
                    for form_field in output_formfields:
                        key = PdfName('T')
                        # Field names are in the "(name)" format
                        old_name = form_field[key].replace(
                            '(', '').replace(')', '')
                        form_field[key] = 'FILE_{n}_FIELD_{m}_{on}'.format(
                            n=num, m=num2, on=old_name)
                        num2 += 1
                    if output_acroform == None:
                        output_acroform = source_acroform
                    else:
                        for key in source_acroform.keys():
                            if key not in output_acroform:
                                output_acroform[key] = source_acroform[key]
                        if (PdfName('DR') in source_acroform.keys()) and (PdfName('Font') in source_acroform[PdfName('DR')].keys()):
                            if PdfName('Font') not in output_acroform[PdfName('DR')].keys():
                                output_acroform[PdfName('DR')][PdfName(
                                    'Font')] = source_acroform[PdfName('DR')][PdfName('Font')]
                        else:
                            for font_key in source_acroform[PdfName('DR')][PdfName('Font')].keys():
                                if font_key not in output_acroform[PdfName('DR')][PdfName('Font')]:
                                    output_acroform[PdfName('DR')][PdfName(
                                        'Font')][font_key] = source_acroform[PdfName('DR')][PdfName('Font')][font_key]
                    if PdfName('Fields') not in output_acroform:
                        output_acroform[PdfName('Fields')] = output_formfields
                    else:
                        output_acroform[PdfName('Fields')] += output_formfields
                num += 1
            else:
                print('form not exists '+inpfn)
        except FileNotFoundError as e:
            print("error: " + e.strerror)
    output.trailer[PdfName('Root')][PdfName('AcroForm')] = output_acroform
    output.write(os.path.join(folder_path, "final.pdf"))

if __name__ == '__main__':
    initf()