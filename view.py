from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from rich.align import Align
import time

console = Console()


def exibir_titulo():
    console.print(Panel(
        Text("⚔️  RPG TERMINAL  ⚔️", justify="center", style="bold yellow"),
        subtitle="[dim]Pressione Enter para começar[/dim]",
        border_style="yellow",
        padding=(2, 10),
    ))
    input()


def menu_login():
    console.print(Panel("Como deseja ser chamado, aventureiro?", border_style="cyan"))
    nome = Prompt.ask("[cyan]Nome[/cyan]")
    return nome


def barra(atual, maximo, cor, label):
    largura = 20
    if maximo <= 0:
        preenchido = 0
    else:
        preenchido = int((atual / maximo) * largura)
        preenchido = max(0, min(largura, preenchido))
    vazio = largura - preenchido
    barra_visual = f"[{cor}]" + "█" * preenchido + "[/]"
    barra_vazia = "[dim]" + "░" * vazio + "[/]"
    return f"{label} {barra_visual}{barra_vazia} {atual}/{maximo}"


def exibir_estado(personagem, vilao):
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column(justify="left",  min_width=30)
    table.add_column(justify="right", min_width=30)

    table.add_row(
        f"[bold cyan]{personagem.nome}[/] (Nível {personagem.level})",
        f"[bold red]{vilao.nome}[/]",
    )
    table.add_row(
        barra(personagem.vida, personagem.vida_max, "green", "HP"),
        barra(vilao.vida,      vilao.vida_max,      "red",   "HP"),
    )
    table.add_row(
        barra(personagem.mana, personagem.mana_max, "blue", "MP"),
        "",
    )
    table.add_row(
        barra(personagem.xp, personagem.xp_max, "yellow", "XP"),
        "",
    )

    console.print(Panel(table, border_style="yellow"))


def menu_acao(personagem):
    table = Table(show_header=False, box=None, padding=(0, 2))

    table.add_row("[bold yellow]1[/]", "⚔️  Atacar")
    table.add_row("[bold yellow]2[/]", f"🔮  Ataque Especial  [dim](Mana: {personagem.mana}/{personagem.mana_max})[/]")
    table.add_row("[bold yellow]3[/]", f"🧪  Usar Item  [dim]({len(personagem.iventario)} itens)[/]")
    table.add_row("[bold yellow]4[/]", "🏃  Fugir")

    console.print(Panel(table, title="Sua vez", border_style="cyan"))

    escolha = Prompt.ask("Escolha", choices=["1", "2", "3", "4"])

    mapa = {"1": "atacar", "2": "especial", "3": "item", "4": "fugir"}
    return mapa[escolha]


def exibir_iventario(personagem):
    if not personagem.iventario:
        console.print("[red]Inventário vazio![/]")
        return None

    table = Table(show_header=False, box=None, padding=(0, 2))
    for i, item in enumerate(personagem.iventario, 1):
        table.add_row(f"[yellow]{i}[/]", item)

    console.print(Panel(table, title="🎒 Inventário", border_style="green"))

    choices = [str(i) for i in range(1, len(personagem.iventario) + 1)]
    escolha = Prompt.ask("Qual item?", choices=choices)
    return personagem.iventario[int(escolha) - 1]


def exibir_acao(resultado):
    if not resultado:
        return

    if resultado.get('acao') == 'atacar':
        console.print(f"[green]⚔️  Você atacou e causou {resultado.get('dano')} de dano![/]")

    elif resultado.get('acao') == 'especial':
        if resultado.get("sucesso"):
            console.print(f"[magenta]🔮 Ataque especial! {resultado.get('dano')} de dano![/]")
        else:
            console.print("[red]❌ Mana insuficiente![/]")

    elif resultado.get('acao') == 'item':
        console.print(f"[green]🧪 Você usou {resultado.get('item')}![/]")

    elif resultado.get("acao") == "fugir":
        if resultado.get("sucesso"):
            console.print("[yellow]🏃 Você fugiu da batalha![/]")
        else:
            console.print("[red]❌ Não conseguiu fugir![/]")


def exibir_item_usado(item):
    if item:
        item_normalizado = item.lower()
        if "mana" in item_normalizado:
            console.print(f"[blue]🧪 Você usou a {item} e recuperou mana![/]")
        elif "poção" in item_normalizado:
            console.print(f"[green]🧪 Você usou a {item} e recuperou vida![/]")
        else:
            console.print(f"[green]🧪 Você usou {item}![/]")


def exibir_resumo_turno(mensagens):
    for mensagem in mensagens:
        console.print(mensagem)


def exibir_acao_vilao(vilao, resultado):
    if resultado['acao'] == 'ataque':
        time.sleep(0.5)
        console.print(f"[red]👹 {vilao.nome} atacou e causou {resultado['dano']} de dano![/]")
        time.sleep(0.8)

    elif resultado['acao'] == 'especial':
        time.sleep(0.5)
        console.print(f"[bold red]💀 {vilao.nome} usou ataque especial! {resultado['dano']} de dano![/]")
        time.sleep(0.8)

    elif resultado['acao'] == 'cura':
        time.sleep(0.5)
        console.print(f"[yellow]✨ {vilao.nome} se curou em {resultado['valor']} pontos![/]")
        time.sleep(0.8)


