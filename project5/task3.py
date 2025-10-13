import random
#qa = {'Question 1?': '1', 'Question 2?': 'Answer 2'} # for test remove the first '#'

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
    # print(random_question) # for test remove the first '#'
    response = input(random_question + '\nEnter response:')
    if response == qa[random_question]:
        #print('ok') # for test remove the first '#'
        return True
        
    else:
        return False
    
#asking = ask_question(qa) # for test remove the first '#'
