import pandas as pd
import os
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
import numpy as np
from tqdm import tqdm

DATA_PATH="./data/"

def get_labels(path=DATA_PATH):
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
	
	print(formants.shape)

	return formants

def save_data_to_array(path=DATA_PATH, max_len=150):
	labels,_,_=get_labels(path)

	for label in labels:
		formant_array=np.zeros((1,6))

#		print(formant_array.shape)

		speechfiles=[path + label + '/' + speech for speech in os.listdir(path+'/'+label)]
		for speech in tqdm(speechfiles,"Saving vectors to label -'{}'".format(label)):
			formant_freq=formants_access(speech,max_len=max_len)
#			print(formant_freq.shape)
			formant_array=np.vstack((formant_array,formant_freq))
#		print(formant_array)
		np.save(label+'.npy',formant_array)

def get_train_test(split_ratio=0.8,random_state=42):
	labels,indices,_=get_labels(DATA_PATH)

	X=np.load(labels[0]+'.npy')
	y=np.zeros(X.shape[0])
	print(X.shape)

#	for i,label in enumerate(labels[1:]):
#		x=np.load(label+'.npy')
#		X=np.vstack((X,x))
#		y=np.append(y,np.full(x.shape[0],fill_value=(i+1)))

#	assert X.shape[1] == len(y)

	return train_test_split(X,y,test_size=(1-split_ratio),random_state=random_state,shuffle=True)


#formants_access("./data/Formant/Formant1/vowel1_0_Formant_frq.txt",100)

#print(prepare_dataset(DATA_PATH))
#save_data_to_array()
get_train_test()