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

from rpidio.ABE_IOPi.iopi import IoPi
from rpidio.inputs import Inputs


class ExtensionBoardAdapter:
    PORT_INPUTS = 8
    PORT_NUMBER = 2

    TOTAL_INPUTS = PORT_NUMBER * PORT_INPUTS

    PORT_0 = 0
    PORT_1 = 1

    def __init__(self, bus, address):
        self.ic = IoPi(bus, address)

        # set the port directions, 1 -> input, 0 -> output
        self.ic.set_port_direction(self.PORT_0, 0xff)
        self.ic.set_port_direction(self.PORT_1, 0xff)

        # enable all pull-up resistors for all ports
        self.ic.set_port_pullups(self.PORT_0, 0xff)
        self.ic.set_port_pullups(self.PORT_1, 0xff)

        # since we have pull-up resistors, we have to invert all ports
        # otherwise a high signal would indicate 'not connected' and vice versa.
        # hence, invert the output and we dont have to do the work then.
        self.ic.invert_port(self.PORT_0, 0xff)
        self.ic.invert_port(self.PORT_1, 0xff)

    def get_total_inputs(self):
        return self.TOTAL_INPUTS

    def read(self, input):
        return bool(self.ic.read_pin(Inputs.get_pin(input)))

    def _int_to_list(self, integer):
        # we just care about the 8 bytes, anything else will be thrown away
        integer = 0xFF & integer

        list_int = 8 * [0]
        for i in range(0, 8):
            last_bit = integer & 0x01
            list_int[i] = last_bit
            integer = integer >> 1

        return list_int

    def read_all(self):
        port0 = self.ic.read_port(self.PORT_0)
        port1 = self.ic.read_port(self.PORT_1)

        return self._int_to_list(port1) + self._int_to_list(port0)
