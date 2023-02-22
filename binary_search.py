#Binary Search, Linked List And Complexity
#The flipping acrd problem

def locate_card(cards, query):

    #Create a variable to keep track of the index position
    position = 0

    #Set up a loop 
    while position < len(cards):

        if cards[position] == query:

            #The answer has been found 
            return position
            
        position += 1

    return -1  



#lets define test cases
#Lets create a big test list
tests = []
#Append the tests
tests.append({
    'input': {
        'cards':[13,11,10,7,4,3,1,0],
        'query': 7
    },
    'output': 3
})

#Query occurs in the middle
#Append the tests
tests.append({
    'input': {
        'cards':[13,11,10,7,4,3,1,0],
        'query': 7
    },
    'output': 3
}
)

#Query is first element
#Append the tests
tests.append({
    'input': {
        'cards':[4,2,1,-1],
        'query': 4
    },
    'output': 0
})

#Query is the last element
#Append the tests
tests.append({
    'input': {
        'cards':[3,-1,-9,-127],
        'query': -127
    },
    'output': 0
})

#Query contains one element
#Append the tests
tests.append({
    'input': {
        'cards':[6],
        'query': 6
    },
    'output': 0
})

#Card doesnt contain the query
#Assume it will return -1
#Append the tests
tests.append({
    'input': {
        'cards':[9,7,5,2,-9],
        'query': 4
    },
    'output': -1
})

#The cards is empty
#Append the tests
tests.append({
    'input': {
        'cards':[],
        'query': 7
    },
    'output': -1
}
)

#The cards have repeating numbers
#Append the tests
tests.append({
    'input': {
        'cards':[8,8,6,6,6,6,6,3,2,2,2,0,0,0],
        'query': 3
    },
    'output': 7
})

#When query occurs many times
#Append the tests
tests.append({
    'input': {
        'cards':[8,8,6,6,6,6,6,3,2,2,2,0,0,0],
        'query': 6
    },
    'output': 2
})

print(tests)

#Lets test using the first test case
#Respresent the test cases as dictionaries
# test = {
#     'input': {
#         'cards':[13,11,10,7,4,3,1,0],
#         'query': 7
#     },
#     'output': 3
# }

# result = locate_card(test['input']['cards'], test['input']['query'])

# print(result == test['output'])

#Now we test all our test cases
from jovian.pythondsa import evaluate_test_case

evaluate_test_case(locate_card, tests)