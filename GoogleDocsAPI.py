
"""
In this file we will implement methods for communication with a google docs spreadsheet, for extracting information from it and formatting it in an adequate manner.
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# this section will be cleaned up in a final version, as of right now, it is highly personalized
file_location = 'ProyectoPrueba.json'  # This is a json that stores my access keys to the spreadsheet
spreadsheet_title = "DATA"  # This is my temporary Google spreadsheet name


class ExcelGatherer():
    """This object will contain all methods interacting with google spreadsheets, given credentials"""
    def __init__(self, file_location):
        self.file_location = file_location
        self.col_headers = []
        self.sheet = ''

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.file_location, scope)
        self.client = gspread.authorize(credentials)

    def SetAndOpenSpreadsheet(self, spreadsheet_title):
        self.sheet_title = spreadsheet_title
        try:
            self.sheet = self.client.open(self.sheet_title).sheet1
        except gspread.exceptions.SpreadsheetNotFound:
                print("No spreadsheet found")

    def GetHeaders(self):
        self.col_headers = self.sheet.row_values(1)
        print("Sheet headers are:")
        header_text = ""
        for elem in self.col_headers:
            header_text += (elem + " ")
        print(header_text)

    def GetColumns(self):
        data_dict = {}

        for num, elem in enumerate(self.col_headers, start=1):
            data_dict[elem] = self.sheet.col_values(num)  # extracting every column and saving it in a dictionary
            data_dict[elem].pop(0)  # Remove column headers from data lists
        return data_dict


#   -----------------------------------------------------------------
# Using the object:

if __name__ == "__main__":
    objName = ExcelGatherer(file_location=file_location)
    objName.SetAndOpenSpreadsheet(spreadsheet_title)
    objName.GetHeaders()
    dictio = objName.GetColumns()
    print(len(dictio))
