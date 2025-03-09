from pyDatalog import pyDatalog

pyDatalog.clear()
# Definir relaciones
pyDatalog.create_terms('es_humano, es_elfo, es_mago, es_aliado, enemigo_de, X, Y')
# Hechos
+ es_humano('Aragorn')
+ es_humano('Boromir')
+ es_elfo('Legolas')
+ es_mago('Gandalf')
# Relaciones de amistad/enemistad
+ es_aliado('Aragorn', 'Legolas')
+ es_aliado('Legolas', 'Gimli')
+ enemigo_de('Gandalf', 'Sauron')
# Reglas de inferencia
es_aliado(X, Y) <= es_aliado(Y, X)  # La alianza es mutua
enemigo_de(X,Y) <= enemigo_de(Y,X)
# Consultas
print(es_humano(X))  # ¿Quiénes son humanos?
print(es_aliado(X, 'Legolas'))  # ¿Quiénes son aliados de Legolas?
print(enemigo_de(X, Y))  # ¿Quiénes tienen enemigos?