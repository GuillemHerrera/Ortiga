from qgis.core import QgsVectorLayer, QgsProject
from PyQt5.QtWidgets import QInputDialog

var = QInputDialog.getText(None, 'NOMBRE DE LA CAPA', 'Introduce el nombre sin extension')

print(var)
vlayer = QgsVectorLayer( "?query=SELECT * FROM zona_cultiu WHERE Familia = '{}'".format(var[0]), "vlayer", "virtual" )
QgsProject.instance().addMapLayer(vlayer)