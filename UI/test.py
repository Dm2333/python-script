import sys
from PyQt4 import QtCore, QtGui
from mygui import Ui_Dialog
class Gongzi(QtGui.QWidget):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.ui = mygui()
                self.ui.mygui(self)
               
#                self.ui.pushButton.setObjectName("pushButton1")
# ��������¼�
#                self.ui.pushButton.connect(self.ui.pushButton,
#                        QtCore.SIGNAL("clicked()"),
#                        self,QtCore.SLOT("close()"))
# ����ť�Ժ��lineEdit ��������ʾ��lable
                self.ui.pushButton.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.printa)
# lineEdit ȡ������ֶ�������Ĳ���
# a = QtCore.QString(win.text())
                self.value = QtCore.QString(self.ui.lineEdit.text())
# lable �������
#                self.ui.label.setText(QtGui.QApplication.translate(self.value)
                self.ui.label.setText(QtGui.QApplication.translate("gongzi","%s" % self.value, None, QtGui.QApplication.UnicodeUTF8))
               
        def printa(self):
                print "%s" % self.value
                self.value = QtCore.QString(self.ui.lineEdit.text())
                self.ui.label.setText(QtGui.QApplication.translate("gongzi","%s" % self.value, None, QtGui.QApplication.UnicodeUTF8))
if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        gongzi = Ui_Dialog()
#        gongzi.ui.pushButton.connect(gongzi.ui.pushButton,
#                        QtCore.SIGNAL("clicked()"),
#                        gongzi.ui.pushButton,QtCore.SLOT("close"))
        gongzi.show()
        sys.exit(app.exec_())
