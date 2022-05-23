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
                      'Database=immilyticsDB;'
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


INVOICE_TEMPLATE_PATH = 'Form_I-140_020322_adobe.pdf'
INVOICE_TEMPLATE_PATH_G28 = 'Form G-28-new.pdf'
legal_resource_path = 'ImmiLytics/Legal Resource - Current.xlsx'
open_i140_resource_path = 'ImmiLytics/Open I-140 Case Report - Current.xlsx'


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

def strcon(value):
    if isinstance(value, str):
        return value
    elif str(value) in ["nan", "NaT", ""]:
        return ""
    elif isinstance(value, float) or isinstance(value, int):
        return str(value).rstrip('0').rstrip('.') if '.' in str(value) else str(value)
    else:
        return str(value)

def index_in_list(a_list, index):
    return index < len(a_list)

def make_text(words):
    """Return textstring output of getText("words").

    Word items are sorted for reading sequence left to right,
    top to bottom.
    """
    line_dict = {}  # key: vertical coordinate, value: list of words
    words.sort(key=lambda w: w[2])  # sort by horizontal coordinate
    for w in words:  # fill the line dictionary
        #print(w)
        y1 = round(w[3], 0)  # bottom of a word: don't be too picky!
        word = w[4]  # the text of the word
        line = line_dict.get(y1, [])  # read current line content
        line.append(word)  # append new word
        line_dict[y1] = line  # write back to dict
    lines = list(line_dict.items())
    lines.sort()  # sort vertically
    
    return "\n".join([" ".join(line[1]) for line in lines])

