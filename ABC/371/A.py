Sab, Sac, Sbc = input().split()

if (Sab == ">" and Sac == "<") or (Sab == "<" and Sac == ">"):
  print("A")
elif (Sab == "<" and Sbc == "<") or (Sab == ">" and Sbc == ">"):
  print("B")
else:
  print("C")