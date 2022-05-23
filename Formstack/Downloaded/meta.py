from pdfrw import PdfReader, PdfWriter   
trailer = PdfReader("ABCD12412, N, VIJAY - Visa Stamp - V1231204082023.pdf")    
trailer.Info.barcode = "Visa"    
PdfWriter("edited2.pdf", trailer=trailer).write()