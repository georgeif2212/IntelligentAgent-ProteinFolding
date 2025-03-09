from pyDatalog import pyDatalog

pyDatalog.clear()
# Definir relaciones
pyDatalog.create_terms('es_superheroe, tiene_poderes, pertenece_a, X, Y')
# Hechos: Personajes y sus categorías
+ es_superheroe('Spider-Man')
+ es_superheroe('Iron Man')
+ es_superheroe('Doctor Strange')
# Reglas: Si alguien es superhéroe, tiene poderes (excepto Iron Man, quien usa tecnología)
tiene_poderes(X) <= es_superheroe(X) & (X != 'Iron Man')

# Pertenencia a equipos
+ pertenece_a('Spider-Man', 'Avengers')
+ pertenece_a('Doctor Strange', 'Illuminati')
# Consultas
print(es_superheroe(X))  # ¿Quiénes son superhéroes?
print(tiene_poderes(X))  # ¿Quién tiene poderes?
print(pertenece_a(X, 'Avengers'))  # ¿Quién pertenece a los Avengers?