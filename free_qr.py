import pyqrcode

print('''
Welcome to free_qr. This is a simple script
that makes QR codes for you! At any point, 
if you want to (e)xit, just type 'e'. 

If you're interested in contributing to 
the project, feel free to fork it and 
send a PR.
	  
Warm regards,
Felipe
''')

new_qrcode = input('Insert link (or type exit): ')
if new_qrcode == "e":
	exit()
name_qrcode = input('Name your file: ')
if name_qrcode == "e":
	exit()

qr = pyqrcode.create(new_qrcode)
qr.png('qrcode.png', scale=8, module_color=[0,0,0,128], background=[0xff, 0xff, 0xcc])
print(qr.terminal(quiet_zone=1))
