import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

base_path = "https://www.release.tdnet.info/inbs/"

def scrape_fiscal_reports_by_date(date, max_pages=100):
    url_template = base_path + "I_list_{:03d}_{}.html"
    
    date_str = date.strftime('%Y%m%d')
    
    all_data = []
    
    page_number = 1
    
    while page_number <= max_pages:
        url = url_template.format(page_number, date_str)
        print(f"Fetching {url}...")
        
        response = requests.get(url)
        
        if response.status_code == 404:
            print(f"Reached to the last page.")
            break
        
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        table = soup.find('table', id='main-list-table')
        if table:
            tr_elements = table.find_all('tr')

            for tr in tr_elements:
                title = tr.find("td", class_="kjTitle").get_text(strip=True)
                if "決算説明資料" in title:
                    row_data = {
                        "time": tr.find("td", class_="kjTime").get_text(strip=True),
                        "code": tr.find("td", class_="kjCode").get_text(strip=True),
                        "name": tr.find("td", class_="kjName").get_text(strip=True),
                        "title": title,
                        "file": tr.find("td", class_="kjTitle").find("a")["href"],
                        "xbrl": tr.find("td", class_="kjXbrl").get_text(strip=True),
                        "place": tr.find("td", class_="kjPlace").get_text(strip=True),
                        "history": tr.find("td", class_="kjHistroy").get_text(strip=True)
                    }
                    all_data.append(row_data)
        
        page_number += 1

    print(f"{len(all_data)} reports found.")
    return all_data

def download_pdfs(data_list, date, download_folder='data'):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    date_str = date.strftime('%Y%m%d')
    
    for data in data_list:
        code = data["code"]
        name = data["name"]
        title = data["title"]
        pdf_url = base_path + data['file']
        pdf_name = f"{date_str}_{code}_{name}_{title}." + data['file'].split('.')[-1]
        pdf_path = os.path.join(download_folder, pdf_name)
        
        print(f"Downloading {pdf_url} to {pdf_path}...")
        
        response = requests.get(pdf_url)
        with open(pdf_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {pdf_name}")
