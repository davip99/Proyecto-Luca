class Juegos:
    
    def __init__(self, rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales):
        self.rank = rank
        self.name = name
        self.platform = platform
        self.year = year
        self.genre = genre
        self.publisher = publisher
        self.na_Sales = na_Sales
        self.eu_sales = eu_sales
        self.jp_sales = jp_sales
        self.other_sales = other_sales
        self.global_sales = global_sales

    def __str__(self):
        return f"Rank: {self.rank}, Name: {self.name}, Platform: {self.platform}, Year: {self.year}, Genre: {self.genre}, Publisher: {self.publisher}, NA_Sales: {self.na_Sales}, EU_sales: {self.eu_sales}, JP_sales: {self.jp_sales}, Other_sales: {self.other_sales}, Global_sales: {self.global_sales}"