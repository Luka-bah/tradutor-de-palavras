meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor", 
            "STALKEAR": "Investigar a vida de alguém online",
            "FLOPADO": "Algo que não viraliza",
            "VDD": "Abreviação de verdade",
            "FARMAR": "Obter recursos em algum tipo de jogo de maneira eficiente e rápida",
            }
palavra = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if palavra in meme_dict.keys():
    print(meme_dict[palavra])
else:
    print('infelizmente não temos essa palavra')
