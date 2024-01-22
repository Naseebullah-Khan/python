# Scope
# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope
# def drink_potion():
#   potion_strenght = 2
#   print(potion_strenght)
# drink_potion()
# print(potion_strenght)

# Global Local
# player_health = 10

# def game():
#   def drink_potion():
#     potion_strength = 2
#     print(player_health)
#   drink_potion()
#   print(potion_strenght)

# game()
# print(player_health)

# There is no Block Scope
# game_level = 3
# def create_enemy():
#   enemies = ["Skeleton","Zombie", "Alien"]
#   if game_level < 5:
#     new_enemies = enemies[0]

#   print(new_enemies)

# print(new_enemies)

# Modifying Global Scope
# enemies = 1

# def increase_enemies():
#   # global enemies
#   # enemies += 2
#   # enemies = 2
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global Constants
PI = 3.1415
URL = "https://www.google.com"
TWITTER_HANDLE = "@naseeb_khan"