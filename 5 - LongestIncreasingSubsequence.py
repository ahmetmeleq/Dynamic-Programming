seq_len = int(input())
sequence = list(map(int,input().split()))

dp_memory = {}

def LIS(start_index):
    if start_index in dp_memory:
        return dp_memory[start_index]
    
    maxi_local = 0
    current_local = 0
    
    
    for i in range(start_index+1, seq_len):
        if(sequence[i]>sequence[start_index]):
            current_local = LIS(i)
            if current_local > maxi_local:
                maxi_local = current_local
    dp_memory[start_index] = maxi_local + 1
    return maxi_local + 1
        
maxi = 0
current = 0

for i in range(seq_len):
    current = LIS(i)
    if current > maxi:
        maxi = current

print(maxi)
