en_pt = dict()

en_pt["hello"] = "olá"
en_pt["how"] = "como"
en_pt["create"] = "criar"
en_pt["name"] = "nome"
en_pt["keyboard"] = "teclado"
en_pt["tear"] = "chá"

print(en_pt)
print(len(en_pt))
print(en_pt["how"])
print("how" in en_pt)
print(en_pt.values())

print(en_pt.get("apple", "maçã")) # returms maçã if the key apple doesn't exist
print(en_pt)