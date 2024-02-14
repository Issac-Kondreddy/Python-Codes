from Bio.Seq import Seq
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(my_seq)
#complement of sequence using compliment A->T, G->C
print("The compliment of nucleotide:",my_seq.complement())
#reverse compliment
print("The reverse complement of nucleotide:", my_seq.reverse_complement())