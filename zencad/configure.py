
CONFIGURE_VIEWADAPTOR_TRACE = False
CONFIGURE_MAINWINDOW_TRACE = False
CONFIGURE_COMMUNICATOR_TRACE = False
CONFIGURE_APPLICATION_TRACE = False
CONFIGURE_MAIN_TRACE = False

CONFIGURE_GUI_INFO = False

CONFIGURE_VIEWADAPTOR_RETRANSLATE_KEYS = True
CONFIGURE_SLEEPED_OPTIMIZATION = True
CONFIGURE_CONSOLE_RETRANSLATE = True 


def verbose(en):
	global CONFIGURE_VIEWADAPTOR_TRACE
	global CONFIGURE_MAINWINDOW_TRACE
	global CONFIGURE_COMMUNICATOR_TRACE
	global CONFIGURE_APPLICATION_TRACE
	global CONFIGURE_MAIN_TRACE

	CONFIGURE_VIEWADAPTOR_TRACE = en
	CONFIGURE_MAINWINDOW_TRACE = en
	CONFIGURE_COMMUNICATOR_TRACE = en
	CONFIGURE_APPLICATION_TRACE = en
	CONFIGURE_MAIN_TRACE = en

def info(en):
	global CONFIGURE_GUI_INFO

	CONFIGURE_GUI_INFO = en