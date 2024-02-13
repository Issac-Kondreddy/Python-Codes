from Bio.Seq import Seq

my_seq = Seq("AGTACACTGGTTGGT")
print("Sequence: ", my_seq)
print("Reverse complement of My Sequence", my_seq.complement())
print("Protein Translation: ", my_seq.translate())