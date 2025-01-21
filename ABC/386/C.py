K = int(input())
S = list(input())
T = list(input())

if S==T:
    print("Yes")
    exit()

if abs(len(S) - len(T)) > 1:
    print("No")
    exit()

if len(S) - len(T) == -1:
    is_ok = True
    i, j = 0, 0
    mismatch_found = False
    while i < len(S) and j < len(T):
        if S[i] != T[j]:
            if mismatch_found:
                is_ok = False
                break
            else:
                mismatch_found = True
                j += 1
        else:
            i += 1
            j += 1
    
elif len(S) - len(T) == 1:
    is_ok = True
    i, j = 0, 0
    mismatch_found = False
    while i < len(T) and j < len(S):
        if T[i] != S[j]:
            if mismatch_found:
                is_ok = False
                break
            else:
                mismatch_found = True
                j += 1
        else:
            i += 1
            j += 1

else:
    is_ok = True
    i = 0
    mismatch_found = False
    while i < len(S):
        if S[i] != T[i]:
            if mismatch_found:
                is_ok = False
                break
            else:
                mismatch_found = True
                i += 1
        
        else:
            i += 1
print("Yes" if is_ok else "No")
