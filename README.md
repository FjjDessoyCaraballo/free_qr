# Free QR Code Generator

A simple Python script that generates QR codes from user input and saves them as PNG images.

## Features

- Generate QR codes from any text or URL
- Save QR codes as PNG images with custom styling
- Display QR codes directly in the terminal
- Easy setup with automated virtual environment creation

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`:
  - PyQRCode==1.2.1
  - pypng==0.20220715.0

## Quick Start

### Option 1: Automated Setup (Recommended)

Run the setup script to automatically create a virtual environment and start the program:

```bash
python setup.py
```

### Option 2: Manual Setup

1. Create a virtual environment:
   ```bash
   python -m venv myvenv
   ```

2. Activate the virtual environment:
   - **Windows:** `myvenv\Scripts\activate`
   - **macOS/Linux:** `source myvenv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:
   ```bash
   python free_qr.py
   ```

## Usage

1. When prompted, enter the text or URL you want to convert to a QR code
2. The script will:
   - Generate a QR code
   - Save it as `qrcode.png` in the current directory
   - Display the QR code in your terminal
3. Type `exit` to quit the program

## Output

- **PNG File:** `qrcode.png` (black QR code on light yellow background, 8x scale)
- **Terminal Display:** ASCII representation of the QR code

## File Structure

```
├── free_qr.py          # Main QR code generator script
├── requirements.txt    # Python dependencies
├── setup.py           # Automated setup script
└── README.md          # This file
```

## Example

```
Insert link (or type exit): https://github.com
```

This will create a QR code that links to GitHub and save it as `qrcode.png`.

## License

This project is licensed under the MIT License.
