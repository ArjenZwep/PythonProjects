import random

#creating the type class, so pokemons have different elements there strong and weak against
class Type:	
    def __init__(self, name, strength, weakness):
        self.name = name
        self.strength = strength
        self.weakness = weakness

class Pokemon:
    #Defining a pokemon with all the needed stats for combat
    def __init__(self, name, level, element, maximum):
        self.name = name
        self.level = level
        self.element = element
        self.maximum = maximum
        self.current = maximum
        self.knocked = False
        self.exp = level * 3

    #Changing the knoked status when someone takes enough damage
    def knocked_out(self):
        self.current = 0
        self.knocked = True
        print(str(self.name) +  ' is now knocked!')

    #This method is simply just removing hp when attacked
    def take_damage(self, damage):
        self.current = self.maximum - damage
        print(f'{self.name} has {self.current} health left!')

    #Method is for taking a potion or healing up
    def regain_health(self, life):
        #Can't regain health when already at max
        if self.maximum == self.current:
          print(str(self.name) + " is already at max life")
        else:
          self.current += life
          #You cannot exceed more than your maximum hp
          if self.current > self.maximum:
            self.current = self.maximum
          print(str(self.name) + "has now " + str(self.current) + " health again!")

    #Method for leveling up, every level gets harder of course
    def level_up(self):
        exp_needed = [2, 7, 11, 15, 20, 27, 36, 49, 60, 72, 85, 100, 120]
        if exp_needed[self.level] > self.exp:
            self.level += 1
            #f'{self.name} just level up to {self.level}!'
            print(str(self.name) + " Level up! to " + str(self.level))


    #attacking a different pokemon, note this was the first itteration when types weren't objects yet, just strings
    def attack(self, pokemon):
        if pokemon.knocked == True:
            print(str(pokemon.name) + " is already knocked out")
        else:
            elements = ["Grass", "Fire", "Water"]
            a_t = elements.index(self.element)
            d_t = elements.index(pokemon.element)
            #Based on type, attacks do half or twice the damage
            if a_t == d_t:
                pokemon.current -= self.level
                print(str(pokemon.name) + " took " + str(self.level) + " damage!")
            elif (a_t == 2 and d_t == 1) or (a_t == 0 and d_t == 2) or (a_t == 1 and d_t == 0):
                pokemon.current -= self.level * 2
                print(str(pokemon.name) + " took " + str(self.level * 2) + " damage!")
            elif (a_t == 1 and d_t == 2) or (a_t == 2 and d_t == 0) or (a_t == 0 and d_t == 1):
                pokemon.current -= self.level / 2
                print(str(pokemon.name) + " took " + str(self.level / 2) + " damage!")
            #In the situation that the defending pokemon gets knocked invoke knocked method and the level up method    
            if pokemon.current <= 0:
                self.exp += pokemon.level
                pokemon.knocked_out()
                self.level_up()
                
    #The new method for attacking improved scalabillity for more types
    def attack_2(self, pokemon):
        if pokemon.knocked == True:
            print(str(pokemon.name) + " is already knocked out")
        else:
            if self.type in pokemon.type.weakness:
                pokemon.current -= self.level * 2
                print(str(pokemon.name) + " took " + str(self.level * 2) + " damage!")
            elif self.type in pokemon.type.strength:
                pokemon.current -= self.level / 2
                print(str(pokemon.name) + " took " + str(self.level / 2) + " damage!")
            else:
                pokemon.current -= self.level
                print(str(pokemon.name) + " took " + str(self.level) + " damage!")
            #In the situation that the defending pokemon gets knocked invoke knocked method and the level up method    
            if pokemon.current <= 0:
                self.exp += pokemon.level
                pokemon.knocked_out()
                self.level_up()


#The trainer object, which can hold multipile pokemons and items
class Trainer:
  def __init__(self, name, pokemons, potions, active):
    self.name = name
    self.pokemons = pokemons
    self.potions = potions
    self.active = active
    
  #This method is for giving potions   
  def give_potion(self, which):
    if which == "Normal":
      self.pokemons[self.active].regain_health(20)
      self.potions -= 1
    else:
      self.pokemons[self.active].regain_health(50)
      self.potions -= 1
        
  #Method for showing which pokemon the trainer has and which one is currently active  
  def show_pokemon(self):
    counter = 1
    for p in self.pokemons:
      if counter - 1 == self.active:
        print(str(counter) + " " + str(p.name) + " this one is currently active")
        counter += 1
      else:
        print(str(counter) + " " + str(p.name))
        counter += 1
        
  #Method for switiching the active pokemon
  def switch(self, which):
    self.active = which
    
  #method for attacking another trainers active pokemon with your own active pokemon
  def attack_trainer(self, trainer):
     self.pokemons[self.active].attack(trainer.pokemons[self.active])
    #Invoking the switch method when current pokemon gets knocked
     if trainer.pokemons[self.active].knocked == True:
         trainer.show_pokemon()
         other_poke = input("Your pokemon got knocked out to wich you want to switch?")
         trainer.switch(other_poke)
        
#defining some standard types      
types = {
    "Water" : Type("Water", ["Fire"], ["Grass"]),
    "Fire" : Type("Fire", ["Grass"], ["Water"]),
    "Grass" : Type("Grass", ["Water"], ["Fire"])
}

#Defining the starterpokemons
starters = {
"Charmander" : Pokemon("Charmander", 7, types["Fire"], 60),
"Squirtle" : Pokemon("Squirtle", 8, types["Water"], 30),
"Bulbasar" : Pokemon("Bulbasar", 3, types["Grass"], 60)
}

#Having some wild pokemons to train against
wild_pokemon = {
"1" : Pokemon("Ratata", random.randint(1, 4), "Water", 20),
"2" : Pokemon("Pidgey", random.randint(1, 4), "Grass", 15)
}


'''This part below is actually playing the game, using the framework we build above to replicate the first minutes of a pokemon game'''

#Choosing a starter!
print("welcome to our pokemon adventure! First of all choose your starter by typing in the name")

for keys in starters:
    print(starters[keys].name)
choose_starter = input()

#Making the trainer Arjen with bulbasar and the chosen starter
arjen = Trainer("arjen", [starters[choose_starter.capitalize()], starters["Bulbasar"]], 3, 0)
print("You have choosen " + str(arjen.pokemons[0].name))

#Function for training in the first few grass patches or fighting your rival
def train_poke(trainer):
    Choose = input("What do you want to do? 1. Train in the wild 2. Fight your rival")
    if Choose == "1":
        Wild_poke = wild_pokemon[str(random.randint(1, 2))]
        print("you have encounterd a " + str(Wild_poke.name))
        while Wild_poke.knocked == False:
            fightflight = input("what do want to do 1.take a potion or 2.attack?")
            if fightflight == "1":
                trainer.give_potion
            else:
                trainer.pokemons[trainer.active].attack(Wild_poke)
            Wild_poke.attack(trainer.pokemons[trainer.active])
        print("you have won!")
train_poke(arjen)