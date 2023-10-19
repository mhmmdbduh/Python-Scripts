import random

def profile(motifs):
    profile_matrix = {'A': [], 'C': [], 'G': [], 'T': []}
    motif_length = len(motifs[0])
    motif_count = len(motifs) + 4  # Add pseudocounts

    for base in 'ACGT':
        for j in range(motif_length):
            count = sum(motif[j] == base for motif in motifs) + 1
            profile_matrix[base].append(count / motif_count)

    return profile_matrix

def motifs_from_profile(profile, dna):
    k = len(profile['A'])
    motifs = []
    
    for string in dna:
        best_motif = ''
        best_prob = -1
        
        for i in range(len(string) - k + 1):
            kmer = string[i:i + k]
            prob = 1
            
            for j, base in enumerate(kmer):
                prob *= profile[base][j]  # Corrected line
                
            if prob > best_prob:
                best_prob = prob
                best_motif = kmer
        
        motifs.append(best_motif)
    
    return motifs

def score(motifs):
    consensus = ''
    motif_length = len(motifs[0])
    total_score = 0
    
    for j in range(motif_length):
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        
        for motif in motifs:
            counts[motif[j]] += 1
        
        max_count = max(counts.values())
        total_score += len(motifs) - max_count
        consensus += max(counts, key=counts.get)
    print(total_score, consensus)
    return total_score, consensus

def randomized_motif_search(dna, k, t):
    motifs = [string[random.randint(0, len(string) - k)] for string in dna]
    best_motifs = motifs[:]
    best_score, _ = score(best_motifs)
    
    while True:
        profile_matrix = profile(motifs)
        motifs = motifs_from_profile(profile_matrix, dna)
        current_score, _ = score(motifs)
        
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs[:]
        else:
            return best_motifs

# Sample Input
# with open('dataset_30307_5.txt') as file:
#     data = file.read().split()
# k = int(data[0])
# t = int(data[1])
# dna = data[2:]
k = 8
t = 5
dna = [
    "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
    "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
    "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
    "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
]

# Run RandomizedMotifSearch 1000 times
best_motifs_list = []
for _ in range(1000):
    best_motifs_list.append(randomized_motif_search(dna, k, t))

# Find the best motif set among the 1000 runs based on the lowest score
best_score = float('inf')
best_motifs = []
for motifs in best_motifs_list:
    current_score, _ = score(motifs)
    if current_score < best_score:
        best_score = current_score
        best_motifs = motifs

# Print the final best motifs
for motif in best_motifs:
    print(motif)
