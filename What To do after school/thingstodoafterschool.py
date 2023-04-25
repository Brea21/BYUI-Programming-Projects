print('Paris, Chrissy and Bella decided that after school they will go to the mall to walk around and hangout. However,  Linda wanted them to skip school to smoke marijuana with her.')
choice=input('What should the girls do? Type MALL or MARIJUANA:  ')
if choice.lower()== 'mall': 
    activity=input('The girls bought some clothes, shoes and snacks. What should the girls do next? Watch a movie, go to the pet store or visit the game room? Type MOVIE or PET or GAMEROOM:')
    if activity.lower() == 'movie': 
        days_end=input('The girls watched Teen Wolf, and then it was time to go home. Would they catch the bus or call their parents? Type BUS or PARENTS:')
        if days_end.lower() == 'bus' :print('The ride home was fun, and the girls said goodbye at the busstop, it was a fun day.')
        if days_end.lower() == 'parents' :print('Their parents came quickly, the girls hugged each other and said goodbye.')
    if activity.lower() == 'pet': 
        pet=input('The girls played with the animals and Paris decided to adopt a pet. Whould she adopt a cat or dog? Type CAT or DOG:')
        if pet.lower() == 'cat' :print('Paris named her pet cat Hope.')
        if pet.lower() == 'dog' :print('Paris named her dog Winter.')     
    if activity.lower() == 'gameroom':
        toy=input('The girls had fun playing and each won the same stuffed toy.Did they win a Teddy Bear or giraffe? Type TEDDY or GIRAFFE:')
        if toy.lower() == 'teddy' :print('The girls won pink teddy bears with a ribbion.')
        if toy.lower() == 'giraffe' :print('The girls won baby blue girraffe.')
if choice.lower() == 'marijuana': 
    bad_choice=input('The girls skipped school and smoke marijuana behind a abandoned building. What happened next? a passerby called the police or Chrissy became unconcious. Type POLICE or CHRISSY:' )
    if bad_choice.lower() == 'police':
        consequence=input('The police caught them and took them to the police station and called their parents to pick them up. Their parents grounded them for one month or three months. Type ONE or THREE:')
        if consequence.lower() == 'one' :print('The girls were grounded for one month and missed the class party.')
        if consequence.lower() == 'three' :print('The girls were grounded for three months and missed their prom.')
    if bad_choice.lower() == 'chrissy':
        punishment=input('Chrissy fell to the floor. The girls were so afraid they shook Chrissy to wake her up. Paris quickly called the ambulance for help. After that scare the girls got suspended from school or had to do community service. Type SUSPENDED or COMMUNITY:')
        if punishment.lower()=='suspended':print('The girls were suspended from school for two weeks.')
        if punishment.lower()=='community':print('The girls had to pick up trash alongside the road. For one week.')
else:
    print('Please try Again.!')

