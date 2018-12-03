print("hello world")
stairs =30

def climb_stairs(n):
    if(n<1):
        return none
    arr = [None]*3
    arr[0] = 1
    arr[1] = 2
    arr[2] = 4
    for i in range(3, n):
        arr.append(arr[i - 1]+arr[i - 2]+arr[i - 3])
    return arr[n - 1]

print(climb_stairs(stairs))