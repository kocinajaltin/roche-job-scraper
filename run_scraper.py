from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from Roche_scrapper import roche_scrape

# ---------- RUN SCRAPER ----------
keywords = ["scientist"]#, "data"]

with pd.ExcelWriter("roche_jobs_test.xlsx") as writer:

    for country in ["Switzerland"]:#, "United Kingdom"]:

        country_df = pd.DataFrame()

        for keyword in keywords:

            df_temp = roche_scrape(keyword, country)
            country_df = pd.concat([country_df, df_temp], ignore_index=True)

        country_df = country_df.drop_duplicates(subset="url")

        # ---------- TECH SKILL LIST ----------
        tech_keywords = [
            "molecular biology","cell culture","western blot","microscopy",
            "sequencing","protein expression","rna","dna",
            "ali","aerosol exposure","teer",
            "high-content imaging","confocal microscopy","transcriptomic analysis",
            "pathway analysis","rna isolation","minion sequencing",
            "immunohistochemistry","microtome slicing","viability assays",
            "mitochondrial markers","dls","cps","smps",
            "segmentation workflows","automated imaging pipelines",
            "nanoparticle","h441","calu-3"
        ]

        # ---------- SKILL COUNTER ----------
        def count_skills(text):

            if pd.isna(text):
                return 0

            text = text.lower()

            return sum(skill in text for skill in tech_keywords)

        country_df["skill_count"] = country_df["description"].apply(count_skills)

        # ---------- SAVE ----------
        country_df.to_excel(writer, sheet_name=country, index=False)


print("Scraping complete. Data saved to roche_jobs.xlsx")
