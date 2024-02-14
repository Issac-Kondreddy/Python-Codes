from Bio.Seq import Seq
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(coding_dna)

template_dna = coding_dna.reverse_complement()
print(template_dna)

messenger_rna = coding_dna.transcribe()
print(messenger_rna)

print(template_dna.reverse_complement().transcribe())

print(messenger_rna.back_transcribe())