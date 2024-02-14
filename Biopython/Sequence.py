from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
my_seq = Seq('GATCGATGGGCCTATATAGGATCGAAAATCGC')
for i, l in enumerate(my_seq):
    print("%i, %s" %(i, l))

#accessing each letter or chemical
print(my_seq[1])
print(my_seq[-1])


#count method for counting a pattern

count_GAT = my_seq.count('GAT')
print(count_GAT)

print(len(my_seq))

#to calculate GC fraction - percentage of Guanine and Ctyocine on the whole of nucleotide bases
#we use GC_fraction

print(gc_fraction(my_seq))

# we can slice a sequence
print(my_seq[2:10])
print(my_seq[::-1])

print(str(my_seq))

fasta_format_string = ">Name\n%s\n" % my_seq
print(fasta_format_string)

#combining strings
seq1 = Seq("ACGT")
seq2 = Seq("AACCGG")
print(seq1 + seq2)


#we can change case
dna_seq = Seq("acgtACGT")
print(dna_seq.upper())
