from Y19.Tests import testing as y19
from Y18.Tests import testing as y18

__name__ = 'AoC'
__version__ = '1.19.05.1'
__author__ = 'faremir'
__author_email__ = 'faremir@jircode.com'
__description__ = 'Advent of Code solutions'

if __name__ == "AoC":
    print("\u2554" + "\u2550" * 32 + "\u2557")
    print("\u2551" + "\u2550" * 8 + " Advent of Code " + "\u2550" * 8 + "\u2551")
    # default = True if input("\u2551 Use default filesystem [y/n]?  \u2560\u2550 ") in ('y', 'Y') else False // TODO uncomment on release
    default = True
    y19(default)
    # y18(default)
