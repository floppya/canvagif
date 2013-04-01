import os
from PyQt4 import QtCore, QtGui
from .ui.ui_mainwindow import Ui_AppMainWindow
from .webview import CanvagifWebView


class CanvagifMainWindow(QtGui.QMainWindow, Ui_AppMainWindow):
    def __init__(self, *args, **kwargs):
        super(CanvagifMainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.webView = CanvagifWebView()
        self.centralwidget.layout().addWidget(self.webView)
        self.webView.show()
        self.recordTimer = QtCore.QTimer(self)
        self._wire()
        self._imageOutputBuffer = []

    def _wire(self):
        self.txtUrl.returnPressed.connect(self.onGotoUrl)
        self.webView.loadStarted.connect(self.onLoadStarted)
        self.webView.loadFinished.connect(self.onLoadFinished)
        self.webView.selectedElementChanged.connect(self.onSelectedElementChanged)
        self.webView.mouseOverElementChanged.connect(self.onMouseOverElementChanged)
        self.webView.urlChanged.connect(self.onUrlChanged)
        self.butReload.clicked.connect(self.webView.reload)
        self.butSelect.toggled.connect(self.onSelectionToggled)
        self.butRecord.toggled.connect(self.onRecordToggled)
        self.butSelectOutputLocation.clicked.connect(self.onSelectOutputLocation)
        self.recordTimer.timeout.connect(self.onRecordTick)

    def onGotoUrl(self):
        url = self.txtUrl.text()
        if not unicode(url).startswith('http'):
            url = 'http://' + url
        self.webView.setUrl(QtCore.QUrl(url))

    def onLoadStarted(self):
        self.statusbar.showMessage('loading started')

    def onLoadFinished(self):
        self.statusbar.showMessage('loading finished', 3000)

    def onSelectionToggled(self, isSelecting):
        self.webView.toggleSelecting(isSelecting)

    def onSelectedElementChanged(self):
        element = self.webView.selectedElement
        name = self._nameForElement(element)
        self.lblSelected.setText(name)
        self.statusbar.showMessage('Selected ' + name, 3000)
        self.butSelect.setChecked(False)

    def onMouseOverElementChanged(self):
        element = self.webView.mouseOverElement
        name = self._nameForElement(element)
        self.statusbar.showMessage(name)

    def _nameForElement(self, element):
        elId = element.attribute('id')
        return '%s id="%s"' % (
            element.tagName(), elId)

    def onRecordToggled(self, isRecording):
        if isRecording:
            self.butRecord.setText('Stop recording')
            self.statusbar.showMessage('Recording...')
            self._startRecording()
        else:
            self.butRecord.setText('Record')
            self.statusbar.showMessage('Stopped recording', 3000)
            self._stopRecording()

    def _startRecording(self):
        self.frame = 0
        self._imageOutputBuffer = []
        fps = int(self.spinFps.value())
        self.recordTimer.start(1000/fps)
        
    def _stopRecording(self):
        self.recordTimer.stop()
        width = int(self.spinOutWidth.value())
        height = int(self.spinOutHeight.value())
        if self._imageOutputBuffer:
            for i, frame in enumerate(self._imageOutputBuffer):
                filename = '%05d.png' % i
                full_filename = os.path.join(self.outputPath, filename)
                frame = frame.scaled(
                    QtCore.QSize(width, height),
                    QtCore.Qt.IgnoreAspectRatio,
                    QtCore.Qt.SmoothTransformation)
                frame.save(full_filename)
    
    def onRecordTick(self):
        element = self.webView.selectedElement
        elementRect = element.geometry()
        image = QtGui.QImage(elementRect.size(), QtGui.QImage.Format_ARGB32)
        painter = QtGui.QPainter(image)
        element.render(painter)
        painter.end()
        self._imageOutputBuffer.append(image)
        self.frame += 1        

    def onSelectOutputLocation(self):
        path = QtGui.QFileDialog.getExistingDirectory(
            self, 'Choose target')
        if not path:
            return
        self.outputPath = unicode(path)

    def onUrlChanged(self, url):
        self.txtUrl.setText(url.toString())

