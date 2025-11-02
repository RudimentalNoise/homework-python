
'''
Obiettivo dello homework è leggere alcune stringhe contenute in una serie di
file e generare una nuova stringa a partire da tutte le stringhe lette.
Le stringhe da leggere sono contenute in diversi file, collegati fra loro a
formare una catena chiusa. Infatti, la prima stringa di ogni file è il nome di
un altro file che appartiene alla catena: partendo da un qualsiasi file e
seguendo la catena, si ritorna sempre nel file di partenza.

Esempio: il contenuto di "A.txt" inizia con "B.txt", il file "B.txt", inizia
con "C.txt" e il file "C.txt" inizia con "A.txt", formando la catena
"A.txt"-"B.txt"-"C.txt".

Oltre alla stringa con il nome del file successivo, ogni file contiene anche
altre stringhe separate da spazi, tabulazioni o caratteri di a capo. La
funzione deve leggere tutte le stringhe presenti nei file della catena e
costruire la stringa che si ottiene concatenando i caratteri con la più alta
frequenza in ogni posizione. Ovvero, nella stringa da costruire, alla
posizione p ci sarà il carattere che ha frequenza massima nella posizione p di
ogni stringa letta dai file. Nel caso in cui ci fossero più caratteri con
la stessa frequenza, si consideri l'ordine alfabetico.
La stringa da costruire ha lunghezza pari alla
lunghezza massima delle stringhe lette dai file.

Quindi, si deve scrivere una funzione che prende in ingresso una stringa A
che rappresenta il nome di un file e restituisce una stringa.
La funzione deve costruire la stringa secondo le indicazioni illustrate sopra
e ritornare le stringa così costruita.

Esempio: se il contenuto dei tre file A.txt, B.txt e C.txt nella directory
test01 è il seguente

test01/A.txt          test01/B.txt         test01/C.txt
-------------------------------------------------------------------------------
test01/B.txt          test01/C.txt         test01/A.txt
house                 home                 kite
garden                park                 hello
kitchen               affair               portrait
balloon                                    angel
                                           surfing

la funzione most_frequent_chars("test01/A.txt") dovrà restituire la stringa
"hareennt".
'''





#metto le parole sottoforma di stringa in una lista
#poi su ciascun indice di tutte le parole faccio un dizionario con le frequenze delle lettere delle parole
#se c'è una parola più di un certo indice la scarto
#metto le le ttere di più alta frequenza dei vari indici in una stringa(in caso di parità metto in ordine alfabetico)


def opening_lista(string):                 #test01/A.txt
    with open('test01/A.txt', 'r', encoding = 'UTF-8') as f:
        s = f.readline().rstrip()
        primo = 'test01/A.txt'  
        r = f.read()
        lista = r.split()
    while s != primo:    
        with open(s,'r', encoding = 'UTF-8') as t:
            s = t.readline().rstrip()
            supporto = t.read().split()
            for parola in supporto:
                #if parola isalpha: 
                lista.append(parola)   
                #else: continue    
    return lista
    
def da_listaparole_a_listaindici(lista):  #lista da sopra senza mettere le lettere in una nuova lista ci faccio già il dizionario ed estraggo la lettera maggiore
    lista_nuova = []
    x = 0
    y = 0
    for words in lista:
        z = len(words)
        if x <= z:
            x = z
    while y != x:
        ultimate_lista = []
        for words in lista:
            try:
                ultimate_lista.append(words[y].lower())
            except Exception:
                pass
        lista_nuova.append(sorted(ultimate_lista))         #aggiunto sorted
        y += 1
    return lista_nuova


#da lista di singoli caratteri divisi per indice a dizionario con ricorrenze
def lista_to_dict(lista_nuova):                #lista da sopra
    ultimate_lista = []
    for liste in lista_nuova:
        diz= {}
        for lettere in liste:
            if lettere in diz:
                diz[lettere] += 1
            else:
                diz[lettere] = 1
        ultimate_lista.append(diz)  
    return ultimate_lista
#da ampliare
#isalpha()
#da dizionario di ricorrenze a stringa finale
#estrarre ogni valore con la massima occorenza dal dizionario oppure se in parità in base all'ordine alfabetico
#problema lunghezza massima
def translation(ultimate_lista):  #lista di dizionari
    stringa = ''
    for dictionary in ultimate_lista:
        max_value = max(dictionary, key=dictionary.get)
        stringa += max_value
    return stringa



def most_frequent_chars(filename: str) -> str:
    # SCRIVI QUI LA TUA SOLUZIONE
    with open(filename , 'r', encoding = 'UTF-8') as f:
        s = f.readline().rstrip()
        primo = filename  
        r = f.read()
        lista = r.split()
    while s != primo:    
        with open(s,'r', encoding = 'UTF-8') as t:
            s = t.readline().rstrip()
            supporto = t.read().split()
            for parola in supporto:
                #if parola isalpha: 
                lista.append(parola)
    lista_nuova = []
    x = 0
    y = 0
    for words in lista:
        z = len(words)
        if x <= z:
            x = z
    while y != x:
        ultimate_lista = []
        for words in lista:
            try:
                ultimate_lista.append(words[y])
            except Exception:
                pass
        lista_nuova.append(sorted(ultimate_lista))         
        y += 1
    ultimate_lista = []
    for liste in lista_nuova:
        diz= {}
        for lettere in liste:
            if lettere in diz:
                diz[lettere] += 1
            else:
                diz[lettere] = 1
        ultimate_lista.append(diz)
    stringa = ''
    for dictionary in ultimate_lista:
        max_value = max(dictionary, key=dictionary.get)
        stringa += max_value
    return stringa
    pass







def da_listaparole_a_listaindici(lista):  
    stringa = ''
    lista_nuova = []
    x = 0
    y = 0
    for words in lista:
        z = len(words)
        if x <= z:
            x = z
    while y != x:
        ultimate_lista = []
        diz = {}
        for words in lista:
            try:
                ultimate_lista.append(words[y].lower())
            except Exception:
                pass
        ultimate_lista = sorted(ultimate_lista)    
        for lettere in ultimate_lista:
            if lettere in diz:
                diz[lettere] += 1
            else:
                diz[lettere] = 1
        max_value = max(diz, key=diz.get)
        stringa += max_value
        y += 1
    return stringa



    
def translation(lista):
    stringa = ''
    diz = {}
    max_len = max(map(len, l))
    ultimate_lista = []
    for i in range(max_len):
        index_letters = [e[i] for e in l if len(e) > i]
        ultimate_lista.append(index_letters)
    ultimate_lista = sorted(ultimate_lista)    
    for lettere in ultimate_lista:
        if lettere in diz:
            diz[lettere] += 1
        else:
            diz[lettere] = 1
    max_value = max(diz, key=diz.get)
    stringa += max_value
    y += 1







    