from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class PlateWeldingDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'Plate welding Simulation Tool Sl(mm)',
            self.OK|self.APPLY|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('Apply')
            
        TabBook_1 = FXTabBook(p=self, tgt=None, sel=0,
            opts=TABBOOK_NORMAL,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_1, text='Part', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_1 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        HFrame_1 = FXHorizontalFrame(p=TabItem_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_1 = FXGroupBox(p=HFrame_1, text='Geometry', opts=FRAME_GROOVE)
        HFrame_2 = FXHorizontalFrame(p=GroupBox_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        VFrame_1 = FXVerticalFrame(p=HFrame_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VFrame_1, ncols=12, labelText='Length[mm]:', tgt=form.L_pKw, sel=0)
        AFXTextField(p=VFrame_1, ncols=12, labelText='    d[mm]    :', tgt=form.d_pKw, sel=0)
        AFXTextField(p=VFrame_1, ncols=12, labelText='    w[mm]    :', tgt=form.w_pKw, sel=0)
        AFXTextField(p=VFrame_1, ncols=12, labelText='    a[mm]    :', tgt=form.a_fKw, sel=0)
        AFXTextField(p=VFrame_1, ncols=12, labelText='    \xa6\xc8[\xa1\xe3]        :', tgt=form.thetaKw, sel=0)
        l = FXLabel(p=VFrame_1, text='Attention: Please use 89.9\xa1\xe3 instead of 90\xa1\xe3 in \xa6\xc8!', opts=JUSTIFY_LEFT)
        fileName = os.path.join(thisDir, 'template.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=HFrame_1, text='', ic=icon)
        tabItem = FXTabItem(p=TabBook_1, text='Property', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_3 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        VFrame_2 = FXVerticalFrame(p=TabItem_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        HFrame_5 = FXHorizontalFrame(p=VFrame_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_4 = FXGroupBox(p=HFrame_5, text='Coupled temp-displacement', opts=FRAME_GROOVE)
        FXCheckButton(p=GroupBox_4, text='Elastic', tgt=form.Button2Kw, sel=0)
        vf = FXVerticalFrame(GroupBox_4, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 6, 4, 6, 4, form.table2Kw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 155)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 105)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setColumnWidth(3, 70)
        table.setColumnType(3, AFXTable.FLOAT)
        table.setLeadingRowLabels("Young's Modulus[MPa]\tPoisson's Ratio\tTemp[\xa1\xe3c]")
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        GroupBox_3 = FXGroupBox(p=HFrame_5, text='Coupled temp-displacement&Heat transfer', opts=FRAME_GROOVE)
        FXCheckButton(p=GroupBox_3, text='Density', tgt=form.Button1Kw, sel=0)
        vf = FXVerticalFrame(GroupBox_3, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 6, 3, 6, 3, form.table1Kw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 145)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 70)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels('Mass Density[t/mm3]\tTemp[\xa1\xe3c]')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        GroupBox_2 = FXGroupBox(p=HFrame_5, text='Coupled temp-displacement&Heat transfer', opts=FRAME_GROOVE)
        FXCheckButton(p=GroupBox_2, text='Conductivity', tgt=form.Button5Kw, sel=0)
        vf = FXVerticalFrame(GroupBox_2, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 6, 3, 6, 3, form.table5Kw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 152)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 100)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels('Conductivity[w/(m*k)]\tTemp[\xa1\xe3c]')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        HFrame_3 = FXHorizontalFrame(p=VFrame_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_7 = FXGroupBox(p=HFrame_3, text='Coupled temp-displacement', opts=FRAME_GROOVE)
        FXCheckButton(p=GroupBox_7, text='Plastic', tgt=form.Button3Kw, sel=0)
        vf = FXVerticalFrame(GroupBox_7, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 6, 4, 6, 4, form.table3Kw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 155)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 105)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setColumnWidth(3, 70)
        table.setColumnType(3, AFXTable.FLOAT)
        table.setLeadingRowLabels('Yield stress[MPa]\tPlastic strain\tTemp[\xa1\xe3c]')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        GroupBox_6 = FXGroupBox(p=HFrame_3, text='Coupled temp-displacement', opts=FRAME_GROOVE)
        FXCheckButton(p=GroupBox_6, text='Expansion', tgt=form.Button4Kw, sel=0)
        vf = FXVerticalFrame(GroupBox_6, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 6, 3, 6, 3, form.table4Kw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 145)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 92)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels('Expansion Coeff[1/K]\tTemp[\xa1\xe3c]')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        GroupBox_5 = FXGroupBox(p=HFrame_3, text='Coupled temp-displacement&Heat transfer', opts=FRAME_GROOVE)
        FXCheckButton(p=GroupBox_5, text='SpecificHeat', tgt=form.Button6Kw, sel=0)
        vf = FXVerticalFrame(GroupBox_5, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 6, 3, 6, 3, form.table6Kw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 152)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 100)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels('specific Heat[mJ/(t*K)]\tTemp[\xa1\xe3c]')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        HFrame_4 = FXHorizontalFrame(p=VFrame_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        l = FXLabel(p=HFrame_4, text='Note: The material is measured in Sl (mm) units.The values of Conductivity and Expansion Coeff are the same in both Sl and Sl (mm) unit system.', opts=JUSTIFY_LEFT)
        tabItem = FXTabItem(p=TabBook_1, text='Mesh', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_4 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        GroupBox_8 = FXGroupBox(p=TabItem_4, text='Seed Edges', opts=FRAME_GROOVE)
        HFrame_10 = FXHorizontalFrame(p=GroupBox_8, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_10, ncols=12, labelText=' partNum :', tgt=form.partNumKw, sel=0)
        l = FXLabel(p=HFrame_10, text='Divided into partNum parts along the Length direction.Length/partNum must be an integer!', opts=JUSTIFY_LEFT)
        HFrame_9 = FXHorizontalFrame(p=GroupBox_8, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_9, ncols=12, labelText='globalSize:', tgt=form.globalSizeKw, sel=0)
        l = FXLabel(p=HFrame_9, text='Just keep it as default', opts=JUSTIFY_LEFT)
        HFrame_8 = FXHorizontalFrame(p=GroupBox_8, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_8, ncols=12, labelText='  upNum  :', tgt=form.upNumKw, sel=0)
        l = FXLabel(p=HFrame_8, text='Just keep it as default', opts=JUSTIFY_LEFT)
        HFrame_7 = FXHorizontalFrame(p=GroupBox_8, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_7, ncols=12, labelText='  dnNum  :', tgt=form.dnNumKw, sel=0)
        l = FXLabel(p=HFrame_7, text='Just keep it as default', opts=JUSTIFY_LEFT)
        HFrame_6 = FXHorizontalFrame(p=GroupBox_8, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_6, ncols=12, labelText='  tkNum   :', tgt=form.tkNumKw, sel=0)
        l = FXLabel(p=HFrame_6, text='d/tkNum must be an integer! Suggestion tkNum=d', opts=JUSTIFY_LEFT)
        l = FXLabel(p=GroupBox_8, text='Attention:Length/partNum/(d/tkNum) also must be an integer!', opts=JUSTIFY_LEFT)
        tabItem = FXTabItem(p=TabBook_1, text='Step', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_5 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        HFrame_11 = FXHorizontalFrame(p=TabItem_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_12 = FXGroupBox(p=HFrame_11, text='Procedure type', opts=FRAME_GROOVE)
        FXRadioButton(p=GroupBox_12, text='Heat transfer', tgt=form.GroupBoxKw1, sel=7)
        FXRadioButton(p=GroupBox_12, text='Coupled temp-displacement', tgt=form.GroupBoxKw1, sel=8)
        GroupBox_11 = FXGroupBox(p=HFrame_11, text='Step-0', opts=FRAME_GROOVE|LAYOUT_FILL_Y)
        l = FXLabel(p=GroupBox_11, text='Default                                    ', opts=JUSTIFY_LEFT)
        GroupBox_9 = FXGroupBox(p=TabItem_5, text='Step-n(1=<n<=partNum)', opts=FRAME_GROOVE)
        VFrame_3 = FXVerticalFrame(p=GroupBox_9, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        HFrame_15 = FXHorizontalFrame(p=VFrame_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_15, ncols=12, labelText='Time period:', tgt=form.Tp1Kw, sel=0)
        AFXTextField(p=HFrame_15, ncols=12, labelText='Maximum number of increments:', tgt=form.Mnoi1Kw, sel=0)
        HFrame_14 = FXHorizontalFrame(p=VFrame_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        l = FXLabel(p=HFrame_14, text='                       Initial', opts=JUSTIFY_LEFT)
        l = FXLabel(p=HFrame_14, text='                 Minimum', opts=JUSTIFY_LEFT)
        l = FXLabel(p=HFrame_14, text='          Maximum', opts=JUSTIFY_LEFT)
        HFrame_13 = FXHorizontalFrame(p=VFrame_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_13, ncols=12, labelText='Increment size:', tgt=form.ISI1Kw, sel=0)
        AFXTextField(p=HFrame_13, ncols=12, labelText='.', tgt=form.ISM1Kw, sel=0)
        AFXTextField(p=HFrame_13, ncols=12, labelText='.', tgt=form.ISMa1Kw, sel=0)
        HFrame_12 = FXHorizontalFrame(p=VFrame_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_12, ncols=12, labelText='Max, allowable temperature change per increment:', tgt=form.Mat1Kw, sel=0)
        GroupBox_10 = FXGroupBox(p=TabItem_5, text='Step-release', opts=FRAME_GROOVE)
        VFrame_4 = FXVerticalFrame(p=GroupBox_10, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        HFrame_19 = FXHorizontalFrame(p=VFrame_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_19, ncols=12, labelText='Time period:', tgt=form.Tp2Kw, sel=0)
        AFXTextField(p=HFrame_19, ncols=12, labelText='Maximum number of increments:', tgt=form.Mnoi2Kw, sel=0)
        HFrame_18 = FXHorizontalFrame(p=VFrame_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        l = FXLabel(p=HFrame_18, text='                       Initial', opts=JUSTIFY_LEFT)
        l = FXLabel(p=HFrame_18, text='                 Minimum', opts=JUSTIFY_LEFT)
        l = FXLabel(p=HFrame_18, text='          Maximum', opts=JUSTIFY_LEFT)
        HFrame_17 = FXHorizontalFrame(p=VFrame_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_17, ncols=12, labelText='Increment size:', tgt=form.ISI2Kw, sel=0)
        AFXTextField(p=HFrame_17, ncols=12, labelText='.', tgt=form.ISM2Kw, sel=0)
        AFXTextField(p=HFrame_17, ncols=12, labelText='.', tgt=form.ISMa2Kw, sel=0)
        HFrame_16 = FXHorizontalFrame(p=VFrame_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_16, ncols=12, labelText='Max, allowable temperature change per increment:', tgt=form.Mat2Kw, sel=0)
        tabItem = FXTabItem(p=TabBook_1, text='Interaction', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_6 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        VFrame_5 = FXVerticalFrame(p=TabItem_6, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_14 = FXGroupBox(p=VFrame_5, text='Surface film condition', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        HFrame_20 = FXHorizontalFrame(p=GroupBox_14, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_20, ncols=12, labelText='Film coefficient:', tgt=form.myfilmCoeffKw, sel=0)
        AFXTextField(p=HFrame_20, ncols=12, labelText='Sink temperature:', tgt=form.mysinkTemperatureKw, sel=0)
        GroupBox_13 = FXGroupBox(p=VFrame_5, text='Surface radiation', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        HFrame_21 = FXHorizontalFrame(p=GroupBox_13, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_21, ncols=12, labelText='Emissivity:', tgt=form.myemissivityKw, sel=0)
        AFXTextField(p=HFrame_21, ncols=12, labelText='Ambient temperature:', tgt=form.myambientTemperatureKw, sel=0)
        tabItem = FXTabItem(p=TabBook_1, text='Load', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_2 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        HFrame_22 = FXHorizontalFrame(p=TabItem_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        VFrame_6 = FXVerticalFrame(p=HFrame_22, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_16 = FXGroupBox(p=VFrame_6, text='Predefined Field', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        AFXTextField(p=GroupBox_16, ncols=12, labelText='Initial Temperature Magnitude:', tgt=form.initialTempKw, sel=0)
        GroupBox_15 = FXGroupBox(p=VFrame_6, text='Body heat Dflux', opts=FRAME_GROOVE)
        HFrame_27 = FXHorizontalFrame(p=GroupBox_15, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_27, ncols=12, labelText='a1:', tgt=form.s_a1Kw, sel=0)
        AFXTextField(p=HFrame_27, ncols=12, labelText='weldingV:', tgt=form.weldingVKw, sel=0)
        HFrame_26 = FXHorizontalFrame(p=GroupBox_15, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_26, ncols=12, labelText=' b :', tgt=form.s_b1Kw, sel=0)
        AFXTextField(p=HFrame_26, ncols=12, labelText='    wu     :', tgt=form.wuKw, sel=0)
        HFrame_25 = FXHorizontalFrame(p=GroupBox_15, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_25, ncols=12, labelText=' c :', tgt=form.s_c1Kw, sel=0)
        AFXTextField(p=HFrame_25, ncols=12, labelText='    wi      :', tgt=form.wiKw, sel=0)
        HFrame_24 = FXHorizontalFrame(p=GroupBox_15, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_24, ncols=12, labelText='a2:', tgt=form.s_a2Kw, sel=0)
        AFXTextField(p=HFrame_24, ncols=12, labelText='    effi    :', tgt=form.effiKw, sel=0)
        HFrame_23 = FXHorizontalFrame(p=GroupBox_15, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        l = FXLabel(p=HFrame_23, text='weldingV: Welding speed; wu: Arc voltage; wi: electric current; effi: thermal efficiency', opts=JUSTIFY_LEFT)
        fileName = os.path.join(thisDir, 'heatsource.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=HFrame_22, text='', ic=icon)
