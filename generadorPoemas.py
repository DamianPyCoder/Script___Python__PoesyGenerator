import markovify

def generar_poema():
    # Lee un archivo con ejemplos de poemas que ya existen
    with open('poemas.txt', 'r', encoding='utf-8') as archivo:
        texto = archivo.read()

    # Genera el modelo de Markov 
    # La biblioteca "markovify" es una herramienta que nos ayuda a crear un tipo de modelo especial llamado "modelo de Markov" utilizando los poemas del archivo. 
    # Luego, utilizamos ese modelo para generar una oración aleatoria que tenga un estilo similar a los poemas que pusiste en el archivo.
    modelo = markovify.Text(texto)

    # Crea el poema y lo imprime
    poema = modelo.make_sentence()
    print(poema)


generar_poema()
