import pandas as pd
import os
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
import numpy as np
from tqdm import tqdm

DATA_PATH="./data/"

def get_labels(path=DATA_PATH)::
	labels=os.listdir(path)
	label_indices=np.arange(0,len(labels))
	return labels, label_indices, to_categorical(label_indices)

def formants_access(file_path,max_len=150):
	formants=pd.read_csv(file_path,sep="\s+",header=None, names=["time","F1","F2","F3","F4","F5"])

	if (max_len > formants.shape[0]):
		pad_width=max_len-formants.shape[0]
		heading_zero=int(pad_width/2)
		trailing_zero=pad_width-heading_zero
		formants=np.pad(formants,pad_width=[(heading_zero,trailing_zero),(0,0)],mode='constant')

	else:
		formants=formants.iloc[:max_len,:]
	
#	print(formants.shape)

	return formants


def get_train_test(split_ratio=0.8,random_state=42,max_len=150):
	labels,indices,_=get_labels(DATA_PATH)

	single_file=os.listdir(DATA_PATH+labels[0]+'/')

	X=formants_access(DATA_PATH+labels[0]+'/'+single_file[0])

	first_formant=[DATA_PATH+labels[0]+'/'+file for file in os.listdir(DATA_PATH+'/'+labels[0])]
		
	for rest_files in first_formant[1:]:
		X=np.vstack((X,formants_access(rest_files,max_len=max_len)))
	
	y=np.zeros(X.shape[0])

	for i,label in enumerate(labels[1:]):

		formant_files=[DATA_PATH+label+'/'+file for file in os.listdir(DATA_PATH+'/'+label)]
		for text_file in formant_files:
			X=np.vstack((X,formants_access(text_file,max_len=max_len)))
			y=np.append(y,np.full(max_len,fill_value=(i+1)))

	assert X.shape[0] == len(y)
	print(X.shape)
	return train_test_split(X,y,test_size=(1-split_ratio),random_state=random_state,shuffle=True)


#formants_access("./data/Formant/Formant1/vowel1_0_Formant_frq.txt",100)

#print(prepare_dataset(DATA_PATH))
#save_data_to_array()
get_train_test()