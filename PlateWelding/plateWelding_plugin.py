from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class PlateWelding_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='Simple_Geom',
            objectName='Plate', registerQuery=False)
        pickedDefault = ''
        self.L_pKw = AFXFloatKeyword(self.cmd, 'L_p', True)
        self.d_pKw = AFXFloatKeyword(self.cmd, 'd_p', True)
        self.w_pKw = AFXFloatKeyword(self.cmd, 'w_p', True)
        self.a_fKw = AFXFloatKeyword(self.cmd, 'a_f', True)
        self.thetaKw = AFXFloatKeyword(self.cmd, 'theta', True)
        self.Button2Kw = AFXBoolKeyword(self.cmd, 'Button2', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.table2Kw = AFXTableKeyword(self.cmd, 'table2', True)
        self.table2Kw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.table2Kw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.table2Kw.setColumnType(2, AFXTABLE_TYPE_FLOAT)
        self.Button1Kw = AFXBoolKeyword(self.cmd, 'Button1', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.table1Kw = AFXTableKeyword(self.cmd, 'table1', True)
        self.table1Kw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.table1Kw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.Button5Kw = AFXBoolKeyword(self.cmd, 'Button5', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.table5Kw = AFXTableKeyword(self.cmd, 'table5', True)
        self.table5Kw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.table5Kw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.Button3Kw = AFXBoolKeyword(self.cmd, 'Button3', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.table3Kw = AFXTableKeyword(self.cmd, 'table3', True)
        self.table3Kw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.table3Kw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.table3Kw.setColumnType(2, AFXTABLE_TYPE_FLOAT)
        self.Button4Kw = AFXBoolKeyword(self.cmd, 'Button4', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.table4Kw = AFXTableKeyword(self.cmd, 'table4', True)
        self.table4Kw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.table4Kw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.Button6Kw = AFXBoolKeyword(self.cmd, 'Button6', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.table6Kw = AFXTableKeyword(self.cmd, 'table6', True)
        self.table6Kw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.table6Kw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.partNumKw = AFXFloatKeyword(self.cmd, 'partNum', True)
        self.globalSizeKw = AFXFloatKeyword(self.cmd, 'globalSize', True, 8)
        self.upNumKw = AFXFloatKeyword(self.cmd, 'upNum', True, 4)
        self.dnNumKw = AFXFloatKeyword(self.cmd, 'dnNum', True, 4)
        self.tkNumKw = AFXFloatKeyword(self.cmd, 'tkNum', True)
        if not self.radioButtonGroups.has_key('GroupBox'):
            self.GroupBoxKw1 = AFXIntKeyword(None, 'GroupBoxDummy', True)
            self.GroupBoxKw2 = AFXStringKeyword(self.cmd, 'GroupBox', True)
            self.radioButtonGroups['GroupBox'] = (self.GroupBoxKw1, self.GroupBoxKw2, {})
        self.radioButtonGroups['GroupBox'][2][7] = 'Heat transfer'
        if not self.radioButtonGroups.has_key('GroupBox'):
            self.GroupBoxKw1 = AFXIntKeyword(None, 'GroupBoxDummy', True)
            self.GroupBoxKw2 = AFXStringKeyword(self.cmd, 'GroupBox', True)
            self.radioButtonGroups['GroupBox'] = (self.GroupBoxKw1, self.GroupBoxKw2, {})
        self.radioButtonGroups['GroupBox'][2][8] = 'Coupled temp-displacement'
        self.Tp1Kw = AFXFloatKeyword(self.cmd, 'Tp1', True)
        self.Mnoi1Kw = AFXFloatKeyword(self.cmd, 'Mnoi1', True, 10000)
        self.ISI1Kw = AFXFloatKeyword(self.cmd, 'ISI1', True)
        self.ISM1Kw = AFXFloatKeyword(self.cmd, 'ISM1', True)
        self.ISMa1Kw = AFXFloatKeyword(self.cmd, 'ISMa1', True)
        self.Mat1Kw = AFXFloatKeyword(self.cmd, 'Mat1', True)
        self.Tp2Kw = AFXFloatKeyword(self.cmd, 'Tp2', True)
        self.Mnoi2Kw = AFXFloatKeyword(self.cmd, 'Mnoi2', True, 10000)
        self.ISI2Kw = AFXFloatKeyword(self.cmd, 'ISI2', True)
        self.ISM2Kw = AFXFloatKeyword(self.cmd, 'ISM2', True)
        self.ISMa2Kw = AFXFloatKeyword(self.cmd, 'ISMa2', True)
        self.Mat2Kw = AFXFloatKeyword(self.cmd, 'Mat2', True)
        self.myfilmCoeffKw = AFXFloatKeyword(self.cmd, 'myfilmCoeff', True)
        self.mysinkTemperatureKw = AFXFloatKeyword(self.cmd, 'mysinkTemperature', True, 20)
        self.myemissivityKw = AFXFloatKeyword(self.cmd, 'myemissivity', True)
        self.myambientTemperatureKw = AFXFloatKeyword(self.cmd, 'myambientTemperature', True, 20)
        self.initialTempKw = AFXFloatKeyword(self.cmd, 'initialTemp', True, 20)
        self.s_a1Kw = AFXFloatKeyword(self.cmd, 's_a1', True)
        self.weldingVKw = AFXFloatKeyword(self.cmd, 'weldingV', True)
        self.s_b1Kw = AFXFloatKeyword(self.cmd, 's_b1', True)
        self.wuKw = AFXFloatKeyword(self.cmd, 'wu', True)
        self.s_c1Kw = AFXFloatKeyword(self.cmd, 's_c1', True)
        self.wiKw = AFXFloatKeyword(self.cmd, 'wi', True)
        self.s_a2Kw = AFXFloatKeyword(self.cmd, 's_a2', True)
        self.effiKw = AFXFloatKeyword(self.cmd, 'effi', True)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import plateWeldingDB
        return plateWeldingDB.PlateWeldingDB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='3D_Plate_welding_Tool', 
    object=PlateWelding_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString='import Plate',
    applicableModules=ALL,
    version='N/A',
    author='N/A',
    description='N/A',
    helpUrl='N/A'
)
