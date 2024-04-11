def encoder(password):
    encoded = ""
    for i in password:
        encoded += encoded + str(int(i)+3)
    return encoded

def decoder(password):
    result = ""
    for i in password:
        result = result + str(int(i) - 3)
    return result

password = "12345"
print(encoder(password))
print(decoder(password))