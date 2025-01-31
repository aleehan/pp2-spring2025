def single(list):
    for movie in list:
        for char in movie.items():
            if char[0] == "imdb" and char[1] > 5.5:
                print(movie["name"], True)

def much(list):
    top = []
    for movie in list:
        for char in movie.items():
            if char[0] == "imdb" and char[1] > 5.5:
                top.append(movie["name"])
    return top

def cat(list, category):
    for movie in list:
        for char in movie.items():
            if char[0] == "category" and char[1] == category:
                print(movie["name"])

def aver(list):
    avg = 0
    for movie in list:
        for char in movie.items():
            if char[0] == "imdb":
                avg = avg + char[1]
    return avg/len(list)

def catavg(list, category):
    avg, amount = 0, 0
    for movie in list:
        for char in movie.items():
            if char[0] == "category" and char[1] == category:
                    avg = avg + movie["imdb"]
                    amount+=1
    return avg/amount

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]