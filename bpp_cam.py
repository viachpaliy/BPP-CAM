#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QAction, qApp
from PyQt5.QtWidgets import QMainWindow, QToolBar, QHBoxLayout, QDialogButtonBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class BPP_CAM(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
   
        desktop_size = QDesktopWidget().screenGeometry()
        self.resize(desktop_size.width()-100, desktop_size.height()-100) 
        self.setWindowTitle('BPP CAM')
        self.setWindowIcon(QIcon('icons/Biesse.bmp'))
        self.init_actions()
        self.init_menu()
        self.init_toolbar()
        self.init_widgets()
        self.show()


    def init_actions(self):
        self.actions = {}
        icons = {"&New" : 'icons/gen18.bmp',
                 "&Open" : 'icons/apri',
                 "&Save" : 'icons/gen3.bmp',
                 "&Exit" : 'icons/exit.bmp',
                 "&Piece" : 'icons/edi16.bmp',
                 "&Variables" : 'icons/edi17.bmp',
                 "&Cut" : 'icons/gen6.bmp',
                 "&Copy" : 'icons/gen5.bmp',
                 "&Paste" : 'icons/incolla.bmp'
                 }
        shortcuts = {"&New" : 'Ctrl+N',
                     "&Open" : 'Ctrl+O',
                     "&Save" : 'Ctrl+S',
                     "&Exit" : 'Ctrl+Q',
                     "&Cut" : 'Ctrl+X',
                     "&Copy" : 'Ctrl+C',
                     "&Paste" : 'Ctrl+V'
                    }
        status_tips = {"&New" : 'New file',
                       "&Open" : 'Open file',
                       "&Save" : 'Save file',
                       "&Exit" : 'Exit application',
                       "&Piece" : 'Piece variables',
                       "&Variables" : 'Program variables',
                       "&Cut" : 'Cut',
                       "&Copy" : 'Copy',
                       "&Paste" : 'Paste'
                       }
        connect_methods ={"&Exit" : self.exit,
                          "&Open" : self.open,
                          "&Save" : self.save
                          }

        for key in icons:
            action = QAction(QIcon(icons[key]), key, self)
            if key in shortcuts:
                action.setShortcut(shortcuts[key])
            if key in status_tips:
                action.setStatusTip(status_tips[key])
                action.setToolTip(status_tips[key])
            if key in connect_methods:
                action.triggered.connect(connect_methods[key]) 
            self.actions[key] = action
      

    def init_menu(self):

        menubar = self.menuBar()
        menus = {'&File' : ["&New","&Open","&Save","Separator","&Exit"],
                 '&Edit' : ["&Cut","&Copy","&Paste"]
                 }
        for key in menus:
            menu = menubar.addMenu(key)
            for item in menus[key]:
                if item in self.actions:
                    menu.addAction(self.actions[item])
                if item == "Separator" :
                    menu.addSeparator()

        self.menubar = menubar

    def init_toolbar(self):
        
        toolbar = self.addToolBar('ToolBar')
        names = ["&New","&Open","&Save","&Exit",
                 "&Cut","&Copy","&Paste"]
        for item in names:
            if item in self.actions:
                toolbar.addAction(self.actions[item])  
        

        self.toolbar = toolbar

    def init_widgets(self):
        hbox = QHBoxLayout()
        left_bb = self.init_left_bb()
               
        hbox.addLayout(left_bb)
        hbox.addWidget(QSplitter(Qt.Vertical))
        self.treeView = QTreeView()
        self.treeView.setHeaderHidden(True)
        self.treeView.setFixedWidth(400)
        hbox.addWidget(self.treeView)
        hbox.addWidget(QSplitter(Qt.Vertical))
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        hbox.addWidget(self.frame)
        hbox.setSpacing(5)
        form = QWidget()
        form.setLayout(hbox)
        self.setCentralWidget(form)

    

    def init_left_bb(self):
        left_bb = QVBoxLayout()
        buttons = ["&Piece","&Variables"]
        for item in buttons:
            tool_button = QToolButton()
            tool_button.setFixedWidth(32)
            tool_button.setFixedHeight(32)
            tool_button.setToolButtonStyle(Qt.ToolButtonIconOnly) 
            if item in self.actions:
                tool_button.addAction(self.actions[item])
                tool_button.setIcon(self.actions[item].icon())
            left_bb.addWidget(tool_button)
        left_bb.setSpacing(5)
        left_bb.addStretch(0)
        return left_bb

    def exit(self):
        QCoreApplication.instance().quit()

    def open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def save(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = BPP_CAM()
    sys.exit(app.exec_())
