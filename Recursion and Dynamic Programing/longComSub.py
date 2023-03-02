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
        'seq': 'serendipitous',
        'seq': 'precipitation'
    },
    'output': 7
}

#General case (list)
t1 = {
    'input': {
        'seq': [1,3,5,6,7,2,5,2,3],
        'seq': [6,2,4,7,1,5,6,2,3]
    },
    'output': 5
}

#No Common Sequence
t2 = {
    'input': {
        'seq': 'asdfwevad',
        'seq': 'opkpoiklklj'
    },
    'output': 0
}

#One sequence of the other
t3 = {
    'input': {
        'seq': 'dence',
        'seq': 'condenced'
    },
    'output': 5
}

#One sequence is empty
t4 = {
    'input': {
        'seq': '',
        'seq': 'opkpoiklklj'
    },
    'output': 0
}

#both sequences are empty
t5 = {
    'input': {
        'seq': '',
        'seq': ''
    },
    'output': 7
}


#The test cases
tests = [t0,t1,t2,t3,t4,t5]

