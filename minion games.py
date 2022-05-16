def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    vowels = 'aeiou'
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string)-i
        else:
            stuart += len(string)-i
    if stuart > kevin:
        print('stuart', stuart)
    elif stuart < kevin:
        print('kevin',kevin)
    else:
        print('draw')

minion_game('banana')
string = 'banana'
