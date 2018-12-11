
"""
This file contains the auxiliary classes that the GUI uses such as TextField, DropDownList, MyPanel1
"""

import wx


class TextField():
    def __init__(self, parent, label, id, default_value, label_size=(160, 25), text_size=(120, 25)):
        # sizer for text and textctrl
        self.field_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # components of the field
        self.field_text = wx.StaticText(parent, wx.ID_ANY, label, size=label_size, style=wx.ST_NO_AUTORESIZE | wx.ALIGN_LEFT)
        self.field_text_box = wx.TextCtrl(parent, id, default_value, size=text_size, style=wx.ALIGN_LEFT | wx.TE_RICH2 | wx.TE_PROCESS_ENTER)
        # components added to sizer
        self.field_sizer.Add(self.field_text, 0, wx.ALL)
        self.field_sizer.Add(self.field_text_box, 0, wx.ALL)

    def Enable(self, enable):
        self.static_text.Enable(enable)
        self.field_text_box.Enable(enable)

    def GetSizer(self):
        return self.field_sizer

    def GetText(self, index):
        return self.field_text_box.GetValue()

    def SetText(self, new_text):
        self.field_text_box.SetValue(new_text)


class MyPanel1(wx.Panel):
    """Temporary class to test the notebook functinality"""
    def __init__(self, parent):
        super(MyPanel1, self).__init__(parent)
        text = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(400, 400))


class DropDownList():
    """Builds a drop menu given the label, fields to be chosen, etc."""
    def __init__(self, parent, label, id, number_fields, default_value, choices, label_size=(150, 25), opt_list_size=(130, 25)):
        # for internal use
        self.choices = choices
        # sizer for text and combobox
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Components of a dropdown menu:
        self.static_text = wx.StaticText(parent, wx.ID_ANY, label, size=(150, 25), style=wx.ALIGN_LEFT | wx.ST_NO_AUTORESIZE)
        # syntax to be used:
        # self.static_text = wx.StaticText(parent, id=ID_ANY, label=EmptyString, pos=DefaultPosition, size=DefaultSize, style=0, name=StaticTextNameStr)
        self.options_list = wx.ComboBox(parent, id, value=default_value, size=opt_list_size, choices=choices, style=wx.CB_READONLY)
        # Components added to sizer
        self.sizer.Add(self.static_text, 0, wx.ALL)
        self.sizer.Add(self.options_list, 0, wx.ALL)

    def Enable(self, enable):
        self.static_text.Enable(enable)
        self.options_list.Enable(enable)

    def GetSizer(self):
        return self.sizer

    def GetText(self):
        return self.choices[self.options_list.GetSelection()]

    def SetOptions(self, list):
        # might need too many internal variables to be implemented (is it needed?)
        # self.options_list = wx.ComboBox(parent, id, value=default_value, size=opt_list_size, choices=choices, style=wx.CB_READONLY)
        pass

    def SetText(self, text):
        return self.options_list.SetValue(text)
