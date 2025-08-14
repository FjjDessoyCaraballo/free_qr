import pyqrcode
import traceback

def main():
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
    try:
        new_qrcode = input('Insert link (or type exit): ')
        if new_qrcode == "e":
            exit()
        name_qrcode = input('Name your file without the extension: ')
        if name_qrcode == "e":
            exit()

        qr = pyqrcode.create(new_qrcode)
        qr.png(f'{name_qrcode}.png', scale=8, module_color=[0,0,0,128], background=[0xff, 0xff, 0xcc])
        print(qr.terminal(quiet_zone=1))
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
