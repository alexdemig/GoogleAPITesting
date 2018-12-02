
"""
In this file we will implement methods for communication with a google docs spreadsheet, for extracting information from it and formatting it in an adequate manner.
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ProyectoPrueba.json', scope)
client = gspread.authorize(creds)

sheet_title = "DATA"  # This is my temporary Google spreadsheet name

try:
    sheet = client.open(sheet_title).sheet1
    col_headers = sheet.row_values(1)
    print("Sheet headers are:")

    header_text = ""
    for elem in col_headers:
        header_text += (elem + " ")
    print(header_text)

    data_dict = {}
    for num, elem in enumerate(col_headers, start=1):
        data_dict[elem] = sheet.col_values(num)  # extracting every column and saving it in a dictionary
        data_dict[elem].pop(0)  # Remove column headers from data lists
        print(len(data_dict[elem]))

except gspread.exceptions.SpreadsheetNotFound:
    print("No spreadsheet found")
