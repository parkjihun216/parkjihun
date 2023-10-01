array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,      35, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,      68, 
]

def sort_bubble(array):
  print('-' * 60)
  print(f'before: {array}')
  index = len(array) 
  for i in range(0, index, 1) : 
      for j in range(0, index-i-1, 1) :
         if array[j] > array[j+1] :
            array[j], array[j+1] = array[j+1], array[j]   
  print(f'after : {array}')

def sort_select(array):
  print('-' * 60)
  print(f'before: {array}')
  for i in range(len(array)) :
    min = i
    for j in range(i + 1, len(array)) :
      if array[min] > array[j] :
        min = j
      array[i], array[min] = array[min], array[i]
  print(f'after : {array}')

def sort_insert(array):
  print('-' * 60)
  print(f'before: {array}')
  for i in range(1, len(array)) :
    for j in range(i, 0, -1) :
      if array[j] < array[j-1] :
          array[j], array[j-1] = array[j-1], array[j]
  print(f'after : {array}')

def sort_shell(array):
  print('-' * 60)
  print(f'before: {array}')
  def a (array) :
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    sort_shell(left)
    sort_shell(right)
    b(left, right)
    
  def b(left, right):
        i = 0
        j = 0
        k = 0
        while (i < len(left)) and (j < len(right)):
            if left[i] < right[j]:
                array[k] = left[i]
                i+=1
                k+=1
            else:
                array[k] = right[j]
                j+=1
                k+=1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k+= 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k+= 1
  print(f'after : {array}')

def main():
  sort_bubble(array[:])
  sort_insert(array[:])
  sort_select(array[:])
  sort_shell(array[:])

if __name__ == '__main__':
  main()

