from pyDatalog import pyDatalog

pyDatalog.clear()

# * Program that validates the amino acid chain of insulin
# ? Chain A (21 amino acids):
# ? GIVEQCCTSICSLYQLENYCN

# ? Chain B (30 amino acids):
#   ? FVNQHLCGSHLVEALYLVCGERGFFYTPKT

# Define a valid amino acid (useful when allowing mutations or insulin variations)
valid_amino_acid = set("GAVLIFPWCYSTNQDEKRHM")

# Define connections
pyDatalog.create_terms("X, Y, chain, have, valid_length, "
                        "amino_acid_sequence")

+chain("A")
+chain("B")

+amino_acid_sequence("A","GIVEQCCTSICSLYQLENYCN")
+amino_acid_sequence("B","FVNQHLCGSHLVEALYLVCGERGFFYTPKT")

# Facts
+have("A", 21)
+have("B", 30)

# Rules
valid_length(X, Y) <= have(Y, X)

# Queries
print("Cadenas disponibles: \n\n",chain(X))
print("Cadena y su secuencia: \n\n",amino_acid_sequence(X,Y))
print("Longitudes esperadas: \n\n",have(X, Y))

