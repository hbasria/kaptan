from PyQt5.QtWidgets import (QTabWidget, QGridLayout, QLabel, QPushButton, QGroupBox, QComboBox, QHBoxLayout,
                             QVBoxLayout, QSpacerItem, QWidget, QSizePolicy, QRadioButton, QCheckBox, QFrame,
                             QProgressBar, QSlider, QScrollBar, QListView, QListWidget, QSpinBox, QListWidgetItem,
                             QTextBrowser, QStyleFactory)
from PyQt5.QtGui import QIcon, QPixmap, QTextCursor
from PyQt5.QtCore import Qt, QEvent, QSize
from .tools import iniToCss
import os

class ThemeTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("QTabWidget#tabWidget::tab-bar {alignment:center;}")
        self.setObjectName("tabWidget")
        self.setCurrentIndex(0)

        self.colorSchemePath = "/usr/share/color-schemes"

        self.createTabWidgetStyle()
        self.createTabWindowStyle()
        self.createTabColorScheme()
        self.createTabDesktopTheme()
        #self.createTabMouseCursor()
        self.createTabIconSet()


    def createTabWidgetStyle(self):
        self.tabWidgetStyle = QWidget()
        self.tabWidgetStyle.setObjectName("tabWidgetStyle")

        self.verticalLayout = QVBoxLayout(self.tabWidgetStyle)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.labelWidgetStyle = QLabel(self.tabWidgetStyle)
        self.labelWidgetStyle.setText(self.tr("Widget Style:"))
        self.labelWidgetStyle.setObjectName("labelWidgetStyle")
        self.horizontalLayout.addWidget(self.labelWidgetStyle)

        self.comboBoxWidgetStyle = QComboBox(self.tabWidgetStyle)
        self.comboBoxWidgetStyle.setObjectName("comboBoxWidgetStyle")
        self.comboBoxWidgetStyle.addItem(self.tr("Breeze"))
        self.comboBoxWidgetStyle.addItem(self.tr("Oxygen"))
        self.comboBoxWidgetStyle.addItem(self.tr("Fusion"))
        self.horizontalLayout.addWidget(self.comboBoxWidgetStyle)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))


        self.previewWidgetStyle = PreviewWidgetStyle(self.tabWidgetStyle)
        self.previewWidgetStyle.tabWidget.setStyle(QStyleFactory.create("Breeze"))

        self.verticalLayout.addWidget(self.previewWidgetStyle)


        self.addTab(self.tabWidgetStyle, self.tr("Widget Style"))

        self.comboBoxWidgetStyle.currentTextChanged.connect(self.previewStyle)

    def previewStyle(self, text):
        self.previewWidgetStyle.tabWidget.setStyle(QStyleFactory.create(text))

    def createTabWindowStyle(self):
        self.tabWindowStyle = QWidget()
        self.tabWindowStyle.setObjectName("tabWindowStyle")

        self.verticalLayout_6 = QVBoxLayout(self.tabWindowStyle)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.listWidgetWindowStyle = QListWidget(self.tabWindowStyle)
        self.listWidgetWindowStyle.setResizeMode(QListView.Adjust)
        self.listWidgetWindowStyle.setIconSize(QSize(340, 105))
        self.listWidgetWindowStyle.setViewMode(QListView.IconMode)
        self.listWidgetWindowStyle.setObjectName("listWidgetWindowStyle")

        item = QListWidgetItem(self.listWidgetWindowStyle)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/data/images/breeze-window.png"))
        item.setIcon(icon)
        item.setText("Breeze")
        item.setStyleText = "org.kde.breeze"
        item = QListWidgetItem(self.listWidgetWindowStyle)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/data/images/oxygen-window.png"))
        item.setIcon(icon1)
        item.setText("Oxygen")
        item.setStyleText = "org.kde.oxygen"

        self.verticalLayout_6.addWidget(self.listWidgetWindowStyle)

        self.addTab(self.tabWindowStyle, self.tr("Window Style"))

    def createTabColorScheme(self):
        self.tabColorScheme = QWidget()
        self.tabColorScheme.setObjectName("tabColorScheme")

        self.verticalLayout_2 = QVBoxLayout(self.tabColorScheme)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.listWidgetColorScheme = QListWidget(self.tabColorScheme)
        self.listWidgetColorScheme.setObjectName("listWidgetColorScheme")
        self.verticalLayout_2.addWidget(self.listWidgetColorScheme)

        self.previewWidgetColor = PreviewWidgetColor(self.tabColorScheme)
        self.verticalLayout_2.addWidget(self.previewWidgetColor)

        self.addTab(self.tabColorScheme, self.tr("Color Scheme"))

        color_list = os.listdir(self.colorSchemePath)
        color_list.sort()

        for color in color_list:
            item = QListWidgetItem(self.listWidgetColorScheme)
            item.setText(color.split(".")[0])
            item.colorSchemeName = color


        self.listWidgetColorScheme.itemClicked.connect(self.previewColorScheme)

    def previewColorScheme(self, item):
        css = iniToCss(os.path.join(self.colorSchemePath,item.colorSchemeName))
        self.previewWidgetColor.previewGroupBox.setStyleSheet(css)

    def createTabDesktopTheme(self):
        self.tabDesktopTheme = QWidget()
        self.tabDesktopTheme.setObjectName("tabDesktopTheme")

        self.gridLayout = QGridLayout(self.tabDesktopTheme)
        self.gridLayout.setObjectName("gridLayout")

        self.listWidgetDesktopTheme = QListWidget(self.tabDesktopTheme)
        self.listWidgetDesktopTheme.setObjectName("listWidgetDesktopTheme")
        self.listWidgetDesktopTheme.setViewMode(QListView.IconMode)
        self.listWidgetDesktopTheme.setIconSize(QSize(660, 70))
        self.gridLayout.addWidget(self.listWidgetDesktopTheme, 0, 0, 1, 1)

        item = QListWidgetItem(self.listWidgetDesktopTheme)
        icon = QIcon(QPixmap(":/data/images/air-panel.png").scaled(QSize(660, 70), Qt.IgnoreAspectRatio, Qt.FastTransformation))
        item.setSizeHint(QSize(660, 70))
        item.setIcon(icon)
        item.panelText = "air"

        item = QListWidgetItem(self.listWidgetDesktopTheme)
        item.setTextAlignment(Qt.AlignHCenter)
        icon = QIcon(QPixmap(":/data/images/breeze-panel.png").scaled(QSize(660, 70), Qt.IgnoreAspectRatio, Qt.FastTransformation))
        item.setSizeHint(QSize(660, 70))
        item.setIcon(icon)
        item.panelText = "default"

        item = QListWidgetItem(self.listWidgetDesktopTheme)
        item.setTextAlignment(Qt.AlignHCenter)
        icon = QIcon(QPixmap(":/data/images/breeze-dark-panel.png").scaled(QSize(660, 70), Qt.IgnoreAspectRatio, Qt.FastTransformation))
        item.setSizeHint(QSize(660, 70))
        item.setIcon(icon)
        item.panelText = "breeze-dark"

        item = QListWidgetItem(self.listWidgetDesktopTheme)
        item.setTextAlignment(Qt.AlignHCenter)
        icon = QIcon(QPixmap(":/data/images/oxygen-panel.png").scaled(QSize(660, 70), Qt.IgnoreAspectRatio, Qt.FastTransformation))
        item.setSizeHint(QSize(660, 70))
        item.setIcon(icon)
        item.panelText = "oxygen"

        self.addTab(self.tabDesktopTheme, self.tr("Desktop Theme"))

    """def createTabMouseCursor(self):
        self.tabMouseCursor = QWidget()
        self.tabMouseCursor.setObjectName("tabMouseCursor")

        self.verticalLayout_4 = QVBoxLayout(self.tabMouseCursor)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.listWidgetMouseCursor = QListWidget(self.tabMouseCursor)
        self.listWidgetMouseCursor.setObjectName("listWidgetMouseCursor")

        self.verticalLayout_4.addWidget(self.listWidgetMouseCursor)
        self.addTab(self.tabMouseCursor, self.tr("Mouse Cursor"))"""

    def createTabIconSet(self):
        self.tabIconSet = QWidget()
        self.tabIconSet.setObjectName("tabIconSet")

        self.verticalLayout_3 = QVBoxLayout(self.tabIconSet)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.listWidgetIconSet = QListWidget(self.tabIconSet)
        self.listWidgetIconSet.setResizeMode(QListView.Adjust)
        self.listWidgetIconSet.setObjectName("listWidgetIconSet")
        self.listWidgetIconSet.setViewMode(QListView.IconMode)
        self.listWidgetIconSet.setIconSize(QSize(370, 64))

        item = QListWidgetItem(self.listWidgetIconSet)
        item.setIcon(QIcon(":/data/images/oxygen-set.png"))
        item.setText("Oxygen")

        item = QListWidgetItem(self.listWidgetIconSet)
        item.setIcon(QIcon(":/data/images/breeze-set.png"))
        item.setText("Breeze")

        self.verticalLayout_3.addWidget(self.listWidgetIconSet)

        self.addTab(self.tabIconSet, self.tr("Icon Set"))


