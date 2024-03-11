from abc import ABC, abstractmethod
import pandas as pd

account=pd.read_csv("accounts_info.csv")
car_urg_deliv=pd.read_csv("car_urg_deliv.csv")
car_rental=pd.read_csv("car_rental.csv")
car_booking=pd.read_csv("car_booking.csv")
car_sale=pd.read_csv("car_sale.csv")





class personal_info():
    def __init__(self):
        while True:
            t = True
            
            while True:
                try:
                    self.Name = str(input("Enter your name: "))
                    x = isinstance(self.Name, str)
                    break
                except:
                    print("Wrong datatype, Try again! ")
                    pass

            while True:
                try:
                    self.Age = eval(input("Enter your age: "))
                    break
                except:
                    print("Wrong datatype, Try again! ")    
    
            while True:
                self.Email = input("Enter your Email: ")
                self.same_Email = account[account['Email'] == self.Email]
                if self.same_Email.empty == False:
                    print("Email already exists, please try again. ")
                else:
                    break
            while True:
                self.Phone_no = input("Enter your Contact Number: ")
                if self.Phone_no[0] == "0":
                    break
                else:
                    print("Try again! ")
            self.City= input("Enter the name of your city: ")
            self.Password=input("Set a strong password: ")
            
            account_dict = {'Name': self.Name , 'Age': self.Age , 'Email': self.Email,
            "Phone number": self.Phone_no, "City": self.City , 'Password' : self.Password}        
            account.loc[len(account)] = account_dict
            account.to_csv("accounts_info.csv", index=False)
            print("---------------------------")
            print("    ~ ACCOUNT CREATED ~ ")
            print("---------------------------")
            break


class main_interface():
    def call(self):
        outer_most_loop =True
        while outer_most_loop:
            print("---------------------------")
            print("|  ACCOUNT REG INTERFACE  |")
            print("---------------------------")
            print("| Already have an account?|")
            print("|     Login       [y]     | \n|     Register    [n]     | \n|     Don't Login [l]     | ")
            print("---------------------------")  
            acc_choice=input("Enter your choice: ")
            print("---------------------------")
            infinite_loop = True
            while infinite_loop:
                
                if acc_choice.lower() == 'y':
                    email_choice = input("|How do you want to login?| \n|     Email       [y]     | \n|     Contact No. [l]     | \n--------------------------- \nEnter your choice: ")
                    print("---------------------------")
                    
                    if email_choice.lower() == "y":
                        checkEmail = input("Email:\n    ") 
                        checkPassword = input("--------------------------- \nPassword:\n     ")              #To check match the password and email of a specific row
                         
                        Emailcheck = account[account['Email'] == checkEmail]        #At this time it is randomnly checking the pass and email of random rows
                        passcheck = Emailcheck[Emailcheck['Password'] == checkPassword]
                        if Emailcheck.empty | passcheck.empty:
                            print("Account not found / Incorrect Email OR Password !")
                            acc_choice= input("Try again [y] / Register Now [n] / Don't Login [l] :")
                            
                            if acc_choice.lower() == "y":
                                pass
                            
                            elif acc_choice.lower() == "n":
                                info = personal_info()
                                self.logged_in = "True"
                                outer_most_loop = False
                                
                                break
                            
                            elif acc_choice.lower() == "l":
                                self.logged_in = "False"
                                infinite_loop = False
                                outer_most_loop = False
                                
                            else:
                                print("Invalid Option ! ")
                        
                        elif not( passcheck.empty & Emailcheck.empty):
                            print("---------------------------")
                            print("       ~ LOGGED IN ~       ")
                            print("---------------------------")
                            self.logged_in = "True"
                            infinite_loop = False
                            outer_most_loop = False

                        else:
                            pass

                    elif email_choice.lower() == "l":
                        checkConntact = int(input("Enter your Contact Number: ")) 
                        checkPassword = input("Enter your Password: ")

                        contactcheck = account[account['Phone number'] == checkConntact]
                        passcheck = contactcheck[contactcheck['Password'] == checkPassword]
                        #To check match the password and email of a specific row
                        if contactcheck.empty | passcheck.empty:
                            print("Account not found / Incorrect Email OR Password !")
                            acc_choice= input("Try again [y] / Register Now [n] / Don't Login [l] :")
                            
                            if acc_choice.lower() == "y":
                                pass
                            
                            elif acc_choice.lower() == "n":
                                info = personal_info()
                                self.logged_in = "True"
                                outer_most_loop = False
                                
                                break
                            
                            elif acc_choice.lower() == "l":
                                self.logged_in = "False"
                                infinite_loop = False
                                outer_most_loop = False
                                
                            else:
                                print("Invalid Option ! ")
                                self.logged_in = "False"
                        elif not( passcheck.empty & contactcheck.empty):
                            game = "True"
                            print("---------------------------")
                            print("       ~ LOGGED IN ~       ")
                            print("---------------------------")
                            self.logged_in = "True"
                            infinite_loop = False
                            outer_most_loop = False

                        else:
                            pass
                    
                    else:
                        print("Wrong option")
                    

                elif acc_choice.lower() == 'n':
                    info = personal_info()
                    print("---------------------------")
                    print("       ~ LOGGED IN ~       ")
                    print("---------------------------")
                    infinite_loop = False
                    outer_most_loop = False
                    self.logged_in = "True"
                    break

                elif acc_choice.lower() == 'l':
                    self.logged_in = "False"
                    infinite_loop = False
                    outer_most_loop = False
                    
                else:
                    print("---------------------------")
                    print("The option doesn't exists ! ")
                    print("---------------------------")
                    self.logged_in = "False"
                    infinite_loop=False


                    
