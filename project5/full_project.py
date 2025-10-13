import random

# This code creates the quiz.txt file for you to test with.
# You can change what gets written to test various scenarios!
f = open('quiz.txt', 'w')
f.write('Question 1?|||Answer1\nQuestion 2?|||Answer 2\n')
f.close()

def load_questions_and_answers(file_name):
    quiz = open (file_name, 'r')
    dictionary_quiz = {}
    for line in quiz:
        line = line.strip('\n')
        index = line.index('|||')
        question = line[:index]
        answer =  line[index+3:]
        dictionary_quiz[question]= answer 
    quiz.close()
        
  
    return dictionary_quiz
        
qa = {'Question 1?': '1', 'Question 2?': 'Answer 2'}

def get_random_question(qa):
    question = random.randint(1, len(qa))
    j = 1
    for i in qa:
        if question == j:
            return i
        j+=j
    
question = get_random_question(qa)    

def ask_question(qa):
    random_question = get_random_question(qa)
    # print(random_question)
    response = input(random_question + '\nEnter response:')
    if response == qa[random_question]:
        #print('ok')
        return True
        
    else:
        return False
    
asking = ask_question(qa)

def main():
    file_name = input('What is the name of the QA file? ')
    number_of_questions = int(input('How many questions should be asked? '))
    questions_answers = load_questions_and_answers(file_name)
    correct_count = 0
    for i in range(number_of_questions):
        if ask_question(questions_answers)
            correct_count += 1
    print('You got', correct_count, 'out of', number_of_questions, 'correct.')
    print('Your percentage grade: ' + str(correct_count / number_of_questions * 100) + '%')
