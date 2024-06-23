import sys
from datetime import datetime
from fetcher import scrape_fiscal_reports_by_date, download_pdfs
from vectorstore import upload_new_files

args = sys.argv

date = datetime.today()
if len(args) > 1:
    date = datetime.strptime(args[1], '%Y%m%d')

print(f"Target date: {date.strftime('%Y%m%d')}")

data = scrape_fiscal_reports_by_date(date)
download_pdfs(data, date)
upload_new_files()

print("Done")

