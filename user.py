from hashlib import sha256
from house import House


class User():
    """
    Represents a user in the system.
    This class stores user information such as name, surname, email, password (hashed),
    and a list of houses associated with the user.
    Methods:
        new_house(): Adds a house to the user's list.
        remove_house(): Removes a house from the user's list.
        change_password(): Changes the user's password.
        get_house_names(): Returns a comma-separated string of house names.
        show_info(): Displays the user's information in a formatted string.
    """
    def __init__(self,name,surname,email,password) -> None:
        self.name = name
        self.surname = surname
        self.email = email
        self.password = sha256(password.encode()).hexdigest()
        self.houses = []

    def new_house(self,house):
        """
        Adds a new "House" object to the user's list of houses.
        Args:
            house (House): The house object to be added.
        Raises:
            TypeError: If the argument is not a House object.
            ValueError: If the house already exist in the user's house list.
        """
        try:
            if isinstance(house, House):
                if (self.houses.__contains__(house)):
                    raise OverflowError("The house is already exist on the list.")
                else:
                    self.houses.append(house)
                    print("The new house have been succsefully added.")
            else:
                error_msg = f"The input 'house' must be an object from 'House' class. Received: {type(house)}"
                raise TypeError(error_msg)
        except TypeError as e:
            print(e)
        except OverflowError as e:
            print(e)

    
    def remove_house(self,house):
        """
        Removes a house from the user's houses list.
        Args:
            house (House): The House object to be removed.
        Raises:
            TypeError: If the argument is not a House object.
            ValueError: If the house does not exist in the user's house list.
        """
        try:
            if not(isinstance(house,House)):
                raise TypeError(f"The argument must be a 'House' object. Received: {type(house)}")
            elif not(self.houses.__contains__(house)):
                raise ValueError("House does not exist in the user houses list.")
            self.houses.remove(house)
            print("The house has been succsesfully removed in user houses list.")
    
        except TypeError as e :
            print(e)
        except ValueError as e : 
            print(e)


    def change_password(self,password,new_password,new_password2):
        """
        Changes the user's password.
        Args:
            password (str): The user's current password.
            new_password (str): The new password the user wants to set.
            new_password2 (str): A confirmation of the new password to ensure it's typed correctly.
        Raises:
            TypeError: If any of the parameters are not strings.
            ValueError: If the current password is incorrect or the new passwords don't match.
        """
        
        try:
            #Check if parameters is string
            if not isinstance(password, str) or not isinstance(new_password, str) or not isinstance(new_password2, str):
                raise TypeError("All parameters must be strings.")

            # Verify password
            if(sha256(password.encode()).hexdigest() != self.password): 
                raise ValueError("Your password is incorrect.")
            else:
                #Checks password match
                if(new_password == new_password2):
                    self.password = sha256(new_password.encode()).hexdigest()
                    print("The user password has been successfully changed.")
                else:
                    raise ValueError("Passwords do not match. Try again.")                    
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)


    def get_house_names(self):
        """
        Returns the names of all houses as a comma-separated string.
        *This function is specifically designed to work with the houses attribute of a User class.  
        Returns:
            A comma-separated string containing the names of all houses.
        """

        names = [house.name for house in self.houses]
        return ", ".join(names)


    def show_info(self):
        """
        Returns a formatted string containing the user's name, surname, email address, and a list of house names.
        This function retrieves information from the `User` object and utilizes the `get_house_names` function to get the comma-separated house names.
        Returns:
            A string with the user's details.
        """
        print(f"""
                Name: {self.name} {self.surname}
                E-mail: {self.email}
                Houses: {self.get_house_names()}
                """)

