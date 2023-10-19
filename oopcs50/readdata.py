with open('dataset_30307_5.txt') as file:
    data = file.read().split()
    k = data[0]
    t = data[1]
    dna = data[2:]
    print(k,t,dna)
