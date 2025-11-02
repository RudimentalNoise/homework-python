
'''
Othello, o Reversi (https://en.wikipedia.org/wiki/Reversi), è un gioco da tavolo
giocato da due giocatori su una scacchiera 8x8. Pur avendo regole
relativamente semplici, Othello è un gioco di notevole profondità strategica.
In questo esercizio bisognerà simulare una versione semplificata di othello,
chiamata Dumbothello, in cui un giocatore cattura le pedine dell'avversario in
prossimità della propria pedina appena giocata.
Ecco le regole di Dumbothello:
- ogni giocatore ha un colore associato: bianco, nero;
- il giocatore con il nero è sempre il primo a giocare;
- a turno, ogni giocatore deve mettere una pedina del suo colore in modo tale
  da catturare una o più pedine avversarie;
- catturare una o più pedine avversarie vuol dire che la pedina giocata dal
  giocatore trasforma nel colore del giocatore tutte le pedine avversarie
  direttamente adiacenti, in una qualunque direzione orizzontale, verticale o diagonale;
- dopo aver giocato la propria pedina, le pedine avversarie catturate cambiano
  tutte colore e diventano dello stesso colore del giocatore che ha appena giocato;
- quando il giocatore di turno non può aggiungere ulteriori pedine in gioco,
  la partita termina. Vince il giocatore che ha più pedine sulla scacchiera
  oppure avviene un pareggio se il numero di pedine dei due giocatori è uguale;
- il giocatore di turno non può aggiungere ulteriori pedine se non ha modo di
  catturare nessuna pedina avversaria con nessuna mossa, oppure non ci sono
  più caselle libere sulla scacchiera.

Si deve scrivere una funzione dumbothello(filename) che legga da un file di testo
indicato dalla stringa filename una configurazione della scacchiera e,
seguendo le regole di Dumbothello, generi ricorsivamente l'albero di gioco completo
delle possibili evoluzioni della partita, in modo tale che ogni foglia dell'albero
sia una configurazione da cui non sia più possibile effettuare alcuna mossa.

La configurazione inziale della scacchiera nel file è rappresentata riga per
riga nel file. Una lettera "B" identifica una pedina del nero, una "W" una
pedina del bianco e il carattere "." una casella vuota. Le lettere sono
separate da uno o più caratteri di spaziatura.

In particolare, la funzione dumbothello restituirà una tripla (a, b, c), in cui:
- a è il numero totale di evoluzioni che terminano con una vittoria del nero;
- b è il numero totale di evoluzioni che terminano con una vittoria del bianco;
- c è il numero totale di evoluzioni che terminano con un pari.

Ad esempio, dato in input un file di testo contenente la scacchiera:
. . W W
. . B B
W W W B
W B B W

La funzione ritornerà la tripla:
(2, 16, 0)

ATTENZIONE: la funzione dumbothello o qualche altra 
funzione usata per la soluzione deve essere ricorsiva.

'''




def is_inside_image(x, y, width, height):
    """ Controlla se le coordinate (x, y) sono all'interno dei limiti dell'immagine """
    return 0 <= x < width and 0 <= y < height

def bfs(x, y, image, visited):
    """ Ricerca in ampiezza per visitare tutti i pixel dello sfondo adiacenti """
    queue = [(x, y)]
    visited[y][x] = True

    while queue:
        x, y = queue.pop(0)
        # Coordinate adiacenti
        adjacent_coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for adj_x, adj_y in adjacent_coords:
            if is_inside_image(adj_x, adj_y, len(image[0]), len(image)) and not visited[adj_y][adj_x] and image[adj_y][adj_x] == image[y][x]:
                queue.append((adj_x, adj_y))
                visited[adj_y][adj_x] = True

def count_background_regions(image):
    """ Conta il numero di regioni delimitate da quattro lati che contengono solo pixel dello sfondo """
    width = len(image[0])
    height = len(image)
    visited = [[False for _ in range(width)] for _ in range(height)]
    count = 0

    for y in range(height):
        for x in range(width):
            if not visited[y][x]:  # Trovato un nuovo punto di partenza per la ricerca
                pixel_color = image[y][x]
                if pixel_color == image[0][0]:  # Controllo se è un pixel di sfondo
                    count += 1
                    bfs(x, y, image, visited)

    return count

