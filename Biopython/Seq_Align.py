from Bio.Blast import NCBIWWW
from Bio.Seq import Seq

my_seq = Seq("AGTACACTGGT")
result_handle = NCBIWWW.qblast("blastn", "nt", my_seq)
