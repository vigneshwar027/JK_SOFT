headers = [ 'Petitioner Name','Petitioner of Primary Beneficiary','Beneficiary Type (Employee / Dependent)','Email Address', 'Beneficiary Record Creation Date', 'Beneficiary Employee Id', 'Beneficiary Last Name', 'Beneficiary First Name', 'Beneficiary Middle Name', 'Primary Beneficiary Last Name', 'Primary Beneficiary First Name', 'Relation', 'Country of Birth', 'Country of Citizenship', 'Immigration Status (I-94)', 'Immigration Status Expiration Date (I-94)', 'I-797 Status', 'I-797 Expiration Date', 'Final NIV (Maxout) Date', 'Maxout Date Applicability and Note', 'PED', 'EAD Type', 'EAD Expiration Date', 'AP Expiration Date', 'DS-2019 Valid From', 'DS-2019 Expiration Date', 'Re-Entry Permit Expiration Date', 'Green Card Expiration Date', 'Passport Expiration Date', 'Visa Type', 'Visa Expiration Date', 'Employee Hire Date', 'Current Job Title', 'Work Address-Street', 'Work Address-City', 'Work Address-State', 'Work Address-Zip', 'Work Address-Country']

headers_table = [ 'PetitionerName','Primary_Petitioner','BeneficiaryType','WorkEmail', 'SourceCreatedDate', 'EmployeeId', 'LastName', 'FirstName', 'MiddleName', 'PrimaryBeneficiaryLastName', 'PrimaryBeneficiaryFirstName', 'RelationType', 'BirthCountry', 'CitizenshipCountry', 'ImmigrationStatus', 'ImmigrationStatusExpirationDate', 'MostRecentI797Status', 'I797ExpirationDate', 'FinalNivDate', 'MaxOutDateNote', 'VisaPedDate', 'EadType', 'EadExpirationDate', 'AdvanceParoleExpirationDate', 'Ds2019ValidFromDate', 'Ds2019ExpirationDate', 'ReEntryPermitExpirationDate', 'GreenCardExpirationDate', 'MostRecentPassportExpirationDate', 'VisaType', 'VisaExpirationDate', 'HireDate', 'JobTitle', 'Address1', 'City', 'StateProvince', 'ZipCode', 'Country']

for x,y in zip(headers,headers_table):
    print(x,'\t',y)