def initf():
    source_dir = os.path.join(cwd, 'immiLytics/Certified PERMs')
    processed_dir = os.path.join(cwd, 'processed')
    output_dir = os.path.join(cwd, 'output')
   
    file_names = os.listdir(source_dir)
    
    for file_name in file_names:
        print('Processing - '+file_name)
        output_pdf_path = os.path.join(output_dir, 'Form I-140_'+file_name)
        output_pdf_path_g28 = os.path.join(output_dir, 'Form G-28_'+file_name)
        dict_data = get_data(os.path.join(source_dir,file_name))
        dict_data2 = {}
        if dict_data:
            dict_data = get_data_csv(dict_data)
        
        for k, v in dict_data.items():
            if v is None or v == "nan":
                dict_data[k] = ''

        #print(dict_data)
        
        full_name = dict_data['Contact Last Name'] if 'Contact Last Name' in dict_data else '' 
        full_name += ', '+dict_data['Contact First Name'] if 'Contact First Name' in dict_data else ''
        full_name += ' '+dict_data['Contact Middle Name'] if 'Contact Middle Name' in dict_data else ''
        full_name = full_name.strip()
        #print(full_name)
        alien_full_name = dict_data['Alien Last Name'] if 'Alien Last Name' in dict_data else '' 
        alien_full_name += ', '+dict_data['Alien First Name'] if 'Alien First Name' in dict_data else ''
        alien_full_name += ' '+dict_data['Alien Middle Name'] if 'Alien Middle Name' in dict_data else ''
        alien_full_name = alien_full_name.strip()
        
        alien_full_name2 = dict_data['Alien First Name'] if 'Alien First Name' in dict_data else '' 
        alien_full_name2 += ' '+dict_data['Alien Last Name'] if 'Alien Last Name' in dict_data else ''
        alien_full_name2 = alien_full_name2.strip()
        
        SOC_code  = (dict_data['SOC'] if 'SOC' in dict_data else '' ).split('-')

        data_dict = [
            {
                "FieldName": "1lawyer.LicNum",
                "FieldValue":dict_data['Bar Number'] if 'Bar Number' in dict_data else ''
            },
            {
                "FieldName": "1petitioner.LName",
                "FieldValue": dict_data['Last Name'] if 'Last Name' in dict_data else ''
            },
            {
                "FieldName": "1petitioner.FName",
                "FieldValue": dict_data['First Name'] if 'First Name' in dict_data else ''
            },
            {
                "FieldName": "1petitioner.MName",
                "FieldValue": dict_data['Middle Name'] if 'Middle Name' in dict_data else ''
            },
            {
                "FieldName": "1contact.SEmp.Company",
                "FieldValue":dict_data['petitioner_name'] if 'petitioner_name' in dict_data else ''
            },
            {
                "FieldName": "1contact.EO.Attn",
                "FieldValue": dict_data['#'] if 'LastName' in dict_data else ''
            },
            {
                "FieldName": "1contact.EO.Addr123",
                "FieldValue": dict_data['Address1'] if 'Address1' in dict_data else ''
            },
            {
                "FieldName": "1contact.EO.Addr123****",
                "FieldValue": dict_data['AddressType'] if 'AddressType' in dict_data else ''
            },
            {
                "FieldName": "1contact.EO.Addr4",
                "FieldValue":dict_data['AddressTypeNumber'] if 'AddressTypeNumber' in dict_data else ''
            },
            {
                "FieldName": "1contact.EO.City",
                "FieldValue":dict_data['City of Birth'] if 'City of Birth' in dict_data else ''
            },
            {
                "FieldName": "1contact.EO.State",
                "FieldValue":dict_data['State of Birth'] if 'State of Birth' in dict_data else ''
            },
            {
                "FieldName": "1contact.EO.Zip",
                    "FieldValue":dict_data['Zip Code'] if 'Zip Code' in dict_data else ''
            },
            {
                "FieldName": "1contact.EO.Country",
                "FieldValue":dict_data['Country'] if 'Country' in dict_data else ''
            },
            {
                "FieldName": "1contact.SEmp.TaxIDComb",
                "FieldValue":dict_data['Employee Id'] if 'Employee Id' in dict_data else ''
            },
            {
                "FieldName": "QuikRadio80315.IMMLY80315.chk1.04",
                "FieldValue":dict_data['Case Priority Category'] if 'Case Priority Category' in dict_data else ''
            },
            {
                "FieldName": "1ben.LName",
                "FieldValue":dict_data['#'] if 'b_lastname' in dict_data else ''
            },
            {
                "FieldName": "1ben.FName",
                "FieldValue":dict_data['Alien First Name'] if 'Alien First Name' in dict_data else ''
            },
            {
                "FieldName": "1ben.MName",
                "FieldValue":dict_data['Alien Middle Name'] if 'Alien Middle Name' in dict_data else ''
            },
            {
                "FieldName": "1ben.M.Attn",
                "FieldValue":dict_data['#'] if 'b_lastname' in dict_data else ''
            },
            {
                "FieldName": "1ben.M.Addr123",
                "FieldValue":dict_data['Alien Address1'] if 'Alien Address1' in dict_data else ''
            },
            {
                "FieldName": "1ben.M.Addr4",
                "FieldValue":dict_data['Contact Address Type'] if 'Contact Address Type' in dict_data else ''
            },
            {
                "FieldName": "1ben.M.City",
                "FieldValue":dict_data['Alien City'] if 'Alien City' in dict_data else ''
            },
            {
                "FieldName": "1ben.M.State",
                "FieldValue":dict_data['Alien State'] if 'Alien State' in dict_data else ''
            },
            {
                "FieldName": "1ben.M.Zip",
                "FieldValue":dict_data['#'] if 'ba_zipcode' in dict_data else ''
            },
            {
                "FieldName": "1ben.M.Country",
                "FieldValue":dict_data['Alien Country'] if 'Alien Country' in dict_data else ''
            },
            {
                "FieldName": "1ben.DOB",
                "FieldValue":dict_data['Alien DOB'] if 'Alien DOB' in dict_data else ''
            },
            {
                "FieldName": "1ben.BP.City",
                "FieldValue":dict_data['Country of Birth'] if 'Country of Birth' in dict_data else ''
            },
            {
                "FieldName": "1ben.BP.State",
                "FieldValue":dict_data['BirthStateProvince'] if 'BirthStateProvince' in dict_data else ''
            },
            {
                "FieldName": "1ben.BP.Country",
                "FieldValue":dict_data['Alien State'] if 'Alien State' in dict_data else ''
            },
            {
                "FieldName": "1ben.Citizenship",
                "FieldValue":dict_data['Country of Citizenship'] if 'Country of Citizenship' in dict_data else ''
            },
            {
                "FieldName": "1ben.AlienRegNumComb",
                "FieldValue":dict_data['Case Number'] if 'Case Number' in dict_data else ''
            },
            {
                "FieldName": "1ben.SSNComb",
                "FieldValue":dict_data['SSN Number'] if 'SSN Number' in dict_data else ''
            },
            {
                "FieldName": "1ben.I94.ArrivalDate",
                "FieldValue":dict_data['I-94 Entry Date'] if 'I-94 Entry Date' in dict_data else ''
            },
            {
                "FieldName": "1ben.I94.IDComb",
                "FieldValue":dict_data['I-94 Number'] if 'I94Number' in dict_data else ''
            },
            {
                "FieldName": "1ben.I94.IDExpire",
                "FieldValue":dict_data['Immigration Status Expiration Date (I-94)'] if 'I94ExpirationDate' in dict_data else ''
            },
            {
                "FieldName": "1ben.I94.IDStatus",
                "FieldValue":dict_data['Immigration Status (I-94)'] if 'Immigration Status (I-94)' in dict_data else ''
            },
            {
                "FieldName": "1ben.GOV.ID",
                "FieldValue":dict_data['Passport Number'] if 'Passport Number' in dict_data else ''
            },
            {
                "FieldName": "1ben.GOV.IDCountry",
                "FieldValue":dict_data['Passport Issuing Country'] if 'Passport Issuing Country' in dict_data else ''
            },
            {
                "FieldName": "1ben.GOV.IDExpire",
                "FieldValue":dict_data['Passport Expiration Date'] if 'Passport Expiration Date' in dict_data else ''
            },
            {
                "FieldName": "IMMLY80315.txt3.19.1",
                "FieldValue":dict_data['#'] if 'b_lastname' in dict_data else ''
            },
            {
                "FieldName": "IMMLY80315.txt3.19.0",
                "FieldValue":dict_data['#'] if 'ba_address1' in dict_data else ''
            },
            {
                "FieldName": "IMMLY80315.txt3.24.0",
                "FieldValue":dict_data['#'] if 'ba_addressunittype' in dict_data else ''
            },
            {
                "FieldName": "IMMLY80315.txt3.29.0",
                "FieldValue":dict_data['#'] if 'ba_city' in dict_data else ''
            },
            {
                "FieldName": "IMMLY80315.txt3.29.2",
                "FieldValue":dict_data['#'] if 'ba_state' in dict_data else ''
            },
            {
                "FieldName": "IMMLY80315.txt3.29.3",
                "FieldValue":dict_data['#'] if 'ba_zipcode' in dict_data else ''
            },
            {
                "FieldName": "IMMLY80315.txt3.34",
                "FieldValue":dict_data['#'] if 'ba_country' in dict_data else ''
            },
            {
                "FieldName": "1contact.SEmp.BusType",
                "FieldValue":dict_data['Petitioner Business Type'] if 'Petitioner Business Type' in dict_data else ''
            },
            {
                "FieldName": "1contact.SEmp.YearEst",
                "FieldValue":dict_data['#'] if 'YearEstablished' in dict_data else ''
            },
            {
                "FieldName": "User.D1272.1contact.SEmp.NumEmployeesUS",
                "FieldValue":dict_data['No of Employees'] if 'No of Employees' in dict_data else ''
            },
            {
                "FieldName": "1contact.SEmp.GrossIncome",
                "FieldValue":dict_data['Petitioner Gross Income'] if 'Petitioner Gross Income' in dict_data else ''
            },
            {
                "FieldName": "1contact.SEmp.NetIncome",
                "FieldValue":dict_data['Petitioner Net Income'] if 'Petitioner Net Income' in dict_data else ''
            },
            {
                "FieldName": "1contact.SEmp.NAICSComb",
                "FieldValue":dict_data['NAICS Code'] if 'NAICS Code' in dict_data else ''
            },
            {
                "FieldName": "IMMLY80315.txt3.01.1",
                "FieldValue":dict_data['#'] if 'l_firstname' in dict_data else ''
            },
            {
                "FieldName": "1authind.LName",
                "FieldValue":dict_data['#'] if 'LastName' in dict_data else ''
            },
            {
                "FieldName": "1authind.FName",
                "FieldValue":dict_data['#'] if 'FirstName' in dict_data else ''
            },
            {
                "FieldName": "1authind.SignTitle",
                "FieldValue":dict_data['Petitioner Authorized Signatory Job Title'] if 'Petitioner Authorized Signatory Job Title' in dict_data else ''
            },
            {
                "FieldName": "1authind.O.Phone",
                "FieldValue":dict_data['Petitioner Authorized Signatory Phone Number'] if 'Petitioner Authorized Signatory Phone Number' in dict_data else ''
            },
            {
                "FieldName": "IMMLY80315.txt3.525",
                "FieldValue":dict_data['#'] if 'MobilePhone' in dict_data else ''
            },
            {
                "FieldName": "1authind.O.Email",
                "FieldValue":dict_data['Petitioner Authorized Signatory Email'] if 'Petitioner Authorized Signatory Email' in dict_data else ''
            },
            {
                "FieldName": "1lawyer.LName",
                "FieldValue":dict_data['Last Name'] if 'Last Name' in dict_data else ''
            },
            {
                "FieldName": "1lawyer.FName",
                "FieldValue":dict_data['First Name'] if 'First Name' in dict_data else ''
            },
            {
                "FieldName": "1lawfirm.Company",
                "FieldValue":dict_data['Firm Name'] if 'Firm Name' in dict_data else ''
            },
            {
                "FieldName": "1lawfirm.O.Addr123",
                "FieldValue":dict_data['Address 1'] if 'Address 1' in dict_data else ''
            },
            {
                "FieldName": "1lawfirm.O.Addr4",
                "FieldValue":dict_data['l_addresstypenumber'] if 'l_addresstypenumber' in dict_data else ''
            },
            {
                "FieldName": "1lawfirm.O.City",
                "FieldValue":dict_data['City'] if 'City' in dict_data else ''
            },
            {
                "FieldName": "1lawfirm.O.State",
                "FieldValue":dict_data['State'] if 'State' in dict_data else ''
            },
            {
                "FieldName": "1lawfirm.O.Zip",
                "FieldValue":dict_data['Zip Code'] if 'Zip Code' in dict_data else ''
            },
            {
                "FieldName": "1lawfirm.O.Country",
                "FieldValue":dict_data['Country'] if 'Country' in dict_data else ''
            },
            {
                "FieldName": "1lawyer.O.Phone",
                "FieldValue":dict_data['Phone Number'] if 'Phone Number' in dict_data else ''
            },
            {
                "FieldName": "1lawyer.O.Mobile",
                "FieldValue":dict_data['Mobile Phone'] if 'Mobile Phone' in dict_data else ''
            },
            {
                "FieldName": "1lawyer.O.Email",
                "FieldValue":dict_data['Email'] if 'Email' in dict_data else ''
            }
        ]


        phone_no = dict_data['Phone Number'] if 'Phone Number' in dict_data else ''
        phone_no2 = dict_data['Phone Number Extn.'] if 'Phone Number Extn.' in dict_data else ''
        phone_no_txt  = str(phone_no)
        if phone_no2:
            phone_no_txt  += ' X '+str(phone_no2)
        
        pphone_no = dict_data['Petitioner Authorized Signatory Phone Number'] if 'Petitioner Authorized Signatory Phone Number' in dict_data else ''
        pphone_no2 = dict_data['Petitioner Authorized Signatory Phone Number Extension'] if 'Petitioner Authorized Signatory Phone Number Extension' in dict_data else ''
        petitioner_phone_no_txt  = str(pphone_no)
        if pphone_no2:
            petitioner_phone_no_txt  += ' X '+str(pphone_no2)

        params = {
            "HostFormOnQuik": True,
            "FormFields": data_dict,
            "QuikFormID": "80315",
            "PrintEditablePDF": True
        }

        data_json = json.dumps(params)

        response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf',
                                 headers=headersAPI, data=data_json)
        api_response = response.json()
        # print(api_response)
        pdf_base64 = api_response['ResultData']['PDF']
        print()
        with open('Form I-140.pdf', 'wb') as pdf:
            pdf.write(base64.b64decode(pdf_base64))


        data_dict_g28 = [
                {
                    "FieldName":"1lawyer.LName",
                    "FieldValue":dict_data['Last Name'] if 'Last Name' in dict_data else ''
                },
                {
                    "FieldName":"1lawyer.FName",
                    "FieldValue":dict_data['First Name'] if 'First Name' in dict_data else ''
                },
                {
                    "FieldName":"1lawyer.MName",
                    "FieldValue":dict_data['Middle Name'] if 'Middle Name' in dict_data else ''
                },
                {
                    "FieldName":"1lawfirm.O.Addr123",
                    "FieldValue":dict_data['Address 1'] if 'Address 1' in dict_data else ''
                },
                {
                    "FieldName":"1lawfirm.O.Addr4",
                    "FieldValue":dict_data['Address Type Number'] if 'Address Type Number' in dict_data else ''
                },
                {
                    "FieldName":"1lawfirm.O.City",
                    "FieldValue":dict_data['City'] if 'City' in dict_data else ''
                },
                {
                    "FieldName":"1lawfirm.O.State",
                    "FieldValue":dict_data['State'] if 'State' in dict_data else ''
                },
                {
                    "FieldName":"1lawfirm.O.Zip",
                    "FieldValue":dict_data['Zip Code'] if 'Zip Code' in dict_data else ''
                },
                {
                    "FieldName":"1lawfirm.O.Country",
                    "FieldValue":dict_data['Country'] if 'Country' in dict_data else ''
                },
                {
                    "FieldName":"1lawyer.O.Phone",
                    "FieldValue":dict_data['Phone Number'] if 'Phone Number' in dict_data else ''
                },
                {
                    "FieldName":"1lawyer.O.Mobile",
                    "FieldValue":dict_data['Mobile Phone'] if 'Mobile Phone' in dict_data else ''
                },
                {
                    "FieldName":"1lawyer.O.Email",
                    "FieldValue":dict_data['Email'] if 'Email' in dict_data else ''
                },
                {
                    "FieldName":"1lawyer.LicNum",
                    "FieldValue":dict_data['Bar Number'] if 'Bar Number' in dict_data else ''
                },
                {
                    "FieldName":"1lawfirm.Company",
                    "FieldValue":dict_data['Firm Name'] if 'Firm Name' in dict_data else ''
                },
                {
                    "FieldName":"IMMLY80314.txt1.21.0",
                    "FieldValue":dict_data['#'] if 'LastName' in dict_data else ''
                },
                {
                    "FieldName":"1ben.LName",
                    "FieldValue":dict_data['Contact Last Name'] if 'Contact Last Name' in dict_data else ''
                },
                {
                    "FieldName":"1ben.FName",
                    "FieldValue":dict_data['Contact First Name'] if 'Contact First Name' in dict_data else ''
                },
                {
                    "FieldName":"1ben.MName",
                    "FieldValue":dict_data['Contact Middle Name'] if 'Contact Middle Name' in dict_data else ''
                },
                {
                    "FieldName":"1ben.SEmp.Company",
                    "FieldValue":dict_data['petitioner_name'] if 'petitioner_name' in dict_data else ''
                },
                {
                    "FieldName":"1ben.SignTitle",
                    "FieldValue":dict_data['Job Title'] if 'Job Title' in dict_data else ''
                },
                {
                    "FieldName":"1ben.EO.Phone",
                    "FieldValue":dict_data['#'] if 'PhoneNumber' in dict_data else ''
                },
                {
                    "FieldName":"1ben.EO.Mobile",
                    "FieldValue":dict_data['#'] if 'MobilePhone' in dict_data else ''
                },
                {
                    "FieldName":"1ben.EO.Email",
                    "FieldValue":dict_data['#'] if 'Email' in dict_data else ''
                },
                {
                    "FieldName":"1ben.EO.Addr123",
                    "FieldValue":dict_data['#'] if 'Address1' in dict_data else ''
                },
                {
                    "FieldName":"1ben.EO.Addr4",
                    "FieldValue":dict_data['#'] if 'AddressTypeNumber' in dict_data else ''
                },
                {
                    "FieldName":"1ben.EO.City",
                    "FieldValue":dict_data['#'] if 'City' in dict_data else ''
                },
                {
                    "FieldName":"1ben.EO.State",
                    "FieldValue":dict_data['#'] if 'State' in dict_data else ''
                },
                {
                    "FieldName":"1ben.EO.Zip",
                    "FieldValue":dict_data['#'] if 'ZipCode' in dict_data else ''
                },
                {
                    "FieldName":"1ben.EO.Country",
                    "FieldValue":dict_data['#'] if 'Country' in dict_data else ''
                },
                {
                    "FieldName":"1ben.LName",
                    "FieldValue":dict_data['#'] if '#' in dict_data else ''
                },
                {
                    "FieldName":"1ben.FName",
                    "FieldValue":dict_data['#'] if 'FirstName' in dict_data else ''
                },
                {
                    "FieldName":"1ben.MName",
                    "FieldValue":dict_data['#'] if 'MiddleName' in dict_data else ''
                },
            ]

        params = {
            "HostFormOnQuik": True,
            "FormFields": data_dict_g28,
            "QuikFormID": "80314",
            "PrintEditablePDF": True
        }

        data_json = json.dumps(params)

        response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf',
                                 headers=headersAPI, data=data_json)
        api_response = response.json()
        # print(api_response)
        pdf_base64 = api_response['ResultData']['PDF']
        # print()
        with open('Form G-28.pdf', 'wb') as pdf:
            pdf.write(base64.b64decode(pdf_base64))

        os.chdir(cwd)
        ouput_pdf_path_location = get_form_filepath(dict_data)
        if ouput_pdf_path_location:
            output_pdf_path = os.path.join(ouput_pdf_path_location, 'Form I-140.pdf')
            output_pdf_path_g28 = os.path.join(ouput_pdf_path_location, 'Form G-28.pdf')

        # write_fillable_pdf(INVOICE_TEMPLATE_PATH, output_pdf_path, data_dict)
        # write_fillable_pdf(INVOICE_TEMPLATE_PATH_G28, output_pdf_path_g28, data_dict_g28)
        shutil.move(os.path.join(source_dir, file_name), os.path.join(processed_dir, file_name))
        pdf_merge_sequence(dict_data, output_pdf_path, output_pdf_path_g28, os.path.join(processed_dir, file_name))
        print(dict_data)
        # process_to_db(dict_data)
    print('Processed')