class PreviewWidgetStyle(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle(self.tr("Preview"))
        self.setMaximumHeight(220)
        self.setObjectName("groupBox")

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tabWidget = QTabWidget(self)
        self.tabWidget.setObjectName("tabWidgetPreview")

        self.tab = QWidget()
        self.tab.setObjectName("tab")

        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setTitle(self.tr("Group Box"))
        self.groupBox.setObjectName("groupBox")


        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setText(self.tr("Radio Button"))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setText(self.tr("Radio Button"))
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.line = QFrame(self.groupBox)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setText(self.tr("Check Box"))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)

        self.horizontalLayout.addWidget(self.groupBox)


        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.progressBar = QProgressBar(self.tab)
        self.progressBar.setProperty("value", 75)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)

        self.horizontalSlider = QSlider(self.tab)
        self.horizontalSlider.setProperty("value", 45)
        self.horizontalSlider.setSliderPosition(45)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.horizontalSlider)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.spinBox = QSpinBox(self.tab)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setText(self.tr("Button"))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.comboBox = QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem(self.tr("Combo Box"))
        self.verticalLayout_3.addWidget(self.comboBox)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalScrollBar = QScrollBar(self.tab)
        self.verticalScrollBar.setPageStep(50)
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)
        self.tabWidget.addTab(self.tab, self.tr("Tab 1"))


        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, self.tr("Tab 2"))

        self.verticalLayout.addWidget(self.tabWidget)

        self.pushButton.installEventFilter(self)
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.radioButton.installEventFilter(self)
        self.radioButton.setFocusPolicy(Qt.NoFocus)
        self.radioButton_2.installEventFilter(self)
        self.radioButton_2.setFocusPolicy(Qt.NoFocus)
        self.checkBox.installEventFilter(self)
        self.checkBox.setFocusPolicy(Qt.NoFocus)
        self.comboBox.installEventFilter(self)
        self.comboBox.setFocusPolicy(Qt.NoFocus)
        self.spinBox.installEventFilter(self)
        self.spinBox.setFocusPolicy(Qt.NoFocus)
        self.horizontalSlider.installEventFilter(self)
        self.horizontalSlider.setFocusPolicy(Qt.NoFocus)
        self.verticalScrollBar.installEventFilter(self)
        self.verticalScrollBar.setFocusPolicy(Qt.NoFocus)
        self.tab.installEventFilter(self)
        self.tab.setFocusPolicy(Qt.NoFocus)
        self.tab_2.installEventFilter(self)
        self.tab_2.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.installEventFilter(self)
        self.tabWidget.setFocusPolicy(Qt.NoFocus)

        self.tabWidget.currentChanged.connect(self.noClick)

    def noClick(self, x):
        self.tabWidget.setCurrentIndex(0)

    def eventFilter(self, obj, event):
        if self.pushButton:
            if event.type() == QEvent.MouseButtonRelease:
                return True
            elif event.type() == QEvent.MouseButtonPress:
                return True
            elif event.type() == QEvent.MouseButtonDblClick:
                return True
            else:
                return False
        else:
            super().eventFilter(obj, event)


