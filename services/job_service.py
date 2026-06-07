import os
import requests
from dotenv import load_dotenv

load_dotenv()

def search_jobs(
    role: str,
    country: str = "",
    city: str = "",
    work_mode: str = "",
    days: int = 7
):
    query = role

    if city:
        query += f" in {city}"
    elif country:
        query += f" in {country}"

    if work_mode:
        query += f" {work_mode}"

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
        "query": query,
        "page": "1",
        "num_pages": "1"
    }

    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    if response.status_code != 200:

        return [
            {
                "error": response.text
            }
        ]

    data = response.json()

    jobs = []

    for job in data.get("data", [])[:10]:

        jobs.append({
            "title": job.get("job_title"),
            "company": job.get("employer_name"),
            "location": job.get("job_city"),
            "country": job.get("job_country"),
            "employment_type": job.get("job_employment_type"),
            "posted_at": job.get("job_posted_at_datetime_utc"),
            "apply_link": job.get("job_apply_link")
        })

    return {
    "query_used": query,
    "jobs": jobs
}