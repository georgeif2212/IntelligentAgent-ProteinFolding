from pyDatalog import pyDatalog

pyDatalog.clear()

# * Program that validates the amino acid chain of insulin
# ? Chain A (21 amino acids): GIVEQCCTSICSLYQLENYCN
# ? Chain B (30 amino acids): FVNQHLCGSHLVEALYLVCGERGFFYTPKT


# Function to compute sequence length
def get_length(seq):
    return len(seq)


# Verify if all characters in a sequence are valid amino acids
def is_valid_sequence(seq):
    return all(aa in valid_amino_acid for aa in seq)


# Define terms
pyDatalog.create_terms(
    "X, Y, Seq, chain, have, amino_acid_sequence, seq_length, valid_amino_acid, valid_sequence"
)

# * Define valid amino acids (for mutation detection)
valid_amino_acid = set("GAVLIFPWCYSTNQDEKRHM")

# * Facts
# ? Define the insulin chains
+chain("A")
+chain("B")

# ? Define the correct insulin sequences
+amino_acid_sequence("A", "GIVEQCCTSICSLYQLENYCN")
+amino_acid_sequence("B", "FVNQHLCGSHLVEALYLVCGERGFFYTPKT")

# ? Define lengths for A and B
+have("A", 21)
+have("B", 30)

# Store sequence lengths as facts
+seq_length("A", get_length("GIVEQCCTSICSLYQLENYCN"))
+seq_length("B", get_length("FVNQHLCGSHLVEALYLVCGERGFFYTPKT"))

# * Rule: Verify if the sequence length matches the expected length
valid_sequence(X, Seq) <= (seq_length(X, Y) & have(X, Y) & amino_acid_sequence(X, Seq))

# Test valid sequences
print("\n ¿La cadena A es válida?:", bool(valid_sequence("A", "GIVEQCCTSICSLYQLENYCN")))
print(
    "¿La cadena B es válida?:",
    bool(valid_sequence("B", "FVNQHLCGSHLVEALYLVCGERGFFYTPKT")),
)

# Test invalid sequences
print(
    "\n¿Una secuencia A mutada (error en aminoácido) es válida?:",
    bool(valid_sequence("A", "GIVEQCCTSICSLYQLENYCX")),
)
print(
    "\n¿Una cadena B con longitud incorrecta es válida?:",
    bool(valid_sequence("B", "FVNQHLCGSHLVEALYLVCGERGFFYTPKTT")),
)


# Queries
# print("Cadenas disponibles:\n", chain(X))
# print("\nCadena y su secuencia:\n", amino_acid_sequence(X, Y))
# print("\nLongitudes esperadas:\n", have(X, Y))
# print("\nLongitud de cada secuencia:\n", seq_length(X, Y))