class PreviewWidgetColor(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle(self.tr("Preview"))
        self.setMaximumHeight(120)

        vboxLayout = QVBoxLayout(self)
        self.previewGroupBox = QGroupBox(self)
        self.previewGroupBox.setObjectName("previewGroupBox")
        vboxLayout.addWidget(self.previewGroupBox)

        self.horizontalLayout = QHBoxLayout(self.previewGroupBox)
        self.verticalLayout = QVBoxLayout()
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.previewLabel = QLabel(self.previewGroupBox)
        self.previewLabel.setText(self.tr("Window Text"))
        self.previewLabel.setObjectName("previewLabel")
        self.verticalLayout.addWidget(self.previewLabel)

        self.previewPushButton = QPushButton(self.previewGroupBox)
        self.previewPushButton.setText(self.tr("Button"))
        self.previewPushButton.setObjectName("previewPushButton")
        self.verticalLayout.addWidget(self.previewPushButton)

        self.previewTextBrowser = QTextBrowser(self.previewGroupBox)
        self.previewTextBrowser.setObjectName("previewTextBrowser")

        self.previewTextBrowser.insertHtml(self.tr("""<style>
        #unclicked {color : rgb(255,0,0);}
        #sunclicked {color : rgb(255,0,255);}
        #clicked {color : rgb(0,255,0);}
        #sclicked {color : rgb(0,0,255);}
        </style>
        <p>Normal metin <a id='unclicked' href='#'>bağlantı</a> <a id='clicked' href='#'>ziyaret edilmiş</a></p>
        <p>Seçili metin <a id='sunclicked' href='#'>bağlantı</a> <a id='sclicked' href='#'>ziyaret edilmiş</a></p>"""))



        cursor = self.previewTextBrowser.textCursor()
        cursor.setPosition(39)
        cursor.setPosition(76, QTextCursor.KeepAnchor)
        self.previewTextBrowser.setTextCursor(cursor)

        self.horizontalLayout.addWidget(self.previewTextBrowser)


        self.previewPushButton.installEventFilter(self.previewGroupBox)
        self.previewPushButton.setFocusPolicy(Qt.NoFocus)

        self.previewTextBrowser.installEventFilter(self.previewGroupBox)
        self.previewTextBrowser.setFocusPolicy(Qt.NoFocus)
        self.previewTextBrowser.setTextInteractionFlags(Qt.NoTextInteraction)

    def eventFilter(self, obj, event):
        if self.previewPushButton:
            if event.type() == QEvent.MouseButtonRelease:
                return True
            elif event.type() == QEvent.MouseButtonPress:
                return True
            elif event.type() == QEvent.MouseButtonDblClick:
                return True

            else:
                return False
        else:
            super().eventFilter(obj, event)