def verschiebung(zeichen: str, schluessel: int):
    zahl = ord(zeichen)
    range = 90 - zahl
    if schluessel - range > 0:
        zahl = 64
        schluessel = schluessel - range
    neueZahl = zahl + schluessel 
    neuesZeichen = chr(neueZahl)
    return neuesZeichen

def verschiebungGrossKlein(zeichen: str, schluessel: int):
    result = ""
    if (zeichen.isupper()):
         result += chr((ord(zeichen) + schluessel-65) % 26 + 65)
    else:
         result += chr((ord(zeichen) + schluessel - 97) % 26 + 97)
    return result

def verschiebungZurückGrossKlein(zeichen: str, schluessel: int):
    result = ""
    if (zeichen.isupper()):
         result += chr((ord(zeichen) - schluessel-65) % 26 + 65)
    else:
         result += chr((ord(zeichen) - schluessel - 97) % 26 + 97)
    return result

def encrypt(text: str, schluessel: int):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += verschiebungGrossKlein(char, schluessel)
    return result

def decrypt(text: str, schluessel: int):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += verschiebungZurückGrossKlein(char, schluessel)
    return result

# Funktionsaufrufe
text = input("Ein Wort eingeben: ")
text = str(text)
schluessel = input("Geben Sie einen Schlüssel ein: ")
schluessel = int(schluessel)

encryptedText = encrypt(text, schluessel)
print(encryptedText)
decryptedText = decrypt(encryptedText, schluessel)
print(decryptedText)