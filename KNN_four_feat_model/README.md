# four_feat_model

Run the following

1. features.py
2. score.py
3. accuracy.py (choose between norm_data and data)

--------------------------------

# Observation with data:

Accuracy = 48.0

k = 360

![A_vs_K](https://user-images.githubusercontent.com/17769945/55044410-3a7f1400-5060-11e9-8341-335aec3960a6.png)

--------------------------------

# Observation with norm_data: (By 100)

Accuracy = 48.1

k = 360

![norm_A_vs_K](https://user-images.githubusercontent.com/17769945/55045269-41f3ec80-5063-11e9-8654-4cdcc9fbc429.png)

--------------------------------

# cross Validation

I performed a 10 fold cross validation on data to find optimal value of k

k = 139

According to the KNN score method accuracy of model at k = 139 is 47.4

So, I think the model is slightly over fitting but its negligible.

![cross_val](https://user-images.githubusercontent.com/17769945/55044900-060c5780-5062-11e9-9461-95ed9b2aaebe.png)

--------------------------------

I performed a 10 fold cross validation on norm_data to find optimal value of k

k = 139

According to the KNN score method accuracy of model at k = 139 is 47.4

So, I think the model is slightly over fitting but its negligible.

we can observe the variation in the graph below.

![norm_cross_val](https://user-images.githubusercontent.com/17769945/55046088-4bcb1f00-5066-11e9-92f4-32da971f4fe6.png)
