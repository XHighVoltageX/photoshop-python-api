from photoshop import ActionDescriptor
from photoshop import ActionReference
from photoshop import Application

# This is a test script written to see how Python scripting works in executing
# Photoshop actions, ExecuteAction()
# Where did I get all this action stuffs(ActionDescriptor, ActionReference, charIDToTypeID etc)?
# It's generated by a plugin Photoshop provides or you can generate one yourself
# See https://www.adobe.com/devnet/photoshop/scripting.html

# Start up Photoshop application
# app = Dispatch('Photoshop.Application')

app = Application()

# psDisplayNoDialogs is a PS COM constant, see pscc2018.py or scripting COM
psDisplayNoDialogs = 3
for index, x in enumerate(range(50)):
    # Execute an existing action from action palette
    idPly = app.charIDToTypeID('Ply ')
    desc8 = ActionDescriptor()
    idnull = app.charIDToTypeID('null')
    ref3 = ActionReference()
    idActn = app.charIDToTypeID('Actn')
    ref3.putName(idActn, 'Sepia Toning (layer)')
    idASet = app.charIDToTypeID('ASet')
    ref3.PutName(idASet, 'Default Actions')
    desc8.putReference(idnull, ref3)
    app.executeAction(idPly, desc8, psDisplayNoDialogs)

    # Create solid color fill layer.
    idMk = app.charIDToTypeID('Mk  ')
    desc21 = ActionDescriptor()
    idNull = app.charIDToTypeID('null')
    ref12 = ActionReference()
    idContentLayer1 = app.stringIDToTypeID('contentLayer')
    ref12.putClass(idContentLayer1)
    desc21.putReference(idNull, ref12)
    idUsng = app.charIDToTypeID('Usng')
    desc22 = ActionDescriptor()
    idType = app.charIDToTypeID('Type')
    desc23 = ActionDescriptor()
    idClr = app.charIDToTypeID('Clr ')
    desc24 = ActionDescriptor()
    idRd = app.charIDToTypeID('Rd  ')
    desc24.putDouble(idRd, index)
    idGrn = app.charIDToTypeID('Grn ')
    desc24.putDouble(idGrn, index)
    idBl = app.charIDToTypeID('Bl  ')
    desc24.putDouble(idBl, index)
    idRGBC = app.charIDToTypeID('RGBC')
    desc23.putObject(idClr, idRGBC, desc24)
    idSolidColorLayer = app.StringIDToTypeID('solidColorLayer')
    desc22.putObject(idType, idSolidColorLayer, desc23)
    idContentLayer2 = app.StringIDToTypeID('contentLayer')
    desc21.putObject(idUsng, idContentLayer2, desc22)
    app.executeAction(idMk, desc21, psDisplayNoDialogs)

    # Select mask
    idSlct = app.charIDToTypeID('slct')
    desc38 = ActionDescriptor()
    idNull1 = app.charIDToTypeID('null')
    ref20 = ActionReference()
    idChnl1 = app.charIDToTypeID('Chnl')
    idChnl2 = app.charIDToTypeID('Chnl')
    idMsk = app.charIDToTypeID('Msk ')
    ref20.putEnumerated(idChnl1, idChnl2, idMsk)
    desc38.putReference(idNull1, ref20)
    idMkVs = app.charIDToTypeID('MkVs')
    desc38.putBoolean(idMkVs, False)
    app.executeAction(idSlct, desc38, psDisplayNoDialogs)

    app.activeDocument.activeLayer.invert()
