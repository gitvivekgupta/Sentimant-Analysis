# Sentiment-Analysis

Run the following

1. features.py
2. score.py
3. accuracy.py (change between data and norm_data)

---------------------------------------------------------------------------------------------------------

# Observation with data

---------------------------------------------------------------------------------------------------------

Accuray is approx: 45.76

k = 52

![A_vs_K](https://user-images.githubusercontent.com/17769945/54927912-183ea680-4f39-11e9-96d9-8fd45c391138.png)

---------------------------------------------------------------------------------------------------------

# Observation with norm_data: (By 100)

---------------------------------------------------------------------------------------------------------

Accuray is approx: 45.73

k = 52

![norm_A_vs_k](https://user-images.githubusercontent.com/17769945/54929699-001c5680-4f3c-11e9-9185-c92a117ba351.png)

---------------------------------------------------------------------------------------------------------

# Cross Validation

---------------------------------------------------------------------------------------------------------

I performed a 10 fold cross validation on data to find the optimal value of k

k = 129

According to KNN score method accuracy of model at k = 129, accuracy is 45.42

so, Here, I think our model is overfitting slightly but negligible.

![cross_val](https://user-images.githubusercontent.com/17769945/54929556-c3e8f600-4f3b-11e9-9496-93775e1ca8d2.png)

---------------------------------------------------------------------------------------------------------

I performed a 10 fold cross validation on norm_data to find the optimal value of k

k = 79

According to KNN score method accuracy of model at k = 79, accuracy is 44.89

so, Here, I think our model is overfitting slightly but negligible.

![norm_cross_val](https://user-images.githubusercontent.com/17769945/54930852-0ca1ae80-4f3e-11e9-915a-fbf58b31e4d7.png)

