"""CSC108/A08: Fall 2021 -- Assignment 1: unscramble

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Michelle Craig, Anya Tafliovich.

"""

# Valid moves in the game.
SHIFT = 'S'
SWAP = 'W'
CHECK = 'C'


# We provide a full solution to this function as an example.
def is_valid_move(move: str) -> bool:
    """Return True if and only if move is a valid move. Valid moves are
    SHIFT, SWAP, and CHECK.

    >>> is_valid_move('C')
    True
    >>> is_valid_move('S')
    True
    >>> is_valid_move('W')
    True
    >>> is_valid_move('R')
    False
    >>> is_valid_move('')
    False
    >>> is_valid_move('NOT')
    False

    """

    return move == CHECK or move == SHIFT or move == SWAP

# Your turn! Provide full solutions to the rest of the required functions.
def get_section_start(section_num: int, section_len: int) -> int:
    """Return the index of the first character of the selected string section
    as an integer.
    Precondition:Each section has at least 1 character.

    >>> get_section_start(1, 4)
    0
    >>> get_section_start(2, 2)
    2
    >>> get_section_start(3, 4)
    8

    """
    return section_num * section_len - section_len

def get_section(game_state: str, section_num: int, section_len: int) -> str:
    """Return the section of the game state that corresponds to the given
    section number as a string.
    Precondition: Both section number and section length are valid for the
    given section number.

    >>> get_section('csca08fun', 2, 3)
    'a08'
    >>> get_section('canada', 3, 2)
    'da'
    >>> get_section('feedback', 2, 4)
    'back'
    >>> get_section('oh', 2, 1)
    'h'
    >>> get_section('01234abcde45678', 2, 5)
    'abcde'

    """
    return game_state[section_len * (section_num - 1):section_len * section_num]

def is_valid_section(game_state: str, possible_section: int,
                     possible_section_len: int) -> bool:
    """Return true only if it is possible to divide up the given state string
    into sections.

    >>> is_valid_section('csca08fall2021', 2, 3)
    False
    >>> is_valid_section('csca08fall2021', 4, 2)
    True
    >>> is_valid_section('csca08fall2021', 8, 2)
    False
    >>> is_valid_section('csca', 4, 1)
    True
    >>> is_valid_section('csca', 4, 3)
    False

    """
    if possible_section <= len(game_state)//possible_section_len:
        if len(game_state) % possible_section_len == 0:
            return True
    return False

def swap(game_state: str, start_index: int, end_index: int) -> str:
    """Return a string which is the result of swapping the character of
    start_index (inclusive) and the character of the end_index (exclusive).
    Precondition: Both start_index and end_index are vaild for the given
    state string, and that start_index < end_index - 1.

    >>> swap('computerscience', 0, 8)
    'romputecscience'
    >>> swap('computerscience', 6, 10)
    'computcrseience'
    >>> swap('cat', 0, 2)
    'act'
    >>> swap('apple', 1, 4)
    'alppe'

    """
    new_start = game_state[end_index - 1]
    new_end = game_state[start_index]
    middle = game_state[start_index + 1:end_index - 1]
    before_start = game_state[:start_index]
    after_end = game_state[end_index:]
    return before_start + new_start + middle + new_end + after_end

def shift(game_state: str, start_index: int, end_index: int) -> str:
    """Return a string applying the shift operation to the section of the given
    game state string between the start index (inclusive) and the end index
    (exclusive).
    Precondition: Both start adn end index are vaild for the given state string,
    and that start_index < end_index -1.

    >>> shift('computerscience', 0, 8)
    'omputercscience'
    >>> shift('computerscience', 6, 10)
    'computrsceience'
    >>> shift('abcde', 1, 3)
    'acbde'

    """
    before_start = game_state[:start_index]
    after_end = game_state[end_index:]
    middle = game_state[start_index + 1:end_index]
    shifted_char = game_state[start_index]
    new_str = before_start + middle + shifted_char + after_end
    return new_str

