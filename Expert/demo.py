cold = ["cold","sore throat","runny nose","congestion","cough","aches"]
flu = ["flu","fever","headache","muscle aches","returning fever"]
ebola = ["ecola","tiredness","death","bruising over 90% of body","black blood"]
disease = [cold, flu, ebola]

symtoms = raw_input('Enter symtoms : ')
symtoms = symtoms.lower()
symtoms = symtoms.split(',')

f = []
def ans(dis,sym):
  for d in dis:
    for s in sym:
      if s in d:
        if d[0] not in f:
          f.append(d[0])

ans(disease, symtoms)
print f
'''
class Disease:
  def __init__(self, name, symptoms):
    self.name = name
    self.symptoms = symptoms

known_diseases = [Disease('cold', set("sore throat|runny nose|congestion|cough|aches".split("|"))), Disease('flu', set("fever|headache|muscle aches|returning fever".split("|"))), Disease('ebola', set("tiredness|death|bruising over 90% of body|black blood".split("|"))]

symptoms = raw_input("Please enter symptoms separated by commas: ")
symptoms = symptoms.lower()
symptoms = symptoms.split(",")

possible = []
for symptom in symptoms:
     for disease in known_diseases:
         if symptom in disease.symptoms:
             possible.append(disease.name)

if possible:
     print("You may have these diseases:")
     print(possible)
else:
     print("Good news! You're going to have a disease named after you!")


class Disease:
     def __init__(self, name, symptoms):
         self.name = name
         self.symptoms = symptoms


known_diseases = [
    Disease('chanyacholi', set(
        "navratri|female|monsoon".split("|"))
    ),
    Disease('sadi', set(
        "diwali|female|winter".split("|"))
    ),
    Disease('formal', set(
        "wedding|male|summer".split("|"))
    ),
]


# note: for Python 2, use "raw_input" instead of input
symptoms = input(
    "Please enter event name,gender and season separated by commas: ")

symptoms = symptoms.lower()
symptoms = symptoms.split(",")

possible = []
for symptom in symptoms:
     for disease in known_diseases:
         if symptom in disease.symptoms:
             possible.append(disease.name)

if possible:
     print("You may have these diseases:")
     print(*possible)
else:
     print("Good news! You're going to have a disease named after you!")
'''