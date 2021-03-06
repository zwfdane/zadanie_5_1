""" Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: pierwsza (BaseContact) powinna przechowywać podstawowe dane kontaktowe 
    takie jak imię, nazwisko, telefon, adres e-mail. Za pomocą kolejnej klasy
    (BusinessContact) rozszerz klasę bazową o przechowywanie informacji związanych z pracą danej osoby – stanowisko, nazwa firmy, telefon służbowy.
    Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci “Wybieram numer +48 123456789 i dzwonię do Jan Kowalski”.
    Wizytówka firmowa powinna wybierać służbowy numer telefonu, a wizytówka bazowa prywatny.
    Oba typy wizytówek powinny mieć dynamiczny atrybut label_length, który zwraca długość imienia i nazwiska danej osoby.
    Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. Niech ta funkcja przyjmuje dwa parametry: rodzaj wizytówki oraz ilość. 
    Wykorzystaj bibliotekę faker do generowania danych."""
    

class BaseContact:
   def __init__(self, first_name, last_name, phone, e_mail):
       self.first_name = first_name
       self.last_name = last_name
       self.phone = phone
       self.e_mail = e_mail
   # Nie jest potrzebne
   def __repr__(self):  
       return f"BaseContact({self.first_name} {self.last_name} {self.phone} {self.e_mail})"  
   # Nie jest potrzebne
   def __str__(self): 
       return f'{self.first_name} {self.last_name} {self.phone} {self.e_mail}' 
   def contact(self):
       return print(f' Wybieram {self.phone} i kontaktuję się z {self.first_name} {self.last_name}.')  
   @property
   def label_length(self):
       return len(self.first_name+self.last_name)

class BusinessContact(BaseContact):
    def __init__(self, company, position, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.business_phone = business_phone
    # Nie jest potrzebne
    def __str__(self): 
       return f'{self.company} {self.position} {self.business_phone}'  
    # Nie jest potrzebne 
    def __repr__(self):  
       return f"BusinessContact({self.first_name} {self.last_name} {self.phone} {self.e_mail})"     
    def contact(self):
         return print(f' Wybieram {self.business_phone} i kontaktuję się z {self.first_name} {self.last_name}.')  

def create_contacts(type,amount):
    from faker import Faker
    fake = Faker()
    # lists of random bussiness cards
    rbc_list = [] 
    if type == "bc":
        for i in range(amount):
            bc = BaseContact(first_name = fake.first_name(), last_name=fake.last_name(), phone=fake.phone_number(), e_mail = fake.ascii_email())
            rbc_list.append(bc)
    if type == "bbc":
        for i in range(amount):
            bc = BusinessContact(first_name = fake.first_name(), last_name=fake.last_name(), phone=fake.phone_number(), e_mail = fake.ascii_email(), 
            company = fake.company(), position = fake.job(), business_phone=fake.phone_number())
            rbc_list.append(bc)
    return rbc_list
if __name__ == "__main__":
    # Testujemy kontakt podstawowy
    bc = BaseContact(first_name = "Bolesław", last_name="Michalski", e_mail = "BoleslawMichalski@jourrapide.com", phone="+48123456788")
    BaseContact.contact(bc)
    # Testujemy kontakt biznesowy
    bcc = BusinessContact(first_name = "Bolesław", last_name = "Michalski", e_mail = "BoleslawMichalski@jourrapide.com", phone="+48123456788", 
      company="Vibrant Man", position = "Boilermaker",business_phone="+48999999999")    
    BusinessContact.contact(bcc)
    # Testujemy create.contacts()
    created_contacts = create_contacts("bc",10)
    for create_contact in created_contacts:
        print(f"{create_contact}")
        print(f"Łączna ilość znaków imienia i nazwiska wynosi (bez spacji): {create_contact.label_length}\n" )
    created_b_contacts = create_contacts("bc",10)
    for create_b_contact in created_b_contacts:
        print(f"{create_b_contact}")
        print(f"Łączna ilość znaków imienia i nazwiska wynosi (bez spacji): {create_b_contact.label_length}\n" )




