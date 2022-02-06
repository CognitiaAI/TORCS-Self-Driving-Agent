from bs4 import BeautifulSoup
import os
import subprocess
import copy

def open_xml():
    f = open(data_gen_path + 'temp.xml','r')
    bs = BeautifulSoup(f.read(),'xml')
    f.close()
    return bs

def write_xml(bs):
    f = open(data_gen_path + 'temp.xml','w')
    f.write(bs.prettify())
    f.close()

def display_xml():
    bs = open_xml()
    print (bs.find('section',{'name':'Tracks'}))
    print (bs.find('section',{'name':'Drivers'}))

def swap_and_write(currentIdx):
    bs = open_xml()
    current = bs.find('section',{'name':'Drivers'}).find('section',{'name':str(currentIdx)})
    nxt = bs.find('section',{'name':'Drivers'}).find('section',{'name':str(currentIdx+1)})
    
    tmp = copy.deepcopy(current)
    current = copy.deepcopy(nxt)
    nxt = tmp
    
    tmp2 = copy.deepcopy(current['name'])
    current['name'] = copy.deepcopy(nxt['name'])
    nxt['name'] = tmp2
    
    bs.find('section',{'name':'Drivers'}).find('section',{'name':str(currentIdx)}).replaceWith(current)
    bs.find('section',{'name':'Drivers'}).find('section',{'name':str(currentIdx+1)}).replaceWith(nxt)
    
    write_xml(bs)



if __name__ == "__main__":
    server_path = '..\\torcs_server'
    os.chdir(server_path)
    data_gen_path = '..\\data_generation\\'
    display_xml()
    categories = ['road', 'dirt', 'oval']
    mod_num = 0
    lastTrack = 'aalborg'

    for i,category in enumerate(categories):
        print ('Category:',category)
        if i > 0:
            bs = open_xml()
            category_name = bs.find(val=categories[i-1])
            category_name['val'] = category
            write_xml(bs)
            display_xml()
        tracks = sorted(os.listdir(r'.\\tracks\\'+category))
        print("Tracks: ", tracks)
        if category == 'road':
            tracks.remove('e-track-1')
            tracks.remove('e-track-2')
        for j,track in enumerate(tracks):
            currentIdx = 1
            print ('Track:',track)
            bs = open_xml()
            track_name = bs.find(val=lastTrack)
            track_name['val'] = track
            toWrite = bs.prettify()
            write_xml(bs)
            display_xml()
            lastTrack = track
            for race_num in range(1,31):
                print ('Race Number:',race_num)
                if (race_num) % 5 == 0:
                    swap_and_write(currentIdx)
                    currentIdx += 1
                    display_xml()
                subprocess.call(['wtorcs.exe', '-r', 
                                '..\\data_generation\\temp.xml'])
                if race_num == 30:
                    f = open(data_gen_path + 'temp.xml','w')
                    f.write(toWrite)
                    f.close()