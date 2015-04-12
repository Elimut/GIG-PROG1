def sito(N):
  N += 1
  sito = [True] * N
 
  for i in range(2, N):
    if sito[i]:
      for j in range(i*2, N, i):
        sito[j]=False
 
  prvocisla=[]
  for i in range(2, N):
    if sito[i]:
      prvocisla.append(i)
  return prvocisla

print(sito(100))      
