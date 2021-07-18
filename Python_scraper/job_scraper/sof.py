import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python"
link_front = "https://stackoverflow.com/jobs/"

def extract_sof_pages():
  r = requests.get(URL)
  soup = BeautifulSoup(r.text, "html.parser")
  pagination = soup.find(name="div", attrs={"class":"s-pagination"})
  links = pagination.find_all("a")

  pages = []
  for link in links[:-1]:
    pages.append(int(link.find("span").string))
  last_page = pages[-1]

  return last_page

def extract_job_info(html):
  title = html.find("h2", {"class":"mb4 fc-black-800 fs-body3"}).find("a")["title"].strip()
  company = html.find("h3", {"class":"fc-black-700 fs-body1 mb4"}).find("span").string
  if company:
    company = company.strip()
  else:
    company = None
  location = html.find("h3", {"class":"fc-black-700 fs-body1 mb4"}).find("span", {"class":"fc-black-500"}).string.strip()
  job_id = html["data-jobid"]

  return {"title" : title, "company" : company, "location" : location, "link" : f"{link_front}{job_id}"}

def extract_sof_jobs(last_page_sof):
  job_infos = []
  for page_num in range(1, last_page_sof + 1):
    print(f"Scraping SOF : Page {page_num}..")
    r = requests.get(f"{URL}&pg={page_num}")
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find_all("div", {"class":"js-result"})

    for result in results:
      job_info = extract_job_info(result)
      job_infos.append(job_info)

  return job_infos

def get_job_infos():
  last_page_sof = extract_sof_pages()
  results = extract_sof_jobs(last_page_sof)

  return results