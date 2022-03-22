"""
The world is in quarantine! There is a new pandemic that struggles mankind. Each continent is isolated from each other but infected people have spread before the warning.

You would be given a map of the world in a type of string:

string s = "01000000X000X011X0X"

'0' : uninfected

'1' : infected

'X' : ocean
The virus can't spread in the other side of the ocean.

If one person is infected every person in this continent gets infected too.
Your task is to find the percentage of human population that got infected in the end.

Return the percentage % of the total population that got infected.
The first and the last continent are not connected!

Example:

 start: map1 = "01000000X000X011X0X"
 end:   map1 = "11111111X000X111X0X"
 total = 15
 infected = 11
 percentage = 100*11/15 = 73.33333333333333
For maps without oceans "X" the whole world is connected.

For maps without "0" and "1" return 0 as there is no population.
"""
import pytest


def quarantine(world: str) -> float:
    """
    Given a map of the world as a string, returns the percentage % of the total population that got infected.

    :param world: map of world as string
    :return: percentage % of the total population that got infected
    """
    
    # split world on "X", filter out empty sub-strings
    sub_strings = [str_ for str_ in world.split("X") if str_]

    # if world is empty or contains only "X" chars, the previous filter yields [], then
    # return 0.0 (this avoids zero-division after the loop)
    if not sub_strings:
        return 0.0

    total_infected = 0  # count of everyone infected
    total_population = 0  # count of everyone in world
    for str_ in sub_strings:
        len_str = len(str_)
        total_population += len_str
        if "1" in str_:
            total_infected += len_str
    return (total_infected/total_population) * 100



@pytest.mark.parametrize(
    "world,expected",
    [
        ("01000000X000X011X0X", 73.333333333),
        ("0000000000000000000", 0),
        ("1111111111111111111", 100),
        ("1111111110111111111", 100),
        ("0000000001000000000", 100),
        ("0X000000010000000X0", 88.23529),
        ("1X000000000000000X1", 11.764705),
        ("1X0X0X0X0X1X0X0X0X1", 30.0),
        ("1X0X0X0X001X0X0X0X1", 45.454545),
        ("01000000X000X011X0X", 73.33333333333333),
        ("01X000X010X011XX", 72.72727272727273),
        ("XXXXX", 0.0),
        ("X00X000000X10X0100", 42.857142857142854),
        ("", 0.0),
        ("1", 100.0),
        ("XXX", 0.0),
        ("1X0X1", 66.6666666666666666),
        ("X1X0X1X", 66.6666666666666666),
    ],
)
def test_basic(world, expected):
    EPSILON = 0.00001
    assert abs(quarantine(world) - expected) < EPSILON
