from hashlib import sha256
from house import House


class User():

    def __init__(self,name,surname,email,password) -> None:
        self.name = name
        self.surname = surname
        self.email = email
        self.password = sha256(password.encode()).hexdigest()
        self.houses = []

    def new_house(self,house):
        """
        The function adds a new "House" object to the user's list of houses.
        It takes a "House" object as input
        """
        #Check if parameters is "House" object
        try:
            if isinstance(house, House):
                if (self.houses.__contains__(house)):
                    raise OverflowError("The house is already exist on the list.")
                else:
                    self.houses.append(house)
                    print("The new house have been succsefully added.")
            else:
                error_msg = f"The input 'house' must be an object from 'House' class. Given: {type(house)}"
                raise TypeError(error_msg)
        except TypeError as e:
            print(e)
        except OverflowError as e:
            print(e)

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
                #Checks password match
                if(new_password == new_password2):
                    #Update password
                    self.password = sha256(new_password.encode()).hexdigest()
                    print("The user password has been successfully changed.")
                else:
                    raise ValueError("Passwords do not match. Try again.")                    
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)


    def house_names(self):
        """
        Returns the names of all houses as a comma-separated string.
        *This function is specifically designed to work with the houses attribute of a User class.
        *It assumes that the house_list parameter contains house objects.

        args:
            house_list: A list of house objects, typically the `houses` attribute of a `User` instance.

        Raises:
            TypeError: If `house_list` doesn't contain house objects with houses attribute.
        Returns:
            A comma-separated string containing the names of all houses.
        """

        names = [house.name for house in self.houses]
        return ", ".join(names)


    def show_info(self):
        """
        Returns a formatted string containing the user's name, surname, email address, and a list of house names.

        This function retrieves information from the `User` object and utilizes the `house_names` function to get the comma-separated house names.

        Returns:
            A string with the user's details.
        """
        print(f"""
                Name: {self.name} {self.surname}
                E-mail: {self.email}
                Houses: {self.house_names()}
                """)