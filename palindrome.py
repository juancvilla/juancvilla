def is_palindrome(cadena):
    cadena = cadena.lower()
    cadena2 = ""
    for x in range(len(cadena)):
        cadena2+=cadena[-x-1]
    return cadena == cadena2
print(is_palindrome("otto"))
print("-")
def is_palindrome2(cadena):
    cadena = cadena.lower()
    return cadena == cadena[::-1]
print(is_palindrome2("ana"))
print("-")
def is_palindrome3(cadena):
    cadena = cadena.lower()
    return cadena == "".join(reversed(cadena))
print(is_palindrome3("ana"))
