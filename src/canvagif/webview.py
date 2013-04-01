from PyQt4 import QtCore, QtGui, QtWebKit


class CanvagifWebView(QtWebKit.QWebView):
    selecting = False
    selectedElement = None
    mouseOverElement = None
    selectedElementChanged = QtCore.pyqtSignal()
    mouseOverElementChanged = QtCore.pyqtSignal()

    def toggleSelecting(self, selecting):
        self.selecting = selecting

    def mouseMoveEvent(self, event):
        if self.selecting:
            result = self.page().currentFrame().hitTestContent(event.pos())
            self.mouseOverElement = result.element()
            self.mouseOverElementChanged.emit()
            if self.selectedElement:
                pass
            else:
                pass
        else:
            super(CanvagifWebView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.selecting:
            self.selectedElement = self.mouseOverElement
            self.selectedElementChanged.emit()
        else:
            super(CanvagifWebView, self).mouseReleaseEvent(event)

