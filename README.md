# Business Card Scanner

A Python application that scans business cards from images and extracts contact information into a structured Excel file with formatted columns.

## Features

- 📸 **Image Processing**: Reads business card images in various formats (JPG, PNG, BMP, GIF, TIFF)
- 🔍 **OCR Text Extraction**: Uses Tesseract OCR to extract text from images
- 📊 **Data Parsing**: Intelligently extracts:
  - Full Name
  - Job Title
  - Company Name
  - Email Address
  - Phone Number
  - Website URL
  - LinkedIn Profile
  - Address
- 📈 **Excel Export**: Creates professionally formatted Excel files with:
  - Styled headers with colors
  - Bordered cells
  - Adjusted column widths
  - Text wrapping for long content
- 🔄 **Batch Processing**: Process multiple business cards at once
- 📝 **Append Mode**: Add new cards to existing Excel files

## Installation

### Prerequisites

- Python 3.8 or higher
- Tesseract OCR engine

#### Install Tesseract OCR

**Windows:**
1. Download installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the installer (default path: `C:\Program Files\Tesseract-OCR`)
3. Update the pytesseract path in your code if needed

**macOS:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
```

### Python Dependencies

```bash
# Clone the repository
git clone https://github.com/davidcarballasreboredo1978/scan_cards.git
cd scan_cards

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### 1. Batch Process Business Cards

Place your business card images in the `input_images` directory and run:

```bash
python main.py scan
```

Options:
```bash
python main.py scan --input input_images --output output_excel --filename results.xlsx
```

**Parameters:**
- `--input` / `-i`: Directory containing business card images (default: `input_images`)
- `--output` / `-o`: Directory to save output Excel file (default: `output_excel`)
- `--filename` / `-f`: Output filename (default: `business_cards.xlsx`)

### 2. Process Single Card

```bash
python main.py process path/to/image.jpg
```

Options:
```bash
python main.py process path/to/image.jpg --output output_excel
```

## Project Structure

```
scan_cards/
├── main.py              # Main application and CLI
├── card_extractor.py    # OCR and text extraction logic
├── excel_exporter.py    # Excel file creation and formatting
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── .gitignore          # Git ignore rules
├── input_images/       # Place business card images here
└── output_excel/       # Generated Excel files
```

## Module Documentation

### CardExtractor Class

Handles OCR and intelligent data extraction from business card images.

**Key Methods:**
- `extract_text_from_image(image_path)`: Extract text using OCR
- `extract_email(text)`: Find email addresses
- `extract_phone(text)`: Find phone numbers
- `extract_name(text)`: Detect person's name
- `process_card(image_path)`: Complete card processing

### ExcelExporter Class

Creates and manages Excel files with formatted business card data.

**Key Methods:**
- `create_workbook(cards_data, filename)`: Create new Excel file
- `append_to_workbook(excel_path, cards_data)`: Add data to existing file

### BusinessCardScanner Class

Main application class that orchestrates the scanning workflow.

**Key Methods:**
- `process_single_image(image_path)`: Process one card
- `process_directory(output_filename)`: Batch process directory

## Example Workflow

1. **Prepare Images:**
   ```bash
   mkdir input_images
   # Copy your business card photos to input_images/
   ```

2. **Run Scanner:**
   ```bash
   python main.py scan
   ```

3. **Check Results:**
   - Open `output_excel/business_cards.xlsx` in Excel or spreadsheet application
   - All extracted data will be organized in columns

## Output Format

The Excel file contains the following columns:

| Name | Job Title | Company | Email | Phone | Website | LinkedIn | Address |
|------|-----------|---------|-------|-------|---------|----------|---------|
| John Doe | Manager | TechCorp | john@techcorp.com | +1-555-1234 | www.techcorp.com | linkedin.com/in/johndoe | 123 Main St |

## Troubleshooting

### Issue: "pytesseract.TesseractNotFoundError"

**Solution:** Tesseract OCR is not installed or not in PATH
- Install Tesseract following the instructions above
- On Windows, update path in code: `pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`

### Issue: Poor OCR Results

**Solutions:**
- Use high-quality images (300+ DPI recommended)
- Ensure good lighting when photographing cards
- Use straight-on angles, not tilted
- Try different image formats

### Issue: Data Extraction Not Accurate

- The extraction uses pattern matching and heuristics
- Review and manually correct the `raw_text` field if needed
- For critical data, manual verification is recommended

## Advanced Usage

### Custom Data Extraction

Edit the `CardExtractor` class to add custom extraction patterns:

```python
def extract_custom_field(self, text: str) -> str:
    """Extract custom field based on your needs"""
    # Add your regex pattern
    pattern = r'your_pattern_here'
    match = re.search(pattern, text)
    return match.group(0) if match else ""
```

### Programmatic Usage

```python
from card_extractor import CardExtractor
from excel_exporter import ExcelExporter

# Extract from single image
extractor = CardExtractor()
card_data = extractor.process_card('path/to/card.jpg')

# Export to Excel
exporter = ExcelExporter()
exporter.create_workbook([card_data], 'output.xlsx')
```

## Dependencies

- **opencv-python**: Image processing
- **pytesseract**: OCR text extraction
- **Pillow**: Image handling
- **openpyxl**: Excel file creation
- **pandas**: Data manipulation
- **numpy**: Numerical operations
- **pydantic**: Data validation
- **click**: CLI interface

## Performance

- Processing speed depends on image size and quality
- Average: 2-5 seconds per business card on standard hardware
- Batch processing 100 cards: ~3-8 minutes

## Limitations

- Data extraction accuracy depends on image quality and card layout
- Works best with English text
- For multilingual support, additional Tesseract language packs may be needed
- Some card layouts may require manual adjustment

## Future Enhancements

- [ ] GUI interface using PyQt or Tkinter
- [ ] Multilingual support
- [ ] Direct contact integration with CSV/vCard export
- [ ] Image preprocessing improvements
- [ ] Machine learning for better field detection
- [ ] Web interface
- [ ] Real-time camera capture

## License

MIT License - Feel free to use and modify

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the card extraction logs
3. Open an issue on GitHub

## Author

Created by: davidcarballasreboredo1978

---

Happy scanning! 📇✨