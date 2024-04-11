def encoder(password):
    encoded = ""
    for i in password:
        encoded += encoded + str(int(i)+3)
    return encoded

def decoder(password):
    decoded = ""
    for i in password:
        decoded += decoded + str(int(i) - 3)
    return decoded