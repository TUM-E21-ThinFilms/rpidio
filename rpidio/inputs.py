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


class Inputs:

    NOT_CONNECTED = (0, 0)
    RESERVED = (0, -1)

    INPUT_1 = (0, 3)
    INPUT_2 = (0, 5)
    INPUT_3 = (0, 7)
    INPUT_4 = (0, 11)
    INPUT_5 = (0, 13)
    INPUT_6 = (0, 15)
    INPUT_7 = (0, 19)
    INPUT_8 = (0, 21)
    INPUT_9 = (0, 23)
    INPUT_10 = (0, 8)
    INPUT_11 = (0, 10)
    INPUT_12 = (0, 12)
    INPUT_13 = (0, 16)
    INPUT_14 = (0, 18)
    INPUT_15 = (0, 22)
    INPUT_16 = (0, 24)
    INPUT_17 = (0, 26)
    INPUT_18 = (0, 29)
    INPUT_19 = (0, 31)
    INPUT_20 = (0, 33)
    INPUT_21 = (0, 35)
    INPUT_22 = (0, 37)
    INPUT_23 = (0, 32)
    INPUT_24 = (0, 36)
    INPUT_25 = (0, 38)
    INPUT_26 = (0, 40)

    INPUT_27 = (1, 1)
    INPUT_28 = (1, 2)
    INPUT_29 = (1, 3)
    INPUT_30 = (1, 4)
    INPUT_31 = (1, 5)
    INPUT_32 = (1, 6)
    INPUT_33 = (1, 7)
    INPUT_34 = (1, 8)
    INPUT_35 = (1, 9)
    INPUT_36 = (1, 10)
    INPUT_37 = (1, 11)
    INPUT_38 = (1, 12)
    INPUT_39 = (1, 13)
    INPUT_40 = (1, 14)
    INPUT_41 = (1, 15)
    INPUT_42 = (1, 16)

    INPUT_43 = (2, 1)
    INPUT_44 = (2, 2)
    INPUT_45 = (2, 3)
    INPUT_46 = (2, 4)
    INPUT_47 = (2, 5)
    INPUT_48 = (2, 6)
    INPUT_49 = (2, 7)
    INPUT_50 = (2, 8)
    INPUT_51 = (2, 9)
    INPUT_52 = (2, 10)
    INPUT_53 = (2, 11)
    INPUT_54 = (2, 12)
    INPUT_55 = (2, 13)
    INPUT_56 = (2, 14)
    INPUT_57 = (2, 15)
    INPUT_58 = (2, 16)

    MAINBOARD = 0
    EXTENSION_BOARD1_BUS1 = 1
    EXTENSION_BOARD1_BUS2 = 2

    def __init__(self):
        pass

    @classmethod
    def _check_input(cls, input):
        assert isinstance(input, tuple)
        assert len(input) == 2
        assert 0 <= input[0] <= 2
        assert 1 <= input[1] <= 40

    @classmethod
    def get_hardware(cls, input):
        cls._check_input(input)
        return input[0]

    @classmethod
    def get_pin(cls, input):
        cls._check_input(input)
        return input[1]

    @classmethod
    def get_pins(cls, inputs):
        assert isinstance(inputs, list)
        return [cls.get_pin(input) for input in inputs]

    @classmethod
    def get_all_inputs(cls):
        return [value for (name, value) in iter(vars(cls).items()) if isinstance(value, tuple)]

    @classmethod
    def get_selective_inputs(cls, selector):
        return [input for input in cls.get_all_inputs() if
                cls.get_hardware(input) == selector and not input == cls.NOT_CONNECTED]

    @classmethod
    def get_inputs_mainboard(cls):
        return cls.get_selective_inputs(cls.MAINBOARD)

    @classmethod
    def get_inputs_extension_board1_bus_1(cls):
        return cls.get_selective_inputs(cls.EXTENSION_BOARD1_BUS1)

    @classmethod
    def get_inputs_extension_board1_bus_2(cls):
        return cls.get_selective_inputs(cls.EXTENSION_BOARD1_BUS2)