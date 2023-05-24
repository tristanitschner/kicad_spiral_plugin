#!/usr/bin/env python

from .interface import *
from math       import *
import pcbnew
import os
import wx

class MyFrame(wx.Frame):
    #super().__init__()
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = "Spiral Plugin", pos = (0,25), size = wx.Size( 350,470 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL|wx.RESIZE_BORDER) 
        self.SetMinSize(self.GetSize())
        topPanel = MyPanel(self)
        topPanel.m_sdbSizer4Cancel.Bind(wx.EVT_BUTTON, self.OnCancel)
        
    def OnCancel(self, event):
        self.Close()

class MyPanel(MyPanel12):
    #super().__init__()
    def __init__(self, parent):
        MyPanel12.__init__(self,parent)
        self.m_sdbSizer4OK.Bind(wx.EVT_BUTTON, self.OnOk)
        self.m_toggleBtn3.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleTurningDirection)
        self.m_toggleBtn5.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleUnitAngle)
        #self.m_toggleBtn31.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleUnits)
        self.m_button16.Bind(wx.EVT_BUTTON, self.OnCurrentSelection)
        self.fgSizer4.AddGrowableCol(0)
        self.fgSizer4.AddGrowableRow(0)
        self.fgSizer5.AddGrowableCol(0)
        self.fgSizer5.AddGrowableRow(0)
        self.fgSizer6.AddGrowableCol(0)
        self.fgSizer6.AddGrowableRow(0)
        self.fgSizer19.AddGrowableCol(0)
        self.fgSizer19.AddGrowableRow(0)
        self.fgSizer99.AddGrowableCol(0)
        self.fgSizer99.AddGrowableCol(2)

        self.gSizer11.AddGrowableCol(1)
        self.gSizer11.AddGrowableRow(0)
        self.gSizer11.AddGrowableRow(1)
        self.gSizer11.AddGrowableRow(2)
        self.gSizer11.AddGrowableRow(3)
        self.gSizer11.AddGrowableRow(4)
        self.gSizer11.AddGrowableRow(5)
        self.gSizer11.AddGrowableRow(6)
        self.gSizer11.AddGrowableRow(7)
        self.gSizer11.AddGrowableRow(8)
        self.gSizer11.AddGrowableRow(9)
        self.gSizer11.AddGrowableRow(10)
        self.gSizer11.AddGrowableRow(11)
        self.bSizer2.AddGrowableCol(0)
        self.bSizer2.AddGrowableRow(0)

        netcount = pcbnew.GetBoard().GetNetInfo().GetNetCount()
        # the length of the two following variables is the same
        netnames = pcbnew.GetBoard().GetNetInfo().NetsByName().keys()
        # .items() contains a list of 2-tuples containing first the name and second the NETINFO_ITEM, needed to set the netclass
        self.netitems = pcbnew.GetBoard().GetNetInfo().NetsByName().items()

        for ii in range(netcount):
            self.m_choice3.Append(str(netnames[ii]))
        layers = []
        i = pcbnew.PCBNEW_LAYER_ID_START
        version = pcbnew.Version()
        if (version.startswith("7.0")):
            while i < pcbnew.PCBNEW_LAYER_ID_START + pcbnew.GetBoard().GetCopperLayerCount() - 1:
                layers.append(pcbnew.BOARD.GetStandardLayerName(i))
                i += 1
            layers.append(pcbnew.BOARD.GetStandardLayerName(pcbnew.PCBNEW_LAYER_ID_START + 31))
        else:
            while i < pcbnew.PCBNEW_LAYER_ID_START + pcbnew.GetBoard().GetCopperLayerCount() - 1:
                layers.append(pcbnew.BOARD_GetStandardLayerName(i))
                i += 1
            layers.append(pcbnew.BOARD_GetStandardLayerName(pcbnew.PCBNEW_LAYER_ID_START + 31))
        for ii in range(len(layers)):
            self.m_choice31.Append(str(layers[ii]))
        if pcbnew.GetUserUnits() == pcbnew.EDA_UNITS_INCHES:
            self.m_staticText15.SetLabel("in")
            self.m_staticText16.SetLabel("in")
            self.m_staticText17.SetLabel("in")
            self.m_staticText20.SetLabel("in")
            self.m_staticText21.SetLabel("in")
            # set sane defaults
            # track width
            self.m_textCtrl4.SetValue(str(pcbnew.ToMils(pcbnew.FromMM(float(self.m_textCtrl4.GetValue()))/1000)))
            # distance between tracks
            self.m_textCtrl5.SetValue(str(pcbnew.ToMils(pcbnew.FromMM(float(self.m_textCtrl5.GetValue()))/1000)))
        elif pcbnew.GetUserUnits() == pcbnew.EDA_UNITS_MILS:
            self.m_staticText15.SetLabel("mil")
            self.m_staticText16.SetLabel("mil")
            self.m_staticText17.SetLabel("mil")
            self.m_staticText20.SetLabel("mil")
            self.m_staticText21.SetLabel("mil")
            # set sane defaults
            # track width
            self.m_textCtrl4.SetValue(str(ToMils(FromMM(float(self.m_textCtrl4.GetValue())))))
            # distance between tracks
            self.m_textCtrl5.SetValue(str(ToMils(FromMM(float(self.m_textCtrl5.GetValue())))))
        else:
            self.m_staticText15.SetLabel("mm")
            self.m_staticText16.SetLabel("mm")
            self.m_staticText17.SetLabel("mm")
            self.m_staticText20.SetLabel("mm")
            self.m_staticText21.SetLabel("mm")

        self.UpdateSelection()

    def AddTrack(self, x0, y0, x1, y1):
        b = pcbnew.GetBoard()
        t = pcbnew.PCB_TRACK(b)
        version = pcbnew.Version()
        print(version)
        if version.startswith("6") or version.startswith("5"):
            t.SetStart(pcbnew.wxPoint(x0,y0))
            t.SetEnd(pcbnew.wxPoint(x1,y1))
        else:
            t.SetStart(pcbnew.VECTOR2I(int(x0),int(y0)))
            t.SetEnd(pcbnew.VECTOR2I(int(x1),int(y1)))
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
        if pcbnew.GetUserUnits() == pcbnew.EDA_UNITS_INCHES:
            self.center_x          = int(pcbnew.FromMils(float(self.m_textCtrl19.GetValue())*1000))
            self.center_y          = int(pcbnew.FromMils(float(self.m_textCtrl10.GetValue())*1000))
            self.start_radius      = int(pcbnew.FromMils(float(self.m_textCtrl12.GetValue())*1000))
            self.trackwidth        = int(pcbnew.FromMils(float(self.m_textCtrl4.GetValue())*1000))
            self.dtracks           = int(pcbnew.FromMils(float(self.m_textCtrl5.GetValue())*1000))
        elif pcbnew.GetUserUnits() == pcbnew.EDA_UNITS_MILS:
            self.center_x          = int(pcbnew.FromMils(float(self.m_textCtrl19.GetValue())))
            self.center_y          = int(pcbnew.FromMils(float(self.m_textCtrl10.GetValue())))
            self.start_radius      = int(pcbnew.FromMils(float(self.m_textCtrl12.GetValue())))
            self.trackwidth        = int(pcbnew.FromMils(float(self.m_textCtrl4.GetValue())))
            self.dtracks           = int(pcbnew.FromMils(float(self.m_textCtrl5.GetValue())))
        else: # millimeters
            self.center_x          = int(1000000.0*float(self.m_textCtrl19.GetValue()))
            self.center_y          = int(1000000.0*float(self.m_textCtrl10.GetValue()))
            self.start_radius      = int(1000000.0*float(self.m_textCtrl12.GetValue()))
            self.trackwidth        = int(1000000.0*float(self.m_textCtrl4.GetValue()))
            self.dtracks           = int(1000000.0*float(self.m_textCtrl5.GetValue()))
        self.segments_per_turn = int(float(self.m_textCtrl11.GetValue()))
        self.additional_segments = int(float(self.m_textCtrl42.GetValue()))
        if self.useRadians:
            self.angle_offset = float(self.m_textCtrl8.GetValue())
        else:
            self.angle_offset = float(self.m_textCtrl8.GetValue())*pi/180.0
        self.group_name        = self.m_textCtrl6.GetValue()
        self.counterclockwise  = self.m_toggleBtn3.GetValue()
        self.chosen_netitem    = self.m_choice3.GetSelection()
        layer_selection        = self.m_choice31.GetSelection()
        if (layer_selection == pcbnew.GetBoard().GetCopperLayerCount() - 1):
            self.chosen_layer = pcbnew.PCBNEW_LAYER_ID_START + 31
        else:
            self.chosen_layer = pcbnew.PCBNEW_LAYER_ID_START + layer_selection

        g = pcbnew.PCB_GROUP(pcbnew.GetBoard())
        g.thisown = 0
        for i in range(self.nturn * self.segments_per_turn + self.additional_segments):
            t = self.AddTrack(*self.Position(i), *self.Position(i + 1))
            g.AddItem(t)
        g.SetName(self.group_name)
        pcbnew.GetBoard().Groups().append(g)
        pcbnew.Refresh()
        wx.MessageBox("Spiral added!")

    def OnToggleTurningDirection(self, event):
        if self.m_toggleBtn3.GetValue():
            self.m_toggleBtn3.SetLabel("counterclockwise")
        else:
            self.m_toggleBtn3.SetLabel("clockwise")

    useRadians = False
    def OnToggleUnitAngle(self, event):
        if self.m_toggleBtn5.GetValue():
            self.m_toggleBtn5.SetLabel("radians")
            self.useRadians = True
        else:
            self.m_toggleBtn5.SetLabel("degrees")
            self.useRadians = False

    def OnCurrentSelection(self, event):
        self.UpdateSelection()

    def UpdateSelection(self):
        selected_groups = [x for x in list(pcbnew.GetBoard().Groups()) if x.IsSelected()]
        selected_items = [x for x in pcbnew.GetBoard().GetTracks() +
                pcbnew.GetBoard().GetFootprints() + list(pcbnew.GetBoard().GetPads()) if x.IsSelected()]
        #wx.MessageBox(str(selected_items))
        # WE ONLY SUPPORT EITHER ONE SELECTED ITEM OR ONE SELECTED GROUP
        # How is a selection internally represented?
        if (selected_groups):
            #g = PCB_GROUP(GetBoard()) # ok, it seems that kicad treats a group
            #g.thisown = 0
            # the same as another, if it contains the same items, regardless of
            # other metadata, so because this group is not added to the board, it
            # results is a segfault, as thisown = 1 and it gets deleted upon
            # leaving this function
            x, y = selected_groups[0].GetBoundingBox().GetCenter()
            if pcbnew.GetUserUnits() == pcbnew.EDA_UNITS_INCHES:
                self.m_textCtrl19.SetValue(str(ToMils(x)/1000))
                self.m_textCtrl10.SetValue(str(ToMils(y)/1000))
            elif pcbnew.GetUserUnits() == pcbnew.EDA_UNITS_MILS:
                self.m_textCtrl19.SetValue(str(ToMils(x)))
                self.m_textCtrl10.SetValue(str(ToMils(y)))
            else:
                self.m_textCtrl19.SetValue(str(ToMM(x)))
                self.m_textCtrl10.SetValue(str(ToMM(y)))
        elif (selected_items):
            if pcbnew.GetUserUnits() == pcbnew.EDA_UNITS_INCHES:
                self.m_textCtrl19.SetValue(str(ToMils(selected_items[0].GetPosition()[0])/1000))
                self.m_textCtrl10.SetValue(str(ToMils(selected_items[0].GetPosition()[1])/1000))
            elif pcbnew.GetUserUnits() == pcbnew.EDA_UNITS_MILS:
                self.m_textCtrl19.SetValue(str(ToMils(selected_items[0].GetPosition()[0])))
                self.m_textCtrl10.SetValue(str(ToMils(selected_items[0].GetPosition()[1])))
            else: # millimeters
                self.m_textCtrl19.SetValue(str(ToMM(selected_items[0].GetPosition()[0])))
                self.m_textCtrl10.SetValue(str(ToMM(selected_items[0].GetPosition()[1])))

class SpiralPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Spiral"
        self.category = "Modify PCB"
        self.description = "Creates spiral tracks"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'spiral.png')
        self.show_toolbar_button = True # change this later

    def Run(self):
        MyFrame(None).ShowWithEffect(wx.SHOW_EFFECT_EXPAND,200)


# default track width:
# trackwidth = GetBoard().GetDesignSettings().GetNetClasses().GetDefault().GetTrackWidth()

# netclasses:
# GetBoard().GetDesignSettings().GetNetClasses().NetClasses().items()
# the default netclass is stored elsewhere:
# GetBoard().GetDesignSettings().GetNetClasses().GetDefault()
