#!/usr/bin/python
from langdetect import detect
from langdetect import detect_langs
import re

#Open files 
def openlang(filename):
  sentences=[]
  f = open(filename, 'r')
  line = f.readlines()
  for l in line:
  	l=l.replace('\r','')
  	sentences.append(l)
  f.close()
  return sentences

#Save files
def to_save(lang,name,content):
	with open(lang+name+'.txt','w') as f:
		f.write(''.join(content))
	return 1

#Make a dictionary with the pairs of English sentence and Korean sentence
def dictionary_list(list1,list2):
	d={}
	for num in range(len(list1)):
		d[list1[num]]=list2[num]
	return d 

#Picking Korean sentences that have more than 50%,
#and English sentences that are pair to Korean sentences
def lang_detecting(d):
	k=[]
	e=[]
	diction={}
	for i in d.keys():
		try:
			bef_s=detect_langs(i)
			for x in bef_s:
				lang=(str(x))[0:2]
				percent=(str(x))[3:]
				diction[lang]=percent
				for lang_ in diction.keys():
					if lang_ == 'ko' and float(diction[lang_])>=0.5:
						k.append(i)
						e.append(d[i])
				diction={}
		except: print("error",i)
	d2=dictionary_list(e,k)
	return d2

#Picking English sentences that have more than 50%, 
#and Korean sentences that are pair to English sentences.
def lang_detecting2(d):
	k=[]
	diction={}
	for i in d.keys():
		try:
			bef_s=detect_langs(i)
			for x in bef_s:
				lang=(str(x))[0:2]
				percent=(str(x))[3:]
				diction[lang]=percent
				for lang_ in diction.keys():
					if lang_ == 'en' and float(diction[lang_])>=0.5:
						e.append(i)
						k.append(d[i])
				diction={}
		except: print("error",i)

	d2=dictionary_list(k,e)
	return d2

e_list=openlang('e_r.txt')
k_list=openlang('k_r.txt')
print(len(e_list),len(k_list))
d=dictionary_list(e_list,k_list)
d2=lang_detecting2(d)
print(len(d2))
to_save('k','_detect_1',d2.keys())
to_save('e','_detect_1',d2.values())
d3=lang_detecting(d2)
print(len(d3))
to_save('e','_detect_2',d3.keys())
to_save('k','_detect_2',d3.values())
