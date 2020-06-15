"""
@Author: Suyash Sonawane (https://github.com/SuyashSonawane)

In second year computer engineering class, group A student’s play cricket, group B
students play badminton and group C students play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET
built-in functions) 
"""

s_cricket = []  # Students playing crickets
s_badminton = []  # Students playing badminton
s_footbal = []  # Students playing football
s_neither = []  # Students how play nothing
s_all = []


def main():
    """
    Main function that contains all the logic

    """

    n = int(input("\nHow many students do you want to enter ? >> "))

    for _ in range(n):
        roll = int(input("\nEnter the roll number of the student ? >>"))
        s_all.append(roll)
        n_games = int(input("\nHow many games does he/she plays ? (0 if none) >>"))
        if n_games == 0:
            s_neither.append(roll)
        i = 0

        while i < n_games:
            category = int(input("1.Cricket\n2.Badminton\n3.Football\n>>"))
            i += 1
            if category == 1:
                s_cricket.append(roll)
            elif category == 2:
                s_badminton.append(roll)
            elif category == 3:
                s_footbal.append(roll)
            else:
                print("Enter correct choice")
                i = i - 1

    while True:
        # Main menu loop

        ui = int(
            input(
                "\nOperations \n1.List of students who play both cricket and badminton\n2.List of students who play either cricket or badminton but not both\n3.Number of students who play neither cricket nor badminton\n4.Number of students who play cricket and football but not badminton.\n99.Exit\n>>"
            )
        )

        if ui == 1:
            playingboth()
        elif ui == 2:
            either_cricket_badminton()
        elif ui == 3:
            neither_cricket_badminton()
        elif ui == 4:
            playing_cricket_football_not_badminton()
        elif ui == 99:
            break
        else:
            print("Enter corrrect option!")


def playingboth():
    # Function for finding all students playing both games (intersection)
    both = []
    for s1 in s_cricket:
        for s2 in s_badminton:
            if s1 == s2:
                both.append(s1)

    both = list(map(str, both))
    print(f"Students playing Cricket and Badminton are " + ",".join(both))


def either_cricket_badminton():
    # Function for finding all the students playing either of the games (Union)
    either = s_cricket
    for s in s_badminton:
        if s not in s_cricket:
            either.append(s)
    either = list(map(str, either))
    print(f"Students playing either Cricket and Badminton are " + ",".join(either))


def neither_cricket_badminton():
    # Function for finding all the students playing neither of the games
    neither = []
    for student in s_all:
        if student not in s_cricket and student not in s_badminton:
            neither.append(student)
    neither = list(map(str, neither))
    print(f"Students playing neither Cricket and Badminton are " + ",".join(neither))


def playing_cricket_football_not_badminton():
    football_cricket = []
    for student in s_all:
        if student in s_cricket and student in s_footbal and student not in s_badminton:
            football_cricket.append(student)

    football_cricket = list(map(str, football_cricket))
    print(
        f"Students playing cricket and football but not badminton are "
        + ",".join(football_cricket)
    )


if __name__ == "__main__":
    main()
