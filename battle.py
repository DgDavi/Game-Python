from random import randint

def turno_vilao(vilao, personagem):
    chance_acao = randint(1, 100)
    hp_porcentagem = vilao.porcentagem_vida()
    pode_curar = vilao.vida < vilao.vida_max and not vilao.ja_curou

    if hp_porcentagem > 0.5:
        if chance_acao < 60:
            acao = 'ataque'
        else:
            if pode_curar:
                acao = 'cura'
            else:
                acao = 'especial'
    else:
        if chance_acao < 40:
            acao = 'ataque'
        elif chance_acao < 90:
            acao = 'especial'
        else:
            if pode_curar:
                acao = 'cura'
            else:
                acao = 'ataque'

    if acao == 'ataque':
        dano_bruto = vilao.ataque + randint(-4, 4)
        dano_final = personagem.receber_dano(dano_bruto)
        return {'acao': 'ataque', 'dano': dano_final}

    elif acao == 'especial':
        dano_bruto = int(vilao.ataque * 1.6) + randint(-5, 5)
        dano_final = personagem.receber_dano(dano_bruto)
        return {'acao': 'especial', 'dano': dano_final}

    elif acao == 'cura':
        cura = int(vilao.vida_max * 0.35)
        vilao.vida = min(vilao.vida_max, vilao.vida + cura)
        vilao.ja_curou = True
        return {'acao': 'cura', 'valor': cura}


def turno_jogador(acao, personagem, vilao):
    if acao == 'atacar':
        dano_bruto = personagem.ataque + randint(-3, 3)
        dano_final = vilao.receber_dano(dano_bruto)
        return {'acao': 'atacar', 'dano': dano_final}

    elif acao == 'especial':
        dano_bruto = personagem.ataque_especial()
        if dano_bruto is None:
            return {'acao': 'especial', 'sucesso': False}
        dano_final = vilao.receber_dano(int(dano_bruto))
        return {'acao': 'especial', 'sucesso': True, 'dano': dano_final}

    elif acao == 'item':
        return {'acao': 'item'}

    elif acao == 'fugir':
        sucesso = randint(1, 100) <= 40
        return {'acao': 'fugir', 'sucesso': sucesso}

    return None