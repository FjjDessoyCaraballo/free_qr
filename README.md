# Free QR Code Generator

A simple Python script that generates QR codes from user input and saves them as PNG images.

## Features

- Generate QR codes from any text or URL
- Save QR codes as PNG images with custom styling
- Display QR codes directly in the terminal
- Easy setup with automated virtual environment creation

## Requirements

- Python 3.x
- uv 0.8.9

## Quick Start

## Usage

Just use the script with `uv`:

```bash
uv run free_qr.py
```

1. Specify URL in CLI;
2. Specify file name without extensio (only png's are outputted)
3. Profit

## Output

- **PNG File:** `{YOUR_FILE_NAME}.png` (black QR code on light yellow background, 8x scale)
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
