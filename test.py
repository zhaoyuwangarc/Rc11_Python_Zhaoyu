import csv

with open("C:/Users/zhaoyu/Desktop/Rc11/GithubDrive/collection/Artworks.csv", encoding='utf-8-sig') as artFile:
    artReader = csv.DictReader(artFile)
    Line1 = next(artReader)
    print(Line1["Artist"])