class delivery(ABC):
   
        @abstractmethod
        def printing():
            pass
        @abstractmethod
        def calculate():
            pass
        @abstractmethod
        def final_price():
             pass

class urg_class():

        def __init__(self):
                print("_______________________________________________________")
                print("             U R G E N T   D E L I V E R Y :   ")
                print(car_urg_deliv)
                print("_______________________________________________________")
                search_choice = int(input("Please select a search method : \nVehicle Name [1] \nVehicle ID [2] \n=  "))
                outer_loop = True
                while outer_loop:
                    if search_choice == 1:
                        loop1=True
                        while loop1:
                            self.choiceurg = input("Search By Vehicle Name : ")
                            self.output = car_urg_deliv[car_urg_deliv['Vehicle Name'] == self.choiceurg]

                            if  self.output.empty: 
                                error = input("Name not found! Do you want to search again?:[y/n] ")
                                if error.lower() == 'y':
                                    pass
                                
                                elif error.lower() == 'n':
                                    loop1 = False
                                    outer_loop = False

                                else:
                                    print("Invalid Option !")
                                    break 
                                    
                            else:
                                print("____________________________________________________")
                                print(self.output)
                                print("____________________________________________________")
                                if self.output[self.output['Status'] == "Avaliable"].empty:
                                    print("We are extremely sorry for this unconvenience, This model is currently unavaliable.")
                                else:                         
                                    avaliablity=urgent_class()
                                    avaliablity.printing(self)
                                    avaliablity.calculate()
                                    avaliablity.final_price()
                                loop1 = False
                                outer_loop = False

                    
                                                
                    elif search_choice == 2:
                        loop1=True
                        while loop1:
                            #Exceptional handling
                            while True:
                                try:
                                    self.choiceurg = int(input("Search By Vehicle ID : "))
                                    break
                                except:
                                    print("Invalid datatype, Kindly enter a valid datatype ")
                            
                            self.output = car_urg_deliv[car_urg_deliv['Vehicle ID'] == self.choiceurg]

                            if  self.output.empty: 
                                error = input("ID not found! Do you want to search again?:[y/n] ")
                                if error.lower() == 'y':
                                    pass
                                
                                elif error.lower() == 'n':
                                    loop1 = False
                                    outer_loop = False

                                else:
                                    print("Invalid Option !")
                                    break 
                                    
                            else:
                                print("____________________________________________________")
                                print(self.output)
                                print("____________________________________________________")
                                if self.output[self.output['Status'] == "Avaliable"].empty:
                                    print("We are extremely sorry for this unconvenience, This model is currently unavaliable.")
                                else:                         
                                    avaliablity=urgent_class()
                                    avaliablity.printing(self)
                                    avaliablity.calculate()
                                    avaliablity.final_price()
                                    loop1 = False
                                    outer_loop = False

                    else:
                        print("Invalid Option ! ")
                        outer_loop = False