def exibir_vitoria(vilao, personagem):
    console.print(Panel(
        Align.center(
            Text.assemble(
                (f"🏆 Você derrotou {vilao.nome}!\n\n", "bold green"),
                (f"+{vilao.xp_recompensa} XP   +{vilao.gold_recompensa} Gold", "bold yellow"),
            )
        ),
        border_style="green",
    ))


def exibir_derrota():
    console.print(Panel(
        Align.center(
            Text.assemble(
                ("💀 Você foi derrotado...\n\n", "bold red"),
                ("Game Over", "bold red"),
            )
        ),
        border_style="red",
    ))


def exibir_level_up(personagem):
    console.print(Panel(
        Align.center(
            Text.assemble(
                ("⬆️  LEVEL UP!\n\n", "bold yellow"),
                (f"Nível {personagem.level}!\n", "bold yellow"),
                ("+5 Ataque  +3 Defesa  +15 HP  +15 Mana", "bold yellow"),
            )
        ),
        border_style="yellow",
    ))


def apresentar_vilao(fase, vilao):
    console.print(
        Panel(
            Align.center(
                Text.assemble(
                    (f"\n{vilao.nome}\n\n", "bold red"),
                    (f'"{vilao.descricao}"\n\n', "italic dim"),
                    (f"HP: {vilao.vida_max}   ", "green"),
                    (f"Ataque: {vilao.ataque}   ", "red"),
                    (f"Defesa: {vilao.defesa}\n", "blue"),
                )
            ),
            title=f"[bold yellow]⚔️  FASE {fase}[/]",
            subtitle="[dim]Prepare-se...[/dim]",
            border_style="red",
            padding=(1, 4),
        )
    )
    input("\nPressione Enter para começar...")


def exibir_fuga():
    console.print(
        Panel(
            Align.center(
                Text.assemble(
                    ("🏃 VOCÊ FUGIU DA BATALHA...\n\n", "bold yellow"),
                    ("Às vezes recuar é a escolha mais sábia.\n", "dim"),
                    ("Mas sua jornada termina aqui.\n", "dim"),
                )
            ),
            title="[bold yellow]🏃 FUGA[/]",
            border_style="yellow",
            padding=(1, 4),
        )
    )


def exibir_vitoria_final(personagem):
    console.print(
        Panel(
            Align.center(
                Text.assemble(
                    ("🏆 PARABÉNS, VOCÊ VENCEU! 🏆\n\n", "bold yellow"),
                    (f"Herói: {personagem.nome}\n", "bold cyan"),
                    (f"Nível: {personagem.level}\n", "bold cyan"),
                    (f"Gold acumulado: {personagem.gold}\n\n", "bold yellow"),
                    ("Você derrotou todos os inimigos\n", "bold green"),
                    ("e salvou o reino!\n", "bold green"),
                )
            ),
            title="[bold yellow]✨ VITÓRIA FINAL ✨[/]",
            border_style="yellow",
            padding=(1, 4),
        )
    )


ITENS_LOJA = [
    {"nome": "Poção pequena",  "preco": 10, "descricao": "Cura 20 HP"},
    {"nome": "Poção grande",   "preco": 25, "descricao": "Cura 50 HP"},
    {"nome": "Poção de mana",  "preco": 20, "descricao": "Restaura 50 MP"},
    {"nome": "Elixir",         "preco": 40, "descricao": "Cura 80 HP e 40 MP"},
]

def exibir_loja(personagem):
    while True:
        # Monta a tabela da loja
        table = Table(show_header=True, border_style="yellow", padding=(0, 2))
        table.add_column("#",        style="bold yellow", justify="center")
        table.add_column("Item",     style="bold white")
        table.add_column("Efeito",   style="dim")
        table.add_column("Preço",    style="bold green", justify="right")

        for i, item in enumerate(ITENS_LOJA, 1):
            table.add_row(
                str(i),
                item["nome"],
                item["descricao"],
                f"{item['preco']} gold",
            )

        console.print(Panel(
            table,
            title="[bold yellow]🏪 LOJA[/]",
            subtitle=f"[cyan]Seu gold: {personagem.gold}[/]",
            border_style="yellow",
        ))

        choices = [str(i) for i in range(1, len(ITENS_LOJA) + 1)] + ["0"]
        escolha = Prompt.ask("Comprar (0 para sair)", choices=choices)

        if escolha == "0":
            break

        item = ITENS_LOJA[int(escolha) - 1]

        if personagem.gold < item["preco"]:
            console.print("[red]❌ Gold insuficiente![/]")
            time.sleep(0.8)
            continue

        personagem.gold -= item["preco"]

        if item["nome"] == "Elixir":
            personagem.vida = min(personagem.vida_max, personagem.vida + 80)
            personagem.mana = min(personagem.mana_max, personagem.mana + 40)
        else:
            personagem.iventario.append(item["nome"])

        console.print(f"[green]✅ {item['nome']} comprado![/]")
        time.sleep(0.8)