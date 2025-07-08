import matplotlib.pyplot as plt
plt.scatter(y_test, linear_predictions, color='blue', label='Linear Regression')
plt.scatter(y_test, rf_predictions, color='green', label='Random Forest')
plt.xlabel('Actual Emissions')
plt.ylabel('Predicted Emissions')
plt.legend()
plt.show()
# 123
