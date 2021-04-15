import os
path1="/media/rakibul/WorkFolder/Work/Thesis/Speech_Recognition/Bangla_Vowel_Recognition/Using_Formant/Audio_Data/"
j=1
for file in os.listdir(path1):
	path2="/media/rakibul/WorkFolder/Work/Thesis/Speech_Recognition/Bangla_Vowel_Recognition/Using_Formant/Audio_Data/"+str(j)+"/"
	i=1
	for filename in os.listdir(path2):
		dst="vowel"+str(j)+"_"+str(i)+".wav"
		src=path2+filename
		dst=path2+dst

		os.rename(src,dst)
		i+=1
	j+=1
