cart = []
prices = []

print("😊🤗Welcome to shopping cart!😊🤗")

while True:
      print("""
      Please select one of the following: 
      1. Add item
      2. View cart
      3. Remove item
      4. Compute total
      5. Quit """)
      action = int(input("Please enter an action: "))
     
      # add items
      if action ==1:
          item = input(f"What item would you like to add?  ") 
          cart.append(item)
          price = input(f"What is the price of {item} ?")
          prices.append(price)
          print({item}," has been added to the cart.")

      # view cart 
      elif action == 2:
          print('The contents of the shopping cart are:')
          for i, item in enumerate(cart):
              print(f"{i + 1}. {item} -{prices,{i}}")
      # remove
      elif action == 3:
           i = int(input(f"Which item would you like to remove? "))
           if i < len(cart) and i > 0:
                cart.pop(i - 1)
                prices.pop(i - 1)
           print(f'{item} '"has been removed.")
      
      # compute total
      elif action == 4:
          total = 0
          for price in prices:
              total = price
          print(f"The total price of the items in the shopping cart is ${total:.2}")

      # quit 
      elif action == 5:
          break  

      
 
    

 
 

    
