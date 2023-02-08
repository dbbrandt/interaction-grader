from interactiongrader import Answer

correct_answer = input("Actor name: ")
user_answer = input("Misspelled actor name: ")
ans = Answer(correct_answer)
if ans.is_misspelling(user_answer):
    print('Correct Answer')
else:
    print('Incorrect answer: {}'.format(user_answer))

print('User input : {}'.format(user_answer))
print('correct Ans: {}'.format(ans.sentence))


