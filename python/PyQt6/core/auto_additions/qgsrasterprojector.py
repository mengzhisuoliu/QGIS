# The following has been generated automatically from src/core/raster/qgsrasterprojector.h
QgsRasterProjector.Approximate = QgsRasterProjector.Precision.Approximate
QgsRasterProjector.Exact = QgsRasterProjector.Precision.Exact
QgsRasterProjector.Precision.baseClass = QgsRasterProjector
try:
    QgsRasterProjector.precisionLabel = staticmethod(QgsRasterProjector.precisionLabel)
    QgsRasterProjector.extentSize = staticmethod(QgsRasterProjector.extentSize)
    QgsRasterProjector.__overridden_methods__ = ['clone', 'bandCount', 'dataType', 'block']
    QgsRasterProjector.__group__ = ['raster']
except (NameError, AttributeError):
    pass
