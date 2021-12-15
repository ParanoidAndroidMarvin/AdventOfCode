import os
import keyboard

from puzzles import binary_diagnostic, dive, giant_squid, hydrothermal_venture, lanternfish, the_treachery_of_whales, \
    seven_segment_search, smoke_basin, syntax_scoring, dumbo_octopus

selected = 1
puzzles = [
    "Sonar Sweep",
    "Dive",
    "Binary Diagnostic",
    "Giant Squid",
    "Hydrothermal Venture",
    "Lanternfish",
    "The Treachery of Whales",
    "Seven Segment Search",
    "Smoke Basin",
    "Syntax Scoring",
    "Dumbo Octopus"
]


def clear():
    print('\n' * 25)
    os.system('cls')


def show_menu():
    clear()
    print('AdventOfCode')
    print('=================')
    print('Choose puzzle:')
    for i in range(1, len(puzzles) + 1):
        print('{2} Day {0}: {1} {3}'.format(i,
                                            puzzles[i - 1],
                                            ">" if selected == i else " ",
                                            "<" if selected == i else " "))
    print('\n[˄]Up [˅]Down [return]Select [esc]Exit')


def up():
    global selected
    selected = max(1, selected - 1)
    show_menu()


def down():
    global selected
    selected = min(len(puzzles), selected + 1)
    show_menu()


def select():
    print('\n\nPuzzle result day {0}:'.format(selected))
    match selected:
        case 1:
            print('Not yet implemented')
        case 2:
            dive.solve()
        case 3:
            binary_diagnostic.solve()
        case 4:
            giant_squid.solve()
        case 5:
            hydrothermal_venture.solve()
        case 6:
            lanternfish.solve()
        case 7:
            the_treachery_of_whales.solve()
        case 8:
            seven_segment_search.solve()
        case 9:
            smoke_basin.solve()
        case 10:
            syntax_scoring.solve()
        case 11:
            dumbo_octopus.solve()


show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('enter', select)
keyboard.add_hotkey('backspace', show_menu)
keyboard.wait('esc')
