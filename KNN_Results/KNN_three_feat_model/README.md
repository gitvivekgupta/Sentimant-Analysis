# Sentiment-Analysis

Run the following

1. features.py
2. score.py
3. accuracy.py (choose between norm_data and data)

# Observation with data:

Accuracy = 48.1

k = 359

![A_vs_k](https://user-images.githubusercontent.com/17769945/54879234-83667b00-4e5c-11e9-980f-231d42cf600d.png)

# Observation with norm_data: (By 100)

Accuracy = 48.0

k = 244

![norm_A_vs_k](https://user-images.githubusercontent.com/17769945/54880103-1f957f80-4e67-11e9-9bcb-469a582b179f.png)


# Observation with norm_data: (By 50) 

-- [Same as of norm by 100]

Accuracy = 48.0

k = 244


# cross Validation

I performed a 10 fold cross validation on data to find optimal value of k

k = 151

According to the KNN score method accuracy of model at k=151 is 47.4

So, I think the model is slightly over fitting but its negligible.


![cross_val](https://user-images.githubusercontent.com/17769945/54879231-7a75a980-4e5c-11e9-9c66-977dc2c4f5bc.png)

--------------------------------

I performed a 10 fold cross validation on norm_data to find optimal value of k

k = 273

According to the KNN score method accuracy of model at k = 273 is 47.8

So, I think the model is slightly over fitting but its negligible.

we can observe the variation in the graph below.

![norm_cross_val](https://user-images.githubusercontent.com/17769945/54881448-224ba100-4e76-11e9-8c96-77c3d0c0ee46.png)


