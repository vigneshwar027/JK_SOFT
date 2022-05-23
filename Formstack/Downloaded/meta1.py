from pdfrw import PdfReader
import os, fnmatch

def find_files(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            try:
                print(PdfReader(os.path.join(root, name)).Info['/barcode'])
                if("Passport" in PdfReader(os.path.join(root, name)).Info['/barcode']):
                    if fnmatch.fnmatch(name, pattern):
                        result.append(os.path.join(root, name))
            except:
                pass
            
    return result



print(find_files("*.pdf","C:/python/2021/Immilytics/reporting_automation/case_report/Downloaded/"))
