#!/usr/bin/env python3

import sys

from OCC.Display.backend import load_pyqt5, load_backend
from OCC.Display.backend import get_qt_modules
import OCC.Core.BRepPrimAPI

if not load_pyqt5():
	print("pyqt5 required to run this test")
	sys.exit()

load_backend("qt-pyqt5")
QtCore, QtGui, QtWidgets, QtOpenGL = get_qt_modules()

import zencad.gui.display


QAPP = None
DISPLAY = None

def init_display_only_mode() -> zencad.gui.display.DisplayWidget:
	global QAPP
	global DISPLAY


	if QAPP is not None:
		raise Exception("QApplication is inited early")

	QAPP = QtWidgets.QApplication(sys.argv[1:])
	DISPLAY = zencad.gui.display.DisplayWidget()

def exec_display_only_mode():
	DISPLAY.show()
	QAPP.exec()
	sys.exit()


if __name__ == "__main__":
	init_display_only_mode()

	my_box = OCC.Core.BRepPrimAPI.BRepPrimAPI_MakeBox(10., 20., 30.).Shape()
	DISPLAY._display.DisplayShape(my_box, update=True)

	exec_display_only_mode()