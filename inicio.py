import logging
from clases import Convertir as conv

if __name__ == "__main__":
	logging.basicConfig()
	_shp_ = conv(input("Ruta Shape: ") ,3500)
	_polSimp=_shp_.simpliPoly()
	_shp_._nom = _shp_.crearShp(_polSimp,'Polygon',"-simpli")
	_linSkele = _shp_.Skeletor(_shp_._nom)
	_shp_.crearShp([{'type':'LineString','coordinates':_l} for _l in _linSkele] ,'LineString',"-Skeletor2")


