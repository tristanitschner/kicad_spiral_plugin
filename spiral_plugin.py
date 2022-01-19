#!/usr/bin/env python

import wx
import os
from pcbnew import *
from .interface import *
from math import *

## TODO:
# refactor code
# add icon
# publish on github

class MyFrame(wx.Frame):
    #super().__init__()
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = "Spiral Plugin", pos = wx.DefaultPosition, size = wx.Size( 436,404 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL)
        topPanel = MyPanel(self)
        topPanel.m_sdbSizer4Cancel.Bind(wx.EVT_BUTTON, self.OnCancel)

    def OnCancel(self, event):
        self.Close()
    
class MyPanel(MyPanel12):
    #super().__init__()
    def __init__(self, parent):
        MyPanel12.__init__(self,parent)
        self.m_sdbSizer4OK.Bind(wx.EVT_BUTTON, self.OnOk)
        self.m_toggleBtn3.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle)

        # the length of the three follows variables is the same
        netcount = GetBoard().GetNetInfo().GetNetCount()
        netnames = GetBoard().GetNetInfo().NetsByName().keys()
        # .items() contains a list of 2-tuples containing first the name and second the NETINFO_ITEM, needed to set the netclass
        self.netitems = GetBoard().GetNetInfo().NetsByName().items()

        for ii in range(netcount):
            self.m_choice3.Append(str(netnames[ii]))
        layers = []
        i = PCBNEW_LAYER_ID_START
        while i < PCBNEW_LAYER_ID_START + GetBoard().GetCopperLayerCount() - 1:
            layers.append(BOARD_GetStandardLayerName(i))
            i += 1
        layers.append(BOARD_GetStandardLayerName(PCBNEW_LAYER_ID_START + 31))
        for ii in range(len(layers)):
            self.m_choice31.Append(str(layers[ii]))

    nturn = 10
    trackwidth = 250000
    dtracks = 1000000
    segments_per_turn = 36
    start_radius = 0
    counterclockwise = 0
    layer = ""
    netitems = []
    chosen_netitems = 0
    chosen_layer = 0
    group_name = ""
    center_x = 0
    center_y = 0
    angle_offset = 0

    def AddTrack(self, x0, y0, x1, y1):
        b = GetBoard()
        t = PCB_TRACK(b)
        t.SetStart(wxPoint(x0,y0))
        t.SetEnd(wxPoint(x1,y1))
        t.SetWidth(self.trackwidth)
        t.SetNet(self.netitems[self.chosen_netitem][1])
        t.SetLayer(self.chosen_layer)
        b.Add(t)
        return t

    def Position(self, i):
        delta_phi = 2*pi / self.segments_per_turn
        delta_r = self.dtracks / self.segments_per_turn
        if (self.counterclockwise): 
            phi = delta_phi*i + self.angle_offset
        else:
            phi = delta_phi*i - self.angle_offset
        r = delta_r*i + self.start_radius
        x = r*cos(phi) + self.center_x
        if (not self.counterclockwise): 
            y = r*sin(phi) + self.center_y
        else:
            y = -r*sin(phi) + self.center_y
        print("Position " + str(x) + "," + str(y))
        return x,y

    def OnOk(self, event):
        self.nturn             = int(float(self.m_textCtrl1.GetValue()))
        self.trackwidth        = int(1000000.0*float(self.m_textCtrl4.GetValue()))
        self.dtracks           = int(1000000.0*float(self.m_textCtrl5.GetValue()))
        self.segments_per_turn = int(float(self.m_textCtrl11.GetValue()))
        self.angle_offset      = float(self.m_textCtrl8.GetValue())*pi/180.0
        self.group_name        = self.m_textCtrl6.GetValue()
        self.center_x          = int(1000000.0*float(self.m_textCtrl9.GetValue()))
        self.center_y          = int(1000000.0*float(self.m_textCtrl10.GetValue()))
        self.start_radius      = int(1000000.0*float(self.m_textCtrl12.GetValue()))
        self.counterclockwise  = self.m_toggleBtn3.GetValue()
        self.chosen_netitem    = self.m_choice3.GetSelection()
        layer_selection        = self.m_choice31.GetSelection()
        if (layer_selection == GetBoard().GetCopperLayerCount()):
            self.chosen_layer = PCBNEW_LAYER_ID_START + 31
        else:
            self.chosen_layer = PCBNEW_LAYER_ID_START + layer_selection
        
        g = PCB_GROUP(GetBoard())
        for i in range(self.nturn * self.segments_per_turn):
            first = self.Position(i)
            second = self.Position(i+1)
            t = self.AddTrack(first[0], first[1], second[0], second[1])
            g.AddItem(t)
        g.SetName(self.group_name)
        GetBoard().Add(g)
        Refresh()
        wx.MessageBox("Spiral added!")

    def OnToggle(self, event):
        if self.m_toggleBtn3.GetValue():
            self.m_toggleBtn3.SetLabel("counterclockwise")
        else:
            self.m_toggleBtn3.SetLabel("clockwise")

class SpiralPlugin(ActionPlugin):
    """Class that gathers the actionplugin stuff"""
    def defaults(self):
        self.name = "Spiral"
        self.category = "Modify PCB"
        self.description = "Creates spiral tracks"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'spiral.png')
        self.show_toolbar_button = True # change this later

    def Run(self):
        #AddTrack(0,0,10000000,10000000)
        MyFrame(None).ShowWithEffect(wx.SHOW_EFFECT_EXPAND,200)
