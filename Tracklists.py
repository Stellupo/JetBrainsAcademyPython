def tracklist(**kwargs):
    for key in kwargs:
        print(key)
        for item in kwargs[key].items():
            print('ALBUM:', item[0], 'TRACK:', item[1], )


tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
                      "On the Other Side": "Samara"},
          "Cure": {"Disintegration": "Lovesong",
                   "Wish": "Friday I'm in love",
                   "Seventeen Seconds": "A Forest"}}
tracklist(**tracks)
