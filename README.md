# Building_digital

**Class Building**
(Add getters and setters)
Attribut: ((x1,y1),(x2,y2),(x3,y3),(x4,y4)), list_element #dictionnaire,list_area#dictionnaire(room,door,window,else),floor#int,l
method: addArea,addElement,getSurface 
TDD_building:
assert1: closed surface
assert2: Exists ? 

Class Area(): 
	
	parametre : list_element(verifier que c'est fermé),
	attribut: list_element, 
	method: getSurface #abstract method , tout les fils auront la même fonction , mais pas le même code pour cette fonction
Class Element() : 
	parametre: coordinate
	coordinate : ((x1,y1),(x2, y2))
	method: getCoordinate,getLenght
	
Class Room(Area) : 
	method:getSurface
Class Wall(element) : 
	#rien
Class Door(element) : 
	#rien 
Class Window(element)
        #rien
Class corridor(Area):
	method:getSurface
Class coordinate: 
	Attribut : x, y
Class patio(Area):
	method:getSurface

