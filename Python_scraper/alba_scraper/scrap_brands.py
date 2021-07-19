import requests
from bs4 import BeautifulSoup
from save_brands import save_brands

alba_url = "http://www.alba.co.kr"


def get_brand_infos():
    url_r = requests.get(alba_url)
    soup = BeautifulSoup(url_r.text, "html.parser")
    superbrand = soup.find("div", {"id": "MainSuperBrand"})
    goodsbox = superbrand.find("ul", {"class": "goodsBox"})
    brands = goodsbox.find_all("li", {"class": "impact"})

    brand_infos = []
    for brand in brands:
        dict = {}
        dict["company"] = brand.find("span", {"class": "company"}).get_text()
        dict["tile"] = brand.find("span", {"class": "title"}).get_text()
        dict["link"] = brand.find("a", {"class": "goodsBox-info"})["href"]
        brand_infos.append(dict)

    return brand_infos


def get_page_count(brand):
    url_r = requests.get(f"{brand['link']}job/brand/?pagesize=50")
    soup = BeautifulSoup(url_r.text, "html.parser")
    try:
        r = soup.find("div", {"class": "goodsList"})
        r = r.find_all("script", {"type": "text/javascript"})
        start_where = r[-1].string.find("(\"")
        page_count = r[-1].string[start_where:start_where+6].strip("(\") ")
    except:
        page_count = 2

    try:
        page_count = int(page_count)
    except:
        page_count = 2

    return page_count


def get_job_data(soup):
    list_a = []
    joblist = soup.find("div", {"class": "goodsList"})
    joblist = joblist.find("tbody")
    joblist = joblist.find_all("tr", {"class": ""})
    for job in joblist:
        dict = {}
        try:
            dict["place"] = job.find("td", {"class": "local"}).get_text()
        except:
            dict["place"] = None
        try:
            dict["title"] = job.find("td", {"class": "title"}).find(
                "span", {"class": "title"}).get_text()
        except:
            dict["title"] = None
        try:
            dict["time"] = job.find("td", {"class": "data"}).get_text()
        except:
            dict["time"] = None
        try:
            dict["pay"] = job.find(
                "td", {"class": "pay"}).get_text(separator=" ")
        except:
            dict["pay"] = None
        try:
            dict["date"] = job.find("td", {"class": "regDate"}).get_text()
        except:
            dict["date"] = None
        list_a.append(dict)

    return list_a


def scrap_brands(brand_infos):
    for brand in brand_infos:
        print("Scraping :", brand["company"], brand["link"])
        page_count = get_page_count(brand)
        list_total = []
        for page in range(page_count):
            url_r = requests.get(
                f"{brand['link']}?pagesize=50&page={page + 1}")
            soup_page = BeautifulSoup(url_r.text, "html.parser")
            list_a = get_job_data(soup_page)
            list_total.extend(list_a)
        save_brands(list_total, brand)
