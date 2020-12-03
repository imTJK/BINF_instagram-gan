if __name__ == "__main__":

    import csv 

    with open("C:\\Users\\Tjorven\\Desktop\\Programmieren\\Python\\BINF_instagram-gan\\webscraping\\rnnTargets.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')