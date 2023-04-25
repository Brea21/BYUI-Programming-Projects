max = 0
max_data = []
min = 100
min_data = []

year_max= 0
year_max_data = []
year_min= 100
year_min_data = []
year_life_expectancies = []



print("🤗 Welcome to Life-Expectancy Program🤗")

interest_year =input("Enter the year of intrest: ")

with open("life-expectancy.csv") as life_file:
       for line in life_file:
              data = line.strip().split(",")   
              country = data[0]
              year = data[2]
              life_expectancy = float(data[3])
              

              if life_expectancy > max:
                     max = life_expectancy
                     max_data = data
              if life_expectancy < min:
                     min = life_expectancy     
                     min_data = data
                                  
              if year == interest_year:
                 year_life_expectancies.append(life_expectancy)
                     
                 if life_expectancy > year_max:
                     year_max = life_expectancy
                     year_max_data = data
                 if life_expectancy < year_min:
                    year_min = life_expectancy     
                    year_min_data = data
             
average = sum(year_life_expectancies)/len(year_life_expectancies)

print()       
print(f"The overall max life expectancy is: {max_data[3]} from {max_data[0]} in {max_data[2]}")
print(f"The overall max life expectancy is: {min_data[3]} from {min_data[0]} in {min_data[2]}")
print()
print(f"For the year {interest_year}:")
print(f"The average life expectancy across all countries was{average}")
print(f"The max life expectancy was in {year_max_data} with {year_max_data[3]} ")
print(f"The min life expectancy was in {year_min_data} with {year_min_data[3]} ")


       