class urgent_class(delivery):
        
        def printing(self,obj):
                self.urgent_price=int(obj.output["Price"])
                self.urgent_tax=int(self.urgent_price*0.17)
                self.urg_final_price=0

                print("The actual amount is= ", int(self.urgent_price))
                print("The Tax amount is= ", int(self.urgent_tax))
        
        def calculate(self):
                self.urg_final_price= int(self.urgent_price) + int(self.urgent_tax)
        
        def final_price(self):
                print("The Final Amount to be paid is= ", int(self.urg_final_price))



class book_class():

        def __init__(self):
                print("____________________________________________________________________________")
                print("               B O O K I N G   T A B L E  :   ")
                print(car_booking)
                print("____________________________________________________________________________")
                search_choice = int(input("Please select a search method : \nVehicle Name [1] \nVehicle ID [2] \n=  "))
                outer_loop = True
                while outer_loop:
                    if search_choice == 1:
                        loop1=True
                        while loop1:
                            while True:
                                self.choicebook = str(input("Search By Vehicle Name : "))
                            excepy
                            self.output = car_booking[car_booking['Vehicle Name'] == self.choicebook]

                            if  self.output.empty: 
                                error = input("Name not found! Do you want to search again?:[y/n] ")
                                if error.lower() == 'y':
                                    pass
                                
                                elif error.lower() == 'n':
                                    loop1 = False
                                    outer_loop = False

                                else:
                                    print("Invalid Option !")
                                    break 
                                    
                            else:
                                print("____________________________________________________________________________")
                                print(self.output)
                                print("____________________________________________________________________________")
                                if self.output[self.output['Status'] == "Avaliable"].empty:
                                    print("We are extremely sorry for this unconvenience, This model is currently unavaliable.")
                                else:                         
                                    avaliablity=booking_class()
                                    avaliablity.printing(self)
                                    avaliablity.calculate()
                                    avaliablity.final_price()  
                                
                                loop1 = False
                                outer_loop = False

                    
                                                
                    elif search_choice == 2:
                        loop1=True
                        while loop1:
                            while True:
                                try:
                                    self.choicebook = int(input("Search By Vehicle ID : "))
                                    break
                                except:
                                    print("Invalid datatype, Kindly enter a valid datatype ")
                            
                            self.output = car_booking[car_booking['Vehicle ID'] == self.choicebook]

                            if  self.output.empty: 
                                error = input("ID not found! Do you want to search again?:[y/n] ")
                                if error.lower() == 'y':
                                    pass
                                
                                elif error.lower() == 'n':
                                    loop1 = False
                                    outer_loop = False

                                else:
                                    print("Invalid Option !")
                                    break 
                                    
                            else:
                                print("____________________________________________________________________________")
                                print(self.output)
                                print("____________________________________________________________________________")
                                if self.output[self.output['Status'] == "Avaliable"].empty:
                                    print("We are extremely sorry for this unconvenience, This model is currently unavaliable.")
                                else:                         
                                    avaliablity=booking_class()
                                    avaliablity.printing(self)
                                    avaliablity.calculate()
                                    avaliablity.final_price()  

                                    loop1 = False
                                    outer_loop = False

                    else:
                        self.output = car_booking[car_booking['Vehicle ID'] == None]
                        print("Invalid Option ! ")
                        outer_loop = False
        def checking_avaliablity(self):
            
                    self.status=None

                    if self.output[self.output['Status'] == "Avaliable"].empty:
                        print("We are extremely sorry for this inconvenience, This model is currently unavaliable.")
                    else:
                        avaliablity=booking_class()
                        avaliablity.printing(self)
                        avaliablity.calculate()
                        avaliablity.final_price()




class booking_class(delivery):

        def printing(self,obj):
            self.booking_price = int(obj.output["Price"])
            self.booking_tax = int(self.booking_price*0.17)
            self.booking_final_price = 0
            self.delivery_time =  int(obj.output['Delivery time(Days)'])

            print("The actual amount is = ", int(self.booking_price))
            print("The Tax amount is = ", int(self.booking_tax))
        
        def calculate(self):
            self.booking_final_price = self.booking_price + self.booking_tax
        
        def final_price(self):
            print("The Final Amount to be paid is = ", int(self.booking_final_price))
            print("Your car will be delivered in ",int(self.delivery_time)," days.")


