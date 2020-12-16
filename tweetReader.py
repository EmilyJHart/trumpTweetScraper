import json
import os

# Extracts each tweet and writes it to a different file.
# Saves tweet files in folder.

# Opens file and converts it into python.
#with open('trumpTweet.json', 'r', encoding='utf8') as f:
    #data = json.load(f)

#path = input('''Type in the path where you want to create your folder 
    #(i.e. C:\\\\Users\\\\Emily Hart\\\\Desktop\\\\twintWebScraper)  ''')
#name = input('Type in the desired folder name (i.e. \\\\tweets)  ')

#newpath = path + name

# Creates new folder where all of trump's tweets will be saved.
#if not os.path.exists(newpath):
    #os.makedirs(newpath)

#i = 1

#for tweet in data['tweets']:
    #filename = 'tweet'+str(i)+'.txt'

    #file = open(os.path.join(newpath, filename), 'w', encoding='utf8')
    #content = tweet['tweet']
    #file.writelines(content + '\n')

    #file.close()
                
    #int(i)
    #i += 1

def main():
    # Extracts each tweet and writes it to a different file.
    # Saves tweet files in folder.

    # Opens file and converts it into python.
    with open('trumpTweet.json', 'r', encoding='utf8') as f:
        data = json.load(f)

    path = input('''Type in the path where you want to create your folder 
        (i.e. C:\\\\Users\\\\Emily Hart\\\\Desktop\\\\twintWebScraper)  ''')
    name = input('Type in the desired folder name (i.e. \\\\tweets)  ')

    newpath = path + name

    fileMaker(newpath, data)
    

def fileMaker(newpath, data):

    # Creates new folder where all of trump's tweets will be saved.

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    i = 1

    for tweet in data['tweets']:
        filename = 'tweet'+str(i)+'.txt'

        file = open(os.path.join(newpath, filename), 'w', encoding='utf8')
        content = tweet['tweet']
        file.writelines(content + '\n')

        file.close()
                        
        int(i)
        i += 1

main()




    

