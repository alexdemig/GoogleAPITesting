
"""
In this file we will implement the graphic user interface with which the user interacts when requesting information from the online spreadsheet
"""

import wx
import GUI_aux as Gaux
import GoogleDocsAPI as API

button_get_credentials_id = 1
dropmenu_sheetname_chooser_id = 2
sheet_chooser_id = 3
SpreadsheetNames = ['this', 'that', 'there']


class MyFrame(wx.Frame):
    """docstring for MyFrame"""
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(750, 700))

        # Main Objects that the GUI interacts with:
        # self.TheCollector = API.ExcelGatherer(self.pathname)
        # is declared in method:
        # GetJSONCredentials

        windowsizer = wx.BoxSizer(wx.HORIZONTAL)

        # Side panel used to navigate information
        self.pnl_general = wx.Panel(self, -1)
        self.pnl_general.SetBackgroundColour(wx.WHITE)
        self.sizer_pnl_general = wx.BoxSizer(wx.VERTICAL)

        self.button_get_credentials = wx.Button(self.pnl_general, button_get_credentials_id, 'Update credentials', (100, 100))
        self.dropmenu_sheetname_chooser = Gaux.DropDownList(self.pnl_general, 'Sheet name', dropmenu_sheetname_chooser_id, 1, '', SpreadsheetNames)
        self.dropmenu_sheetname_chooser.Enable(False)
        self.sheet_chooser = Gaux.TextField(self.pnl_general, "Introduce sheet name:", sheet_chooser_id, '', label_size=(120, 25), text_size=(120, 25))

        self.sizer_pnl_general.Add(self.button_get_credentials, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 10)
        self.sizer_pnl_general.Add(self.dropmenu_sheetname_chooser.GetSizer(), 0, wx.ALL, 10)
        self.sizer_pnl_general.Add(self.sheet_chooser.GetSizer(), 0, wx.ALL, 10)
        self.pnl_general.SetSizer(self.sizer_pnl_general)

        # -----------------------------------------------------------------------------------
        # main panel containing the notebook
        self.pnl_informacion = wx.Panel(self, -1)
        self.pnl_informacion.SetBackgroundColour(wx.WHITE)
        self.sizer_pnl_informacion = wx.BoxSizer(wx.VERTICAL)

        self.nb = wx.Notebook(self.pnl_informacion)
        self.nb.AddPage(Gaux.MyPanel1(self.nb), "Panel1")
        self.nb.AddPage(Gaux.MyPanel1(self.nb), "Panel2")
        # self.nb.Centre()
        # self.nb.Show(True)
        self.sizer_pnl_informacion.Add(self.nb, 0, wx.ALL, 10)
        self.pnl_informacion.SetSizer(self.sizer_pnl_informacion)

        windowsizer.Add(self.pnl_general, 0, wx.EXPAND, 100)
        windowsizer.Add(wx.StaticLine(self, style=wx.LI_VERTICAL), 0, wx.EXPAND | wx.ALIGN_CENTRE_HORIZONTAL, 10)
        windowsizer.Add(self.pnl_informacion, 0, wx.EXPAND, 10)

        # main SetSizer
        self.SetSizer(windowsizer)

        # Binding button and event calls
        self.Bind(wx.EVT_BUTTON, self.GetJSONCredentials, id=button_get_credentials_id)

    def GetJSONCredentials(self, event):
        with wx.FileDialog(self, "Open JSON credentials file", wildcard="Json files (*.JSON)|*.JSON", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            # the user changed their mind
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            # Proceed loading the file chosen by the user
            try:
                self.pathname = fileDialog.GetPath()
                self.TheCollector = API.ExcelGatherer(self.pathname)
                self.dropmenu_sheetname_chooser.Enable(True)
            except IOError:
                pass
                # wx.LogError("Cannot open file '%s'.")


class MyApp(wx.App):
    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self):
        frame = MyFrame(None, -1, 'Fetch and visualize data from Google spreadsheets')
        frame.Show(True)
        frame.Centre()
        return True

#   -----------------------------------------------------------------
# Using the GUI class

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
