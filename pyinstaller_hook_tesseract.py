# Hook for Tesseract OCR
# This file is used to ensure that Tesseract OCR is properly bundled with PyInstaller.

hiddenimports = [
    'pytesseract',
]

# Additional data files (if any) can be added here

data = [
    ('/path/to/tesseract', '.'),  # Adjust the path accordingly
]
