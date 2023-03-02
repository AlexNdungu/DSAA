# We are given two sequences and we need to find the length of the longest common subsequence between them.

#Inputs
# seq1 - serendipitous
# seq2 - precipitation

#Output
#lcs length = 7

def lcs_recursive(seq1,seq2, idx1=0, idx2=0):
    
    if idx1 == len(seq1) or idx2 == len(seq2):

        return 0
    
    elif seq1[idx1] == seq2[idx2]:

        return 1 + lcs_recursive(seq1, seq2, idx1 + 1, idx2 + 1)
    
    else:
        option1 = lcs_recursive(seq1, seq2, idx1+1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2 + 1)
        return max(option1,option2)

#Test cases
# General Case(strings)
t0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}

#General case (list)
t1 = {
    'input': {
        'seq1': [1,3,5,6,7,2,5,2,3],
        'seq2': [6,2,4,7,1,5,6,2,3]
    },
    'output': 5
}

#No Common Sequence
t2 = {
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

#One sequence of the other
t3 = {
    'input': {
        'seq1': 'dence',
        'seq2': 'condenced'
    },
    'output': 5
}

#One sequence is empty
t4 = {
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

#both sequences are empty
t5 = {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}


#The test cases
tests = [t0,t1,t2,t3,t4,t5]

# lets test one outcome first

#print(lcs_recursive(t0['input']['seq1'],t0['input']['seq2']))

from jovian.pythondsa import evaluate_test_cases

#evaluate_test_cases(lcs_recursive,tests)

# Now we optimize this by Memorization

def lcs_memo(seq1,seq2):

    memo = {}
    def recurse(idx1=0,idx2=0):

        key = (idx1, idx2)

        if key in memo:

            return memo[key]
        
        elif idx1 == len(seq1) or idx2 == len(seq2):

            memo[key] = 0

        elif seq1[idx1] == seq2[idx2]:

            memo[key] = 1 + recurse(idx1+1, idx2+1)

        else:

            memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))        

        return memo[key]

    return recurse(0,0)    


# lets test one outcome first

#print(lcs_recursive(t0['input']['seq1'],t0['input']['seq2']))

evaluate_test_cases(lcs_memo,tests)