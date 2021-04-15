for foldername from 1 to 7	
#Main folders...like Word1, Word2...upto 7

for fln from 1 to 40		
#number of files in each subfolders

use_sound$ = "vowel'foldername'_'fln'" 		
#each file name in the subfolder

Read from file... /media/rakibul/WorkFolder/Work/Thesis/Speech_Recognition/Bangla_Vowel_Recognition/Using_Formant/Audio_Data/Vowel/vowel'foldername'/'use_sound$'.wav


#filedelete /media/rakibul/WorkFolder/Work/Thesis/Speech Recognition/Bangla Vowel Recognition/Using Formant/data/1/'use_sound$'_Formant_frq.txt
#filedelete /media/rakibul/WorkFolder/Work/Thesis/Speech Recognition/Bangla Vowel Recognition/Using Formant/data/1/'use_sound$'_Formant_bw.txt


max_formnt_number=5
To Formant (keep all)... 0 'max_formnt_number' 5500 0.025 50
select Formant 'use_sound$'
#Draw... 0 0 0 0 yes Curve
tot_sample=Get number of frames
s_time=Get time step

for i from 5 to 'tot_sample'
     vtime=('i'-1)*'s_time'
     f1=Get value at time... 1 'vtime' Hertz Linear
     bw1=Get bandwidth at time... 1 'vtime' Hertz Linear
     f2=Get value at time... 2 'vtime' Hertz Linear
     bw2=Get bandwidth at time... 2 'vtime' Hertz Linear
     f3=Get value at time... 3 'vtime' Hertz Linear
     bw3=Get bandwidth at time... 3 'vtime' Hertz Linear
     f4=Get value at time... 4 'vtime' Hertz Linear
     bw4=Get bandwidth at time... 4 'vtime' Hertz Linear
      f5=Get value at time... 5 'vtime' Hertz Linear
     bw5=Get bandwidth at time... 5 'vtime' Hertz Linear
     fileappend  /media/rakibul/WorkFolder/Work/Thesis/Speech_Recognition/Bangla_Vowel_Recognition/Using_Formant/Audio_Data/Formant/Formant'foldername'/'use_sound$'_Formant_frq.txt 'vtime:3'       'f1:2'          'f2:2'        'f3:2'         'f4:2'         'f5:2'  'newline$'    
 #    fileappend  /media/rakibul/WorkFolder/Work/Thesis/Speech Recognition/Bangla Vowel Recognition/Using Formant/data/1/'use_sound$'_Formant_bw.txt 'vtime:3'        'bw1:2'      'bw2:2'     'bw3:2'    'bw4:2'      'bw5:2'  'newline$'
endfor
Remove

select Sound 'use_sound$'
Remove
endfor
endfor

















