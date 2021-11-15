def number_guessing_game():
  logo=""""

                    (   (                )          )         *             (      
  (                )\ ))\ )    *   ) ( /(       ( /(       (  `     (      )\ )   
  )\ )      (  (  (()/(()/(  ` )  /( )\())(     )\())   (  )\))(  ( )\ (  (()/(   
  (()/(      )\ )\  /(_))(_))  ( )(_)|(_)\ )\   ((_)\    )\((_)()\ )((_))\  /(_))  
  /(_))_ _ ((_|(_)(_))(_))   (_(_()) _((_|(_)   _((_)_ ((_|_()((_|(_)_((_)(_))    
  (_)) __| | | | __/ __/ __|  |_   _|| || | __| | \| | | | |  \/  || _ ) __| _ \   
    | (_ | |_| | _|\__ \__ \    | |  | __ | _|  | .` | |_| | |\/| || _ \ _||   /   
    \___|\___/|___|___/___/    |_|  |_||_|___| |_|\_|\___/|_|  |_||___/___|_|_\   
                                                                                  """
                                                
  print(logo+"\n\n")
  print("Welcome to the number guessing game \n")
  print("I'm thinking of a number between 1 to 100\n")
  import random as rd
  import click
  def new_game() : 
   next_game=input("One more game ? Y or N").lower()
   if next_game=="y":
    click.clear()
    number_guessing_game()

  answer=rd.randint(1,100)
  level=input("Choose a level, easy or difficult:  ").lower()
  if level=="easy":
    no_of_guesses=10
  else:
    no_of_guesses=5
  for i in range(0,no_of_guesses):
    
    while no_of_guesses>=0:
      num=int(input("Make a guess:  "))
      
      if num>answer:
        print("Too high")
        no_of_guesses-=1
        print(f"You have {no_of_guesses} attempts left")
        break
      elif num<answer:
        print("Too low")
        no_of_guesses-=1
        print(f"You have {no_of_guesses} attempts left")
        break
      elif num==answer:
        print("Right Answer \n\n You won !!")
        break
    else:
      new_game()

number_guessing_game()
