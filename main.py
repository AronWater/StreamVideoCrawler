# window use dir  
# ubuntu use cat
# discover that window cat has a limitation to the length,    so i open ubuntu termial to do that
# Current problem,   system command return 1 ,however the final video is ok, which is weird


out_file_name = "thisIStHEfINalVideo"
theurlYourCopyFromBrowser = 'https://ptz141.ust.hk/rvcprotected/mp4:19SP_ISOM3710-L1_190325_95845.mp4/media_w2113062051_5.ts?UId=kclukac&SessionId=pohiocpxptevexuu30bqard0'
file_name = '{}.ts'
index_begin = int(0)
index_end = int(1000)

import sys
import urllib.request
from os import system, remove
import re
import platform
pattern=r"_\d+.ts"    #  "+"  is1to*, "*" is0to* , "?" is 0to1
createTemplate=re.sub(pattern,"_{}.ts",theurlYourCopyFromBrowser)

file_names = []
for i in range(index_begin, index_end + 1):
    curr_file_name = file_name.format(i)
    curr_url = createTemplate.format(i)
    file_names += [curr_file_name]
    print('Downloading {} '.format(i)+"  th part of the video,  ",    index_end-i , "    more to go")
    try :
        urllib.request.urlretrieve(curr_url, curr_file_name)
    except:
        print('Except catched')
        print('end of video detected')
        break
    
print('All files downloaded')
print('Joining into a single .ts file...')

import os 
import pyperclip


command=''
for file_name in file_names:
    command += '{} '.format(file_name)

prefix= ['type' if platform.system()=='Windows' else 'cat'][0] +' '

command = prefix + command + '> {}'.format(out_file_name + '.ts')

command=command.strip()

pyperclip.copy(command)
print('cliped to clipboard')

system(command)








# print(command[-100:])


# system('ffmpeg -i {}.ts -acodec copy -vcodec copy {}.mp4'.format(out_file_name, out_file_name))
# print('Clenaing up...')
# for file_name in file_names:
#     remove(file_name)
# remove('{}.ts'.format(out_file_name))








###############################################the following is from peter


# import requests, io, re, loginCAS, os
# from bs4 import BeautifulSoup

# # def uploadToYoutube(fullPath):
# # 	os.chdir("./uploadVideo")
# # 	uploadVideo.callMain(file=fullPath, title=videoName, privacyStatus="unlisted")
# # 	os.remove(fullPath)
# # 	os.chdir("../")

# sessions=requests.Session()
# loginCAS.loginCAS(sessions)

# # Video Link File -> Playlist
# # It is done by the Linux lab machine
# videoLink="https://ptz143.ust.hk/rvcprotected/mp4:19SP_MSBD5008-L1_190319_31408.mp4/playlist.m3u8?UId=&SessionId=3maol52typiyjz52mnjysv4z"
# videoLink=videoLink.replace("wtkung","")
# videoLinkFirstPart=videoLink[:videoLink.rfind("/")+1]
# videoName=videoLink[39:videoLink.find(".",40)]

# # Playlist -> Chunklist
# playlistCode=sessions.get(videoLink).text
# playlistCodeIO=io.StringIO(playlistCode)
# for i in range(playlistCode.count("\n")):
# 	tempLine=playlistCodeIO.readline()
# 	if tempLine[0]!="#":
# 		chunklist=tempLine
# 		del tempLine
# 		break #Need this line if more efficiency is preferred

# # Chunklist -> Video Source File
# chunklistCode=sessions.get(videoLinkFirstPart+chunklist).text
# chunklistCodeIO=io.StringIO(chunklistCode)
# f=open(videoName,"wb")
# for i in range(chunklistCode.count("\n")):
# 	tempLine=chunklistCodeIO.readline()
# 	if tempLine[0]!="#":
# 		#print(sessions.get(videoLinkFirstPart+tempLine).content)
# 		f.write(sessions.get(videoLinkFirstPart+tempLine).content)
# 		print("Downloading: "+tempLine.strip())

# import requests, lxml
# from bs4 import BeautifulSoup


# def loginCAS(session):

# 	itscAccount="hahahahaha"
# 	itscPassword="hahahahahahahaha"

#     soupCode=BeautifulSoup(session.get("https://cas.ust.hk/cas/login").content,"lxml")
# 	soupCodeInputTag=soupCode.select("input")

# 	data={
# 		"username":itscAccount,
# 		"password":itscPassword,
# 		"execution":(soupCodeInputTag[0].attrs)["value"],
# 		"_eventId":"submit",
# 		"geolocation":""
# 	}

# 	session.post("https://cas.ust.hk/cas/login",data=data)
