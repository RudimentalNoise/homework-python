
'''
Siete stati appena ingaggiati in una software house di videogiochi e
dovete renderizzare su immagine il giochino dello snake salvando
l'immagine finale del percorso dello snake e restituendo la lunghezza
dello snake.
Si implementi la funzione generate_snake che prende in ingresso un
percorso di un file immagine, che e' l'immagine di partenza
"start_img" che puo' contenere pixel di background neri, pixel di
ostacolo per lo snake di colore rosso e infine del cibo di colore
arancione. Lo snake deve essere disegnato di verde. Inoltre bisogna
disegnare in grigio la scia che lo snake lascia sul proprio
cammino. La funzione inoltre prende in ingresso una posizione iniziale
dello snake, "position" come una lista di due interi X e Y. I comandi
del giocatore su come muovere lo snake nel videogioco sono disponibili
in una stringa "commands".  La funzione deve salvare l'immagine finale
del cammino dello snake al percorso "out_img", che e' passato come
ultimo argomento di ingresso alla funzione. Inoltre la funzione deve
restituire la lunghezza dello snake al termine del gioco.

Ciascun comando in "commands" corrisponde ad un segno cardinale ed e
seguito da uno spazio. I segni cardinali possibli sono:

| NW | N | NE |
| W  |   | E  |
| SW | S | SE |

che corrispondono a movimenti dello snake di un pixel come:

| alto-sinistra  | alto  | alto-destra  |
| sinistra       |       | destra       |
| basso-sinistra | basso | basso-destra |

Lo snake si muove in base ai comandi passati e nel caso in cui
mangia del cibo si allunga di un pixel.

Lo snake puo' passare da parte a parte dell'immagine sia in
orizzontale che in verticale. Il gioco termina quando sono finiti i
comandi oppure lo snake muore. Lo snake muore quando:
- colpisce un ostacolo
- colpisce se stesso quindi non puo' passare sopra se stesso
- si incrocia in diagonale in qualsiasi modo. Ad esempio, un percorso
  1->2->3-4 come quello sotto a sinistra non e' lecito mentre quello a
  destra sotto va bene.

  NOT OK - diagonal cross        OK - not a diagonal cross
       | 4 | 2 |                    | 1 | 2 |
       | 1 | 3 |                    | 4 | 3 |

Ad esempio considerando il caso di test data/input_00.json
lo snake parte da "position": [12, 13] e riceve i comandi
 "commands": "S W S W W W S W W N N W N N N N N W N" 
genera l'immagine in visibile in data/expected_end_00.png
e restituisce 5 in quanto lo snake e' lungo 5 pixels alla
fine del gioco.

NOTA: analizzate le immagini per avere i valori esatti dei colore da usare.

NOTA: non importate o usate altre librerie
'''


HOMEWORK 6
generate_snake('input_00.png', [12,13], "S W S W W W S W W N N W N N N N N W N", 'out_img')
2 righe, 3 colonne
lista = [[(0,0,0),(0,0,0),(0,0,0))],[(0, 0, 0), (0, 0, 0),(0, 0, 0)]]

