import pandas as pd
import matplotlib.pyplot as plt

# Sample Sales Dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [200, 250, 300, 280, 320, 350]
}

df = pd.DataFrame(data)

print("Sales Data:")
print(df)

# Plotting the sales graph
plt.plot(df["Month"], df["Sales"])
plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
