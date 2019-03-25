# Sentiment-Analysis

Run the following

1. features.py
2. score.py
3. accuracy.py
4. cross_val.py

# Observation with data

Accuray is approx: 45.76%

k = 52

![A_vs_K](https://user-images.githubusercontent.com/17769945/54880310-78661780-4e69-11e9-89f0-ef2e81ae9a86.png)

# Observation with norm_data: (By 100)

Accuray is approx: 45.73%

k = 52

![norm_A_vs_K](https://user-images.githubusercontent.com/17769945/54880417-528d4280-4e6a-11e9-94b3-0cd5073113ff.png)

# Cross Validation

---------------------
I performed a 10 fold cross validation on data to find the optimal value of k

k = 128

According to KNN score method accuracy of model at k = 128, accuracy is 45.57

so, Here, I think our model is overfitting slightly but negligible.

![cross_val](https://user-images.githubusercontent.com/17769945/54880913-52904100-4e70-11e9-91e9-03ff19ae8fee.png)


---------------------
I performed a 10 fold cross validation on norm_data to find the optimal value of k

k = 128

According to KNN score method accuracy of model at k = 128, accuracy is 45.57

so, Here, I think our model is overfitting slightly but negligible.

So, No change.

The graph below has observable variations

![norm_cross_val](https://user-images.githubusercontent.com/17769945/54880959-e5c97680-4e70-11e9-8f06-9225e29a99cd.png)



---------------------
