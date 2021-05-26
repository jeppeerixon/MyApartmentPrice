import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

#xlfile = pd.ExcelFile("kvmrum.xls")
#krkvm = pd.read_excel(xlfile, "Årshistorik", usecols=["kr/kvm"])
#artal = pd.read_excel(xlfile, "Årshistorik", usecols=["År"])
#print(df.head()) # shows headers with top 5 rows

kvm_arr = np.array([kvm_ren]).reshape(-1,1)
slut_arr = np.array([slut_ren]).reshape(-1,1)
print('- - - - - - - - -')
in_kvm = input('Ange kvadratmeter: ')
inp_kvm = int(in_kvm)


model = LinearRegression()
model.fit(kvm_arr, slut_arr)
inp_slut = model.predict(np.array([inp_kvm]).reshape(-1,1))

print('- - - - - - - - -')
print('AI PROSSEING DONE')
print('- - - - - - - - -')
print('Exp value:', inp_slut)
print('- - - - - - - - -')
print('On Size KVM:', inp_kvm)
print('- - - - - - - - -')

#plt.plot(np.linspace(30,120,100).reshape(-1,1), model.predict(np.linspace(30,120,100).reshape(-1,1)), 'r')
plt.scatter(kvm_arr, slut_arr)
plt.scatter(inp_kvm, inp_slut)
#plt.scatter(time_artal[int_ar], model.predict(np.array([int_ar]).reshape(-1,1),))
plt.ylim(2000000, 7000000)
plt.xlim(0, 125)
plt.show()