# Utilizzo della funzione
filename = 'prova_seria.png'
image = images.load(filename)
background_regions_count = count_background_regions(image)
print("Numero di regioni delimitate da quattro lati contenenti solo pixel dello sfondo:", background_regions_count)


##### DFS


def is_inside_image(x, y, width, height):
    """ Controlla se le coordinate (x, y) sono all'interno dei limiti dell'immagine """
    return 0 <= x < width and 0 <= y < height

def dfs(x, y, image, visited):
    """ Ricerca in profondità per visitare tutti i pixel dello sfondo adiacenti """
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        if is_inside_image(x, y, len(image[0]), len(image)) and not visited[y][x] and image[y][x] == image[0][0]:
            visited[y][x] = True

            # Coordinate adiacenti
            adjacent_coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for adj_x, adj_y in adjacent_coords:
                if is_inside_image(adj_x, adj_y, len(image[0]), len(image)) and not visited[adj_y][adj_x] and image[adj_y][adj_x] == image[y][x]:
                    stack.append((adj_x, adj_y))

def count_background_regions(image):
    """ Conta il numero di regioni delimitate da quattro lati che contengono solo pixel dello sfondo """
    width = len(image[0])
    height = len(image)
    visited = [[False for _ in range(width)] for _ in range(height)]
    count = 0

    for y in range(height):
        for x in range(width):
            if not visited[y][x]:  # Trovato un nuovo punto di partenza per la ricerca
                pixel_color = image[y][x]
                if pixel_color == image[0][0]:  # Controllo se è un pixel di sfondo
                    count += 1
                    dfs(x, y, image, visited)

    return count

# Utilizzo della funzione
filename = 'prova_seria.png'
image = images.load(filename)
background_regions_count = count_background_regions(image)
print("Numero di regioni delimitate da quattro lati contenenti solo pixel dello sfondo:", background_regions_count)




#### DFS ricorsiva


def is_inside_image(x, y, width, height):
    """ Controlla se le coordinate (x, y) sono all'interno dei limiti dell'immagine """
    return 0 <= x < width and 0 <= y < height

def dfs(x, y, image, visited):
    """ Ricerca in profondità per visitare tutti i pixel dello sfondo adiacenti (ricorsione di coda) """
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        if is_inside_image(x, y, len(image[0]), len(image)) and not visited[y][x] and image[y][x] == image[0][0]:
            visited[y][x] = True

            # Coordinate adiacenti
            adjacent_coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for adj_x, adj_y in adjacent_coords:
                if is_inside_image(adj_x, adj_y, len(image[0]), len(image)) and not visited[adj_y][adj_x] and image[adj_y][adj_x] == image[y][x]:
                    stack.append((adj_x, adj_y))

def count_background_regions(image):
    """ Conta il numero di regioni delimitate da quattro lati che contengono solo pixel dello sfondo """
    width = len(image[0])
    height = len(image)
    visited = [[False for _ in range(width)] for _ in range(height)]
    count = 0

    for y in range(height):
        for x in range(width):
            if not visited[y][x]:  # Trovato un nuovo punto di partenza per la ricerca
                pixel_color = image[y][x]
                if pixel_color == image[0][0]:  # Controllo se è un pixel di sfondo
                    count += 1
                    dfs(x, y, image, visited)

    return count

# Utilizzo della funzione
filename = 'prova_seria.png'
image = images.load(filename)
background_regions_count = count_background_regions(image)
print("Numero di regioni delimitate da quattro lati contenenti solo pixel dello sfondo:", background_regions_count)






Ora il programma deve costruire un' immagine di output di più pixel posti tutti su una stessa riga da sinistra a destra in orizzontale. 
in questa immagine il primo pixel partendo da sinistra deve avere lo stesso colore del sfondo dell'immagine di input che lo si prende dallo spigolo 
in alto a sinistra. Poi i pixel successivi dovranno corrispondere ai colori(diversi da quello dello sfondo) delle linee colorate che formano uno 
spigolo cioè quando si trovano 5 pixel dello stesso colore tutti attaccati tra di loro nell'immagine di input che si incontrano nella visita 
in profondità usata per calcolare il numero di regioni all'interno dell'immagine di input prima partendo 
dallo spigolo in alto a sx, poi in alto a dx, poi in basso a sx, e infine in basso a dx. I colori devono essere salvati in ordine inverso 
rispetto a come si trovano usando la visita.