def get_data(fname):
    doc = fitz.open(fname)
    all_annots=[]  
    data_dict = {}  
    #page = doc[0]
    for _pno, page in enumerate(doc):  # iterate the document pages
    #if True:
        text = page.getText("words")  # get plain text (is in UTF-8)
        text1=make_text(text)
        all_annots.append(text1)
        
        text_data = text1.split('\n')
    
        if _pno == 0:
            #print(text_data)
            employer_list_index = [index for index, string in enumerate(text_data) if "Employer’s name" in string]
            employer_data = text_data[int(employer_list_index[0])+1]
            data_dict["Employer Name"] = employer_data
            
            contact_list_index = [index for index, string in enumerate(text_data) if "Contact’s last" in string]
            contact_data = text_data[int(contact_list_index[0])+1].split()
            if len(contact_data) >= 3:
                data_dict["Contact Last Name"] = contact_data[0] if index_in_list(contact_data, 0) else ''
                data_dict["Contact First Name"] = ' '.join(contact_data[1:-1]) if index_in_list(contact_data, 1) else ''
                data_dict["Contact Middle Name"] = contact_data[-1] if index_in_list(contact_data, 3) else ''
            else:
                data_dict["Contact Last Name"] = contact_data[0] if index_in_list(contact_data, 0) else ''
                data_dict["Contact First Name"] = ' '.join(contact_data[1:]) if index_in_list(contact_data, 1) else ''
                data_dict["Contact Middle Name"] = contact_data[2] if index_in_list(contact_data, 3) else ''
            
            

            contact_address1_index = [index for index, string in enumerate(text_data[int(contact_list_index[0]):]) if "2. Address 1" in string]
            contact_address1_data = text_data[int(contact_list_index[0])+int(contact_address1_index[0])+1]
            data_dict["Contact Address1"] = contact_address1_data
            data_dict["Contact Address2"] = text_data[int(contact_list_index[0])+int(contact_address1_index[0])+3] if '3' not in text_data[int(contact_list_index[0])+int(contact_address1_index[0])+3] else ''

            country_state_indexm = [index for index, string in enumerate(text_data[int(contact_list_index[0]):]) if "3. City State" in string]
            country_state_index = int(contact_list_index[0])+int(country_state_indexm[0])+1 

            country_state_text = str(text_data[country_state_index]).split()
            #print(country_state_text)
            contact_city = country_state_text[0]
            if country_state_text[1].isupper():
                contact_country = country_state_text[1:-1]
            else:
                contact_city += ' '+country_state_text[1]
                contact_country = country_state_text[2:-1]

            contact_postal_code = country_state_text[-1]
            country_state_text2 = str(text_data[country_state_index+1]) if '4.' not in text_data[country_state_index+1] else ''
            country_split = (country_state_text2.strip())
            contact_state = country_split
            data_dict["Contact City"] = contact_city
            data_dict["Contact State"] = contact_state
            data_dict["Contact Postal Code"] = str(contact_postal_code).split('.')[0]
            data_dict["Contact Country"] = ' '.join(contact_country)
            
            fein_no_index = [index for index, string in enumerate(text_data) if "8. NAICS Code" in string]
            fein_no_text = (str(text_data[fein_no_index[0]+1]).strip()).split()[0]
            naics_code_text = (str(text_data[fein_no_index[0]+1]).strip()).split()[1]
            data_dict["FEIN No"] = fein_no_text
            data_dict["NAICS Code"] = naics_code_text

            no_of_employees_index = [index for index, string in enumerate(text_data) if "5. Number of employees 6." in string]
            no_of_employees_text = ''
            year_of_commenced_business_text = ''
            no_of_employees_text += str(text_data[no_of_employees_index[0]+2]) if "7." not in text_data[no_of_employees_index[0]+1] else ''
            year_of_commenced_business_text += str(text_data[no_of_employees_index[0]+1]) if "7." not in text_data[no_of_employees_index[0]+2] else ''

            data_dict["No of Employees"] = no_of_employees_text
            data_dict["Year of Commenced Business"] = year_of_commenced_business_text
            
        
        elif _pno == 1:
            #print(text_data)
            soc_index = [index for index, string in enumerate(text_data) if "2. SOC/" in string]
            soc_text = (str(text_data[soc_index[0]+1]).strip()).split()[1]
            data_dict["SOC"] = soc_text

            primary_worksite_index = [index for index, string in enumerate(text_data) if "1. Primary worksite" in string]
            primary_worksite_text = (str(text_data[primary_worksite_index[0]+1]).strip())
            data_dict["Primary Worksite"] = primary_worksite_text

            job_address2_index = [index for index, string in enumerate(text_data[int(primary_worksite_index[0]):]) if "Address 2" in string]
            job_address2_data = text_data[int(primary_worksite_index[0])+int(job_address2_index[0])+1]
            data_dict["Job Address2"] = text_data[int(primary_worksite_index[0])+int(job_address2_index[0])+1] if '2.' not in text_data[int(primary_worksite_index[0])+int(job_address2_index[0])+1] else ''

            job_address2_index = int(primary_worksite_index[0])+int(job_address2_index[0])
            country_state_index = int(job_address2_index)+3 if '2. City State' in text_data[int(job_address2_index)+2] else int(job_address2_index)+2

            country_state_text = str(text_data[country_state_index])
            country_state_text += ' '+str(text_data[country_state_index+1]) if '3.' not in text_data[country_state_index+1] else ''
            
            country_split = (country_state_text.strip()).split()
            job_city = ' '.join(country_split[2:])
            job_state = country_split[0]
            job_postal_code = country_split[1]
            data_dict["Job City"] = job_city
            data_dict["Job State"] = job_state
            data_dict["Job Postal Code"] = str(job_postal_code).split('.')[0]

            


            job_title_index = [index for index, string in enumerate(text_data) if "3. Job title" in string]
            job_title_text = (str(text_data[job_title_index[0]+1]).strip()) if '4.' not in text_data[job_title_index[0]+1] else ''
            data_dict["Job Title"] = job_title_text

            wages_index = [index for index, string in enumerate(text_data) if "From: To:" in string]
            wages_text = (str(text_data[wages_index[0]+2]).strip()) if ',' not in text_data[wages_index[0]+2] else ''
            wages_text += ' '+(str(text_data[wages_index[0]+3]).strip()) if ',' not in text_data[wages_index[0]+3] else ''
            wages_text += ' '+(str(text_data[wages_index[0]+4]).strip()) if ',' not in text_data[wages_index[0]+4] else ''
            wages_text += ' '+(str(text_data[wages_index[0]+5]).strip()) if ',' not in text_data[wages_index[0]+5] else ''
            #print(wages_text)
            wages= (str(text_data[wages_index[0]+6]).strip()) if ','  in text_data[wages_index[0]+7] else (str(text_data[wages_index[0]+5]).strip())
            wages_split = (wages_text.strip().encode()).split()
            wages_list = []
            wages_selected = None
            wages_per = ''
            for i,w in enumerate(wages_split):
                if w == b'Month' or w == b'Year'  or w == b'Hour'  or w == b'Week'  or w == b'Bi-Weekly':
                    wages_list.append(w.decode())
                else:
                    if w == b'\x14':
                        wages_selected =i-1
            
            #print(wages_list)
            #print(wages_selected)
            if wages_selected:
                wages_per = wages_list[wages_selected]


            data_dict["Wage Per"] = wages_per
            data_dict["Wage"] = wages
            
        
        elif _pno == 4:
            #print(text_data)
            alien_list_index = [index for index, string in enumerate(text_data) if "1. Alien’s last" in string]
            alien_text = (str(text_data[alien_list_index[0]+1]).strip()).split()
            if len(alien_text) > 3:
                data_dict["Alien Last Name"] = alien_text[0] if index_in_list(alien_text, 0) else ''
                data_dict["Alien First Name"] = ' '.join(alien_text[1:-1]) if index_in_list(alien_text, 1) else ''
                data_dict["Alien Middle Name"] = alien_text[-1] if index_in_list(alien_text, 3) else ''
            else:
                data_dict["Alien Last Name"] = alien_text[0] if index_in_list(alien_text, 0) else ''
                data_dict["Alien First Name"] = ' '.join(alien_text[1:]) if index_in_list(alien_text, 1) else ''
                data_dict["Alien Middle Name"] = alien_text[2] if index_in_list(alien_text, 3) else ''

            
            alien_address1_index = [index for index, string in enumerate(text_data[int(alien_list_index[0]):]) if "2. Current address 1" in string]
            alien_address1_data = text_data[int(alien_list_index[0])+int(alien_address1_index[0])+1]
            data_dict["Alien Address1"] = alien_address1_data
            data_dict["Alien Address2"] = text_data[int(alien_list_index[0])+int(alien_address1_index[0])+3] if '3' not in text_data[int(alien_list_index[0])+int(alien_address1_index[0])+3] else ''

            country_state_index = int(alien_list_index[0])+int(alien_address1_index[0])+5 if '3. City State' in text_data[int(alien_list_index[0])+int(alien_address1_index[0])+4] else int(alien_list_index[0])+int(alien_address1_index[0])+4
            country_state_text = str(text_data[country_state_index])
            alien_city = country_state_text
            country_state_text2 = ' '+str(text_data[country_state_index+1]) if '4.' not in text_data[country_state_index+1] else ''
            
            country_split = (country_state_text2.strip()).split()
            alien_state = country_split[0]
            alien_postal_code = country_split[-1]
            alien_country = country_split[1:-1]
            data_dict["Alien City"] = alien_city
            data_dict["Alien State"] = alien_state
            data_dict["Alien Postal Code"] = str(alien_postal_code).split('.')[0]
            data_dict["Alien Country"] = ' '.join(alien_country)

            alien_list2_index = [index for index, string in enumerate(text_data) if "5. Country of" in string]
            alien_text2 = (str(text_data[alien_list2_index[0]+1]).strip()).split()
            data_dict["Country of Citizenship"] = alien_text2[0] if index_in_list(alien_text2, 0) else ''
            data_dict["Country of Birth"] = alien_text2[1] if index_in_list(alien_text2, 1) else ''

            alien_dob_index = [index for index, string in enumerate(text_data) if "7. Alien’s date of birth" in string]
            alien_text3 = (str(text_data[alien_dob_index[0]+1]).strip()).split()
            data_dict["Alien DOB"] = alien_text3[0] if index_in_list(alien_text3, 0) else ''
            #print(data_dict["Alien DOB"], data_dict["Alien DOB"].count('/'))
            if '/' in data_dict["Alien DOB"] and data_dict["Alien DOB"].count('/') != 2 :
                alien_dob = data_dict["Alien DOB"].replace("/","")
                alien_dob = str(alien_dob[0:2])+'/'+str(alien_dob[2:4])+'/'+str(alien_dob[4:])
                data_dict["Alien DOB"] = alien_dob
            alien_reg_index = [index for index, string in enumerate(text_data) if "9. Alien registration" in string]
            alien_text4 = (str(text_data[alien_reg_index[0]+1]).strip())
            alien_text5 = ' '+(str(text_data[alien_reg_index[0]+2]).strip()) if '11.' not in text_data[alien_reg_index[0]+2] else ''
            alien_reg_text = (alien_text4 + alien_text5).strip()
            data_dict["Alien Registration No"] = alien_reg_text.split()[-1]

        elif _pno == 8:
            #print(text_data)
            eta_list_index = [index for index, string in enumerate(text_data) if "This Certification is valid from" in string]
            eta_text = (str(text_data[eta_list_index[0]+1]).strip()).split()
            data_dict["Certificate Valid From"] = eta_text[0] if index_in_list(eta_text, 0) else ''
            data_dict["Certificate Valid To"] = eta_text[1] if index_in_list(eta_text, 1) else ''

            eta_list_index2 = [index for index, string in enumerate(text_data) if "Signature of Certify" in string]
            eta_text2 = (str(text_data[eta_list_index2[0]+1]).strip())
            eta_text3 = (str(text_data[eta_list_index2[0]+2]).strip())
            data_dict["Case Number"] = eta_text2
            data_dict["Filing Date"] = eta_text3
            
        
    doc.close()
    return data_dict

