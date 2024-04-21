sum = 0 
shopping_dict = {
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "warzywniak": ['marchew', 'seler', 'rukola'],
}
for key, value  in shopping_dict.items():
    print(f"Idę do {key.capitalize()} i kupuję tam {[v.capitalize() for v in value ]}")
    sum = sum + len(value)    
print(f"W sumie kupuję {sum} produktów")
print("Pamiętaj, żeby wziąć razowy chleb")
print("W warzywniaku nie zapłacisz kartą")