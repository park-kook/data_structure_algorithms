
#Create a function called word_split() which takes in a string phrase and a 
#set list_of_words. The function will then determine if it is possible to 
#split the string in a way in which words can be made from the list of words. 
#You can assume the phrase will only contain words found in the dictionary 
#if it is completely splittable.



def word_split(phrase,list_of_words, output=None): #call recursively the function, we put None
     
    if output is None:
        output=[]  
    for word in list_of_words:

        if phrase.startswith(word): #startssith means starts with this 'word' in phrase sentence, it it is
            #then it returns True. 
            output.append(word)
            
            return word_split(phrase[len(word):],list_of_words,output)
  
    return output #if no phrase start with happen from second if above statement

word_split('themanran',['clown','ran','man'])
word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
word_split('ilovedogsJohn',['dogs','am','i','a','lover','love','John'])
phrase = 'ilovedogsJohn'
phrase.startswitch('i')
