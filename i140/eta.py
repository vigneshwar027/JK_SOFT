import os
import sys, fitz
import pandas as pd
import csv 
import re
import pdfrw
import shutil
import pyodbc

cwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(cwd)


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=localhost;'
                      'Database=immilyticsi140;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
#print('connection made')


def process_to_db(dict_data):
    results = cursor.execute("SELECT * FROM dbo.CaseETA9089 where PERMDOLCaseNumber='{}' ".format(dict_data['Case Number'])).fetchall()
    length = len(results)
    if length <= 0:
        cursor.execute("INSERT INTO dbo.CaseETA9089  VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format
                       (
                        dict_data['Case Number'],
                        dict_data['Filing Date'],
                        dict_data['Signed Date'],
                        dict_data['Certificate Valid From'],
                        dict_data['Certificate Valid To'],
                        dict_data['Contact First Name'],
                        dict_data[ 'Contact Address1'],
                        dict_data[ 'Contact Address2'],
                        dict_data[ 'Contact City'],
                        dict_data[ 'Contact State'],
                        dict_data[ 'Contact Postal Code'],
                        dict_data[ 'Contact Country'],
                        dict_data[ 'Contact Phone'],
                        dict_data['Contact Phoneext'],
                        dict_data[ 'No of Employees'],
                        dict_data[ 'Year of Commenced Businees'],
                        dict_data[ 'FEIN No'],
                        dict_data[ 'NAICS Code'],
                        dict_data[ 'Contact Last Name'],
                        dict_data[ 'Contact First Name'],
                        dict_data[ 'Contact Middle Name'],
                        dict_data[ 'Contact Address1'],
                        dict_data[ 'Contact Address2'],
                        dict_data[ 'Contact City'],
                        dict_data[ 'Contact State'],
                        dict_data[ 'Contact Postal Code'],
                        dict_data[ 'Contact Country'],
                        dict_data[ 'Contact Phone'],
                        dict_data['Contact Phoneext'],
                        dict_data[ 'Contact Email'],
                        dict_data[ 'Agent Last Name'],
                        dict_data[ 'Agent First Name'],
                        dict_data[ 'Agent Middle Name'],
                        dict_data[ 'Agent Firmname'],
                        dict_data[ 'Agent Firmein'],
                        dict_data[ 'Agent Address1'],
                        dict_data[ 'Agent Address2'],
                        dict_data['Agent City'],
                        dict_data[ 'Agent State'],
                        dict_data[ 'Agent Postal Code'],
                        dict_data[ 'Agent Country'],
                        dict_data[ 'Agent Phone'],
                        dict_data[ 'Agent Phoneext'],
                        dict_data[ 'Agent Email'],
                        dict_data[ 'SOC'],
                        dict_data[ 'Job Title'],
                        dict_data[ 'Job Duties'],
                        dict_data['Primary Worksite'],
                        dict_data[ 'Job Address2'],
                        dict_data[ 'Job City'],
                        dict_data['Job State'],
                        dict_data[ 'Job Postal Code'],
                        dict_data['Wage From'],
                        dict_data['Wage To'],
                        dict_data[ 'Wage Per'],
                        dict_data[ 'Alien Last Name'],
                        dict_data[ 'Alien First Name'],
                        dict_data[ 'Alien Middle Name'],
                        dict_data[ 'Alien Address1'],
                        dict_data['Alien Address2'],
                        dict_data['Agent City'],
                        dict_data[ 'Alien State'],
                        dict_data[ 'Alien Postal Code'],
                        dict_data[ 'Alien Country'],
                        dict_data['Alien DOB'],
                        dict_data['Country of Birth'],
                        dict_data[ 'Country of Citizenship'],
                        dict_data[ 'Alien Registration No'],
                        dict_data[ 'Alien Classofadm'],
                        dict_data['Alien Admission No']))
        cursor.commit()
    else:
        cursor.execute("UPDATE dbo.CaseETA9089 SET PERMFilingDate = '{}', PERMCertificationDate = '{}',\
        PERMValidFrom = '{}',\
        PERMValidTo = '{}', \
        PetitionerName = '{}', \
        PetitionerAddress1 = '{}', \
        PetitionerAddress2 = '{}', \
        PetitionerCity = '{}', \
        PetitionerState = '{}', \
        PetitionerZipCode = '{}', \
        PetitionerCountry = '{}', \
        PetitionerPhone = '{}', \
        PetitionerPhoneExt = '{}', \
        NumberOfEmployees = '{}',\
        YearCommencedBusiness = '{}', \
        FEIN = '{}', \
        NAICSCode = '{}',\
        PetitionerContactLastName = '{}', \
        PetitionerContactFirstName = '{}', \
        PetitionerContactMiddleInitial = '{}', \
        PetitionerContactAddress1 = '{}', \
        PetitonerContactAddress2 = '{}', \
        PetitionerContactCity = '{}', \
        PetitionerContactState = '{}', \
        PetitionerContactZipCode = '{}', \
        PetitionerContactCountry = '{}', \
        PetitionerContactPhoneNumber = '{}', \
        PetitionerContactPhoneExt = '{}', \
        PetitionerContactEmail = '{}', \
        AttorneyAgentLastName = '{}', \
        AttorneyAgentFirstName = '{}', \
        AttorneyAgentMiddleInitial = '{}', \
        AttorneyAgentFirmName = '{}', \
        AttorneyAgentFirmFEIN = '{}', \
        AttorneyAgentAddress1 = '{}', \
        AttorneyAgentAddress2 = '{}', \
        AttorneyAgentCity = '{}', \
        AttorneyAgentState = '{}', \
        AttorneyAgentZipCode = '{}', \
        AttorneyAgentCountry = '{}', \
        AttorneyAgentPhoneNumber = '{}', \
        AttorneyAgentPhoneExt = '{}', \
        AttorneyAgentEmail = '{}', \
        SOCCODE = '{}', \
        JobTitle = '{}', \
        JobDuties = '{}', \
        WorkLocationAddress1 = '{}', \
        WorkLocationAddress2 = '{}', \
        WorkLocationCity = '{}', \
        WorkLocationState = '{}', \
        WorkLocationZipCode = '{}', \
        OfferedWageFrom = '{}',\
        OfferedWageTo = '{}',\
        OfferedWageType = '{}',\
        BeneficiaryLastName = '{}',\
        BeneficiaryFirstName = '{}',\
        BeneficiaryMiddleName = '{}',\
        BeneficiaryAddress1 = '{}',\
        BeneficiaryAddress2 = '{}',\
        BeneficiaryAddressCity = '{}',\
        BeneficiaryAddressState = '{}',\
        BeneficiaryAddressZipCode = '{}',\
        BeneficiaryAddressCountry = '{}',\
        BeneficiaryDateofBirth = '{}',\
        BeneficiaryCountryofBirth = '{}',\
        BeneficiaryCountryofCitizenship = '{}',\
        BeneficiaryAlienNumber = '{}',\
        BeneficiaryClassofAdmission = '{}',\
        BeneficiaryI94Number = '{}' WHERE PERMDOLCaseNumber = '{}'".format(dict_data['Filing Date'],
            dict_data['Signed Date'],
            dict_data['Certificate Valid From'],
            dict_data['Certificate Valid To'],
            dict_data['Contact First Name'],
            dict_data[ 'Contact Address1'],
            dict_data[ 'Contact Address2'],
            dict_data[ 'Contact City'],
            dict_data[ 'Contact State'],
            dict_data[ 'Contact Postal Code'],
            dict_data[ 'Contact Country'],
            dict_data[ 'Contact Phone'],
            dict_data['Contact Phoneext'],
            dict_data[ 'No of Employees'],
            dict_data[ 'Year of Commenced Businees'],
            dict_data[ 'FEIN No'],
            dict_data[ 'NAICS Code'],
            dict_data[ 'Contact Last Name'],
            dict_data[ 'Contact First Name'],
            dict_data[ 'Contact Middle Name'],
            dict_data[ 'Contact Address1'],
            dict_data[ 'Contact Address2'],
            dict_data[ 'Contact City'],
            dict_data[ 'Contact State'],
            dict_data[ 'Contact Postal Code'],
            dict_data[ 'Contact Country'],
            dict_data[ 'Contact Phone'],
            dict_data['Contact Phoneext'],
            dict_data[ 'Contact Email'],
            dict_data[ 'Agent Last Name'],
            dict_data[ 'Agent First Name'],
            dict_data[ 'Agent Middle Name'],
            dict_data[ 'Agent Firmname'],
            dict_data[ 'Agent Firmein'],
            dict_data[ 'Agent Address1'],
            dict_data[ 'Agent Address2'],
            dict_data['Agent City'],
            dict_data[ 'Agent State'],
            dict_data[ 'Agent Postal Code'],
            dict_data[ 'Agent Country'],
            dict_data[ 'Agent Phone'],
            dict_data[ 'Agent Phoneext'],
            dict_data[ 'Agent Email'],
            dict_data[ 'SOC'],
            dict_data[ 'Job Title'],
            dict_data[ 'Job Duties'],
            dict_data['Primary Worksite'],
            dict_data[ 'Job Address2'],
            dict_data[ 'Job City'],
            dict_data['Job State'],
            dict_data[ 'Job Postal Code'],
            dict_data['Wage From'],
            dict_data['Wage To'],
            dict_data[ 'Wage Per'],
            dict_data[ 'Alien Last Name'],
            dict_data[ 'Alien First Name'],
            dict_data[ 'Alien Middle Name'],
            dict_data[ 'Alien Address1'],
            dict_data['Alien Address2'],
            dict_data['Agent City'],
            dict_data[ 'Alien State'],
            dict_data[ 'Alien Postal Code'],
            dict_data[ 'Alien Country'],
            dict_data['Alien DOB'],
            dict_data['Country of Birth'],
            dict_data[ 'Country of Citizenship'],
            dict_data[ 'Alien Registration No'],
            dict_data[ 'Alien Classofadm'],
            dict_data['Alien Admission No'], 
            dict_data['Case Number']))

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
    source_dir = os.path.join(cwd, 'ImmiLytics\Certified PERMs')
    file_names = os.listdir(source_dir)
    
    for file_name in file_names:
        print('Processing - '+file_name)
        dict_data = get_data(os.path.join(source_dir,file_name))
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
        data_dict = {
            'Pt1Line1a_LastName': dict_data['Contact Last Name'] if 'Contact Last Name' in dict_data else '',
            'form1[0].#subform[0].Pt1Line1b_GivenName[0]': dict_data['Contact First Name'] if 'Contact First Name' in dict_data else '',
            'form1[0].#subform[0].Pt1Line1c_MiddleName[0]': dict_data['Contact Middle Name'] if 'Contact Middle Name' in dict_data else '',
            'form1[0].#subform[0].Line2_CompanyName[0]':dict_data['Employer Name'] if 'Employer Name' in dict_data else '',
            'form1[0].#subform[0].Line6a_InCareofName[0]': full_name,
            'form1[0].#subform[0].Line6b_StreetNumberName[0]':dict_data['Contact Address1'] if 'Contact Address1' in dict_data else '',
            'form1[0].#subform[0].Line6c_AptSteFlrNumber[0]':dict_data['Contact Address2'] if 'Contact Address2' in dict_data else '',
            'form1[0].#subform[0].Line6d_CityOrTown[0]':dict_data['Contact City'] if 'Contact City' in dict_data else '',
            'form1[0].#subform[0].Line6e_State[0]': dict_data['Contact State'] if 'Contact State' in dict_data else '',
            'form1[0].#subform[0].Line6f_ZipCode[0]': dict_data['Contact Postal Code'] if 'Contact Postal Code' in dict_data else '',
            'form1[0].#subform[0].Line6i_Country[0]': dict_data['Contact Country'] if 'Contact Country' in dict_data else '',
            'form1[0].#subform[0].Pt1Line3_TaxNumber[0]': dict_data['FEIN No'] if 'FEIN No' in dict_data else '',
            'form1[0].#subform[1].Pt3Line1a_FamilyName[0]': dict_data['Alien Last Name'] if 'Alien Last Name' in dict_data else '',
            'form1[0].#subform[1].Pt3Line1b_GivenName[0]': dict_data['Alien First Name'] if 'Alien First Name' in dict_data else '',
            'form1[0].#subform[1].Pt3Line1c_MiddleName[0]': dict_data['Alien Middle Name'] if 'Alien Middle Name' in dict_data else '',
            'form1[0].#subform[1].Line2a_InCareofName[0]': alien_full_name,
            'form1[0].#subform[1].Line2b_StreetNumberName[0]': dict_data['Alien Address1'] if 'Alien Address1' in dict_data else '',
            'form1[0].#subform[1].Line2c_AptSteFlrNumber[0]':dict_data['Alien Address2'] if 'Alien Address2' in dict_data else '',
            'form1[0].#subform[1].Line2d_CityOrTown[0]':dict_data['Alien City'] if 'Alien City' in dict_data else '',
            'form1[0].#subform[1].Line2e_State[0]':dict_data['Alien State'] if 'Alien State' in dict_data else '',
            'form1[0].#subform[1].Line2f_ZipCode[0]':dict_data['Alien Postal Code'] if 'Alien Postal Code' in dict_data else '',
            'form1[0].#subform[1].Line2i_Country[0]':dict_data['Alien Country'] if 'Alien Country' in dict_data else '',
            'form1[0].#subform[1].Line5_DateOfBirth[0]':dict_data['Alien DOB'] if 'Alien DOB' in dict_data else '',
            'form1[0].#subform[1].Line8_Country[0]':dict_data['Country of Birth'] if 'Country of Birth' in dict_data else '',
            'form1[0].#subform[1].Line9_Country[0]':dict_data['Country of Citizenship'] if 'Country of Citizenship' in dict_data else '',
            'form1[0].#subform[1].Line11_Alien[0].Pt3Line8_AlienNumber[0]':dict_data['Alien Registration No'] if 'Alien Registration No' in dict_data else '',
            'form1[0].#subform[2].Line2a_InCareofName[1]':alien_full_name2,
            'form1[0].#subform[2].Line3d_StreetNumberName[0]': dict_data['Alien Address1'] if 'Alien Address1' in dict_data else '',
            'form1[0].#subform[2].Line3e_AptSteFlrNumber[0]': dict_data['Alien Address2'] if 'Alien Address2' in dict_data else '',
            'form1[0].#subform[2].Line3f_CityOrTown[0]': dict_data['Alien City'] if 'Alien City' in dict_data else '',
            'form1[0].#subform[2].Line3h_Province[0]': dict_data['Alien State'] if 'Alien State' in dict_data else '',
            'form1[0].#subform[2].Line3g_PostalCode[0]': dict_data['Alien Postal Code'] if 'Alien Postal Code' in dict_data else '',
            'form1[0].#subform[2].Line3i_Country[0]': dict_data['Alien Country'] if 'Alien Country' in dict_data else '',
            #'form1[0].#subform[2].Line7_No[0]':'N',
            #'form1[0].#subform[2].Line8_No[0]':'N',
            #'form1[0].#subform[2].Line1a_Employer[0]':'Y',
            'form1[0].#subform[2].Line2b_DateEstablished[0]': dict_data['Year of Commenced Businees'] if 'Year of Commenced Businees' in dict_data else '',
            'form1[0].#subform[2].Line2c_NumberofEmployees[0]': dict_data['No of Employees'] if 'No of Employees' in dict_data else '',
            'form1[0].#subform[2].Line2f[0].Line2f_NAICSCode[0]': dict_data['NAICS Code'] if 'NAICS Code' in dict_data else '',
            'form1[0].#subform[2].Line2g_LaborCertification[0]':dict_data['Case Number'] if 'Case Number' in dict_data else '',
            'form1[0].#subform[3].Line2h_LaborCertification[0]': dict_data['Filing Date'] if 'Filing Date' in dict_data else '',
            'form1[0].#subform[3].Line2i_LaborCertificationDate[0]': dict_data['Certificate Valid To'] if 'Certificate Valid To' in dict_data else '',
            'form1[0].#subform[3].Line1_JobTitle[0]': dict_data['Job Title'] if 'Job Title' in dict_data else '',
            'form1[0].#subform[3].Line2_SOCCode1[0]': SOC_code[0] if len(SOC_code) >= 1 else '',
            'form1[0].#subform[3].Line2_SOCCode2[0]': SOC_code[1] if len(SOC_code) >= 2 else '',
            'form1[0].#subform[3].Line8_Wages[0]':dict_data['Wage'] if 'Wage' in dict_data else '',
            'form1[0].#subform[3].Line8_Per[0]':dict_data['Wage Per'] if 'Wage Per' in dict_data else '',
            'form1[0].#subform[3].Line9a_StreetNumberName[0]': dict_data['Primary Worksite'] if 'Primary Worksite' in dict_data else '',
            'form1[0].#subform[3].Line9b_AptSteFlrNumber[0]':dict_data['Job Address2'] if 'Job Address2' in dict_data else '',
            'form1[0].#subform[3].Line9c_CityOrTown[0]': dict_data['Job City'] if 'Job City' in dict_data else '',
            'form1[0].#subform[3].Line9d_State[0]': dict_data['Job State'] if 'Job State' in dict_data else '',
            'form1[0].#subform[3].Line9e_ZipCode[0]':dict_data['Job Postal Code'] if 'Job Postal Code' in dict_data else '',
            
            }
        #write_fillable_pdf(INVOICE_TEMPLATE_PATH, output_pdf_path, data_dict)
        #shutil.move(os.path.join(source_dir, file_name), os.path.join(processed_dir, file_name))
        #print(data_dict)
    cursor.commit()
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
            
            employer_list_index = [index for index, string in enumerate(text_data) if "Employer’s name" in string]
            employer_data = text_data[int(employer_list_index[0])+1]
            data_dict["Employer Name"] = employer_data
            
            employer_address1_index = [index for index, string in enumerate(text_data[int(employer_list_index[0]):]) if "2. Address 1" in string]
            employer_address1_data = text_data[int(employer_list_index[0])+int(employer_address1_index[0])+1]
            data_dict["Employer Address1"] = employer_address1_data
            data_dict["Employer Address2"] = text_data[int(employer_list_index[0])+int(employer_address1_index[0])+3] if '3' not in text_data[int(employer_list_index[0])+int(employer_address1_index[0])+3] else ''

            employer_state_indexm = [index for index, string in enumerate(text_data[int(employer_list_index[0]):]) if "3. City State" in string]
            employer_state_index = int(employer_list_index[0])+int(employer_state_indexm[0])+1 
            
            employer_state_text = str(text_data[employer_state_index]).split()
            
            
            employer_postal_code = employer_state_text.pop(len(employer_state_text)-1)
            employer_city = ' '.join(employer_state_text)
            employer_state_text2 = str(text_data[employer_state_index+1]) if '4.' not in text_data[employer_state_index+1] else ''
            employer_split = (employer_state_text2.strip())
            employer_state = employer_split.replace("UNITED STATES OF AMERICA","")
            employer_country = "UNITED STATES OF AMERICA"
            data_dict["Employer City"] = employer_city
            data_dict["Employer State"] = employer_state
            data_dict["Employer Postal Code"] = employer_postal_code
            data_dict["Employer Country"] = employer_country
            
            employer_phone_index = [index for index, string in enumerate(text_data[int(employer_list_index[0]):]) if "4. Phone number" in string]
            employer_phone_index1 = int(employer_list_index[0])+int(employer_phone_index[0])+1
            
            employer_phone=text_data[employer_phone_index1].split()
            
            data_dict["Employer Phone"] = employer_phone[0]
            try:
                data_dict["Employer Phoneext"] = employer_phone[1]
            except:
                data_dict["Employer Phoneext"]=""
                pass
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
            data_dict["Contact Postal Code"] = contact_postal_code
            data_dict["Contact Country"] = ' '.join(contact_country)
            
            contact_phone_index = [index for index, string in enumerate(text_data[int(contact_list_index[0]):]) if "4. Phone number" in string]
            contact_phone_index1 = int(contact_list_index[0])+int(contact_phone_index[0])+1
            
            contact_phone=text_data[contact_phone_index1].split()
            
            data_dict["Contact Phone"] = contact_phone[0]
            try:
                data_dict["Contact Phoneext"] = contact_phone[1]
            except:
                data_dict["Contact Phoneext"]=""
                pass
            contact_email_index = [index for index, string in enumerate(text_data[int(contact_list_index[0]):]) if "5. E-mail address" in string]
            contact_email_index1 = int(contact_list_index[0])+int(contact_email_index[0])+1
            
            contact_email=text_data[contact_email_index1]
            data_dict["Contact Email"] = contact_email
            
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
            data_dict["Year of Commenced Businees"] = year_of_commenced_business_text
            
        
        elif _pno == 1:
            #print(text_data)
            agent_list_index = [index for index, string in enumerate(text_data) if "Agent or attorney’s last" in string]
            agent_data = text_data[int(agent_list_index[0])+1].split()
            if len(agent_data) >= 3:
                data_dict["Agent Last Name"] = agent_data[0] if index_in_list(agent_data, 0) else ''
                data_dict["Agent First Name"] = ' '.join(agent_data[1:-1]) if index_in_list(agent_data, 1) else ''
                data_dict["Agent Middle Name"] = agent_data[-1] if index_in_list(agent_data, 3) else ''
            else:
                data_dict["Agent Last Name"] = agent_data[0] if index_in_list(agent_data, 0) else ''
                data_dict["Agent First Name"] = ' '.join(agent_data[1:]) if index_in_list(agent_data, 1) else ''
                data_dict["Agent Middle Name"] = agent_data[2] if index_in_list(agent_data, 3) else ''
            
            

            agent_address1_index = [index for index, string in enumerate(text_data[int(agent_list_index[0]):]) if "5. Address 1" in string]
            agent_address1_data = text_data[int(agent_list_index[0])+int(agent_address1_index[0])+1]
            data_dict["Agent Address1"] = agent_address1_data
            data_dict["Agent Address2"] = text_data[int(agent_list_index[0])+int(agent_address1_index[0])+3] if '6' not in text_data[int(agent_list_index[0])+int(agent_address1_index[0])+3] else ''

            country_state_indexm = [index for index, string in enumerate(text_data[int(agent_list_index[0]):]) if "6. City State" in string]
            country_state_index = int(agent_list_index[0])+int(country_state_indexm[0])+1 

            country_state_text = str(text_data[country_state_index])
            #print(country_state_text)
            agent_city = country_state_text
            agent_country="UNITED STATES OF AMERICA"
            country_pcode_index = int(agent_list_index[0])+int(country_state_indexm[0])+2

            country_pcode_text = str(text_data[country_pcode_index]).split()

            agent_postal_code = country_pcode_text[len(country_pcode_text)-1]
            country_state_text2 = str(text_data[country_state_index+1]) if '4.' not in text_data[country_state_index+1] else ''
            country_split = (country_state_text2.strip())
            agent_state = ""
            data_dict["Agent City"] = agent_city
            data_dict["Agent State"] = agent_state
            data_dict["Agent Postal Code"] = agent_postal_code
            data_dict["Agent Country"] = agent_country
            
            agent_phone_index = [index for index, string in enumerate(text_data[int(agent_list_index[0]):]) if "3. Firm EIN" in string]
            agent_phone_index1 = int(agent_list_index[0])+int(agent_phone_index[0])+2
            agent_firmein_index1 = int(agent_list_index[0])+int(agent_phone_index[0])+1
            
            agent_phone=text_data[agent_phone_index1].split()
            agent_firmein=text_data[agent_firmein_index1]
            data_dict["Agent Firmein"]=agent_firmein
            
            data_dict["Agent Phone"] = agent_phone[0]
            try:
                data_dict["Agent Phoneext"] = agent_phone[1]
            except:
                data_dict["Agent Phoneext"]=""
                pass
                
            agent_firmname_index = [index for index, string in enumerate(text_data[int(agent_list_index[0]):]) if "2. Firm name" in string]
            agent_firmname_index1 = int(agent_list_index[0])+int(agent_firmname_index[0])+1
                        
            agent_firmname=text_data[agent_firmname_index1]
            agent_email_index = [index for index, string in enumerate(text_data[int(agent_list_index[0]):]) if "7. E-mail address" in string]
            agent_email_index1 = int(agent_list_index[0])+int(agent_email_index[0])+1
            
            agent_email=text_data[agent_email_index1]
            data_dict["Agent Firmname"] = agent_firmname
            data_dict["Agent Email"] = agent_email
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
            data_dict["Job Postal Code"] = job_postal_code

            


            job_title_index = [index for index, string in enumerate(text_data) if "3. Job title" in string]
            job_title_text = (str(text_data[job_title_index[0]+1]).strip()) if '4.' not in text_data[job_title_index[0]+1] else ''
            data_dict["Job Title"] = job_title_text
            data_dict["Job Duties"] = "See attached Certified 9089 for details"

            wages_index = [index for index, string in enumerate(text_data) if "From: To:" in string]
            wages_text = (str(text_data[wages_index[0]+2]).strip()) if ',' not in text_data[wages_index[0]+2] else ''
            wages_text += ' '+(str(text_data[wages_index[0]+3]).strip()) if ',' not in text_data[wages_index[0]+3] else ''
            wages_text += ' '+(str(text_data[wages_index[0]+4]).strip()) if ',' not in text_data[wages_index[0]+4] else ''
            wages_text += ' '+(str(text_data[wages_index[0]+5]).strip()) if ',' not in text_data[wages_index[0]+5] else ''
            #print(wages_text)
            wages_from= (str(text_data[wages_index[0]+6]).strip()) if ','  in text_data[wages_index[0]+7] else (str(text_data[wages_index[0]+5]).strip())
            wages_to= (str(text_data[wages_index[0]+7]).strip()) if ','  in text_data[wages_index[0]+8] else (str(text_data[wages_index[0]+6]).strip())
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
            data_dict["Wage From"] = wages_from
            data_dict["Wage To"] = wages_to
            
        
        elif _pno == 4:
            
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
            data_dict["Alien Postal Code"] = alien_postal_code
            data_dict["Alien Country"] = ' '.join(alien_country)

            alien_list2_index = [index for index, string in enumerate(text_data) if "5. Country of" in string]
            alien_text2 = (str(text_data[alien_list2_index[0]+1]).strip()).split()
            data_dict["Country of Citizenship"] = alien_text2[0] if index_in_list(alien_text2, 0) else ''
            data_dict["Country of Birth"] = alien_text2[1] if index_in_list(alien_text2, 1) else ''

            alien_dob_index = [index for index, string in enumerate(text_data) if "7. Alien’s date of birth" in string]
            alien_text3 = (str(text_data[alien_dob_index[0]+1]).strip()).split()
            data_dict["Alien DOB"] = alien_text3[0] if index_in_list(alien_text3, 0) else ''
            data_dict["Alien Classofadm"] = alien_text3[1]

            alien_reg_index = [index for index, string in enumerate(text_data) if "9. Alien registration" in string]
            alien_text4 = (str(text_data[alien_reg_index[0]+1]).strip())
            alien_text5 = ' '+(str(text_data[alien_reg_index[0]+2]).strip()) if '11.' not in text_data[alien_reg_index[0]+2] else ''
            alien_reg_text = (alien_text4 + alien_text5).strip()
            
            data_dict["Alien Registration No"] = alien_reg_text.split()[-1]
            data_dict["Alien Admission No"] = alien_reg_text.split()[0]

        elif _pno == 8:
            #print(text_data)
            eta_list_index = [index for index, string in enumerate(text_data) if "This Certification is valid from" in string]
            eta_text = (str(text_data[eta_list_index[0]+1]).strip()).split()
            eta_text4 = (str(text_data[eta_list_index[0]+2]).strip())
            data_dict["Certificate Valid From"] = eta_text[0] if index_in_list(eta_text, 0) else ''
            data_dict["Certificate Valid To"] = eta_text[1] if index_in_list(eta_text, 1) else ''

            eta_list_index2 = [index for index, string in enumerate(text_data) if "Signature of Certify" in string]
            eta_text2 = (str(text_data[eta_list_index2[0]+1]).strip())
            eta_text3 = (str(text_data[eta_list_index2[0]+2]).strip())
            data_dict["Case Number"] = eta_text2
            data_dict["Filing Date"] = eta_text3
            data_dict["Signed Date"] = eta_text4
    print(data_dict)

    process_to_db(data_dict)
        
    doc.close()
    return data_dict

def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    for page in template_pdf.pages:
        annotations = page.get("/Annots")
        #annotations = template_pdf.pages[0][ANNOT_KEY]
        for annotation in annotations:
            #annotation.update(pdfrw.PdfDict(AP=""))
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict.keys():
                        annotation.update(pdfrw.PdfDict(V='{}'.format(data_dict[key])))
                        
    #     pdfrw.PdfDict(AP=data_dict[key], V=data_dict[key])
        pdfrw.PdfWriter().write(output_pdf_path, template_pdf)




if __name__ == '__main__':
    initf()

