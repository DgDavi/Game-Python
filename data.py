from vilao import Vilao

def get_vilao():
    return [
        # Fase 1 — Fácil
        Vilao("Goblin Bêbado",       "Um goblin cambaleante que cheira a fermentado.",         40,  10,  2,  20,  15),
        Vilao("Rato Gigante",         "Um roedor monstruoso com presas enferrujadas.",           55,  12,  3,  25,  18),

        # Fase 3 — Médio
        Vilao("Lobo Sombrio",         "Um lobo de olhos vermelhos que uiva na escuridão.",       70,  15,  4,  35,  25),
        Vilao("Esqueleto Guerreiro",  "Um soldado morto-vivo que nunca descansou.",              85,  18,  6,  42,  30),

        # Fase 5 — Médio-difícil
        Vilao("Cavaleiro Corrompido", "Um antigo herói tomado pela escuridão.",                 120,  22,  8,  55,  40),
        Vilao("Ogro das Cavernas",    "Uma criatura brutal que esmaga tudo com os punhos.",     135,  25,  7,  60,  45),

        # Fase 7 — Difícil
        Vilao("Mago das Trevas",      "Um feiticeiro que manipula sombras e mentes.",           150,  30,  6,  80,  60),
        Vilao("Vampiro Nobre",        "Um conde imortal que drena a força dos aventureiros.",   165,  33, 10,  88,  70),

        # Fase 9 — Boss final
        Vilao("Dragão Ancião",        "Uma besta milenar cujo rugido abala montanhas.",         220,  40, 15, 120, 100),
        Vilao("Rei das Trevas",       "O senhor supremo da escuridão, fonte de todo o mal.",    280,  48, 18, 150, 130),
    ]