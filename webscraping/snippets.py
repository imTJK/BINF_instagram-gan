import json
from os import walk
import os

def csvToText(path, pathOut):
    import csv 

    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        with open(pathOut, 'r+') as txt:
            for row in reader:
                txt.write(str(row['username'] + ','))


def normalizeFolder(path):
    (_,_,filenames) = walk(path).__next__()

    for file in filenames:
        fpath = path + file
        if os.path.exists(fpath):
            if ".mp4" in fpath:
                print("\n removed {}".format(file))
                os.remove(fpath)
            elif ".json" in fpath:
                os.rename(fpath, path + "metadata\\" + file)

def normalize_json(path):
    (_,_,filenames) = walk(path).__next__()

    user =  {'username': "",
            'posts':
                [{
                    'image_path' : '',
                    'caption' : '',
                    'likes' : 0,
                    'comments' : 0
                }]
            }

    def list_contains(list, word):
        for x in list:
            if str(x) == word:
                return True
        return False


    save_path = "C:\\Users\\Tjorven\\Desktop\\Programmieren\\Python\\BINF_instagram-gan\\webscraping\\scraped-posts\\metadata\\json-posts"
    for file in filenames: 
            fpath = path + file
            if os.path.exists(fpath):
                with open(fpath, 'r', encoding="utf-8") as f:
                    metadata = json.load(f)
                    user['username'] = fpath.split('metadata\\')[1].split('.json')[0]


                    for post in metadata['GraphImages']:    
                        if post['__typename'] != "GraphVideo":
                            image_path = ''
                            for x in str(post['display_url']).split('/'):
                                if len(x) > 50:
                                    image_path = 'C:\\Users\\Tjorven\Desktop\\Programmieren\\Python\\BINF_instagram-gan\\webscraping\\scraped-posts\\' + x.split('?_nc')[0]

                            caption = post['edge_media_to_caption']['edges'][0]['node']['text'] if len(post['edge_media_to_caption']['edges']) > 0 else 'empty'
                        
                            user['posts'].append({
                                'images' :  image_path,
                                'caption' : caption,
                                'likes' : post['edge_media_preview_like']['count'],
                                })

                            print(image_path)

                    f.close()

                    file = open(save_path + user['username'] + '.json', 'w') 
                    json.dump(user, file, indent=4)
                    f.close()


                    

if __name__ == "__main__":
    path = r"C:\Users\Tjorven\Desktop\Programmieren\Python\BINF_instagram-gan\webscraping\scraped-posts\\"
    
    normalizeFolder(path)
    normalize_json(path)