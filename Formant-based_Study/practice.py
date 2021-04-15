import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

path="./data/Formant1/"
formants=pd.read_csv(path+"vowel1_0_Formant_frq.txt",delim_whitespace=True,header=None,dtype=np.float64,na_values="--undefined--")
formants.columns=["time","F1","F2","F3","F4","F5"]
max_len=100
if (max_len > formants.shape[0]):
	pad_width=max_len-formants.shape[0]
	heading_zero=int(pad_width/2)
	trailing_zero=pad_width-heading_zero
	formants=np.pad(formants,pad_width=[(heading_zero,trailing_zero),(0,0)],mode='constant')

else:
	formants=formants.iloc[:max_len,:]

print(formants)

scaler=MinMaxScaler()
scaler.fit(formants)
formants=scaler.transform(formants)

print(formants)