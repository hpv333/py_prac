def game():
  import art
  print(art.logo)

  import random
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 
 
 
  user_cards = []
  computer_cards = []

  for _ in range(2):
    new_card = deal_card()
    """remember we can't add new card to usercards since we can add nly a list to a list and new_card is not a list"""
    user_cards.append(new_card)
    computer_cards.append(new_card)

  print(f"User cards are : {user_cards}")
  print(f"Computer cards are : {computer_cards[0]}")
  

  def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
      return 0
    if 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)

  def compare(user_score,computer_score):
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    if user_score==computer_score:
      return "Draw"
    elif user_score<computer_score and user_score<=21:
      return "User wins"
    elif user_score>computer_score and computer_score<=21:
      return "Computer wins "  

  computer_score=calculate_score(computer_cards)
  next_card=input("Do you want another card ? Y or N").lower()
  if next_card=="y":
    card3 = deal_card()
    user_cards.append(card3)    
    if computer_score<17:
      new_card=deal_card()
      computer_cards.append(new_card)
    u_score=calculate_score(user_cards)
    c_score=calculate_score(computer_cards)
    result=compare(u_score,c_score)
    print(result)
  
  else:
    u_score=calculate_score(user_cards)
    c_score=calculate_score(computer_cards)
    result=compare(u_score,c_score)
    print(result)
  
  
  again=input("one more game? Y or N").lower()
  if again=="y":
    import click
    def clrscr():
      click.clear()
    clrscr()
    game()
  else:
    print("\n \n Game ends ! have a great day ")
game()
