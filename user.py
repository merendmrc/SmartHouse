from hashlib import sha256
from house import House

class User():
    def __init__(self,name,surname,email,password) -> None:
        self.name = name
        self.surname = surname
        self.email = email
        self.password = sha256(password.encode()).hexdigest()
        self.houses = []


    def newHouse(self,house):
        """
        The function adds a new "House" object to the user's list of houses.
        It takes a "House" object as input
        """
        if isinstance(house, House):
            self.houses.append(house)
        else:
            error_msg = f"The input 'house' must be an object from 'House' class. Given: {type(house)}"
            raise TypeError(error_msg)
        

    def change_password(self,password,new_password,new_password2):
        """
        The function changes user password.
        Takes 3 parameters as string: password, new_password, new_password2
        """
        try:
            #Check if parameters is string
            if not isinstance(password, str) or not isinstance(new_password, str) or not isinstance(new_password2, str):
                raise TypeError("All parameters must be strings.")

            # Verify password
            if(sha256(password.encode()).hexdigest() != self.password): 
                raise ValueError("Your password is incorrect.")
            else:
                #Check password match
                if(new_password == new_password2):
                    self.password = sha256(new_password.encode()).hexdigest()
                    print("The user password has been successfully changed.")
                else:
                    raise ValueError("Passwords do not match. Try again.")                    
        except ValueError as e:
            print(e)

eren = User("er","3re","edgs","ds")
eren.change_password(1,2,3)