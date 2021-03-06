# Copyright (C) 2018, see AUTHORS.md
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from rpidio.ABE_IOPi.helpers import ABEHelpers
from rpidio.mainboard import Mainboard
from rpidio.extboard import ExtensionBoardAdapter
from rpidio.inputs import Inputs


class InputReader:

    def __init__(self):
        self._mainb = Mainboard()

        i2c_helper = ABEHelpers()
        self._bus = i2c_helper.get_smbus()

        self._extb1_bus1 = ExtensionBoardAdapter(self._bus, 0x20)
        self._extb1_bus2 = ExtensionBoardAdapter(self._bus, 0x21)

    def __del__(self):
        self._bus.close()

    def read(self, input):
        if Inputs.get_hardware(input) == Inputs.MAINBOARD:
            return self._mainb.read(input)
        elif Inputs.get_hardware(input) == Inputs.EXTENSION_BOARD1_BUS1:
            return self._extb1_bus1.read(input)
        elif Inputs.get_hardware(input) == Inputs.EXTENSION_BOARD1_BUS2:
            return self._extb1_bus2.read(input)
        else:
            raise RuntimeError("Unknown input given")

    def read_all(self):
        reading_mainb = self._mainb.read_all()
        reading_extb1_bus1 = self._extb1_bus1.read_all()
        reading_extb1_bus2 = self._extb1_bus2.read_all()

        return reading_extb1_bus2 + reading_extb1_bus1 + reading_mainb