# def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
#     check_box_list = ['Line3b_Unit0', 'Line3b_Unit1', 'Line3b_Unit2', 'Line12b_Unit0', 'Line12b_Unit1', 'Line12b_Unit2', \
#         'part2petitiontype4', 'part2petitiontype5', 'Line6c_Unit2', 'Line6c_Unit21', 'Line6c_Unit22', 'Line2b_unit20', 'Line2b_unit21', 'Line2b_unit22', 'part8item3unit21', 'part8item3unit22', 'part8item3unit23']
#     template_pdf = pdfrw.PdfReader(input_pdf_path)
#     template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
#     for page in template_pdf.pages:
#         annotations = page.get("/Annots")
#         #annotations = template_pdf.pages[0][ANNOT_KEY]
#         for annotation in annotations:
#             #annotation.update(pdfrw.PdfDict(AP=""))
#             if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
#                 if annotation[ANNOT_FIELD_KEY]:
#                     key = annotation[ANNOT_FIELD_KEY][1:-1]
#                     #print('key ', key)
#                     if key in data_dict.keys():
#
#                         if str(key) in check_box_list:
#                             #print('*********************************', data_dict[key])
#                             annotation.update(
#                                     pdfrw.PdfDict(V=pdfrw.PdfName(
#                                         strcon(data_dict[key])), AS=pdfrw.PdfName(strcon(data_dict[key])))
#                             )
#                         else:
#                             annotation.update(pdfrw.PdfDict(V='{}'.format(data_dict[key])))
#
#
#     #     pdfrw.PdfDict(AP=data_dict[key], V=data_dict[key])
#         pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

