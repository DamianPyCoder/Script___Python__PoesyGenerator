import markovify

def generar_poema():
    # Lee un archivo con ejemplos de poemas que ya existen
    with open('poemas.txt', 'r', encoding='utf-8') as archivo:
        texto = archivo.read()

    # Genera el modelo de Markov 
    modelo = markovify.Text(texto)

    # Crea el poema y lo imprime
    poema = modelo.make_sentence()
    print(poema)


generar_poema()
