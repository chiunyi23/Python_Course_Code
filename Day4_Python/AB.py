import random

def set_answer():
    ran = random.randint(1000, 9999)
    return ran

print(set_answer())

def judge_guess(guess, ans):
    A = 0
    B = 0
    for i in range(4):
        for j in range(4):
            print('in')
            if guess[i] is ans[j]:
                if i is j:
                    A = A + 1
                else:
                    B = B + 1
    str(A) + "A" + str(B) + "B"
    return str

is_Play = True
is_Correct = False

while is_Play:
    ans = str(set_answer())
    while is_Correct is False:
        n = input()
        check = judge_guess(n, ans)
        if(check is "correct!"):
            print(check)
            is_Correct = True
        else:
            print(check)

