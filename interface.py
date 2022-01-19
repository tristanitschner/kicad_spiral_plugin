# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyPanel12
###########################################################################

class MyPanel12 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 452,386 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Name (for group)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer10.Add( self.m_staticText8, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, u"spiral", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_textCtrl6, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( gSizer10, 1, wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Net name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gSizer11.Add( self.m_staticText9, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		gSizer11.Add( self.m_choice3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( gSizer11, 1, wx.EXPAND, 5 )

		gSizer111 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Layer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		gSizer111.Add( self.m_staticText91, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		m_choice31Choices = []
		self.m_choice31 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice31Choices, 0 )
		self.m_choice31.SetSelection( 0 )
		gSizer111.Add( self.m_choice31, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( gSizer111, 1, wx.EXPAND, 5 )

		gSizer14 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Center x,y (in mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gSizer14.Add( self.m_staticText13, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_textCtrl9, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.m_textCtrl10, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer14.Add( gSizer15, 1, wx.EXPAND, 5 )


		bSizer2.Add( gSizer14, 1, wx.EXPAND, 5 )

		gSizer17 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Start diameter (in mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		gSizer17.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer17.Add( self.m_textCtrl12, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( gSizer17, 1, wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Number of turns", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )

		gSizer16 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Segments per turn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer16.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, u"64", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.m_textCtrl11, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( gSizer16, 1, wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Track width (in mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gSizer2.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, u"0.25", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Distance between tracks (in mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gSizer6.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, u"0.5", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_textCtrl5, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( gSizer6, 1, wx.EXPAND, 5 )

		gSizer13 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer2.Add( gSizer13, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Angle offset (in degrees)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer9.Add( self.m_staticText10, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl8, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( gSizer9, 1, wx.EXPAND, 5 )

		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Turning direction", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer12.Add( self.m_staticText11, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_toggleBtn3 = wx.ToggleButton( self, wx.ID_ANY, u"clockwise", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_toggleBtn3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( gSizer12, 1, wx.EXPAND, 5 )

		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
		self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
		m_sdbSizer4.Realize();

		bSizer2.Add( m_sdbSizer4, 1, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

	def __del__( self ):
		pass


