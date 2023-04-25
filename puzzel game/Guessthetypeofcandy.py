word ='starburst'

guess = ''
guess_count = 0
print('Your hint is:',end= '')
for letter in word:
      print('_', end=' ')
print()
      

while word !=guess:  
    guess_count =guess_count + 1 
    guess = input('What is your guess? ')
    for b ,letter in enumerate(guess.lower()) :
      if letter == word[b]:
         print(letter.upper(),end=' ')
      elif letter in word :
         print(letter.lower(),end=' ')
        
      else:
         print('_', end=' ')
print()
            

print('🍭Congratulations!🎉 You guess it!!🍭')      
print(f'It took you {guess_count} guesses.')