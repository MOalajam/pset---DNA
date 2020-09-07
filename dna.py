from sys import argv, exit
import csv

#TODO
def str_count ( dna , Str ):
    count = 0

    for letter in range(len(dna)):
        is_str = True

        for i in range(len(Str)) :

            if dna[letter + i] != Str[i] :
                is_str = False

        if is_str == True:
            count += 1
    return count


with open(argv[1] , "r") as data_file :
    reader = csv.reader(data_file)
    data = list(reader)

with open(argv[2] , "r") as dna_file :
    in_dna = dna_file.read()


DNA_str_info_list = []

for  i in range(1 , len(data)) :
    DNA_str_info_list.append(str_count(in_dna,data[i][0]))
    
for j in range (1 , len(data[0]))    
    for p in range(len(data))
                 
        person_found = True
        if(data[j][p + 1] != DNA_str_info_list[p]):
            person_found = False          
         
    if person_found == True :
        print(data[0][j])
        exit(0)
