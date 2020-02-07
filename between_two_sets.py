def compute_gcd(x,y):
    if (y==0):
        return x
    else:
        return compute_gcd(y, x % y)

def getTotalX(a, b):
    lcm_num = a[0]
    gcd_num = b[0]
    count = 0
    if len(a) > 1:
        for i in range(1, len(a)):
            lcm_num = (lcm_num*a[i]//compute_gcd(lcm_num,a[i]))
            print(lcm_num)
    if len(b) > 1:
        for i in range(1, len(b)):
            gcd_num = compute_gcd(gcd_num,b[i])
            print(gcd_num)

    for x in range(lcm_num, gcd_num+1, lcm_num):
        if compute_gcd(x, gcd_num) == x: 
            count += 1
            
    return count
  

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    result = getTotalX(arr, brr)

    print(str(result) + '\n')
