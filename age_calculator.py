import datetime

def main():
    try:
        birth_year = int(input("Entre l'année de naissance: "))
        jour = int(input("Entre le jour de naissance: "))
        mois = int(input("Entre mois de naissance: "))

        current_year = datetime.date.today().year 
        current_day = datetime.date.today().day 
        current_month = datetime.date.today().month

        age = current_year - birth_year 

        

        print("--------------------")
        print(f"Current Year: {current_year}")
        print(f"You are approximately {age} years old.")
        
        if current_month  == mois and current_day == jour:
            print("Joyeux anniversaire bro")
        else:
            print("courage mon frere, l'anniv va arriver very soon")
    except Exception as e:
        print("donne une date en chiffre stp ex:(2000)")

if __name__ == "__main__":
    main()
