# Roche Careers Job Scraper

A Python-based Selenium scraper that extracts job listings from the Roche Careers website.
The script collects job titles, locations, full descriptions, and links, then ranks jobs based on the presence of relevant technical skills.

This tool was built to automatically identify job postings that match specific research or technical expertise.

---

# Features

* Scrapes Roche career listings for specified keywords
* Filters jobs by country
* Extracts:

  * Job title
  * Location
  * Full job description
  * Job URL
* Counts occurrences of relevant technical skills within each job description
* Outputs results into an Excel file with separate sheets per country

---

# Project Structure

```
roche-job-scraper/
│
├── Roche_scrapper.py      # Main scraping logic
├── run_scraper.py         # Script used to execute the scraper
├── README.md
└── roche_jobs.xlsx        # Output file (generated after running)
```

---

# Requirements

* Python **3.9+**
* Google Chrome
* ChromeDriver matching your Chrome version

ChromeDriver download:
https://chromedriver.chromium.org/

Make sure ChromeDriver is accessible in your system **PATH**.

---

# Setup

## 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/roche-job-scraper.git
cd roche-job-scraper
```

---

## 2️⃣ Create a Virtual Environment

Creating a virtual environment ensures dependencies do not interfere with your system Python installation.

### Mac / Linux

```
python3 -m venv venv
source venv/bin/activate
```

### Windows

```
python -m venv venv
venv\Scripts\activate
```

After activation your terminal should show something like:

```
(venv)
```

---

## 3️⃣ Install Dependencies

```
pip install selenium pandas openpyxl
```

---

# Running the Scraper

Run the script:

```
python run_scraper.py
```

The script will:

1. Search Roche careers using predefined keywords
2. Filter jobs by country
3. Extract job titles, locations, descriptions, and URLs
4. Count relevant technical skills in each job description
5. Save the results to:

```
roche_jobs.xlsx
```

Each country will appear as a **separate sheet** in the Excel file.

---

# Example Output

| title              | location | skill_count | url  |
| ------------------ | -------- | ----------- | ---- |
| Data Scientist     | Basel    | 3           | link |
| Research Scientist | Penzberg | 7           | link |

The **skill_count** column indicates how many relevant technical skills appear in the job description.

---

# Customisation

## Change Search Keywords

Inside the script:

```
keywords = ["scientist", "data"]
```

---

## Change Countries

```
["Switzerland", "United Kingdom"]
```

---

## Modify Skill Keywords

The scraper counts occurrences of predefined technical skills such as:

* molecular biology
* sequencing
* nanoparticle
* microscopy
* RNA isolation
* high-content imaging

You can edit or extend this list depending on your expertise.

---

# Notes

* The Roche careers website loads job listings dynamically, so Selenium is required.
* Each job posting is opened in a separate browser tab to retrieve the full description.
* Duplicate job listings are automatically removed before saving.

---

# Disclaimer

This project is intended for **personal use and educational purposes**.
Please ensure scraping complies with the website's terms of service.

---

# Author

Altin
PhD researcher in respiratory biology and computational data analysis.