def check(game_state: str, start_index: int, end_index: int, answ: str) -> bool:
    """Return true if the game_state string between the start index (inclulsive)
    and the end index (exclusive) is the same as the answer string.

    >>> check('csca80fun', 6, 9, 'csca08fun')
    True
    >>> check('ccsa80fun', 0, 3, 'csca08fun')
    False
    >>> check('asshimi', 2, 5, 'sashimi')
    True

    """
    game_state_str = game_state[start_index:end_index]
    answ_str = answ[start_index:end_index]
    return game_state_str == answ_str

def check_section(game_state: str, section_num: int, section_len: int,
                  answ: str) -> bool:
    """Return true if the string of the specific section is the same as the
    answer.
    Precondition: section_num and section_len are vaild for the given string,
    and the fourth argument is a vaild answer for the given game_state string.

    >>> check_section('ccsa80fun', 3, 3, 'csca08fun')
    True
    >>> check_section('ccsa80fun', 1, 3, 'csca08fun')
    False
    >>> check_section('1234abcd1234', 2, 4, '4321dcba4321')
    False
    >>> check_section('1234abcd1234', 2, 4, '4321abcd4321')
    True
    """

    get_game_str = get_section(game_state, section_num, section_len)
    get_answ_str = get_section(answ, section_num, section_len)
    return get_game_str == get_answ_str

def change_section(game_state: str, game_move: str, section_num: int,
                   section_len: int) -> str:
    """Return a new game state from applying the given game move on the section
    with the given section number.
    Precondition: Section number and section length is a vaild number,
    and the second argument is a vaild game move that specifies eith a Swap
    or a Shift opeartion.

    >>> change_section('computerscience', 'W', 2, 5)
    'compucerstience'
    >>> change_section('cryptocat', 'S', 2, 3)
    'crytopcat'
    >>> change_section('abcdefghigko', 'S', 1, 6)
    'bcdefaghigko'
    >>> change_section('helloworld', 'W', 4, 2)
    'hellowrold'
    >>> change_section('blueball', 'S', 3, 2)
    'blueabll'
    >>> change_section('blueball', 'W', 2, 4)
    'bluelalb'

    """
    get_section_str = get_section(game_state, section_num, section_len)
    before_section_str = game_state[:section_len * (section_num - 1)]
    after_section_str = game_state[section_len * (section_num):]

    if game_move == 'S':
        shifted_section = shift(get_section_str, 0, len(get_section_str))
        return before_section_str + shifted_section + after_section_str

    if game_move == 'W':
        swapped_section = swap(get_section_str, 0, len(get_section_str))
        return before_section_str + swapped_section + after_section_str
    return None

def get_move_hint(game_state: str, section_num: int, section_len: int,
                  answ: str) -> str:
    """Return a suggestion for which game move to perform next.
    Precondition: Section number and section length are vaild for the given
    game state string, and the fourth argument is a vaild answer string for
    given game state.

    >>> get_move_hint('TCADOGFOXEMU', 1, 3, 'CATDGOXOFEMU')
    'S'
    >>> get_move_hint('TACDOGFOXEMU', 1, 3, 'CATDOGXOFEMU')
    'W'
    >>> get_move_hint('adcdhfge', 2, 4, 'abcdefgh')
    'W'
    >>> get_move_hint('dabcefgh', 1, 4, 'abcdefgh')
    'S'
    """

    shift_once = shift(game_state, get_section_start(section_num, section_len),
                       section_len + get_section_start(section_num, section_len)
                       )

    shift_twice = shift(shift_once, get_section_start(section_num, section_len),
                        section_len + get_section_start(section_num,
                                                        section_len))

    swap_once = swap(game_state, get_section_start(section_num, section_len),
                     section_len + get_section_start(section_num, section_len))

    get_shifted_once_str = get_section(shift_once, section_num, section_len)
    get_shifted_twice_str = get_section(shift_twice, section_num, section_len)
    get_swapped_once_str = get_section(swap_once, section_num, section_len)
    get_answ_str = get_section(answ, section_num, section_len)

    if get_shifted_once_str == get_answ_str:
        return 'S'
    if get_shifted_twice_str == get_answ_str:
        return 'S'
    if get_swapped_once_str == get_answ_str:
        return 'W'
    return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
