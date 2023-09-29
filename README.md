# Google Maps Reviews Scraper

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

This Python project is a simple web scraper designed to extract reviews from a Google Maps link. It saves the scraped data in an XLSX file for further analysis. This project is for educational purposes only.

## Features

- Scrapes reviews from a Google Maps link.
- Extracts key information such as reviewer name, rating, review text, and date.
- Stores the scraped data in an XLSX file for easy analysis.

## Requirements

- Python 3.7 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/google-maps-reviews-scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd google-maps-reviews-scraper
   ```

3. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Modify the `main.py` script to specify the Google Maps URL you want to scrape.

2. Run the `main.py` script:

   ```bash
   python main.py
   ```

3. The scraped data will be saved in an XLSX file named `reviews.xlsx` in the project directory.

## Example

Here is an example of how to use the scraper:

```python
# Modify main.py to set the Google Maps URL you want to scrape
# Then run the scraper:
python main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is for educational purposes only. Use it responsibly and in accordance with the terms of service of the websites you intend to scrape. The developers are not responsible for any misuse or legal consequences resulting from the use of this project.
```

Please note that I updated the README to mention modifying the `main.py` script to set the Google Maps URL you want to scrape, as the original code did not specify how to input the URL. Make sure to replace `"https://maps.google.com/your-google-maps-link"` in the code with the actual Google Maps URL you want to scrape.
