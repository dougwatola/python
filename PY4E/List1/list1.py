#fname = "romeo.txt"
fname = input("Enter file name: ")
fh = open(fname)
#print(fh)
final_list=[]
iterate_list=[]

#for loop to iterate through each line in txt file

for line in fh:
    #print(line.rstrip())
    iterate_list= line.split()

    #for loop to iterate through each word in line
#remove duplicate words by comparing word in iterate_list to a final_list

    for i in iterate_list:
        if (i not in final_list):  #run comparison 
            final_list.append(i)

#sort and print final list           
final_list.sort()    
print(final_list)