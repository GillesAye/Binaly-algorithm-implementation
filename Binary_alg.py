# Gives indexes
def binary_tester(array,x) :

    low = 0
    mid =0
    high =  len(array)-1

    while low <= high :

        mid = (high + low) // 2

        # If number is less than x ignore right part
        if array[mid] < x:
            low = mid -1

        # If number is more than x then ignore left part
        elif array[mid] > x:
            low = mid +1

        else :
            return mid 
        
# Test array 

array = [ 1,2,3,4,5,6,7]

x = 4

result = binary_tester(array, x)

print (result)

    

   
