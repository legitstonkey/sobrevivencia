print("Instalação abandonada")
print("você acorda em uma sala escura, a unica luz disponível é a de um monitor piscando")
print("á sua frente, há uma porta de ferro entreaberta e, ao lado, um alçapão no chão.")
a1 = input("Você decide (A) passar pela porta ou (B) abrir o alçapão?")
if a1 == ("A"):
    print("\n-Caminho da porta- Você passa pela porta de ferro silenciosamente")
    print("O corredor está cheio de névoa e você ouve passos pesados vindo em sua direção")
    escolha_porta = input("Você decide (A) correr de volta ou (B) se esconder atrás das caixas? ")

    if escolha_porta == "A":
        print("\nVocê correu em pânico, tropecou na névoa e foi pego!")
    elif escolha_porta == "B":
        print("\nVocê se escondeu atrás das caixas e a criatura passou direto. seguro!")
    else:
        print("O medo te paralisou no corredor e você foi pego!")

elif a1 == ("B"):
    print("\n-Caminho do alçapão- você abre o alçapão e desce por uma escada velha")
    print("Lá embaixo, você encontra um porão inundado com água até os tornozelos")
    escolha_alcapao = input("Você escolhe (A) chapinhar na água ou (B) ficar parado ouvindo? ")
    if escolha_alcapao == "A":
        print("\nmorreu. o barulho na água atraiu a criatura, você foi pego!")
    elif escolha_alcapao == "B":
        print("\nviveu. você ouviu o monstro, voltou e nao foi pego!")
    else:
        print("Você hesitou demais, a escada quebrou e você foi pego!")



