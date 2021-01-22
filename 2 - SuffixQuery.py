def count_former(recurrent_list):
    memory = []
    unique_count_list = []
    count = 0
    for item in recurrent_list[::-1]:
        if not item in memory:
            count = count + 1
            memory.append(item)
        unique_count_list.append(count)
    return unique_count_list[::-1], count


n,m = map(int,input().split())
recurrent_list = list(map(int,input().split()))

unique_count_list, last_count = count_former(recurrent_list)
for _ in range(m):
    position = int(input())
    print(unique_count_list[position-1])
