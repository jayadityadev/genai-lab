import re
import wikipediaapi

from pydantic import BaseModel, Field
from typing import List, Optional


class InstitutionDetails(BaseModel):
    name: str
    founder: Optional[str] = None
    founded: Optional[str] = None
    branches: List[str] = Field(default_factory=list)
    number_of_employees: Optional[int] = None
    summary: Optional[str] = None


def fetch_institution_details(institution_name: str) -> InstitutionDetails:
    # 1. Setup Wikipedia API with a proper User-Agent
    user_agent = "InstitutionScraper/1.0 (contact: myemail@example.com)"
    wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language="en")
    page = wiki.page(institution_name)

    if not page.exists():
        raise ValueError(f"The page for '{institution_name}' does not exist.")

    full_text = page.text

    # 2. Helper function to extract info using Regex
    def extract_pattern(pattern, text, is_list=False):
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            content = match.group(1).strip()
            if is_list:
                return [item.strip() for item in content.split(",") if item.strip()]
            return content
        return [] if is_list else None

    # 3. Extraction logic
    founder_pattern = r"(?:founded|established|started)\s+by\s+([^.\n,]+)"
    founder_match = re.search(founder_pattern, full_text, re.IGNORECASE)
    founder = founder_match.group(1).strip() if founder_match else "Unknown"

    year_pattern = r"(?:founded|established|started|incorporated)(?:\s+in)?(?:\s+the\s+year)?\s+(\d{4})"
    year_match = re.search(year_pattern, full_text, re.IGNORECASE)
    founded = year_match.group(1) if year_match else "Unknown"

    branches = extract_pattern(r"Branches\s*[:\-]?\s*(.*)", full_text, is_list=True)
    raw_employees = extract_pattern(r"Number of employees\s*[:\-]?\s*([\d,]+)", full_text)

    emp_count = None
    if raw_employees:
        try:
            emp_count = int(raw_employees.replace(",", ""))
        except ValueError:
            emp_count = None

    return InstitutionDetails(
        name=page.title,
        founder=founder,
        founded=founded,
        branches=branches,
        number_of_employees=emp_count,
        summary=(page.summary[:500] + "...") if page.summary else None,
    )


if __name__ == "__main__":
    try:
        val = input("Enter the Institution name: ")
        data = fetch_institution_details(val)
        print(data.model_dump_json(indent=2))
    except Exception as e:
        print(f"Error: {e}")