def is_inside_region(x, y, region_x, region_y, region_width, region_height):
    """ Controlla se le coordinate (x, y) sono all'interno dei limiti della regione """
    return region_x <= x < region_x + region_width and region_y <= y < region_y + region_height

def dfs(x, y, image, visited):
    """ Ricerca in profondità per visitare tutti i pixel dello sfondo adiacenti """
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        if is_inside_image(x, y, len(image[0]), len(image)) and not visited[y][x] and image[y][x] == image[0][0]:
            visited[y][x] = True

            # Coordinate adiacenti
            adjacent_coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for adj_x, adj_y in adjacent_coords:
                if is_inside_image(adj_x, adj_y, len(image[0]), len(image)) and not visited[adj_y][adj_x] and image[adj_y][adj_x] == image[y][x]:
                    stack.append((adj_x, adj_y))
                    
def dfs_colored(x, y, image, visited, target_color):
    """ Ricerca in profondità per visitare pixel colorati adiacenti """
    stack = [(x, y)]
    colored_pixels = set()

    while stack:
        x, y = stack.pop()
        if is_inside_image(x, y, len(image[0]), len(image)) and not visited[y][x] and image[y][x] == target_color:
            visited[y][x] = True
            colored_pixels.add(image[y][x])

            # Coordinate adiacenti
            adjacent_coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for adj_x, adj_y in adjacent_coords:
                if is_inside_image(adj_x, adj_y, len(image[0]), len(image)) and not visited[adj_y][adj_x] and image[adj_y][adj_x] == target_color:
                    stack.append((adj_x, adj_y))

    return colored_pixels

def count_background_regions(image):
    """ Conta il numero di regioni delimitate da quattro lati che contengono solo pixel dello sfondo """
    width = len(image[0])
    height = len(image)
    visited = [[False for _ in range(width)] for _ in range(height)]
    count = 0

    for y in range(height):
        for x in range(width):
            if not visited[y][x]:  # Trovato un nuovo punto di partenza per la ricerca
                pixel_color = image[y][x]
                if pixel_color == image[0][0]:  # Controllo se è un pixel di sfondo
                    count += 1
                    dfs(x, y, image, visited)

    return count, generate_output_image(image)
    
def generate_output_image(image):
    """ Genera l'immagine di output seguendo le specifiche fornite """
    width = len(image[0])
    height = len(image)
    visited = [[False for _ in range(width)] for _ in range(height)]
    output_image = [[image[0][0]]]

    for y in range(height):
        for x in range(width):
            if not visited[y][x] and image[y][x] != image[0][0]:
                colored_pixels = dfs_colored(x, y, image, visited, image[y][x])
                colored_pixels = sorted(colored_pixels, reverse=True)

                for color in colored_pixels:
                    output_image[0].append(color)

    return output_image

# Utilizzo della funzione
filename = 'small01.in.png'
image = images.load(filename)
background_regions_count = count_background_regions(image)
output_image = generate_output_image(image)

print("Numero di regioni delimitate da quattro lati contenenti solo pixel dello sfondo:", background_regions_count)
print("Immagine di output generata:")
print(output_image)

# Salva l'immagine di output
output_filename = 'output.png'
images.save(output_image, output_filename)


import images
def ex1(input_file,output_file):
    im = images.load(input_file)
    bg = im[0][0]
    listacol= [bg]
    num_rect = appezzamento(im, listacol, bg)
    images.save([listacol], output_file)
    return num_rect
    
def ap(im,listacol, bg):
    H = len(im)
    W = len(im[0])
    for i in range(H):
        row = im[i]
        if row[0] != bg:
            colore_row = row[0]
            dividi_rect = True
            for y in range(len(row)):
                if row[y] != colore_row:
                    dividi_rect = False
            if dividi_rect:
                first_row = im[0]
                for j in range(len(first_row)):
                    if im[0][j] == colore_row:
                        start_j = j
                    start_i = i
                    sub_rect1 = [ im[i][:start_j] for i in range(start_i) ]
                    sub_rect2 = [ im[i][start_j+1:W] for i in range(start_i) ]
                    sub_rect3 = [ im[i][:start_j] for i in range(start_i+1, H) ]
                    sub_rect4 = [ im[i][start_j+1:W] for i in range(start_i+1, H) ]
                    listacol.append(colore_row)
                    return ap(sub_rect4,listacol, bg) + ap(sub_rect3, listacol, bg) + ap(sub_rect2, listacol, bg) + ap(sub_rect1, listacol, bg)
    return 1