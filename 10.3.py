def create_vcard(name, phone, email, address):
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nADR:{address}\nEND:VCARD"
    
    with open(f"{name}_contact.vcf", 'w') as file:
        file.write(vcard)
    print(f"vCard for {name} created.")
name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email: ")
address = input("Enter your address: ")
create_vcard(name, phone, email, address)
