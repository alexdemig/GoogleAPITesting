
"""
In this file we will implement methods for communication with a google docs spreadsheet, for extracting information from it and formatting it in an adequate manner.
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class ExcelGatherer():
    """This object will contain all methods interacting with google spreadsheets, given credentials"""
    def __init__(self, file_location):
        self.file_location = file_location
        self.col_headers = []
        self.sheet = ''

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.file_location, scope)
        self.client = gspread.authorize(credentials)
        # print(self.client.list_spreadsheet_files())
        # print(self.client.list_spreadsheet_files()[0]['name'])

        # list_spreadsheet_files gets a list of a dict that contains misc. information, including the spreadsheet we have access to
        # the implementation is ugly, but the only way to interact with the Gspread API to extract the spreadsheet name
        self.spreadsheet_title = self.client.list_spreadsheet_files()[0]['name']
        try:
            self.spreadsheet = self.client.open(self.spreadsheet_title)
            # Sets the worksheet as the first one by default
            self.sheet = self.spreadsheet.get_worksheet(0)
            print("success")
            # testing:
            # self.worksheets_list = spreadsheet.worksheets()
            # print(type(self.worksheets_list)
            # self.sheet = spreadsheet.worksheet(self.worksheets_list[0])
        except gspread.exceptions.SpreadsheetNotFound:
                print("No spreadsheet named {self.spreadsheet_title} found\n")

    def GetWorksheets(self):
        self.worksheets_list = self.spreadsheet.worksheets()
        return self.worksheets_list

    def SetCurrentWorksheet(self, worksheet_to_be_used):
        self.sheet = self.spreadsheet.worksheet(worksheet_to_be_used)

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
    objName = ExcelGatherer('ProyectoPrueba.json')
    objName.GetHeaders()
    dictio = objName.GetColumns()
    print(type(dictio['ID']))

    # print(objName.list_spreadsheet_files())
