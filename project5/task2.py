import random
# qa = {'Question 1?': 'Answer 1', 'Question 2?': 'Answer 2'} # for test remove the first '#'

def get_random_question(qa):
    question = random.randint(1, len(qa))
    j = 1
    for i in qa:
        if question == j:
            return i
        j+=j
    
# question = get_random_question(qa) # for test remove the first '#'