class rent_class():

        def __init__(self):
                print("________________________________________________________")
                print("                R E N T A L    T A B L E  :    ")
                print(car_rental)
                print("________________________________________________________")
                search_choice = int(input("Please select a search method : \nVehicle Name [1] \nVehicle ID [2] \n=  "))
                outer_loop = True
                while outer_loop:
                    if search_choice == 1:
                        loop1=True
                        while loop1:
                            self.choicerental = input("Search By Vehicle Name : ")
                            self.output = car_rental[car_rental['Vehicle Name'] == self.choicerental]

                            if  self.output.empty: 
                                error = input("Name not found! Do you want to search again?:[y/n] ")
                                if error.lower() == 'y':
                                    pass
                                
                                elif error.lower() == 'n':
                                    loop1 = False
                                    outer_loop = False

                                else:
                                    print("Invalid Option !")
                                    break 
                                    
                            else:
                                print("________________________________________________________")
                                print(self.output)
                                print("________________________________________________________")
                                if self.output[self.output['Status'] == "Avaliable"].empty:
                                    print("We are extremely sorry for this inconvenience, This model is currently unavaliable.")
                                else:                 
                                    avaliablity=Rental_class()
                                    avaliablity.printing(self)
                                    avaliablity.calculate()
                                    avaliablity.final_price()

                                    loop1 = False
                                    outer_loop = False

                    
                                                
                    elif search_choice == 2:
                        loop1=True
                        while loop1:
                            while True:
                                try:
                                    self.choicerental = int(input("Search By Vehicle ID : "))
                                    break            
                                except:                        
                                    print("Invalid datatype, Kindly enter a valid datatype ")
                            self.output = car_rental[car_rental['Vehicle ID'] == self.choicerental]

                            if  self.output.empty: 
                                error = input("ID not found! Do you want to search again?:[y/n] ")
                                if error.lower() == 'y':
                                    pass
                                
                                elif error.lower() == 'n':
                                    loop1 = False
                                    outer_loop = False

                                else:
                                    print("Invalid Option !")
                                    break 
                                    
                            else:
                                print("________________________________________________________")
                                print(self.output)
                                print("________________________________________________________")
                                if self.output[self.output['Status'] == "Avaliable"].empty:
                                    print("We are extremely sorry for this inconvenience, This model is currently unavaliable.")
                                else:                 
                                    avaliablity=Rental_class()
                                    avaliablity.printing(self)
                                    avaliablity.calculate()
                                    avaliablity.final_price()

                                loop1 = False
                                outer_loop = False

                    else:
                        self.output = car_rental[car_rental['Vehicle ID'] == None]
                        print("Invalid Option ! ")
                        outer_loop = False
class Rental_class(delivery):
        
        def printing(self,obj):
                self.rental_price=obj.output["Price"]
                
                self.days = eval(input("For how many days do you want the car for rent: "))
                self.rental_final_price=0

                print("The rent per day is = ", int(self.rental_price))
        
        def calculate(self):
                self.rental_final_price= self.rental_price * self.days
        
        def final_price(self):
                print("The Final Amount to be paid is = ", int(self.rental_final_price),"Ruppes")


