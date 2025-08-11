import pyqrcode

new_qrcode = input('Insert link (or type exit): ')

if new_qrcode == "exit":
	exit()

qr = pyqrcode.create(new_qrcode)
qr.png('qrcode.png', scale=8, module_color=[0,0,0,128], background=[0xff, 0xff, 0xcc])
print(qr.terminal(quiet_zone=1))
