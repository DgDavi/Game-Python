from view import (exibir_titulo, menu_login, apresentar_vilao, exibir_estado,
                  menu_acao, exibir_iventario, exibir_acao_vilao, exibir_acao,
                  exibir_level_up, exibir_vitoria, exibir_derrota, exibir_fuga,
                  exibir_item_usado, exibir_vitoria_final, exibir_loja)
from data import get_vilao
from battle import turno_jogador, turno_vilao
from personagem import Personagem
import os


def main():
    exibir_titulo()
    nome = menu_login()
    personagem = Personagem(nome)
    viloes = get_vilao()

    for fase, vilao in enumerate(viloes, 1):
        limpar_tela()
        apresentar_vilao(fase, vilao)
        desfecho = batalha(personagem, vilao)

        if desfecho == 'vitoria':
            subiu = personagem.receber_xp(vilao.xp_recompensa)
            personagem.gold += vilao.gold_recompensa
            personagem.vida = min(personagem.vida_max, personagem.vida + 30)
            exibir_vitoria(vilao, personagem)
            if subiu:
                exibir_level_up(personagem)
                input("\nPressione Enter para ir à loja...")
            if fase < len(viloes):
                input("\nPressione Enter para ir à loja...")
                limpar_tela()
                exibir_loja(personagem)

        elif desfecho == 'derrota':
            limpar_tela()
            exibir_derrota()
            return

        elif desfecho == 'fuga':
            limpar_tela()
            exibir_fuga()
            return

    exibir_vitoria_final(personagem)


def batalha(personagem, vilao):
    desfecho = 'derrota'

    while personagem.vivo() and vilao.vivo():
        limpar_tela()
        exibir_estado(personagem, vilao)
        acao = menu_acao(personagem)

        if acao == 'item':
            item = exibir_iventario(personagem)
            if item:
                personagem.usar_item(item)
                exibir_item_usado(item)
            continue

        resultado_jogador = turno_jogador(acao, personagem, vilao)
        if resultado_jogador:
            exibir_acao(resultado_jogador)

        if acao == 'fugir' and resultado_jogador['sucesso']:
            desfecho = 'fuga'
            break

        if not vilao.vivo():
            desfecho = 'vitoria'
            break

        resultado_vilao = turno_vilao(vilao, personagem)
        exibir_acao_vilao(vilao, resultado_vilao)

    return desfecho


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()
