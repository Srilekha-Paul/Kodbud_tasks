# ATS Resume Selector
# Author: Srilekha Paul 😉

import os
import re
import pandas as pd

def clean_text(text):
    """Remove special characters and make text lowercase"""
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.lower()

def get_keywords(text):
    """Extract unique keywords"""
    return set(text.split())

def calculate_match(resume_text, job_keywords):
    """Count matching keywords between resume and job description"""
    resume_words = get_keywords(clean_text(resume_text))
    matches = resume_words.intersection(job_keywords)
    score = (len(matches) / len(job_keywords)) * 100
    return round(score, 2)

def main():
    resumes_folder = "resumes"   # Folder where resumes are stored
    job_file = "job_description.txt"

    if not os.path.exists(resumes_folder):
        print("⚠️ Folder 'resumes' not found! Create it and add some .txt resumes.")
        return

    if not os.path.exists(job_file):
        print("⚠️ Job description file not found! Please create 'job_description.txt'.")
        return

    # Read job description
    with open(job_file, "r", encoding="utf-8") as f:
        job_description = clean_text(f.read())

    job_keywords = get_keywords(job_description)
    print(f"🔍 Job Keywords ({len(job_keywords)}):", ", ".join(list(job_keywords)[:10]), "...")

    results = []

    # Read each resume file
    for filename in os.listdir(resumes_folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(resumes_folder, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                resume_text = f.read()
                match_score = calculate_match(resume_text, job_keywords)
                results.append({"Resume": filename, "Match (%)": match_score})

    # Sort by best match
    results.sort(key=lambda x: x["Match (%)"], reverse=True)

    # Save results in CSV
    df = pd.DataFrame(results)
    df.to_csv("ATS_Results.csv", index=False)
    print("\n✅ Results saved to 'ATS_Results.csv'")
    print(df)

if __name__ == "__main__":
    main()
