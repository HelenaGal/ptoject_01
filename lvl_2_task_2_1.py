# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

sp_1 = [4, 6, 2, 1, 9, 63, -134, 566]
sp_2 = [-52, 56, 30, 29, -54, 0, -110]
sp_3 = [42, 54, 65, 87,0]
sp_4 = [5]

def minimum(arr):
  arr_sort = sorted(arr)
  return arr_sort[0]
 
    

def maximum(arr):
  arr_sort = sorted(arr)
  n=len(arr)-1
  return arr_sort[n]



print(sp_1, 'max=', maximum(sp_1), ', min=', minimum(sp_1))
print(sp_2, 'max=', maximum(sp_2), ', min=', minimum(sp_2))
print(sp_3, 'max=', maximum(sp_3), ', min=', minimum(sp_3))
print(sp_4, 'max=', maximum(sp_4), ', min=', minimum(sp_4))
