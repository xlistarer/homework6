
'''Task 1

Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values. '''
elemlist=list(map(str, input('vvedite strochky: ').split( )))
elemset=set(elemlist)
elemdict={}
for key in elemlist:
    elemdict.update({key:elemlist.count(key)})
print(elemdict)
'''Task 2

Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total price of stock.

 '''
def count_total_price(price, count):
    first=set((price.keys()))
    second=set((count.keys()))
    all=list(first&second)
    summ=0
    for i in range(len(all)):
        summ+=price[all[i]]*count[all[i]]
    return summ
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
print('Общая сумма ваших покупок:',count_total_price(stock,prices))
'''Task 3

List comprehension exercise

Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

 '''

print([(i,i*i) for i in range(1,10)])