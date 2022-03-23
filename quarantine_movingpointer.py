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
    Author: William Noonan

    Given a map of the world as a string, returns the percentage % of the total population that got infected.

    Instead of splitting world on "X" and using a nested loop to check containment of "1" in each substring,
    this approach passes over world one character at a time, updating the infected count on the fly. Therefore this
    approach is more efficient than the string-splitting approach.

    :param world: map of world as string
    :return: percentage % of the total population that got infected
    """
    total_population = 0  # world population
    total_infected = 0  # total infected in world
    continent_population = 0  # population of continent
    num_infected = 0  # number of infected people in continent
    for i in range(len(world)):
        char = world[i]
        if char in {"0", "1"}:  # set of 0 and 1 for O(1) containment check
            total_population += 1
            continent_population += 1
            if num_infected or char == "1":
                num_infected = continent_population
        else:
            # this is the "X" case (I think this is more readable than a 'if char == "X" ... else ...' format)
            total_infected += num_infected
            continent_population = 0
            num_infected = 0

    # update total infected
    total_infected = max(total_infected, total_infected + num_infected)

    return (total_infected/total_population) * 100 if total_population > 0 else 0.0  # avoids zero-division



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
