class Film(object):
    def __init__(self, IMDb_number=None, Title=None, Also_known_as=None,
                Year=None, Duration_minutes=None, Rating=None, Format=None, I_own_this_movie=None,
                I_have_seen_this_movie=None, Loaned_out=None, Search_field=None, Trailer_URL=None, Personal_notes=None,
                 Taglines=None, Plot_outline=None, Plots=None, Languages=None, Subtitles=None, Audio=None, Video=None,
                 Country=None, Genres=None, Director=None, Writer=None, Producer=None, Music=None, Cast=None):
        self.IMDb_number = IMDb_number
        self.Title = Title
        self.Also_known_as = Also_known_as
        self.Year = Year
        self.Duration_minutes = Duration_minutes
        self.Rating = Rating
        self.Format = Format
        self.Search_field = Search_field
        self.I_own_this_movie = I_own_this_movie
        self.I_have_seen_this_movie = I_have_seen_this_movie
        self.Loaned_out = Loaned_out
        self.Trailer_URL = Trailer_URL
        self.Personal_notes = Personal_notes
        self.Taglines = Taglines
        self.Plot_outline = Plot_outline
        self.Plots = Plots
        self.Languages = Languages
        self.Subtitles = Subtitles
        self.Audio = Audio
        self.Video = Video
        self.Country = Country
        self.Genres = Genres
        self.Director = Director
        self.Writer = Writer
        self.Producer = Producer
        self.Music = Music
        self.Cast = Cast


    @classmethod
    def value_positive(cls):
        #random choose the title of films
        import random
        list_of_titles=["Snatch", "Kill Bill", "Rocky", "Devil", "Pulp fiction", "Star wars"]
        return cls(IMDb_number="0003", Title=random.choice(list_of_titles), Also_known_as="Test-information",
                   Year="2015", Duration_minutes="0000", Plots="test-test")

    @classmethod
    def value_negative(cls):
        return cls(IMDb_number="0003", Also_known_as="Test-information", Year="2015", Duration_minutes="0000",
                   Plots="test-test")

    @classmethod
    def value_search_positive(cls):
        #random choose the title of films
        import random
        #list_of_titles=["Snatch", "Kill Bill", "Rocky", "Devil", "Pulp fiction", "Star wars"]
        return cls(Search_field="Rocky")#random.choice(list_of_titles)

    @classmethod
    def value_search_negative(cls):
        return cls(Search_field="No title film")