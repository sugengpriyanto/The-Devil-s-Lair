print('''
     
                 ___-----------___
           __--~~                 ~~--__
       _-~~                             ~~-_
    _-~                                     ~-_
   /                                           \
  |                                             |
 |                                               |
 |                                               |
|                                                 |
|                                                 |
|                                                 |
 |                                               |
 |  |    _-------_               _-------_    |  |
 |  |  /~         ~\           /~         ~\  |  |
  ||  |             |         |             |  ||
  || |               |       |               | ||
  || |              |         |              | ||
  |   \_           /           \           _/   |
 |      ~~--_____-~    /~V~\    ~-_____--~~      |
 |                    |     |                    |
|                    |       |                    |
|                    |  /^\  |                    |
 |                    ~~   ~~                    |
  \_         _                       _         _/
    ~--____-~ ~\                   /~ ~-____--~
         \     /\                 /\     /
          \    | ( ,           , ) |    /
           |   | (~(__(  |  )__)~) |   |
            |   \/ (  (~~|~~)  ) \/   |
             |   |  [ [  |  ] ]  /   |
              |                     |
               \                   /
                ~-_             _-~
                   ~--___-___--~

''')
print("Welcome to The Devil's Lair.")
print("Your mission is to find the way out.\nOr you will be trapped here forever") 
print("There are 2 doors in the left and right")
print("Choose the right door")
door1 = int(input("1 / 2 ? "))
if door1 == 1:
  print("Not so easy. Now you are in the edge of the high cliff of my castle.\nDo you want to ride flying dragon? Or you want to jump off the cliff?")
  door2 = input("ride / jump ? ")
  if door2 == "ride":
    print("That's my dragon. It will bring you to the devil's prison. Hahahaha.")
    print("Game Over")
  else:
    print("You wake up from your nightmare. The Devil's Lair is only on your dream")
else:
  print("You fell into a hole. Game Over")
