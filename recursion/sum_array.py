def sum_array1(arr, size):
  if size == 1:
    return arr[0]
  
  return arr[0] + sum_array1(arr[1:], size -1)

def sum_array2(arr, size):
  if size == 1:
    return arr[0]
  
  return arr[size-1] + sum_array2(arr[:-1], size -1)



a = [1,2,3,5,6]
n = len(a)
print(sum_array1(a, n))
print(sum_array2(a, n))