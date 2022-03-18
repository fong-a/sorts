def bubble_sort(list):
    count_swaps = 1
    length_modifier = 1    
    while count_swaps >0:
        counter = 0
        count_swaps = 0

        while counter < len(list)-length_modifier:
            if list[counter] > list[counter+1]:
                temp = list[counter+1]
                list[counter+1] = list[counter]
                list[counter] = temp
                count_swaps +=1

            counter = counter + 1
        length_modifier+=1    

bubble_sort([8,2,5,3,9,4,1])

# STANDARD ALGORITM (SEARCHES AND SORTS)
