import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.utils import to_categorical
import numpy as np
from tqdm import tqdm

DATA_PATH="./data/"

max_length=120

scaler=MinMaxScaler()

def get_labels(path=DATA_PATH):
	labels=os.listdir(path)
	label_indices=np.arange(0,len(labels))
	return labels, label_indices, to_categorical(label_indices)

def formants_access(file_path,max_len):
	formants=pd.read_csv(file_path,delim_whitespace=True,header=None,dtype=np.float64,na_values="--undefined--")
	formants.columns=["time","F1","F2","F3","F4","F5"]
	
	formants=formants[::10]
	
	scaler=MinMaxScaler()
	scaler.fit(formants)
	formants=scaler.transform(formants)

	if (max_len > formants.shape[0]):
		pad_width=max_len-formants.shape[0]
#		heading_zero=int(pad_width/2)
#		trailing_zero=pad_width-heading_zero
#		formants=np.pad(formants,pad_width=[(heading_zero,trailing_zero),(0,0)],mode='constant')
		formants=np.pad(formants,pad_width=[(0,pad_width),(0,0)],mode='constant')


	else:
		formants=formants[:max_len,:]
	
#	print(formants.shape)

	return formants


def get_train_test(split_ratio=0.8,random_state=42,max_len=max_length):
	labels,indices,_=get_labels(DATA_PATH)

	y=np.array([])

	for i,label in enumerate(labels):

		temp_vector=[]
		formant_files=[DATA_PATH+label+'/'+file for file in os.listdir(DATA_PATH+'/'+label)]
		for text_file in formant_files:
			accessed_data=formants_access(text_file,max_len=max_length)
			accessed_data=np.expand_dims(accessed_data,axis=0)

			temp_vector.append(accessed_data)
		
		x=temp_vector[0]
#		print(temp_vector[25])
		for j,_ in enumerate(temp_vector[1:]):
			x=np.vstack((x,temp_vector[j+1]))
	
		if i==0:
			X=x
		else:
			X=np.vstack((X,x))
#		print(X)
		y=np.append(y,np.full(x.shape[0],fill_value=i))
#	print(y)
	assert X.shape[0] == len(y)
#	print(X.shape)
#	print(y.shape)
	return train_test_split(X,y,test_size=(1-split_ratio),random_state=random_state,shuffle=True)


#formants_access("./data/Formant/Formant1/vowel1_0_Formant_frq.txt",100)

#print(prepare_dataset(DATA_PATH))

#get_train_test()