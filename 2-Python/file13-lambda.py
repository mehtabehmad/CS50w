people = [
    {"name":"abid", "University":"LUMS"},
    {"name":"karim", "University":"NUST"},
    {"name":"nasir", "University":"UMT"},
]

# fix for the error
def f(person):
    return person['name']

people.sort(key=f)
print(people)

# instead we can have used lambad function for such a one time simple function
people.sort(key=lambda person: person['University'])
print(people)

