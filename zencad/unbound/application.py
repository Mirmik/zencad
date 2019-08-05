# coding: utf-8

import zencad
import zencad.console
import zencad.texteditor
import zencad.viewadaptor
import zencad.lazifier
import zencad.opengl
import zencad.texteditor

import zencad.unbound.communicator
import zencad.unbound.actions

import pyservoce
import evalcache

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import multiprocessing
import os
import pickle
import runpy

from zencad.unbound.mainwindow import MainWindow

def start_main_application():
	print("START_MAIN_APPLICATION")
	app = QApplication([])
	
	zencad.opengl.init_opengl()
	app.setWindowIcon(QIcon(os.path.dirname(__file__) + "/../industrial-robot.svg"))
	
	#pal = app.palette()
	#pal.setColor(QPalette.Window, QColor(160, 161, 165))
	#app.setPalette(pal)
	client = zencad.unbound.communicator.Communicator(ipipe=3, opipe=4)
	
	mw = MainWindow(client_communicator=client)
	mw.show()
	
	app.aboutToQuit.connect(lambda: client.send({"cmd":"stopworld"}))
	
	app.exec()


def start_application(ipipe, opipe):
	os.dup2(ipipe, 3)
	os.dup2(opipe, 4)

	os.environ["ZENCAD_MODE"] = "MAINONLY"

	os.execve("/usr/bin/python3", ["/usr/bin/python3", "-m", "zencad"], os.environ)


def start_unbound_application(scene):
	global MAIN_COMMUNICATOR
	global DISPLAY_WINID

	ipipe = os.pipe()
	opipe = os.pipe()

	proc = multiprocessing.Process(target = start_application, args=(opipe[0], ipipe[1]))
	proc.start()

	os.close(ipipe[1])
	os.close(opipe[0])

	MAIN_COMMUNICATOR = zencad.unbound.communicator.Communicator(ipipe=ipipe[0], opipe=opipe[1])
	MAIN_COMMUNICATOR.start_listen()

	app = QApplication([])
	zencad.opengl.init_opengl()

	def receiver(data):
		data = pickle.loads(data)
		print("client:", data)
		if data["cmd"] == "stopworld": app.quit()

	MAIN_COMMUNICATOR.newdata.connect(receiver)

	DISPLAY_WINID=zencad.viewadaptor.DisplayWidget(scene, view=scene.viewer.create_view())

	MAIN_COMMUNICATOR.send({"cmd":"hello"})
	MAIN_COMMUNICATOR.send({"cmd":"bindwin", "id":int(DISPLAY_WINID.winId())})

	DISPLAY_WINID.show()

	app.exec()


def start_worker(ipipe, opipe, path):
	os.dup2(ipipe, 3)
	os.dup2(opipe, 4)

	os.environ["ZENCAD_MODE"] = "REPLACE_WINDOW"

	os.execve("/usr/bin/python3", ["/usr/bin/python3", "-m", "zencad", path], os.environ)

def start_unbounded_worker(path):
	ipipe = os.pipe()
	opipe = os.pipe()

	proc = multiprocessing.Process(target = start_worker, args=(opipe[0], ipipe[1], path))
	proc.start()

	os.close(ipipe[1])
	os.close(opipe[0])

	communicator = zencad.unbound.communicator.Communicator(ipipe=ipipe[0], opipe=opipe[1])

	return communicator

def update_unbound_application(scene):
	print("UPDATE_UNBOUND_APPLICATION")

	global MAIN_COMMUNICATOR
	global DISPLAY_WINID

	MAIN_COMMUNICATOR = zencad.unbound.communicator.Communicator(ipipe=3, opipe=4)
	MAIN_COMMUNICATOR.start_listen()

	app = QApplication([])
	zencad.opengl.init_opengl()

	def receiver(data):
		data = pickle.loads(data)
		print("client:", data)
		if data["cmd"] == "stopworld": app.quit()

	MAIN_COMMUNICATOR.newdata.connect(receiver)

	DISPLAY_WINID=zencad.viewadaptor.DisplayWidget(scene, view=scene.viewer.create_view())

	MAIN_COMMUNICATOR.send({"cmd":"hello"})
	MAIN_COMMUNICATOR.send({"cmd":"bindwin", "id":int(DISPLAY_WINID.winId())})

	DISPLAY_WINID.show()

	app.exec()
