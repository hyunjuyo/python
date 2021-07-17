import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python"

def extract_stackoverflow_pages():

  r = requests.get(URL)
  #print(r)
  #print(r.status_code)

  #print(r.text)

  soup = BeautifulSoup(r.text, "html.parser")

  pagination = soup.find(name="div", attrs={"class":"s-pagination"})

  #print(pagination)

  links = pagination.find_all("a")

  pages = []

  for link in links[:-1]:
    pages.append(int(link.find("span").string))

  last_page = pages[-1]

  return last_page

def extract_job_info(html):
  title = html.find("h2", {"class":"mb4 fc-black-800 fs-body3"}).find("a")["title"].strip()
  company = html.find("h3", {"class":"fc-black-700 fs-body1 mb4"}).find("span").string.strip()
  return {"title" : title, "company" : company}

def extract_stackoverflow_jobs(last_page_stackoverflow):
  job_infos = []
  # for page_num in range(1, last_page_stackoverflow + 1):
  #   r = requests.get(f"{URL}&pg={page_num}")
  #   print(r.status_code)

  r = requests.get(f"{URL}&pg=1")
  soup = BeautifulSoup(r.text, "html.parser")
  results = soup.find_all("div", {"class":"grid--cell fl1"})

  for result in results:
    job_info = extract_job_info(result)
    job_infos.append(job_info)
  print(job_infos)