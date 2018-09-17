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

import RPi.GPIO
from rpidio.inputs import Inputs


class Mainboard:

    def __init__(self):
        try:
            RPi.GPIO.setmode(RPi.GPIO.BOARD)
            RPi.GPIO.setup(Inputs.get_pins(Inputs.get_inputs_mainboard()), RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_DOWN)
        except:
            raise RuntimeError("Mainboard pin setup failed")

    def __def__(self):
        RPi.GPIO.cleanup()

    def get_total_inputs(self):
        return 26

    def read(self, input):
        try:
            return RPi.GPIO.input(Inputs.get_pin(input))
        except:
            raise RuntimeError("Cannot read pin %s on the mainboard" % str(Pins.get_pin(input)))

    def read_all(self):
        try:
            return [RPi.GPIO.input(input) for input in Inputs.get_pins(Inputs.get_inputs_mainboard())]
        except:
            raise RuntimeError("Cannot read the mainboard")
