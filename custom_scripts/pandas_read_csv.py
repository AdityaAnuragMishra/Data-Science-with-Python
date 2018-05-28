# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.DataFrame(pd.read_csv("../resources/cars.csv"))
jobs = pd.DataFrame(pd.read_csv("../resources/Information_gain_job_advertisements.csv"))
industries = pd.DataFrame(pd.read_json("../resources/industries.json"))


# Print out cars
print(industries)

# Print all colums
print(list(industries.resultList))