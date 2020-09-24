# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return [sequence]

    # Recursive cases
    else:
        # Set up list to be returned
        perms = []
        last_letter = sequence[-1]
        sequence = sequence[:-1]
        prev_perm_list = get_permutations(sequence)
        
        # Insert 'last_letter' at each position for each permutation
        for p in prev_perm_list:
            for pos in range(0,len(p)+1):
                new_p = p[:pos] + last_letter + p[pos:]
                perms.append(new_p)

        return list(set(perms))

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
    example_input = 'abc'
#    print('Input:', example_input)
    print ('Input:' + example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Expected Output: ' + '["abc", "acb", "bac", "bca", "cab", "cba"]')
#    print('Actual Output:', get_permutations(example_input))
    print ('Actual Output: ' + str(get_permutations(example_input)))
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here
