class Personagem:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.level = 1
        self.xp = 0
        self.xp_max = 30
        self.vida = 100
        self.vida_max = 100
        self.ataque = 15
        self.defesa = 8
        self.mana = 65
        self.mana_max = 65
        self.gold = 0
        self.iventario = ['Poção pequena']
        
    def receber_dano(self, dano):
        dano_final = max(1, dano - self.defesa)
        self.vida = max(0, self.vida - dano_final)
        return dano_final
    
    def curar(self, vida):
        if self.vida == self.vida_max:
            return False
        self.vida = min(self.vida_max, self.vida + vida)
        return True
    
    def usar_item(self, item):
        if item == 'Poção pequena':
            self.vida  = min(self.vida_max, self.vida + 20)
        elif item == 'Poção grande':
            self.vida = min(self.vida_max, self.vida + 50)
        elif item == 'Poção de mana':
            self.mana = min(self.mana_max, self.mana + 50)
        else:
            return False
        
        self.iventario.remove(item)
        return True
    
    def ataque_especial(self):
        if self.mana < 25:
            return None
        dano_final = self.ataque * 1.5 + self.level * 5
        self.mana -= 25
        return dano_final
    
    def subir_nivel(self):
        self.level += 1
        self.xp -= self.xp_max
        self.xp_max = self.level * 30
        self.vida_max += 15
        self.vida = self.vida_max
        self.ataque += 5
        self.defesa += 3
        self.mana_max += 15
        self.mana = self.mana_max
    
    def receber_xp(self, xp):
        self.xp += xp
        if self.xp >= self.xp_max:
            self.subir_nivel()
            return True
        return False
    
    def vivo(self):
        return self.vida > 0


