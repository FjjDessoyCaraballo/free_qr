import pyqrcode

new_linktree = input('Insert link: ')

qr = pyqrcode.create(new_linktree)
qr.png('linktree_qrcode.png', scale=8, module_color=[0,0,0,128], background=[0xff, 0xff, 0xcc])
print(qr.terminal(quiet_zone=1))