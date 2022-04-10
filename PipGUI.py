import threading


def thread(fn):
    def execute(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return execute


class PipGUI:

    menudefs = [
        ('pacman', [
                     ('Open Package Manager', '<<pip-open>>'),
        ]),]

    def __init__(self, editwin):
        self.editwin = editwin
        self.text = editwin.text
        self.text.bind('<<pip-open>>', self.test_event)
    
    def test_event(self, event):
        self.test()

    # We use @thread here so it does not block IDLE while executing
    @thread
    def test(self):
        from PyQt5 import QtWidgets, uic
        from PyQt5.QtCore import QTimer, QTime
        from PyQt5.QtGui import QTextCursor, QStandardItemModel, QStandardItem, QIcon
        from PyQt5 import QtTest
        import PyQt5
        import sys
        import requests
        from lxml.html import fromstring
        from urllib.parse import quote
        import urllib.request
        import threading
        import os


        def thread(fn):
            def execute(*args, **kwargs):
                threading.Thread(target=fn, args=args, kwargs=kwargs).start()
            return execute


        class MainUI(QtWidgets.QMainWindow):

            def __init__(self):
                super(MainUI, self).__init__()

                scriptDir = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "PacMan"
                
                uic.loadUi(scriptDir + os.path.sep + 'gui.ui', self)

                self.setFixedSize(800, 616)

                # labels that will change on update
                self.changeOnUpdate = [self.packageVersion, self.packageDescription, self.packageHref, self.pipCommand]

                self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'python.ico'))

                self.btn_searchPackage.clicked.connect(self.search_packages)

                self.btn_installPackage.clicked.connect(self.install_package)
                self.btn_installPackage.setEnabled(False)

                self.btn_uninstallPackage.clicked.connect(self.uninstall_package)
                self.btn_uninstallPackage.setEnabled(False)
                
                self.packageList.clicked.connect(self.item_clicked)
                self.packageList.enabled = False
                self.packageList.isAbleToSelect = True # custom attribute

                #entries = ['matplotlib', 'numba', 'numpy', 'jit', 'json', 'pip']

                #for i in entries:
                #    item = QStandardItem(i)
                #    self.model.appendRow(item)

                class AppURLopener(urllib.request.FancyURLopener):
                    version = "Mozilla/5.0 etc etc"

                self.opener = AppURLopener()

            @thread
            def item_clicked(self, index):
                #print(f'row={index.row()}')
                #print(f'data={index.data()}')
                #item = self.packageList.item(index.row())

                if self.packageList.isAbleToSelect:

                    self.btn_installPackage.setEnabled(False)
                    self.btn_uninstallPackage.setEnabled(False)
                    
                    self.packageName.setTitle(index.data())

                    for i in self.changeOnUpdate:
                        i.setText('Получение информации...')
                    
                    self.packageList.isAbleToSelect = False
                    self.packageList.setEnabled(False)
                    #print(self.packageList.item(index.row()).href)
                    response = self.opener.open(self.packageList.item(index.row()).href)
                    response = response.read().decode('utf-8')
                    parser = fromstring(response)

                    urlLink='<a href="'
                    urlLink+=f"{self.packageList.item(index.row()).href}"
                    urlLink+=f'">{self.packageList.item(index.row()).href}</a>'
                    #print(urlLink)
                    self.packageHref.setText(urlLink)

                    for elem in parser.xpath("//span[@id='pip-command']"):
                        self.pipCommand.setText(elem.text)

                    for elem in parser.xpath("//div[@class='package-header']/div[@class='package-header__left']/h1[@class='package-header__name']/text()"):
                        #print(elem.strip().split()[-1])
                        self.packageVersion.setText(elem.strip().split()[-1])

                    for elem in parser.xpath("//p[@class='package-description__summary']/text()"):
                        #print(elem)
                        self.packageDescription.setText(elem.strip())
                        
                    self.packageList.isAbleToSelect = True
                    self.packageList.setEnabled(True)
                    self.btn_installPackage.setEnabled(True)
                    self.btn_uninstallPackage.setEnabled(True)

                
            @thread
            def search_packages(self, *args):

                package_name = self.searchPackageName.text()
                page = '1'

                self.btn_searchPackage.setText('Поиск...')
                self.btn_searchPackage.setEnabled(False)

                response = self.opener.open(f'https://pypi.org/search/?q={package_name}&page={page}')
                response = response.read().decode('utf-8')

                parser = fromstring(response)

                self.packageList.clear()

                urls = []
                for elem in parser.xpath("//a[@class='package-snippet']"):
                    urls.append('https://pypi.org' + elem.get('href'))
                
                for index, elem in enumerate(parser.xpath("//h3[@class='package-snippet__title']/span[@class='package-snippet__name']")):
                    self.packageList.addItems([elem.text])
                    
                    item = self.packageList.takeItem(index)
                    setattr(item, 'href', urls[index])
                    self.packageList.addItem(item)

                self.btn_searchPackage.setText('Найти')
                self.btn_searchPackage.setEnabled(True)


            def install_package(self, *args):

                pip_install_command = self.pipCommand.text()
                
                os.system(f'{pip_install_command} & pause')

            def uninstall_package(self, *args):

                pip_uninstall_command = self.pipCommand.text()
                cmd = pip_uninstall_command.split()
                cmd[1] = 'uninstall'
                pip_uninstall_command = ' '.join(cmd)

                os.system(f'{pip_uninstall_command} & pause')

        app = QtWidgets.QApplication(sys.argv)

        main = MainUI()
        main.show()

        app.exec_()

