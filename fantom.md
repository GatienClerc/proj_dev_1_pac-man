# fantome

- Blicky (rouge)
- Pinky (rose)
- Inky (cyan)
- Clyde (orange)
---

## Rouge: Blinky 
comportment: déterminé, agressif  
en jeu: 
1. Case cible: la position actuelle de Pac-Man.(chasseur)
2. À chaque intersection, Blinky regarde les directions disponibles et choisit celle qui le rapproche le plus de sa cible.
2. Quand il reste peu de pac-gommes dans le niveau, Blinky accélère et devient encore plus rapide et menaçant. <br> C'est l'état « Cruise Elroy ».
3. Coin de base: supérieur a doit
---
## Rose: Pinky
comportment: rusée, sournoise, sa stratégie est de piéger pac-man  
en jeu: 
1. Case cible: calcule 4 case devant pac-man pour le pieger
2. Coin de base: supérieur a gauche

---
## Cyan: Inky
comportment:  simple d'esprit, maladroit, oit il poursuit Pac-Man, soit il va dans la direction opposée  
en jeu:
1. Case cible: prend 2 case devant Pac-Man, puis trace un vecteur entre Blinky et ce point, <br> et enfin double la longueur de ce vecteur pour déterminer la destination
2. Coin de base:  inférieur droit

---
## Orange: Clyde
comportment: vagabodage, évite pack-man  
en jeu:
1. Case cible: si + de 8 case de pac-man vas a sa position si - de 8 case revient dans sont coin
2. Coin de base:  inférieur gauche