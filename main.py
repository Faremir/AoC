from Y19.Tests import testing as y19
from Y18.Tests import testing as y18

__name__ = 'AoC'
__version__ = '1.19.05'
__author__ = 'faremir'
__author_email__ = 'faremir@jircode.com'
__description__ = 'Advent of Code solutions'


def header(string_variables):
    print('\u2554{horizontal_line}\u2557\n'
          '\u2551{spaces}Advent of Code{spaces}\u2551\n'
          '\u255A{horizontal_line}\u255D'
          .format(**string_variables, spaces = " " * 9))


if __name__ == "AoC":
    string_vars = {'horizontal_line': "\u2550" * 32}
    header(string_vars)
    # default = True if input("\u2551 Use default filesystem [y/n]?  \u2560\u2550 ") in ('y', 'Y') else False
    # TODO uncomment on release
    default = True
    # y18(default, string_vars)
    y19(default, string_vars)
