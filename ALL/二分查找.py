#评测题目: 输入一个已经排序的数组（从小到大），和一个数字，输出两个index，分别是这个数字在数组中第一次和最后一次出现的位置
  
# sorted_arr = [1,2,3,4,5,5,5,6,7,8,9]
sorted_arr = [1,2,2,2,3,4]
# query_key = 2
query_key = 5

arr_len = len(sorted_arr)
# 6

mid_idx = arr_len // 2
# 3

left_idx, right_idx = 0, arr_len - 1
# 0, 5

first_idx, last_idx = 0, 0 

def search_direction(left_idx, right_idx):
  # search single direction
  # return the first and last idx of the query key

  # search_mid_idx = 1
  while left_idx < right_idx:
      search_mid_idx = (left_idx + right_idx) // 2
    
      # sorted_arr[search_mid_idx] = sorted_arr[1] = 2
      if sorted_arr[search_mid_idx] <= query_key:
        # right_idx = 0
        right_idx = search_mid_idx - 1

        if sorted_arr[left_idx] == query_key:
          # first_idx = 0
          first_idx = left_idx
        else:
          left_idx += 1

        if sorted_arr[right_idx] == query_key:
          # last_idx = 
          last_idx = right_idx          

      else:
        #  sorted_arr[search_mid_idx] > query_key:
        left_idx = search_mid_idx + 1
        
        if sorted_arr[left_idx] == query_key:
          first_idx = left_idx

        if sorted_arr[right_idx] == query_key:
          last_idx = right_idx
        else:
          right_idx -= 1

      search_mid_idx = (right_idx + left_idx) // 2
    
  return first_idx, last_idx
    
# search left
# search_direction(0, 3)
left_first_idx, left_last_idx = search_direction(left_idx, mid_idx)

# search right
# search_direction(4, 5)
right_first_idx, right_last_idx = search_direction(mid_idx+1, right_idx)

print(min(left_first_idx, right_first_idx), max(left_last_idx, right_last_idx))


# corner cases:
# 1. if there is no query key (k) inside this array
# 2. if there is only one query k inside this array
# 3. [..., 1, 2, 2, 2, 3, ...], query 2, mid = 2

# left_idx, right_idx

        
# >= , search left
# <, search right
        
# <=, search right,
# >, search left
      
# search left direction
while left_idx < right_idx:
	mid_idx = (left_idx + right_idx) // 2
    if sorted_arr[mid_idx] >= query_key
    	# if query_key == 2
    	# sorted_arr[mid_idx] = 2
		right_idx = mid_idx # [...,(1),(2),2,2,...]
    else:
      	left_idx = mid_idx

first_left_idx = left_idx

# search right direction
while left_idx < right_idx:
  	mid_idx = (left_idx + right_idx) // 2
    if sorted_arr[mid_idx] <= query_key
    	left_idx = mid_idx
    else:
      	right_idx = mid_idx
        
last_right_idx = right_idx
        