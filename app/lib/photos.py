import csv
from random import sample

class Photos:
    CSV_PATH = 'data/observations-182134.csv'

    def __init__(self):
        self.photos = {}

        with open(self.CSV_PATH) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                scientific_name = row['scientific_name'].lower()
                if scientific_name not in self.photos:
                    self.photos[scientific_name] = []
                self.photos[scientific_name].append(row['image_url'])

    def get_photos(self, scientific_name, num_photos=2):
        return sample(self.photos[scientific_name], num_photos)
