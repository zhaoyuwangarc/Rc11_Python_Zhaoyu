import csv
import requests
from PIL import Image
from io import BytesIO


class ArtTate:
    def __init__(self, id, width, depth, height, imageUrl, artist):
        self.id = id
        self.width = width
        self.depth = depth
        self.height = height
        self.imageUrl = imageUrl
        self.artist = artist
        self.imagePath = ''

    def describe(self):
        print("artist:" + self.artist, "id:" + self.id, "width:" + str(self.width),
              "depth:" + str(self.depth), "height:" + str(self.height))

    def getImageFile(self):
        if self.imageUrl:
            response = requests.get(self.imageUrl)
            try:
                im = Image.open(BytesIO(response.content))
            except OSError:
                return None
            path = "C:/Users/zhaoyu/Desktop/Rc11/GithubDrive/Assignment/TateImages/" + self.artist + ".jpg"
            self.imagePath = path
            im.save(path, "JPEG")


artPieces = []
with open("C:/Users/zhaoyu/Desktop/Rc11/GithubDrive/collection/Artwork_data.csv", encoding='utf-8-sig') as artFile:
    artReader = csv.DictReader(artFile)

    for row in artReader:
        id = row['id']
        width = row['width']
        height = row['height']
        depth = row['depth']
        imageUrl = row['thumbnailUrl']
        artist = row['artist']
        if width or depth or height:
            artPiece = ArtTate(id, width, depth, height, imageUrl, artist)
            artPieces.append(artPiece)

for art in artPieces:
    if "Charlton, Alan" in art.artist:
        art.getImageFile()
