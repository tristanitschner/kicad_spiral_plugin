
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE! - oh boy, too late...
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyPanel12
###########################################################################

class MyPanel12 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.bSizer2 = wx.FlexGridSizer(0,1,0,0)
		self.bSizer2.SetFlexibleDirection( wx.BOTH )
		self.bSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.gSizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
		self.gSizer11.SetFlexibleDirection( wx.BOTH )
		self.gSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Group name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.gSizer11.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, u"spiral", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gSizer11.Add( self.m_textCtrl6, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		#self.bSizer2.Add( gSizer10, 1, wx.EXPAND, 5 )


		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Net name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.gSizer11.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		self.gSizer11.Add( self.m_choice3, 0, wx.ALL|wx.EXPAND, 5 )


		self.bSizer2.Add( self.gSizer11, 1, wx.EXPAND, 5 )

		#self.gSizer111 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Layer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		self.gSizer11.Add( self.m_staticText91, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		m_choice31Choices = []
		self.m_choice31 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice31Choices, 0 )
		self.m_choice31.SetSelection( 0 )
		self.gSizer11.Add( self.m_choice31, 0, wx.ALL|wx.EXPAND, 5 )


		#self.bSizer2.Add( self.gSizer11, 1, wx.EXPAND, 5 )

		#self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		#self.bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )


		#self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"Units", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.m_staticText111.Wrap( -1 )

		#self.gSizer11.Add( self.m_staticText111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		#self.m_toggleBtn31 = wx.ToggleButton( self, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.gSizer11.Add( self.m_toggleBtn31, 0, wx.ALL|wx.EXPAND, 5 )


		#self.bSizer2.Add( gSizer121, 1, wx.EXPAND, 5 )

		#self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		#self.bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		#gSizer14 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Center x, y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.gSizer11.Add( self.m_staticText13, 0,wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		#gSizer15 = wx.GridSizer( 0, 2, 0, 0 )

	#	self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
	#	gSizer15.Add( self.m_textCtrl9, 0, wx.ALL|wx.EXPAND, 5 )


                ## coordinate x

		self.fgSizer99 = wx.FlexGridSizer( 0, 4, 0, 0 )
		self.fgSizer99.SetFlexibleDirection( wx.BOTH )
		self.fgSizer99.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl19.SetMinSize((0,-1))
		self.fgSizer99.Add( self.m_textCtrl19, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.fgSizer99.Add( self.m_staticText21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		#gSizer14.Add( gSizer15, 1, wx.EXPAND, 5 )


		#self.gSizer11.Add( self.fgSizer99, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		#self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		#gSizer15.Add( self.m_textCtrl10, 0, wx.ALL|wx.EXPAND, 5 )

                ## coordinate y


		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl10.SetMinSize((0,-1))
		self.fgSizer99.Add( self.m_textCtrl10, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.fgSizer99.Add( self.m_staticText20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		#gSizer14.Add( gSizer15, 1, wx.EXPAND, 5 )


		self.gSizer11.Add( self.fgSizer99, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		#gSizer23 = wx.GridSizer( 0, 2, 0, 0 )


		self.gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"center from selection", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gSizer11.Add( self.m_button16, 0, wx.ALL|wx.EXPAND, 5 )


		#self.bSizer2.Add( gSizer23, 1, wx.EXPAND, 5 )

		#gSizer17 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Initial radius", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.gSizer11.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		self.fgSizer4.SetFlexibleDirection( wx.BOTH )
		self.fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fgSizer4.Add( self.m_textCtrl12, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.fgSizer4.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.gSizer11.Add( self.fgSizer4, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )




		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Number of turns", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.gSizer11.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gSizer11.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		#self.bSizer2.Add( gSizer17, 1, wx.EXPAND, 5 )

		#gSizer16 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Segments per turn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.gSizer11.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, u"64", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gSizer11.Add( self.m_textCtrl11, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		#self.bSizer2.Add( gSizer16, 1, wx.EXPAND, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Additional Segments", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		self.gSizer11.Add( self.m_staticText42, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl42 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gSizer11.Add( self.m_textCtrl42, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		#gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Track width", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.gSizer11.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		self.fgSizer5.SetFlexibleDirection( wx.BOTH )
		self.fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, u"0.25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fgSizer5.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.fgSizer5.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.gSizer11.Add( self.fgSizer5, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL , 5 )


		#self.bSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )

		#gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Distance between tracks", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.gSizer11.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		self.fgSizer6.SetFlexibleDirection( wx.BOTH )
		self.fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, u"0.5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fgSizer6.Add( self.m_textCtrl5, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.fgSizer6.Add( self.m_staticText17, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.gSizer11.Add( self.fgSizer6, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL , 5 )


		#bSizer11.Add( gSizer6, 1, wx.EXPAND, 5 )

		#gSizer13 = wx.GridSizer( 0, 2, 0, 0 )


		#self.bSizer2.Add( gSizer13, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Angle offset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.gSizer11.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.fgSizer19 = wx.FlexGridSizer( 0, 2, 0, 0 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl8.SetMinSize((0,-1))
		self.fgSizer19.Add( self.m_textCtrl8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_toggleBtn5 = wx.ToggleButton( self, wx.ID_ANY, u"degrees", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fgSizer19.Add( self.m_toggleBtn5, 0, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )


		self.gSizer11.Add( self.fgSizer19, 3, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		#self.gSizer11.Add( gSizer9, 1, wx.EXPAND, 5 )

		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Turning direction", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.gSizer11.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_toggleBtn3 = wx.ToggleButton( self, wx.ID_ANY, u"clockwise", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gSizer11.Add( self.m_toggleBtn3, 0, wx.ALL|wx.EXPAND, 5 )


		#self.gSizer11.Add( gSizer12, 1, wx.EXPAND, 5 )

		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
		self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
		m_sdbSizer4.Realize();

		self.bSizer2.Add( m_sdbSizer4, 1, wx.ALIGN_RIGHT, 5 )



		self.SetSizer( self.bSizer2 )
		self.Layout()

	def __del__( self ):
		pass


