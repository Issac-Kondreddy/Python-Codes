from Bio import SeqIO

for record in SeqIO.parse("sample.fasta", "fasta"):
    print(f"ID: {record.id}")
    print(f"Sequence: {str(record.seq)}\n")