class car_Sale():

    def __init__(self):
        print("________________________________________________________")
        print("     WE WILL ONLY BE BUYING THE CARS LISTED BELOW ")
        print(car_sale)
        print("________________________________________________________")
        loop = True
        while loop:
            self.search_choice = input("Which car do you want to sell: ")
            self.output = car_sale[car_sale['Vehicle Name'] == self.search_choice]

            if  self.output.empty: 
                error = input("Name not found! Do you want to search again?:[y/n] ")
                if error.lower() == 'y':
                    pass
                        
                elif error.lower() == 'n':
                    loop = False

                else:
                    print("Invalid Option !")
                            
            else:
                print("________________________________________________________")
                print(self.output)
                print("________________________________________________________")
                loop = False
                self.condition = eval(input("Enter the condition of the car: "))

                x = int(self.output["Price"])
                if self.condition == 10:
                    print("We are intrested to buy this vehicle in",int(x),"Ruppes.")
                    print("________________________________________________________")
                    while True:
                        try:
                            self.Phone_no = eval(input("Enter your Contact Number with country code: +"))
                            break
                        except:
                            print("Invalid datatype, Kindly enter a valid datatype ")
            
                    print("Inspection team has been informed ! \nThey will contact on", self.Phone_no ,"in 2 to 3 working days. ")
                    
                elif self.condition == 9:
                    print("We are intrested to buy this vehicle in",int(x-(0.1*x)),"Ruppes.")
                    print("________________________________________________________")
                    while True:
                        try:
                            self.Phone_no = eval(input("Enter your Contact Number with country code: +"))
                            break
                        except:
                            print("Invalid datatype, Kindly enter a valid datatype ")
            
                    print("Inspection team has been informed ! \nThey will contact on", self.Phone_no ,"in 2 to 3 working days. ")

                elif self.condition == 8:
                    print("We are intrested to buy this vehicle in",int(x-(0.2*x)),"Ruppes.")
                    print("________________________________________________________")
                    while True:
                        try:
                            self.Phone_no = eval(input("Enter your Contact Number with country code: +"))
                            break
                        except:
                            print("Invalid datatype, Kindly enter a valid datatype ")
            
                    print("Inspection team has been informed ! \nThey will contact on", self.Phone_no ,"in 2 to 3 working days. ")

                elif self.condition == 7:
                    print("We are intrested to buy this vehicle in",int(x-(0.3*x)),"Ruppes.")
                    print("________________________________________________________")
                    while True:
                        try:
                            self.Phone_no = eval(input("Enter your Contact Number with country code: +"))
                            break
                        except:
                            print("Invalid datatype, Kindly enter a valid datatype ")
            
                    print("Inspection team has been informed ! \nThey will contact on", self.Phone_no ,"in 2 to 3 working days. ")

                elif self.condition == 6:
                    print("We are intrested to buy this vehicle in",int(x-(0.4*x)),"Ruppes.")
                    print("________________________________________________________")
                    while True:
                        try:
                            self.Phone_no = eval(input("Enter your Contact Number with country code: +"))
                            break
                        except:
                            print("Invalid datatype, Kindly enter a valid datatype ")
            
                    print("Inspection team has been informed ! \nThey will contact on", self.Phone_no ,"in 2 to 3 working days. ")
                
                elif self.condition < 6:
                    print("Khalas itla barra we won't buy your garbage. Visit again soon :)")


cl = main_interface()
cl.call()

