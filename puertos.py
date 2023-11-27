from clases import Convertir
import pathlib as ph
import json
from arcpy.da import SearchCursor as sc
from arcpy import env as e
a = [sc,e]
ws = "%s\\datos\\puertos.gdb\\" % str(ph.Path.cwd())
a[1].workspace = ws
a[1].overwriteOutput
clss =  Convertir(a[1].workspace+"\\poligon",1)
datos = [clss.SkeletorFet(json.loads(row[1])["rings"]) for row in a[0](clss._nom,["OID@","SHAPE@JSON"])]
clss.crearShp(datos,"Linestring","calis")

