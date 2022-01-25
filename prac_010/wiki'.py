import wikipedia

content = wikipedia.search("Monty")
wikipedia.summary("Monty")
try:
    monty = wikipedia.summary("Monty")
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)

monty = wikipedia.page("Monty")
print(monty.title)
print(monty.summary)
print(monty.url)