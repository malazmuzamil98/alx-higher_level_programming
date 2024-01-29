#!/usr/bin/python3
"""
This module contains an algorithm that resolves the N-Queen puzzle
using backtracking
"""


def isSafe(m_queen, nqueen):
    """Method that determines if the queens can or can't kill each other"""

    for i in range(nqueen):

        if m_queen[i] == m_queen[nqueen]:
            return False

        if abs(m_queen[i] - m_queen[nqueen]) == abs(i - nqueen):
            return False

    return True


"""
This module contains an algorithm that resolves the N-Queen puzzle
using backtracking
"""


def print_result(m_queen, nqueen):
    """_summary_

    Args:
        m_queen (_type_): _description_
        nqueen (_type_): _description_
    """

    res = []

    for i in range(nqueen):
        res.append([i, m_queen[i]])

    print(res)


"""
This module contains an algorithm that resolves the N-Queen puzzle
using backtracking
"""


def Queen(m_queen, nqueen):
    """_summary_

    Args:
        m_queen (_type_): _description_
        nqueen (_type_): _description_
    """

    if nqueen is len(m_queen):
        print_result(m_queen, nqueen)
        return

    m_queen[nqueen] = -1

    while((m_queen[nqueen] < len(m_queen) - 1)):

        m_queen[nqueen] += 1

        if isSafe(m_queen, nqueen) is True:

            if nqueen is not len(m_queen):
                Queen(m_queen, nqueen + 1)
