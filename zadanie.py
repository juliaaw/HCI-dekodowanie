import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aseegg as ag

czestProbkowania=200

dane=pd.read_csv('sub-01_trial-02.csv', names=['numer', 'ch1', 'ch2', 'ch3', 'ch4','bodziec'])

#obliczanie czasu
czas=int(len(dane['ch1'])/czestProbkowania)
t=np.linspace(0, czas, czas*czestProbkowania)

#wykres przed filtracja
plt.plot(t, dane['ch1'][0:czas*czestProbkowania],  color="b")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [mV]")
plt.show()

#filtracja pasmowo-zaporowa i pasmowo-przepustowa
przefiltrowany1=ag.pasmowozaporowy(dane['ch1'], czestProbkowania, 49, 51)
przefiltrowany2=ag.pasmowoprzepustowy(przefiltrowany1, czestProbkowania, 1, 50)

#wykres po filtracji
plt.plot(t, przefiltrowany2 [0:czas*czestProbkowania], color="b")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [mV]")
plt.show()

#pętla warunkująca mrugniecie i odczytujaca kod
cnt=0
prev=0
kod=[]

for i in przefiltrowany2:
    if i>=0.1 and prev<0.1:
        kod.append(dane['bodziec'][cnt])
    prev=i
    cnt+=1

print("Kod wymrugany przez osobę badaną:", kod)
