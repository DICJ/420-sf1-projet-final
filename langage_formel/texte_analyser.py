from urllib import request

#liste des sentiments (à utiliser dans vos fonctions seulement)
amour = ["love", "affection", "heart", "kiss", "romance"]
colère = ["anger", "hate", "rage", "fury", "violence"]
peur = ["fear", "terror", "afraid", "horror", "scared"]
tristesse = ["sad", "cry", "tears", "grief", "sorrow"]


#fonction permettant de recevoir le livre sous forme de liste de ligne (en string) du livre
#elle retourne la liste de ligne du roman
def book_to_line_list():

    #creation de la list de lignes vide
    line_lst = []

    #importation du livre dans un string appelé text
    response = request.urlopen("http://www.gutenberg.org/files/2554/2554-0.txt")
    raw = response.read()
    text = raw.decode("utf-8-sig")

    cpt = 0

    #pour chaque ligne de la string entre 126 et 22091 on insert la ligne dans la liste
    for line in text.splitlines():
        if cpt > 126 and cpt < 22091:
            line_lst.append(line)
        cpt+=1

    #on retourne la liste
    return line_lst


#mettre vos prochaines fonction en-dessous
