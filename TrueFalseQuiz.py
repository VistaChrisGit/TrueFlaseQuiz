# [ ] Create the program, run tests
# This is a True or False Quiz using preset answer key and questions

def tf_quiz(Q_string, A_string):
    if Q_string == A_string:
        print('Correct!')
    else:
        print('Wrong!')
        
A1 = 'T'
A2 = 'F'
A3 = 'F'
A4 = 'T'
A5 = 'T'

Q1 = input('The sky is blue - T or F? ').upper()
tf_quiz(Q1, A1)
Q2 = input('The sky is red - T or F? ').upper()
tf_quiz(Q2, A2)
Q3 = input('The sky is black - T or F? ').upper()
tf_quiz(Q3, A3)
Q4 = input('My wife is a beautiful woman - T or F? ').upper()
tf_quiz(Q4, A4)
Q5 = input('It is hot!!!! T or F? ').upper()
tf_quiz(Q5, A5)
