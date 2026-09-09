import random

def calcular_dano(ataque: int, forca: int, chance_critico: float = 0.2) -> dict:
    """
    Calcula o dano fictício de um personagem baseado em atributos.
    
    :param ataque: Valor de ataque base do personagem.
    :param forca: Valor de força que multiplica o dano.
    :param chance_critico: Chance (de 0 a 1) de o golpe causar dano dobrado.
    :return: Um dicionário com o valor do dano e se foi crítico ou não.
    """
    # Adiciona uma variação aleatória de 85% a 110% para o dano não ser sempre igual
    variacao = random.uniform(0.85, 1.10)
    
    # Fórmula base: (Ataque + Força acumulada) multiplicada pela variação
    dano_base = int((ataque + (forca * 1.5)) * variacao)
    
    # Determina se o golpe foi crítico
    foi_critico = random.random() < chance_critico
    
    if foi_critico:
        dano_final = dano_base * 2
    else:
        dano_final = dano_base
        
    return {
        "dano": dano_final,
        "critico": foi_critico
    }

# Exemplo de teste para rodar o script diretamente
if __name__ == "__main__":
    print("⚔️ --- Simulador de Combate --- ⚔️")
    
    # Atributos de um Guerreiro fictício
    atq_guerreiro = 50
    forc_guerreiro = 30
    
    resultado = calcular_dano(ataque=atq_guerreiro, forca=forc_guerreiro)
    
    if resultado["critico"]:
        print(f"💥 ¡ATAQUE CRÍTICO! Você causou {resultado['dano']} de dano devastador!")
    else:
        print(f"🗡️ Você atacou o inimigo e causou {resultado['dano']} de dano.")
