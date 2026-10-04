#DNA SEQUENCE CALCULATOR

#Validating DNA sequence

DNA_sequence = input("Enter your nucleotide sequence: ")
print(f"DNA sequence = {DNA_sequence}")

Uppercase_Sequence = DNA_sequence.upper()
print(f"Converted sequence:{Uppercase_Sequence}")

if Uppercase_Sequence == "":
    print("Error: DNA sequence cannot be empty.")
    raise SystemExit

valid = True
for i in Uppercase_Sequence:
  if i in ('A','T','G','C'):
    print(i)
  else:
    print(f"{i} is Invalid nucleotide")
    valid = False
    

if valid:
  print("Valid DNA sequence")
else:
  print("Invalid DNA sequence")
  raise SystemExit
  

#Nucleotide composition

Total_length = len(Uppercase_Sequence)
print(f"The total length of sequence is {Total_length}")

count_A= 0
count_T=0
count_G=0
count_C=0

for i in Uppercase_Sequence:
  if i == 'A':
    count_A+=1

  elif i == 'T':
    count_T+=1

  elif i == 'G':
    count_G+=1

  elif i=='C':
    count_C+=1

print(f"Number of A: {count_A}")
print(f"Number of T: {count_T}")
print(f"Number of G: {count_G}")
print(f"Number of C: {count_C}")

#GC% Content calculation

GC = count_G + count_C
GC_content = (GC/Total_length)*100
print(f"The total GC content is {GC_content}%")

#AT% Content calculation

AT = count_A + count_T
AT_content = (AT/Total_length)*100
print(f"The total AT content is {AT_content}%")

#Complemntary DNA

complementary = ""
for i in Uppercase_Sequence:
  if i == 'A':
    complementary+='T'
  elif i == 'T':
    complementary+='A'
  elif i == 'G':
    complementary+='C'
  elif i == 'C':
    complementary+='G'

print(f"The complement strand is complementary = {complementary}")

#Reverse complement

reverse_complement = complementary[::-1]
print(f"The reverse complement is {reverse_complement}")

#Transcription

RNA = ""

for i in Uppercase_Sequence:
  if i == 'T':
    RNA+='U'
  else:
    RNA+=i

print(f"The strand after transcription is:{RNA}")

#Translation

Genetic_codons = {

    # U U _
    'UUU': 'F',
    'UUC': 'F',
    'UUA': 'L',
    'UUG': 'L',

    # U C _
    'UCU': 'S',
    'UCC': 'S',
    'UCA': 'S',
    'UCG': 'S',

    # U A _
    'UAU': 'Y',
    'UAC': 'Y',
    'UAA': 'STOP',
    'UAG': 'STOP',

    # U G _
    'UGU': 'C',
    'UGC': 'C',
    'UGA': 'STOP',
    'UGG': 'W',

    # C U _
    'CUU': 'L',
    'CUC': 'L',
    'CUA': 'L',
    'CUG': 'L',

    # C C _
    'CCU': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',

    # C A _
    'CAU': 'H',
    'CAC': 'H',
    'CAA': 'Q',
    'CAG': 'Q',

    # C G _
    'CGU': 'R',
    'CGC': 'R',
    'CGA': 'R',
    'CGG': 'R',

    # A U _
    'AUU': 'I',
    'AUC': 'I',
    'AUA': 'I',
    'AUG': 'M',

    # A C _
    'ACU': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',

    # A A _
    'AAU': 'N',
    'AAC': 'N',
    'AAA': 'K',
    'AAG': 'K',

    # A G _
    'AGU': 'S',
    'AGC': 'S',
    'AGA': 'R',
    'AGG': 'R',

    # G U _
    'GUU': 'V',
    'GUC': 'V',
    'GUA': 'V',
    'GUG': 'V',

    # G C _
    'GCU': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',

    # G A _
    'GAU': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',

    # G G _
    'GGU': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G'
}

protein = ""

for i in range(0,len(RNA), 3):
    codon = RNA[i:i+3]

    if (len(codon)<3):
      break

    if codon in ('UAA','UAG','UGA'):
      break

    if codon not in Genetic_codons:
      print(f"Invalid codons: {codon}")
      break

    amino_acids = Genetic_codons[codon]
    protein+=amino_acids

print(f"Protein sequence: {protein}")

#Nucleotide Frequency

f_A = count_A / Total_length
f_T = count_T / Total_length
f_G = count_G / Total_length
f_C = count_C / Total_length

print("Frequency of A:", f_A)
print("Frequency of T:", f_T)
print("Frequency of G:", f_G)
print("Frequency of C:", f_C)

#Amino acid composition

amino_acid_count = {}

for i in protein:
  if i in amino_acid_count:
    amino_acid_count[i]+=1
  else:
    amino_acid_count[i]=1

print(amino_acid_count)

#Total lenghth of protein sequence

total_protein_length = len(protein)
print(f"The total length of protein is {total_protein_length}")

#Protein Molecular Weight

amino_acid_mass = {
    'A': 89.09,    # Alanine
    'R': 174.20,   # Arginine
    'N': 132.12,   # Asparagine
    'D': 133.10,   # Aspartic acid
    'C': 121.15,   # Cysteine
    'E': 147.13,   # Glutamic acid
    'Q': 146.15,   # Glutamine
    'G': 75.07,    # Glycine
    'H': 155.16,   # Histidine
    'I': 131.17,   # Isoleucine
    'L': 131.17,   # Leucine
    'K': 146.19,   # Lysine
    'M': 149.21,   # Methionine
    'F': 165.19,   # Phenylalanine
    'P': 115.13,   # Proline
    'S': 105.09,   # Serine
    'T': 119.12,   # Threonine
    'W': 204.23,   # Tryptophan
    'Y': 181.19,   # Tyrosine
    'V': 117.15    # Valine
}

total_mass = 0

for i in protein:
  total_mass+=amino_acid_mass[i]

MW_protein = total_mass - ((total_protein_length-1)*18.015)
print(f"The molecular weight of protein is {MW_protein}Da")

#DNA molecular weight
dna_mass = {
    'A': 313.21,
    'T': 304.20,
    'G': 329.21,
    'C': 289.18
}

total_dna_mass = 0
for i in Uppercase_Sequence:
  total_dna_mass+=dna_mass[i]
print(f"The total mass of DNA sequence is:{total_dna_mass}")
