#9) while ციკლისა და input-ის საშვალებით მომხარებელს შემოატანინეთ პაროლი სანამ არ იქნება ის "ემი რაზმი"-ის ტოლი.

password = "ჩემი რაზმი"

Password = input("enter your password:")

if Password == password:
    print("your password is correct")

elif Password != password:
    print("your password is incorrect.")