def get_data_csv(dict_data):
    
    dict_data['legal_resource_xref'] = ''
    if dict_data['Case Number']:
        df = pd.read_excel(open_i140_resource_path)
        list_h = df.columns.tolist()
        total_rows = len(df)
        for index, row in df.iterrows():
            #print(row['Underlying PERM DOL Case Number'].strip(), str(dict_data['Case Number']).strip())
            if str(row['Underlying PERM DOL Case Number']).strip() ==  str(dict_data['Case Number']).strip():
                #print(index, 'index')
                organization_xref = ''
                if "Organization Xref" in row and row["Organization Xref"]:
                    organization_xref = str(row["Organization Xref"]).strip()
                
                organization_name = ''
                if "Organization Name" in row and row["Organization Name"]:
                    organization_name = str(row["Organization Name"]).strip()

                petitioner_xref = ''
                if "Petitioner Xref" in row and row["Petitioner Xref"]:
                    petitioner_xref = str(row["Petitioner Xref"]).strip()
                
                petitioner_name = ''
                if "Petitioner Name" in row and row["Petitioner Name"]:
                    petitioner_name = str(row["Petitioner Name"]).strip()

                dict_data['organization_xref'] = organization_xref
                dict_data['organization_name'] = organization_name
                dict_data['petitioner_xref'] = petitioner_xref
                dict_data['petitioner_name'] = petitioner_name
                dict_data['Case Xref'] = row["Case Id"]

                if "Petitioner Authorized Signatory Last Name" in row and row["Petitioner Authorized Signatory Last Name"]:
                    dict_data['Contact Last Name'] = str(row["Petitioner Authorized Signatory Last Name"]).strip()
                if "Petitioner Authorized Signatory First Name" in row and row["Petitioner Authorized Signatory First Name"]:
                    dict_data['Contact First Name'] = str(row["Petitioner Authorized Signatory First Name"]).strip()
                if "Petitioner Authorized Signatory Middle Name" in row and row["Petitioner Authorized Signatory Middle Name"]:
                    dict_data['Contact Middle Name'] = str(row["Petitioner Authorized Signatory Middle Name"]).strip()
                
                if "Petitioner Name" in row and row["Petitioner Name"]:
                    dict_data['Employer Name'] = str(row["Petitioner Name"]).strip()
                if "Petitioner Authorized Signatory Address 1" in row and row["Petitioner Authorized Signatory Address 1"]:
                    dict_data['Contact Address1'] = str(row["Petitioner Authorized Signatory Address 1"]).strip()
                #
                if "Petitioner Authorized Signatory  Address Type" in row and row["Petitioner Authorized Signatory  Address Type"]:
                    dict_data['Contact Address Type'] = str(row["Petitioner Authorized Signatory  Address Type"]).strip()
                if "Petitioner Authorized Signatory Address Type Number" in row and row["Petitioner Authorized Signatory Address Type Number"]:
                    dict_data['Contact Address2'] = str(row["Petitioner Authorized Signatory Address Type Number"]).strip()
                if "Petitioner Authorized Signatory City" in row and row["Petitioner Authorized Signatory City"]:
                    dict_data['Contact City'] = str(row["Petitioner Authorized Signatory City"]).strip()
                if "Petitioner Authorized Signatory  State" in row and row["Petitioner Authorized Signatory  State"]:
                    dict_data['Contact State'] = str(row["Petitioner Authorized Signatory  State"]).strip()
                if "Petitioner Authorized Signatory Zip Code" in row and row["Petitioner Authorized Signatory Zip Code"]:
                    dict_data['Contact Postal Code'] = str(row["Petitioner Authorized Signatory Zip Code"]).strip()
                if "Petitioner Authorized Signatory Country" in row and row["Petitioner Authorized Signatory Country"]:
                    dict_data['Contact Country'] = str(row["Petitioner Authorized Signatory Country"]).strip()
                if "Petition FEIN" in row and row["Petition FEIN"]:
                    dict_data['FEIN No'] = str(row["Petition FEIN"]).strip()
                #
                if "Case Priority Category" in row and row["Case Priority Category"]:
                    dict_data['Case Priority Category'] = str(row["Case Priority Category"]).strip()

                if "Beneficiary Xref" in row and row["Beneficiary Xref"]:
                    dict_data['beneficiary_xref'] = str(row["Beneficiary Xref"]).strip()
                if "Beneficiary Last Name" in row and row["Beneficiary Last Name"]:
                    dict_data['Alien Last Name'] = str(row["Beneficiary Last Name"]).strip()
                if "Beneficiary First Name" in row and row["Beneficiary First Name"]:
                    dict_data['Alien First Name'] = str(row["Beneficiary First Name"]).strip()
                if "Beneficiary Middle Name" in row and row["Beneficiary Middle Name"]:
                    dict_data['Alien Middle Name'] = str(row["Beneficiary Middle Name"]).strip()
                if "Current Residence Address 1" in row and row["Current Residence Address 1"]:
                    dict_data['Alien Address1'] = str(row["Current Residence Address 1"]).strip()
                if "Current Residence Address Type Number" in row and row["Current Residence Address Type Number"]:
                    dict_data['Alien Address2'] = str(row["Current Residence Address Type Number"]).strip()
                if "Current Residence Address City" in row and row["Current Residence Address City"]:
                    dict_data['Alien City'] = str(row["Current Residence Address City"]).strip()
                if "Current Residence Address State" in row and row["Current Residence Address State"]:
                    dict_data['Alien State'] = str(row["Current Residence Address State"]).strip()
                if "Current Residence Address Zip Code" in row and row["Current Residence Address Zip Code"]:
                    dict_data['Alien Postal Code'] = str(row["Current Residence Address Zip Code"]).strip()
                if "Current Residence Address Country" in row and row["Current Residence Address Country"]:
                    dict_data['Alien Country'] = str(row["Current Residence Address Country"]).strip()
                if "Date of Birth" in row and row["Date of Birth"]:
                    dict_data['Alien DOB'] = str(row["Date of Birth"]).strip()
                    if '/' in dict_data["Alien DOB"] and dict_data["Alien DOB"].count('/') != 2 :
                        alien_dob = dict_data["Alien DOB"].replace("/","")
                        alien_dob = str(alien_dob[0:2])+'/'+str(alien_dob[2:4])+'/'+str(alien_dob[4:])
                        dict_data["Alien DOB"] = alien_dob
                #
                if "City of Birth" in row and row["City of Birth"]:
                    dict_data['City of Birth'] = str(row["City of Birth"]).strip()
                if "Country of Birth" in row and row["Country of Birth"]:
                    dict_data['Country of Birth'] = str(row["Country of Birth"]).strip()
                #
                if "State of Birth" in row and row["State of Birth"]:
                    dict_data['State of Birth'] = str(row["State of Birth"]).strip()
                if "Country of Citizenship" in row and row["Country of Citizenship"]:
                    dict_data['Country of Citizenship'] = str(row["Country of Citizenship"]).strip()
                if "Alien Number" in row and row["Alien Number"]:
                    dict_data['Alien Registration No'] = str(row["Alien Number"]).strip()
                
                ##
                if "SSN" in row and row["SSN"]:
                    dict_data['SSN Number'] = str(row["SSN"]).strip()
                if "I-94 Entry Date" in row and row["I-94 Entry Date"]:
                    dict_data['I-94 Entry Date'] = str(row["I-94 Entry Date"]).strip()
                if "Immigration Status Expiration Date (I-94)" in row and row["Immigration Status Expiration Date (I-94)"]:
                    dict_data['Immigration Status Expiration Date (I-94)'] = str(row["Immigration Status Expiration Date (I-94)"]).strip()
                if "I-94 Number" in row and row["I-94 Number"]:
                    dict_data['I-94 Number'] = str(row["I-94 Number"]).strip()
                if "Current Immigration Status (I-94)" in row and row["Current Immigration Status (I-94)"]:
                    dict_data['Immigration Status (I-94)'] = str(row["Current Immigration Status (I-94)"]).strip()
                if "Passport Number" in row and row["Passport Number"]:
                    dict_data['Passport Number'] = str(row["Passport Number"]).strip()
                if "Passport Issuing Country" in row and row["Passport Issuing Country"]:
                    dict_data['Passport Issuing Country'] = str(row["Passport Issuing Country"]).strip()
                if "Passport Expiration Date" in row and row["Passport Expiration Date"]:
                    dict_data['Passport Expiration Date'] = str(row["Passport Expiration Date"]).strip()
                if "Last Country of Permanent Residence Abroad" in row and row["Last Country of Permanent Residence Abroad"]:
                    dict_data['Last Country of Permanent Residence Abroad'] = str(row["Last Country of Permanent Residence Abroad"]).strip()
                if "Foreign Residence Address 1" in row and row["Foreign Residence Address 1"]:
                    dict_data['Foreign Residence Address 1'] = str(row["Foreign Residence Address 1"]).strip()
                #
                if "Foreign Residence Address Type" in row and row["Foreign Residence Address Type"]:
                    dict_data['Foreign Residence Address Type'] = str(row["Foreign Residence Address Type"]).strip()
                if "Foreign Residence Address Type Number" in row and row["Foreign Residence Address Type Number"]:
                    dict_data['Foreign Residence Address Type Number'] = str(row["Foreign Residence Address Type Number"]).strip()
                if "Foreign Residence Address City" in row and row["Foreign Residence Address City"]:
                    dict_data['Foreign Residence Address City'] = str(row["Foreign Residence Address City"]).strip()
                if "Foreign Residence Address State" in row and row["Foreign Residence Address State"]:
                    dict_data['Foreign Residence Address State'] = str(row["Foreign Residence Address State"]).strip()
                if "Foreign Residence Address Zip Code" in row and row["Foreign Residence Address Zip Code"]:
                    dict_data['Foreign Residence Address Zip Code'] = str(row["Foreign Residence Address Zip Code"]).strip()
                if "Foreign Residence Address Country" in row and row["Foreign Residence Address Country"]:
                    dict_data['Foreign Residence Address Country'] = str(row["Foreign Residence Address Country"]).strip()
                if "Current Residence Address 1" in row and row["Current Residence Address 1"]:
                    dict_data['Alien Address1'] = str(row["Current Residence Address 1"]).strip()
                #
                if "Current Residence Address Type" in row and row["Current Residence Address Type"]:
                    dict_data['Current Residence Address Type'] = str(row["Current Residence Address Type"]).strip()
                if "Current Residence Address Type Number" in row and row["Current Residence Address Type Number"]:
                    dict_data['Alien Address2'] = str(row["Current Residence Address Type Number"]).strip()
                if "Current Residence Address City" in row and row["Current Residence Address City"]:
                    dict_data['Alien City'] = str(row["Current Residence Address City"]).strip()
                if "Current Residence Address State" in row and row["Current Residence Address State"]:
                    dict_data['Alien State'] = str(row["Current Residence Address State"]).strip()
                if "Current Residence Address Zip Code" in row and row["Current Residence Address Zip Code"]:
                    dict_data['Alien Postal Code'] = str(row["Current Residence Address Zip Code"]).strip()
                if "Current Residence Address Country" in row and row["Current Residence Address Country"]:
                    dict_data['Alien Country'] = str(row["Current Residence Address Country"]).strip()
                #
                if "Petitioner Business Type" in row and row["Petitioner Business Type"]:
                    dict_data['Petitioner Business Type'] = (str(row["Petitioner Business Type"]).strip())
                if "Petitioner Year Established" in row and row["Petitioner Year Established"]:
                    dict_data['Year of Commenced Business'] = (str(row["Petitioner Year Established"]).strip()).split('.')[0]
                if "Petitioner Number of Employees" in row and row["Petitioner Number of Employees"]:
                    dict_data['No of Employees'] = (str(row["Petitioner Number of Employees"]).strip()).split('.')[0]
                ##
                if "Petitioner Gross Income" in row and row["Petitioner Gross Income"]:
                    dict_data['Petitioner Gross Income'] = str(row["Petitioner Gross Income"]).strip()
                if "Petitioner Net Income" in row and row["Petitioner Net Income"]:
                    dict_data['Petitioner Net Income'] = str(row["Petitioner Net Income"]).strip()
                if "Petitioner Authorized Signatory Job Title" in row and row["Petitioner Authorized Signatory Job Title"]:
                    dict_data['Petitioner Authorized Signatory Job Title'] = str(row["Petitioner Authorized Signatory Job Title"]).strip()
                if "Petitioner Authorized Signatory Phone Number" in row and row["Petitioner Authorized Signatory Phone Number"]:
                    dict_data['Petitioner Authorized Signatory Phone Number'] = str(row["Petitioner Authorized Signatory Phone Number"]).strip()
                if "Petitioner Authorized Signatory Phone Number Extension" in row and row["Petitioner Authorized Signatory Phone Number Extension"]:
                    dict_data['Petitioner Authorized Signatory Phone Number Extension'] = str(row["Petitioner Authorized Signatory Phone Number Extension"]).strip()
                if "Petitioner Authorized Signatory Mobile Number" in row and row["Petitioner Authorized Signatory Mobile Number"]:
                    dict_data['Petitioner Authorized Signatory Mobile Number'] = str(row["Petitioner Authorized Signatory Mobile Number"]).strip()
                if "Petitioner Authorized Signatory Email" in row and row["Petitioner Authorized Signatory Email"]:
                    dict_data['Petitioner Authorized Signatory Email'] = str(row["Petitioner Authorized Signatory Email"]).strip()

                #Legal Resource
                if "Primary Attorney Employee Id" in row and row["Primary Attorney Employee Id"]:
                    dict_data['Employee Id'] = (str(row["Primary Attorney Employee Id"]).strip()).split('.')[0]
                    df2 = pd.read_excel(legal_resource_path)
                    for index2, row2 in df2.iterrows():
                        #print(str(row2['Employee Id']).strip(), dict_data['Employee Id'])
                        if str(row2['Employee Id']).strip() ==  str(dict_data['Employee Id']):
                            #print('index2', index2)
                            dict_data['Legal Resource Xref'] = str(row2['Legal Resource Xref']).strip()
                            
                            if "Last Name" in row2 and row2["Last Name"]:
                                dict_data['Last Name'] = str(row2["Last Name"]).strip()
                            if "First Name" in row2 and row2["First Name"]:
                                dict_data['First Name'] = str(row2["First Name"]).strip()
                            if "Middle Name" in row2 and row2["Middle Name"]:
                                dict_data['Middle Name'] = str(row2["Middle Name"]).strip()
                            if "Middle Name" in row2 and row2["Middle Name"]:
                                dict_data['Middle Name'] = str(row2["Middle Name"]).strip()
                            if "Address 1" in row2 and row2["Middle Name"]:
                                dict_data['Address 1'] = str(row2["Address 1"]).strip()
                            if "Address Type" in row2 and row2["Address Type"]:
                                dict_data['Address Type'] = str(row2["Address Type"]).strip()
                            if "Address Type Number" in row2 and row2["Address Type Number"]:
                                dict_data['Address Type Number'] = str(row2["Address Type Number"]).strip()
                            if "City" in row2 and row2["City"]:
                                dict_data['City'] = str(row2["City"]).strip()
                            if "State" in row2 and row2["State"]:
                                dict_data['State'] = str(row2["State"]).strip()
                            if "Zip Code" in row2 and row2["Zip Code"]:
                                dict_data['Zip Code'] = str(row2["Zip Code"]).strip()
                            if "Country" in row2 and row2["Country"]:
                                dict_data['Country'] = str(row2["Country"]).strip()
                            if "Phone Number" in row2 and row2["Phone Number"]:
                                dict_data['Phone Number'] = str(row2["Phone Number"]).strip()
                            if "Phone Number Extn." in row2 and row2["Phone Number Extn."] and row2["Phone Number Extn."] != 'nan':
                                dict_data['Phone Number Extn.'] = str(row2["Phone Number Extn."]).strip()
                            if "Mobile Phone" in row2 and row2["Mobile Phone"]:
                                dict_data['Mobile Phone'] = str(row2["Mobile Phone"]).strip()
                            if "Email" in row2 and row2["Email"]:
                                dict_data['Email'] = str(row2["Email"]).strip()
                            if "Fax" in row2 and row2["Fax"]:
                                dict_data['Fax'] = str(row2["Fax"]).strip()
                            if "Licensing Authority" in row2 and row2["Licensing Authority"]:
                                dict_data['Licensing Authority'] = str(row2["Licensing Authority"]).strip()
                            if "Bar Number" in row2 and row2["Bar Number"]:
                                dict_data['Bar Number'] = str(row2["Bar Number"]).strip()
                            if "Firm Name" in row2 and row2["Firm Name"]:
                                dict_data['Firm Name'] = str(row2["Firm Name"]).strip()
                            
                            break
                        
                
                
                break


    return dict_data            
                
