print('''LIST OF PARTIES\n1. BJP\n2. CONGRESS\n3. AAP\n4. NOTA\n''')
party=int(input("Enter the party you want to vote for : "))

if party==1:
    print("YOU HAVE VOTED FOR BJP")
elif party==2:
    print("YOU HAVE VOTED FOR CONGRESS")
elif party==3:
    print("YOU HAVE VOTED FOR AAP")
elif party==4:
    print("YOU HAVE VOTED FOR NOTA")
else:
    print("PLEASE TRY AGAIN")