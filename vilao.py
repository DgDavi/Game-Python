class Vilao:
    def __init__(self, nome, descricao, vida, ataque, defesa, xp_recompensa, gold_recompensa):
        self.nome = nome
        self.descricao = descricao
        self.vida_max = vida
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.xp_recompensa = xp_recompensa
        self.gold_recompensa = gold_recompensa
        self.ja_curou = False

    def receber_dano(self, dano):
        dano_final = max(1, dano - self.defesa)
        self.vida = max(0, self.vida - dano_final)
        return dano_final

    def vivo(self):
        return self.vida > 0

    def porcentagem_vida(self):
        return self.vida / self.vida_max