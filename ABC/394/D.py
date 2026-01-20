S = input()

former = ['(', '[', '<']
latter = [')', ']', '>']

dict = {'(': ')', '[': ']', '<': '>'}

N = len(S)
kakko = []

i = 0
c = 0
 
while i < N:
    if S[i] in former:
        kakko.append(dict[S[i]])
        i += 1
        
    else:
        n = len(kakko)
        if n == 0:
            print("No")
            exit()
            
        kakko.reverse()
        for j in range(n):
            if i + j >= N or S[i + j] != kakko[j]:    
                print("No")
                exit()

        kakko = []        
        i += n
if S[N-1] in former:
    print("No")
else:
    print("Yes")    