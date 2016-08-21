# -*- coding: utf-8 -*-
"""
Simple examples demonstrating the use of GLMeshItem.

"""

## Add path to library (just for examples; you do not need this)

import pyqtgraph as pg
import pyqtgraph.opengl as gl

app = pg.Qt.QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('3D Graph')
w.setCameraPosition(distance=40)

xAxis = gl.GLGridItem()
yAxis = gl.GLGridItem()
zAxis = gl.GLGridItem()
yAxis.rotate(90,0,1,0)
zAxis.rotate(90,1,0,0)
xAxis.scale(2, 2, 1)
yAxis.scale(2, 2, 1)
zAxis.scale(2, 2, 1)

w.addItem(xAxis)
w.addItem(yAxis)
w.addItem(zAxis)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        pg.Qt.QtGui.QApplication.instance().exec_()
