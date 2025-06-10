
class HighTemperatureError(Exception):
    pass

def convert_temperature(temp):
    
    if not isinstance(temp, (int, float)):
        raise TypeError("Temperature must be a number.")

    assert -272 <= temp <= 10000, "Temperature out of reasonable range."

    if temp > 1000:
        raise HighTemperatureError("Temperature is too high for common use.")

    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C = {fahrenheit}°F")

user_input = input("Enter temperature in Celsius: ")

try:
    temp_value = float(user_input) 
    convert_temperature(temp_value)
except TypeError as te:
    print("TypeError:", te)
except AssertionError as ae:
    print("AssertionError:", ae)
except HighTemperatureError as he:
    print("HighTemperatureError:", he)
except ValueError:
    print("ValueError: Please enter a valid numeric temperature.")