def pdf_merge_sequence(data_dict, output_pdf_path, output_pdf_path_g28, source_filepath):

    chk_by = None
    folder_name = None
    if data_dict['organization_xref'] and data_dict['organization_name']:
        folder_name = str(data_dict['organization_xref'])+' - '+str(data_dict['organization_name'])
        chk_by = "Organization"

    if folder_name is None:
        if data_dict['petitioner_xref'] and data_dict['petitioner_name']:
            folder_name = str(data_dict['petitioner_xref'])+' - '+str(data_dict['petitioner_name'])
            chk_by = "Petitioner"
    
    os.chdir(cwd)
    if os.path.exists(os.path.join('ImmiLytics', folder_name)):
        folder_path = os.path.join('ImmiLytics', folder_name)
        if chk_by =="Organization":
            if data_dict['petitioner_xref'] and data_dict['petitioner_name']:
                folder_name2 = str(data_dict['petitioner_xref'])+' - '+str(data_dict['petitioner_name'])
                folder_path2 = os.path.join(folder_path, folder_name2)
        else:
            folder_path2 = folder_path
    
    beneficiary_xref = ''
    beneficiary_lname = ''
    beneficiary_fname = ''
    beneficiary_name = ''
    folder_name4 = ''
    folder_path4 = ''
    beneficiary_xref = data_dict['beneficiary_xref']
    beneficiary_lname = str(data_dict["Alien Last Name"]).strip()
    beneficiary_fname = str(data_dict["Alien First Name"]).strip()
    
    #print(folder_path2)
    beneficiary_name = str(beneficiary_xref)+' - '+beneficiary_lname+', '+beneficiary_fname
    if folder_path2:
        if os.path.exists(os.path.join(folder_path2, beneficiary_name)):
            folder_name3 = beneficiary_name
            folder_path3 = os.path.join(folder_path2, folder_name3)
    
    #print(folder_path3)
    #print(os.path.join(folder_path3, "Supporting Docs"))
    if folder_path3:
        if os.path.exists(os.path.join(folder_path3, "Supporting Docs")):
            folder_path4 = os.path.join(folder_path3, "Supporting Docs")

    print(folder_path4)
    pdfs = []
    if folder_path4:
        os.chdir(folder_path4)
        sequence = ["Masters Degree", "Masters Transcripts", "Bachelors Degree", "Bachelors Transcripts",
        "EVL", "Additional Supporting Docs", "Misc. Docs", "Passport", "I-94", "Pay Stub", "PR Sponsorship Letter"]

        sequence_multiple = ["Additional Supporting Docs", "Misc. Docs", "Pay Stubs"]
        pdf_files = glob.glob("*.pdf")
        
        pdfs.append(output_pdf_path_g28)
        pdfs.append(output_pdf_path)
        pdfs.append(source_filepath)
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
        pdfdocs(pdfs, folder_path3)
        '''merger = PdfFileMerger()

        for pdf in pdfs:
            merger.append(pdf)

        os.chdir(cwd) 
        merger.append(output_pdf_path)
        merger.append(output_pdf_path_g28)
        merger.write("final.pdf")
        merger.close()'''


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


