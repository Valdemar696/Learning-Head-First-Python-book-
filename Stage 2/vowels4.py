vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels: ')
fund = {}
fund['a'] = 0
fund['e'] = 0
fund['i'] = 0
fund['o'] = 0
fund['u'] = 0
for letter in word:
    if letter in vowels:
        fund[letter] += 1
for k,v in sorted(fund.items()):
    print (k, 'was found', v, 'time(s).')