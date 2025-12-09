import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# b. Import the data 
# Creating a simple advertising dataset
data = {
    'Advertising': [12.0 , 20.5,21.0,15.5, 15.3,23.5,24.5,21.3,23.5,28.0,24.0,15.5,17.3,25.3,25.0,36.5,36.5,29.6,30.5,28.0,26.0,21.5,19.7,19.0,16.0,20.7,26.5,30.6,32.3,29.5,28.3,31.3,32.3,26.4,23.4,16.4],  
    'Sales': [15.0,16.0,18.0,27.0,21.0,49.0,21.0,22.0,28.0,36.0,40.0,3.0,21.0,29.0,62.0,65.0,46.0,44.0,33.0,62.0,22.0,12.0,24.0,3.0,5.0,14.0,36.0,40.0,49.0,7.0,52.0,65.0,17.0,5.0,17.0,1.0]     
}

df = pd.DataFrame(data)

print(df.describe())
X = df[['Advertising']]
y = df['Sales']

plt.scatter(X, y, color='blue')
plt.xlabel("Advertising Spend (Rs1000s)")
plt.ylabel("Sales (Rs1000s)")
plt.title("Advertising vs Sales")
plt.show()

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')  # Regression line
plt.xlabel("Advertising Spend (Rs1000s)")
plt.ylabel("Sales (Rs1000s)")
plt.title("Linear Regression: Advertising vs Sales")
plt.show()

print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)