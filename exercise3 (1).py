# Γράψτε έναν κώδικα σε Python ο οποίος να εμφανίζει μόνο τα σχόλια ενός αρχείου που έχει γραφτεί σε C++


from utils import get_string_from_file

string = '# this is not a comment'


# state=0 simainei kodikas
# state=1 simainei string mono
# state=2 simainei string diplo
# state=3 simainei comment

def main():  # sxolio 1 def main():
    state = 0
    comment = ''
    '"'
    text = get_string_from_file('exercise3.py')  # sxolio3843957
    for c in text:
        if state == 0 and (c == '\'' or c == '"'):
            state = 1
        elif state == 1 and (c == '\'' or c == '"'):
            state = 0
        elif state == 0 and c == '#':
            state = 2
        elif state == 2:
            comment = comment + c
            if c == '\n':
                print(comment)
                comment = ''
                state = 0


if __name__ == '__main__':
    main()
