from random import gauss

class Device():
    """
    Represents a generic device.
    Attributes:
        name (str): The name of the device.
        state (bool): The state of the device. Default is False (closed).
    """
    def __init__(self,name,state=False) -> None:
        self.name = name
        self.state = state

    def change_state(self):
        """
        Changes the state of the device.
        If state is True(open) -> Changes it to False(closed)
        If state is False(closed) -> Changes it to True(open)
        """
        if(self.state):
            self.state = False
        else:
            self.state =True

    def show_info(self):
        """
        Prints informations about the device.
        """
        print(f"""
    Name : {self.name}
    State : {"Open" if self.state else "Close"}
""")

class Air_conditioner(Device):
    """
    Represents an air conditioner device.
    Inherits from the Device class.
    Attributes:
        name (str): The name of the air conditioner.
        state (bool): The state of the air conditioner. Default is False (closed).
        temperature (float): The current temperature set on the air conditioner. Default is a random value generated with mean 25 and standard deviation 5.
    """
    def __init__(self, name, state=False) -> None:
        super().__init__(name, state)
        self.temperature = round(gauss(25,5),1)

    def set_temp(self, new_temp):
        """
        Set the temperature of the air conditioner.
        Args:
            new_temp (float): The new temperature to set.
        Raises:
            TypeError: If the new_temp is not a float.
            ValueError: If the air conditioner is currently turned off.
        """
        try:
            if self.state == False:
                raise ValueError("Cannot set temperature when the air conditioner is turned off.")
            if not isinstance(float(new_temp),float):
                raise TypeError("The argument 'new_temp' must be an float object.")
            
            self.temperature = round(new_temp,1)

        except TypeError as e:
            print(e)

        except ValueError as e:
            print(e)

    def show_info(self):
        """
        Shows information about the air conditioner
        """
        print(f"""
    Name : {self.name}
    State : {"Open" if self.state else "Close"}
    Temp : {self.temperature if self.state else "Unkown"}
""")

class Lamp(Device):
    """
    Represents a Lamp(lighting) device
    Inherits from the Device class.
    Attributes:
        name(str) : Name of the Lamp object
        state(bool) : The state of the Lamp. Default is False(closed)
        Brightness(float) : The brightness of the Lamp. 0-> closed, 10-> max brightness
    """
    def __init__(self, name,state=False) -> None:
        super().__init__(name, state)
        self.brightness = 10 if self.state else 0
        
    def change_state(self):
        """
        Changes the state of the device.
        If state is True(open) -> Changes it to False(closed)
        If state is False(closed) -> Changes it to True(open)
        """
        super().change_state()
        self.brightness = 10 if self.state else 0

    def set_brigthness(self,new_value):
        """
        Changes the brightness of the Lamp.
        args:
            new_value(int) : A float value to set brightness
        Raises:
            TypeError: If new_value is not a integer.
            ValueError: If new_value is not bettween 0 and 10
        """
        try: 
            if not isinstance(new_value,int):
                raise TypeError("The argument 'new_value' must be integer[0,10].")
            if new_value>10 or new_value<0:
                raise ValueError("The argument must be between 1 and 10")
            self.brightness = new_value
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)


    def show_info(self):
        """
        Prints information about the Lamp.
        """
        print(f"""
    Name : {self.name}
    State : {"Open" if self.state else "Close"}
    Brightness : {self.brightness}
""")

