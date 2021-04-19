import os, random, shutil

source ='D:/ANIMAL_CARE/DOG_APP/IMG-20210407T211432Z-001/IMG/dogs/train/'
destinacija="D:/ANIMAL_CARE/DOG_APP/IMG-20210407T211432Z-001/IMG/dogs/valid/"

# Definisati put. U ovom slucaju je prije 
# imena fajla 63 karaktera (koji se trebaju obrisati)
def PrintThree(string):
    return string[63:]

if __name__ == '__main__':
    for item in os.listdir(source):
        item = os.path.join(source, item)
        if os.path.isdir(item):
            folder=PrintThree(item)
            sourc =source+folder
            put_end=destinacija+folder

            if os.path.isdir(put_end)==True:
                print(folder)
                files = os.listdir(sourc)
                no_of_files = len(files) // 5  #20% od ukupnog broja slika se prebacuje u folder sa istim imenom

                for file_name in random.sample(files, no_of_files):
                    shutil.move(os.path.join(sourc, file_name), put_end)
              
        else:
            print("Unknown!")



