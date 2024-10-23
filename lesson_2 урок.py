"Наследование и Множество"

class Game:
    def __init__(self, game_name, graphics, game_year,company):
        self.game_name=game_name
        self.graphics=graphics
        self.game_yaer=game_year
        self.company=company
    
    def info(self):
        print(f"Game - {self.game_name} - {self.graphics} - {self.game_yaer} - {self.company} - {self.multiplayer}")

# game = Game('MobileLegends','FULL HD','2017','Tencent')
# game.info()

class Roblox(Game):
    def __init__(self, game_name, graphics, game_year, company,multiplayer):
        super().__init__(game_name, graphics, game_year, company)
        # Game.__init__(self, game_name, graphics, game_year, company)
        self.multiplayer=multiplayer
        self.name = 'Erbol'
        self.gender = 'man'
        self.skin = 'sky'
        self.hp = '100'

    def info_player(self):
        print(f'Player - {self.name}, Gender - {self.gender}, Skin - {self.skin}, Health point - {self.hp}')

    def edit_player(self):
        name = input('Введите тмя игрока: ')
        gender = input("Введите пол игрока: ")
        skin = input("Введите облик: ")
        self.name = name
        self.gender = gender
        self.skin = skin
  
# roblox = Roblox("Roblox", "ULTRA", "2006", "Roblox_corparatyon","Да")
# roblox.info()
# roblox.edit_player()
# roblox.info_player()

class Strike(Roblox):
    def __init__(self, game_name, graphics, game_year, company, multiplayer):
        super().__init__(game_name, graphics, game_year, company, multiplayer)

    def info_player(self):
        return super().info_player()
ct = Strike("Roblox", "ULTRA", "2006", "Roblox_corparatyon","Да")
ct.edit_player()
ct.info_player()