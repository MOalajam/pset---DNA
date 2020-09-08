from sys import argv, exit
import csv

def str_count ( dna , Str ):
    count = 0
    max_count = 0
    k = 0

    for letter in range(len(dna) -  len(Str)):
        is_str = True

        for i in range(len(Str)) :
            if dna[letter + i] != Str[i] :
                is_str = False

        if is_str == True:
                k = 1
                count += 1
                if count > max_count :
                    max_count = count
        else :
            if k >= 1 :
                k += 1

        if k > len(Str) :
            k = 0
            if is_str == False:
                count = 0

    return max_count




with open(argv[1] , "r") as data_file :
    data = list(csv.reader(data_file))

with open(argv[2] , "r") as dna_file :
    in_dna = dna_file.read()


DNA_str_info_list = []
DNA_str_info_list.append("  ")


for i in range( 1 , len(data[0])) :
    DNA_str_info_list.append(str_count(in_dna,data[0][i]))


for j in range (1 , len(data) - 1):
    found = True
    for i in range (1 , len(data[0]) - 1):


        if data[j][i] != DNA_str_info_list[i]:
            found = False

    if found == True :
        print(data[j][0])
        exit(0)








