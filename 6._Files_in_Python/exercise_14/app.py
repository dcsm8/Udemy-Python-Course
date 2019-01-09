"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

questions_file = open('questions.txt', 'r')
questions = {}

for line in questions_file.readlines():
    question, answer = line.strip().split('=')
    questions[question] = answer

questions_file.close()

correct_answers = 0
maximum_score = len(questions)

for question, answer in questions.items():
    user_answer = input('{}='.format(question))
    if user_answer == answer:
        correct_answers = correct_answers + 1

result_file = open('result.txt', 'w')

result_file.write(
    'Your final score is {}/{}.'.format(correct_answers, maximum_score))

result_file.close()