def get_form_filepath(data_dict):

    chk_by = None
    folder_name = None
    if data_dict['organization_xref'] and data_dict['organization_name']:
        folder_name = str(data_dict['organization_xref'])+' - '+str(data_dict['organization_name'])
        chk_by = "Organization"

    if folder_name is None:
        if data_dict['petitioner_xref'] and data_dict['petitioner_name']:
            folder_name = str(data_dict['petitioner_xref'])+' - '+str(data_dict['petitioner_name'])
            chk_by = "Petitioner"
    
    os.chdir(cwd)
    if os.path.exists(os.path.join('ImmiLytics', folder_name)):
        folder_path = os.path.join('ImmiLytics', folder_name)
        if chk_by =="Organization":
            if data_dict['petitioner_xref'] and data_dict['petitioner_name']:
                folder_name2 = str(data_dict['petitioner_xref'])+' - '+str(data_dict['petitioner_name'])
                folder_path2 = os.path.join(folder_path, folder_name2)
        else:
            folder_path2 = folder_path
    
    beneficiary_xref = ''
    beneficiary_lname = ''
    beneficiary_fname = ''
    beneficiary_name = ''
    folder_name3 = ''
    folder_path3 = ''
    beneficiary_xref = data_dict['beneficiary_xref']
    beneficiary_lname = str(data_dict["Alien Last Name"]).strip()
    beneficiary_fname = str(data_dict["Alien First Name"]).strip()
    
    #print(folder_path2)
    beneficiary_name = str(beneficiary_xref)+' - '+beneficiary_lname+', '+beneficiary_fname
    if folder_path2:
        if os.path.exists(os.path.join(folder_path2, beneficiary_name)):
            folder_name3 = beneficiary_name
            folder_path3 = os.path.join(folder_path2, folder_name3)
    
    return folder_path3

    
if __name__ == '__main__':
    initf()