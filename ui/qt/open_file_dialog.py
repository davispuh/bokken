# -*- coding: utf-8 -*-
"""
Bokken Disassembler Framework
Copyright (C) 2014 David Martínez Moreno <ender@debian.org>

I am providing code in this repository to you under an open source license.
Because this is a personal repository, the license you receive to my code
is from me and not my employer (Facebook).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.
"""

"""Open File dialog in Qt4 for Bokken."""

from PyQt4 import QtCore, QtGui

class OpenFileDialog(QtGui.QWidget):
    def __init__(self, backends=(), core=None, file='', first_run=False):
        super(OpenFileDialog, self).__init__()
        self.backends = backends

    def initUI(self):
        pass
