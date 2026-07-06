fruits = {"Pomme":"rouge", "banane":"jaune", "orange":"orange"};
fruits["kiwi"] = "vert";
Couleur_banane = fruits["banane"];
print(f"La couleur de la banane est : {Couleur_banane}");
fruits["Pomme"] = "vert";
del fruits["banane"];
print(fruits.keys());
