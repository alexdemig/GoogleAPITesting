
"""
In this file we will implement the graphic user interface with which the user interacts when requesting information from the online spreadsheet
"""

import wx

button_get_credentials_id = 1
dropmenu_sheetname_chooser_id = 2
SpreadsheetNames = ['this', 'that', 'there']


class MyFrame(wx.Frame):
    """docstring for MyFrame"""
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(750, 700))

        windowsizer = wx.BoxSizer(wx.HORIZONTAL)

        # Side panel used to navigate information
        self.pnl_general = wx.Panel(self, -1)
        self.pnl_general.SetBackgroundColour(wx.WHITE)
        self.sizer_pnl_general = wx.BoxSizer(wx.VERTICAL)

        self.button_get_credentials = wx.Button(self.pnl_general, button_get_credentials_id, 'Update credentials', (100, 100))
        self.dropmenu_sheetname_chooser = DropMenu(self.pnl_general, 'Spreadsheet name', dropmenu_sheetname_chooser_id, 1, '', SpreadsheetNames)
        self.dropmenu_sheetname_chooser.Enable(False)

        self.sizer_pnl_general.Add(self.button_get_credentials, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 10)
        self.sizer_pnl_general.Add(self.dropmenu_sheetname_chooser.GetSizer(), 0, wx.ALL, 10)
        self.pnl_general.SetSizer(self.sizer_pnl_general)

        # -----------------------------------------------------------------------------------
        # main panel containing the notebook
        self.pnl_informacion = wx.Panel(self, -1)
        self.pnl_informacion.SetBackgroundColour(wx.WHITE)
        self.sizer_pnl_informacion = wx.BoxSizer(wx.VERTICAL)

        self.nb = wx.Notebook(self.pnl_informacion)
        self.nb.AddPage(MyPanel1(self.nb), "Panel1")
        self.nb.AddPage(MyPanel1(self.nb), "Panel2")
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
        self.Bind(wx.EVT_BUTTON, self.activate_drop, id=button_get_credentials_id)

    def activate_drop(self, event):
        if True:
            self.dropmenu_sheetname_chooser.Enable(True)


class MyPanel1(wx.Panel):
    """Temporary class to test the notebook functinality"""
    def __init__(self, parent):
        super(MyPanel1, self).__init__(parent)
        text = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(400, 400))


class DropMenu():
    """Builds a drop menu given the label, fields to be chosen, etc."""
    def __init__(self, parent, label, id, number_fields, default_value, choices, label_size=(150, 24), opt_list_size=(130, 24)):
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.static_text = wx.StaticText(parent, wx.ID_ANY, label=label + ':\t', size=label_size, style=wx.ALIGN_LEFT | wx.ST_NO_AUTORESIZE)
        self.opt_list = []
        self.sizer.Add(self.static_text, 0, wx.ALL)
        for i in range(0, number_fields):
            self.opt_list.append(wx.ComboBox(parent, id, size=opt_list_size, value=default_value, choices=choices, style=wx.CB_READONLY))
            self.sizer.Add(self.opt_list[i], 0, wx.ALL)
        self.choices = choices

    def GetText(self, i):
        return self.choices[self.opt_list[i].GetSelection()]

    def SetText(self, i, text):
        return self.opt_list[i].SetValue(text)

    def GetSizer(self):
        return self.sizer

    def Enable(self, enable):
        self.static_text.Enable(enable)
        for elem in self.opt_list:
            elem.Enable(enable)


class MyApp(wx.App):
    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self):
        frame = MyFrame(None, -1, 'Fetch and visualize data from Google spreadsheets')
        frame.Show(True)
        frame.Centre()
        return True


app = MyApp()
app.MainLoop()
