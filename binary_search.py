#Binary Search, Linked List And Complexity
#The flipping acrd problem

def locate_card(cards, query):

    #Create 

    #lets define test cases

    #Letscreate a big test list
    tests = []

    #Respresent the test cases as dictionaries
    test = {
        'input': {
            'cards':[13,11,10,7,4,3,1,0],
            'query': 7
        },
        'output': 3
    }

    #Append the tests
    tests.append(test)

    #Query occurs in the middle
    test1 = {
        'input': {
            'cards':[13,11,10,7,4,3,1,0],
            'query': 7
        },
        'output': 3
    }

    #Append the tests
    tests.append(test1)

    #Query is first element
    test2 = {
        'input': {
            'cards':[4,2,1,-1],
            'query': 4
        },
        'output': 0
    }

    #Append the tests
    tests.append(test2)

    #Query is the last element
    test3 = {
        'input': {
            'cards':[3,-1,-9,-127],
            'query': -127
        },
        'output': 0
    }

    #Append the tests
    tests.append(test3)

    #Query contains one element
    test4 = {
        'input': {
            'cards':[6],
            'query': 6
        },
        'output': 0
    }

    #Append the tests
    tests.append(test4)

    #Card doesnt contain the query
    #Assume it will return -1

    test5 = {
        'input': {
            'cards':[9,7,5,2,-9],
            'query': 4
        },
        'output': -1
    }

    
    #Append the tests
    tests.append(test5)

    #The cards is empty
    test6 = {
        'input': {
            'cards':[],
            'query': 7
        },
        'output': -1
    }

    
    #Append the tests
    tests.append(test6)

    #The cards have repeating numbers
    test7 = {
        'input': {
            'cards':[8,8,6,6,6,6,6,3,2,2,2,0,0,0],
            'query': 3
        },
        'output': 7
    }


    #Append the tests
    tests.append(test7)

    #When query occurs many times
    test8 = {
        'input': {
            'cards':[8,8,6,6,6,6,6,3,2,2,2,0,0,0],
            'query': 6
        },
        'output': 2
    }


    #Append the tests
    tests.append(test8)

    #Look at the test cases
    print(tests)