class choice():
    loop = True
    while loop:

        print("---------------------------")
        print("|     S H O W R O O M     |")
        print("---------------------------")
        print("1.Car Purchase")
        print("2.Car Rent Service")
        print("3.Car sale")
        print("4.Exit")
        print("---------------------------")
        while True:
            try:
                choice=eval(input("Enter your choice: "))
                break
            except:
                print("Invalid datatype, Kindly enter a valid datatype ")
        print("---------------------------")        

        if choice == 1:
            inner_loop = True
            while inner_loop:
                print("For Urgent Delivery [d] ")
                print("For Booking [b] ")
                print("---------------------------")
                choice2=input("Enter your choice: ")
                print("---------------------------")
                if choice2.lower() == "d":

                    urgent=urg_class()
                    # urgent.checking_avaliablity()
                    inner_loop = False

                
                elif choice2.lower() == "b":
                    urgent=book_class()
                    # urgent.checking_avaliablity()
                    inner_loop = False
                
                else:
                    
                    print(" ~ Invalid Option ~ ")
                    print("---------------------------")
                    break
                   
        elif choice == 2:
            print("For rent [q]")
            print("For special offer [w]")
            print("---------------------------")
            choice2=input("Enter your choice: ")
            print("---------------------------")
            if choice2 == "q":
                urgent=rent_class()
                # urgent.checking_avaliablity()
                inner_loop = False


            elif choice2 == "w":
                print("     Special offers \n(only for those who are logged in)")
                if cl.logged_in == "True":
                    Special_loop = True
                    while Special_loop:

                        print("_____________________________")
                        print("1. Economic Travel Package")
                        print("2. Premium Travel Package")
                        print("3. Economic Wedding Package")
                        print("4. Premium Wedding Package")
                        print("_____________________________")
                        while True:
                            try:
                                offerchoice=eval(input("Enter your choice: "))
                                break
                            except:
                                print("Invalid datatype, Kindly enter a valid datatype ")
                        print("_____________________________")
                        
                        if offerchoice == 1:
                            print("How many people are travelling?")
                            print("1. Upto 5  people \n2. upto 10 people \n3. upto 20 people \n4. More people")
                            print("_____________________________")
                            while True:
                                try:
                                    economic_travel_choice = eval(input("Enter your choice: "))
                                    break
                                except:
                                    print("Invalid datatype, Kindly enter a valid datatype ")
                            print("_____________________________")
                            if economic_travel_choice == 1:
                                days = eval(input("For how many days do you want this package: "))
                                econ_price = 5000*days
                                print("The total amount to be paid is",econ_price,"Rupees")
                            
                            elif economic_travel_choice == 2:
                                days = eval(input("For how many days do you want this package: "))
                                econ_price = 10000*days
                                print("The total amount to be paid is",econ_price,"Rupees")

                            elif economic_travel_choice == 3:
                                days = eval(input("For how many days do you want this package: "))
                                econ_price = 15000*days
                                print("The total amount to be paid is",econ_price,"Rupees")
                            elif economic_travel_choice == 4:
                                print("Sorry for inconvinience \nNo Larger packages avaliable,You can take 2 packages from above.")
                            else:
                                print("This option is unavaliable.")
                            loop = False
                            Special_loop = False
                            
                        elif offerchoice == 2:
                            print("How many people are travelling?")
                            print("1. Upto 5  people \n2. upto 10 people \n3. upto 20 people \n4. More people")
                            print("_____________________________")
                            while True:
                                try:
                                    premium_travel_choice = eval(input("Enter your choice: "))
                                    break
                                except:
                                    print("Invalid datatype, Kindly enter a valid datatype ")
                            print("_____________________________")
                            if premium_travel_choice == 1:
                                days = eval(input("For how many days do you want this package: "))
                                prem_price = 10000*days
                                print("The total amount to be paid is",prem_price,"Rupees")
                            
                            elif premium_travel_choice == 2:
                                days = eval(input("For how many days do you want this package: "))
                                prem_price = 15000*days
                                print("The total amount to be paid is",prem_price,"Rupees")

                            elif premium_travel_choice == 3:
                                days = eval(input("For how many days do you want this package: "))
                                prem_price = 25000*days
                                print("The total amount to be paid is",prem_price,"Rupees")
                            elif premium_travel_choice == 4:
                                print("Sorry for inconvinience \nNo Larger packages avaliable,You can take 2 packages from above.")
                            else:
                                print("This option is unavaliable.")
                            Special_loop = False

                        elif offerchoice ==3:
                            print("The economic wedding offer is compromises of 5(4 seater cars) and 1(20 seater bus)")
                            eco_choice = input("Do you want to accept the offer[y]/[n]:")
                            if eco_choice.lower() == "y":
                                print("The total amount to be paid is 100000Rs only")
                                Special_loop = False
                            elif eco_choice.lower() == "n":
                                print("Choose again!")
                            
                            Special_loop = False
                            loop = True
                        
                    
                        elif offerchoice == 4:
                            print("The premium wedding offer is compromises of 5(luxary 4 seater cars) and 2(20 seater luxary bus)")
                            eco_choice = input("Do you want to accept the offer[y]/[n]:")
                            if eco_choice.lower() == "y":
                                print("The total amount to be paid is 200000Rs only")
                                Special_loop = False
                            elif eco_choice.lower() == "n":
                                print("Choose again!")
                        
                        else:
                            print("Wrong option ! ")


                elif cl.logged_in == "False":     #Check if we are logged in or no
                    is_reg = input("Sorry, This feature is only avaliable for account holder customers! Do you want to register? [y/n] ")
                    
                    if is_reg.lower() == "y":
                        cl.call()
                         
                    elif is_reg.lower() == "n":
                        pass
                    else:
                        print("Invalid entry. Please enter y or n.")

            else:
                print("Wrong Option! ")
                
        elif choice == 3:
            car_sale = car_Sale()
        
        elif choice == 4:
            print("        ~ GOODBYE ~        ")
            print("---------------------------")
            loop = False
        
        else:
            print("Kindly Enter a valid option ! ")
            print("---------------------------")