def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
    # Scrivi qui il tuo codice
    snake_head = [position[::-1]]
    head = position[::-1]                                                       #contiene le coordinate della testa
    tail = position[::-1]
    counter = 1
    img = start(start_img, position)                                                #matrice
    cibo = (255,128,0)
    ostacolo = (255,0,0)
    corpo = (0,255,0)
    scia = (128,128,128)
    lista = commands.split()
    for com in lista:
        if com == 'N': 
            if counter == 1:                                               #controllo se è più lungo di 1 lo snake, perchè se lo è va colorata di nero la coda ad ogni spostamento
                if head[0]-1 < 0:                                          #se coordinata x < 0 
                    tail = snake_head[0]
                    head = [len(img)-1,head[1]]
                    if img[head[0]][head[1]] == cibo:                     #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:               #or next == corpo:
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                     #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                      #vecchia posizione di head

                else:
                    tail = snake_head[0]
                    head = [head[0]-1,head[1]]        
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:               #ostacolo
                        images.save(img, out_img)
                        return counter
                    else:
                        img[head[0]][head[1]] = corpo 
                        snake_head.append(head) 
                        del snake_head[0]                      #strada libera
                        img[tail[0]][tail[1]] = scia                      #aggiorno la coda

            elif counter > 1:  
                if snake_head[-1][0]-1 < 0:
                    tail = snake_head[0]                                  #ultima head della lista
                    head = [len(img)-1,snake_head[-1][1]]                    #ultima riga stessa colonna nuova posizione della head
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                else:
                    tail = snake_head[0]
                    head = [snake_head[-1][0]-1, snake_head[-1][1]]       #nuove coordinate della testa    
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #x e y della tail


        elif com == 'S':
            #current_pos[x+1][y]
            if counter == 1:                                             #controllo se è più lungo di 1 lo snake, perchè se lo è va colorata di nero la coda ad ogni spostamento
                if head[0]+1 >= len(img):                                  #se coordinata x < 0 
                    tail = snake_head[0]
                    head = [0,head[1]] 
                    if img[head[0]][head[1]] == cibo:                   #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:             #or next == corpo:
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                   #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                    #vecchia posizione di head

                else:
                    tail = snake_head[0]
                    head = [head[0]+1,head[1]]        
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:             #or img[head[0]-1][head[1]] == corpo:     #ostacolo
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #aggiorno la coda

            elif counter > 1:  
                if snake_head[-1][0]+1 >= len(img):
                    tail = snake_head[0]                                  #ultima head della lista
                    head = [0,snake_head[-1][1]]                          #ultima riga stessa colonna nuova posizione della head
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                else:
                        tail = snake_head[0]
                        head = [snake_head[-1][0]+1, snake_head[-1][1]]       #nuove coordinate della testa   
                        if img[head[0]][head[1]] == cibo:
                            img[head[0]][head[1]] = corpo
                            counter += 1
                            snake_head.append(head)
                        elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                            images.save(img, out_img)
                            return counter
                        else: 
                            img[head[0]][head[1]] = corpo
                            snake_head.append(head)
                            del snake_head[0]
                            img[tail[0]][tail[1]] = scia                     #x e y della tail

        elif com == 'E':
            #current_pos[x][y+1]
            if counter == 1:                                              #controllo se è più lungo di 1 lo snake, perchè se lo è va colorata di nero la coda ad ogni spostamento
                if head[1]+1 >= len(img[0]):                                #se coordinata x < 0      QUI
                    tail = snake_head[0]
                    head = [head[0],0]                                           #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:              #or next == corpo:
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                else:
                    tail = snake_head[0]
                    head = [head[0],head[1]+1]                                   #QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:              #ostacolo
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #aggiorno la coda

            elif counter > 1:  
                if snake_head[-1][1]+1 >= len(img[0]):                      #QUI
                    tail = snake_head[0]                                  #ultima head della lista
                    head = [snake_head[-1][0],0]                          #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                else:
                    tail = snake_head[0]
                    head = [snake_head[-1][0], snake_head[-1][1]+1]       #nuove coordinate della testa  QUI   
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #x e y della tail

        elif com == 'W':
            #current_pos[x][y-1]
            if counter == 1:                                              #controllo se è più lungo di 1 lo snake, perchè se lo è va colorata di nero la coda ad ogni spostamento
                if head[1]-1 < 0:                                         #se coordinata x < 0      QUI
                    tail = snake_head[0]
                    head = [head[0],len(img[0])-1]                                 #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo: 
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                else:
                    tail = snake_head[0]
                    head = [head[0],head[1]-1]                                   #QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:              #ostacolo
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #aggiorno la coda

            elif counter > 1:  
                if snake_head[-1][1]-1 < 0:                               #QUI
                    tail = snake_head[0]                                  #ultima head della lista
                    head = [snake_head[-1][0],len(img[0])-1]                 #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                else:
                    tail = snake_head[0]
                    head = [snake_head[-1][0], snake_head[-1][1]-1]       #nuove coordinate della testa  QUI   
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #x e y della tail


        elif com == 'NE':
            #current_pos[x-1][y+1]   sbordamento alto, sbordamento destro
            if counter == 1:                                              #controllo se è più lungo di 1 lo snake, perchè se lo è va colorata di nero la coda ad ogni spostamento
                if head[0]-1 < 0 and head[1]+1 >= len(img[0]):              # controllo angolo      QUI
                    tail = snake_head[0]
                    head = [len(img)-1, 0]                                            #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo: 
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                elif head[0]-1 < 0:                                       #controllo sbordamento      QUI
                    tail = snake_head[0]
                    head = [len(img)-1, head[1]+1]                                         #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo: 
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                elif head[1]+1 >= len(img[0]):                              #controllo sbordamento      QUI
                    tail = snake_head[0]
                    head = [head[0]-1, 0]                                           #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo: 
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                else:
                    tail = snake_head[0]
                    head = [head[0]-1,head[1]+1]                                          #QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:              #ostacolo
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #aggiorno la coda

            elif counter > 1:  
                if snake_head[-1][0]-1 < 0 and snake_head[-1][1]+1 >= len(img[0]) :        #controllo angolo          QUI
                    tail = snake_head[0]                                                 #ultima head della lista
                    head = [len(img)-1,0]                                                   #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                elif snake_head[-1][0]-1 < 0:                               #controllo sbordamento          QUI
                    tail = snake_head[0]                                  #ultima head della lista
                    head = [len(img)-1, snake_head[-1][1]+1]                 #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                elif snake_head[-1][1]+1 >= len(img[0]):                      #controllo sbordamento          QUI
                    tail = snake_head[0]                                  #ultima head della lista
                    head = [snake_head[-1][0]-1, 0]                       #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                else:
                    tail = snake_head[0]
                    head = [snake_head[-1][0]-1, snake_head[-1][1]+1]     #nuove coordinate della testa  QUI
                    if img[head[0]][head[1]-1] == corpo and img[head[0]+1][head[1]] == corpo:             #aggiunta per controllo cross-diagonale, guardo l'ultima posizione della testa e controllo intorno
                        images.save(img, out_img)
                        return counter   
                    elif img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #x e y della tail


        elif com == 'NW':                                                 #sbordamento alto e sinistro
            #current_pos[x-1][y-1]
            if counter == 1:                                              #controllo se è più lungo di 1 lo snake, perchè se lo è va colorata di nero la coda ad ogni spostamento
                if head[0]-1 < 0 and head[1]-1 < 0:                       #controllo angolo      QUI
                    tail = snake_head[0]
                    head = [len(img)-1, len(img[0])-1]                                  #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:     
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                elif head[0]-1 < 0:                                       #controllo sbordamento      QUI
                    tail = snake_head[0]
                    head = [len(img)-1, head[1]-1]                                          #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo: 
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                elif head[1]-1 < 0:                                       #controllo sbordamento      QUI
                    tail = snake_head[0]
                    head = [head[0]-1, len(img[0])-1]                                  #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo: 
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                else:
                    tail = snake_head[0]
                    head = [head[0]-1, head[1]-1]                                         #QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:              #ostacolo
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #aggiorno la coda

            elif counter > 1:  
                if snake_head[-1][0]-1 < 0 and snake_head[-1][1]-1 < 0:        #controllo angolo          QUI
                    tail = snake_head[0]                                       #ultima head della lista
                    head = [len(img)-1,len(img[0])-1]                                #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                elif snake_head[-1][0]-1 < 0:                               #controllo sbordamento          QUI
                    tail = snake_head[0]                                  #ultima head della lista
                    head = [len(img)-1, snake_head[-1][1]-1]                 #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                elif snake_head[-1][1]-1 < 0:                               #controllo sbordamento          QUI
                    tail = snake_head[0]                                  #ultima head della lista
                    head = [snake_head[-1][0]-1, len(img[0])-1]              #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                else:
                    tail = snake_head[0]
                    head = [snake_head[-1][0]-1, snake_head[-1][1]-1]     #nuove coordinate della testa  QUI   
                    if img[head[0]+1][head[1]] == corpo and img[head[0]][head[1]+1] == corpo:             #aggiunta per controllo cross-diagonale, guardo l'ultima posizione della testa e controllo intorno
                        images.save(img, out_img)
                        return counter  
                    elif img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #x e y della tail

        elif com == 'SE':                                                 #sbordamento basso e destro
            #current_pos[x+1][y+1]
            if counter == 1:                                              #controllo se è più lungo di 1 lo snake, perchè se lo è va colorata di nero la coda ad ogni spostamento
                if head[0] >= len(img)-1 and head[1] >= len(img[0])-1:        # controllo angolo      QUI
                    tail = snake_head[0]
                    head = [0,0]                                         #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:         
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                elif head[0]+1 >= len(img):                                 #controllo sbordamento      QUI
                    tail = snake_head[0]
                    head = [0, head[1]+1]                                          #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:        
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                elif head[1]+1 >= len(img[0]):                              #controllo sbordamento      QUI
                    tail = snake_head[0]
                    head = [head[0]+1, 0]                                          #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:              #or next == corpo:
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                else:
                    tail = snake_head[0]
                    head = [head[0]+1, head[1]+1]                                          #QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:              #ostacolo
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #aggiorno la coda

            elif counter > 1:  
                if snake_head[-1][0] >= len(img)-1 and snake_head[-1][1] >= len(img[0])-1:        #controllo angolo          QUI
                    tail = snake_head[0]                                                      #ultima head della lista
                    head = [0,0]                                                              #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                                               #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                elif snake_head[-1][0]+1 >= len(img):                         #controllo sbordamento          QUI
                    tail = snake_head[0]                                  #ultima head della lista
                    head = [0, snake_head[-1][1]+1]                       #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                elif snake_head[-1][1]+1 >= len(img[0]):                      #controllo sbordamento          QUI
                    tail = snake_head[0]                                  #ultima head della lista
                    head = [snake_head[-1][0]+1, 0]                       #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                else:
                    tail = snake_head[0]
                    head = [snake_head[-1][0]+1, snake_head[-1][1]+1]     #nuove coordinate della testa  QUI   
                    if img[head[0]][head[1]] == corpo and img[head[0]][head[1]] == corpo:             #aggiunta per controllo cross-diagonale, guardo l'ultima posizione della testa e controllo intorno
                        images.save(img, out_img)
                        return counter 
                    elif img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #x e y della tail

        elif com == 'SW':                                                 #sbordamento basso e sinistro
            #current_pos[x+1][y-1] 
            if counter == 1:                                              #controllo se è più lungo di 1 lo snake, perchè se lo è va colorata di nero la coda ad ogni spostamento
                if head[0]+1 >= len(img) and head[1]-1 < 0:                 #controllo angolo      QUI
                    tail = snake_head[0]
                    head = [0, len(img[0])-1]                                 #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:        
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                elif head[0]+1 >= len(img):                                 #controllo sbordamento      QUI
                    tail = snake_head[0]
                    head = [0,head[1]-1]                                         #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo: 
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                elif head[1]-1 < 0:                                       #controllo sbordamento      QUI
                    tail = snake_head[0]
                    head = [head[0]+1, len(img[0])-1]                                  #QUI
                    if img[head[0]][head[1]] == cibo:                    #c'è del cibo
                        img[head[0]][head[1]] = corpo
                        counter += 1   
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo: 
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #vecchia posizione di head

                else:
                    tail = snake_head[0]
                    head = [head[0]+1, head[1]-1]                                          #QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)
                    elif img[head[0]][head[1]] == ostacolo:              #ostacolo
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo                    #strada libera
                        snake_head.append(head) 
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #aggiorno la coda

            elif counter > 1:  
                if snake_head[-1][0]+1 >= len(img) and snake_head[-1][1]-1 < 0:            #controllo angolo          QUI
                    tail = snake_head[0]                                                 #ultima head della lista
                    head = [0,len(img[0])-1]                                               #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                                          #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                elif snake_head[-1][0]+1 >= len(img):                         #controllo sbordamento          QUI
                    tail = snake_head[0]                                  #ultima head della lista
                    head = [0, snake_head[-1][1]-1]                      #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                elif snake_head[-1][1]-1 < 0:                               #controllo sbordamento          QUI
                    tail = snake_head[0]                                  #ultima head della lista
                    head = [snake_head[-1][0]+1, len(img[0])-1]              #ultima riga stessa colonna nuova posizione della head       QUI
                    if img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)                           #la head si trova a [-1]  
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else:  
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]  
                        img[tail[0]][tail[1]] = scia

                else:
                    tail = snake_head[0]
                    head = [snake_head[-1][0]+1, snake_head[-1][1]-1]     #nuove coordinate della testa  QUI
                    if img[head[0]][head[1]+1] == corpo and img[head[0]-1][head[1]] == corpo:             #aggiunta per controllo cross-diagonale, guardo l'ultima posizione della testa e controllo intorno
                        images.save(img, out_img)
                        return counter    
                    elif img[head[0]][head[1]] == cibo:
                        img[head[0]][head[1]] = corpo
                        counter += 1
                        snake_head.append(head)  
                    elif img[head[0]][head[1]] == ostacolo or img[head[0]][head[1]] == corpo:
                        images.save(img, out_img)
                        return counter
                    else: 
                        img[head[0]][head[1]] = corpo
                        snake_head.append(head)
                        del snake_head[0]
                        img[tail[0]][tail[1]] = scia                     #x e y della tail
    images.save(img, out_img)
    return counter
    pass


def start(start_img,position):
    img = images.load(start_img)
    img[position[1]][position[0]] = (0,255,0)
    return img
    pass