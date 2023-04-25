def calculate_windchill(temp, speed):
    windchill = 35.74 + 0.6215 * temp - 35.75 * speed ** 0.16 + 0.4275 * temp * speed **0.16
    return windchill


def convert_c_to_f(temp):
    temp = temp * 9 / 5 + 32
    return temp

temp = float(input("What is the temperature? "))
temp_type = input("Fahrenheit or Celsius (F/C)?")
 
if temp_type == "C":
    temp = convert_c_to_f(temp)

for speed in range(5, 61, 5):
    windchill = calculate_windchill(temp,speed)
    print(f"At temperature {temp}F, and wind speed {speed} mph, the windchill is: {windchill}F")
    
   





  

    