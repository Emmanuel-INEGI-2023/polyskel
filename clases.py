import shapefile
import polyskel
#from fiona import open

def enum(v):
    return v+1

class Convertir:
    def __init__(self,_s_,_f):
        self._nom = _s_
        self._file = open("%s.json" % _s_,"w")
        self._fac = _f
        self.mm = [] 
        self._mx = 0
        self._my = 0

    def simpliPoly(_s):
        _newPol = []
        for _r in shapefile.Reader(_s._nom).shapeRecords():
            _row, _coo = _r.shape.__geo_interface__,_r.shape.__geo_interface__["coordinates"]
            for i in range(len(_coo)):
                _canC = len(_coo[i])
                [_row["coordinates"][i].pop(j) for j in range(1,int(_canC/2))]
            _newPol.append(_row)
        return _newPol
                    

    def Skeletor(_s,_n):
        _lines,e = [],0
        for _r in shapefile.Reader(_n).shapeRecords():
            _coo = _r.shape.__geo_interface__["coordinates"]
            pol, holes = _coo[0], _coo[1:] if len(_coo)>1 else []
            skeleton = polyskel.skeletonize(pol,holes)
            for arc in skeleton:
                for sink in arc.sinks:
                    e = enum(e)
                    _lines.append([(arc.source.x, arc.source.y),(sink.x, sink.y)])
        return _lines
    
    def SkeletorFet(_s,_g_):
        _lines,e = [],0
        pol, holes = _g_[0], _g_[1:] if len(_g_)>1 else []
        try:
            skeleton = polyskel.skeletonize(pol,holes)
            for arc in skeleton:
                for sink in arc.sinks:
                    e = enum(e)
                    _lines.append([(arc.source.x, arc.source.y),(sink.x, sink.y)])
            return _lines
        except Exception as e:
            print(e)

    def crearShp(_s,_dat,_tip,_proc):
        id=1
        schema = {'geometry':_tip,'properties': {'id': 'int','principal':'bool'}}
        _file = '%s%s.shp' % (_s._nom.split('\\')[-1],_proc)
        with open(_file, 'w', 'ESRI Shapefile', schema,crs = "EPSG:4326") as c:
            for _d in _dat:
                c.write({'geometry':_d,'properties': {'id': id,'principal':True}})
                id += 1
        return _file
            

                
 
