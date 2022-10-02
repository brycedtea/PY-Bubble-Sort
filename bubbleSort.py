""" 
first bubble sort algorithm
def bubble_sort(lst):
      for i in range(len(lst)-1):
          for j in range(len(lst) - 1):
              if lst[j] > lst[j+1]:
                  lst[j], lst[j+1] = lst[j+1], lst[j]
      
      return lst

see what the sorting algorithm is doing
def bubble_sort(lst):

for i in range(len(lst)):
    print(f"iteration ")
    for j in range(len(lst) - 1):
        print(f"comparing {lst[j], lst[j+1]}")
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
    
return lst

"""


# more efficient bubble sort algorithm
def bubble_sort(lst):

  for i in range(len(lst)):
      swapped = False
      print(f"iteration ")
      for j in range(len(lst) - 1):
          print(f"comparing {lst[j], lst[j+1]}")
          if lst[j] > lst[j+1]:
              lst[j], lst[j+1] = lst[j+1], lst[j]
              swapped = True

      if not swapped:
          return
      
  return lst


sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")



# more efficient 
def bubble_sort(lst):

  for i in range(len(lst)):
      swapped = False
      print(f"iteration ")
      for j in range(len(lst) - 1):
          print(f"comparing {lst[j], lst[j+1]}")
          if lst[j] > lst[j+1]:
              lst[j], lst[j+1] = lst[j+1], lst[j]
              swapped = True

      if not swapped:
          return
      
  return lst
