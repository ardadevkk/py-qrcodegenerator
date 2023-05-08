import pyqrcode

qrurl = input("Enter Your URL: ")#You Put your URL 

qr_code = pyqrcode.create(qrurl)#Generate QR Code
qr_code.svg('qrcode.svg',scale=5)#Save QR Code
