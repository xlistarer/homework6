
'''Task 1

Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values. '''
elemlist=list(map(str, input('vvedite strochky: ').split( )))
elemset=set(elemlist)
elemdict={}
for key in elemlist:
    elemdict.update({key:elemlist.count(key)})
print(elemdict)