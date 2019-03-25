# Sentiment-Analysis

Run the following

1. features.py
2. score.py
3. accuracy.py (choose between norm_data and data)

---------------------------------------------------------------------------------------------------------

# Observation with data:

---------------------------------------------------------------------------------------------------------

Accuracy = 47.99

k = 244

![A_vs_K](https://user-images.githubusercontent.com/17769945/54925103-a6179300-4f33-11e9-8505-e92eae6a1546.png)

---------------------------------------------------------------------------------------------------------

# Observation with norm_data: (By 100)

---------------------------------------------------------------------------------------------------------

Accuracy = 48.0

k = 244

![norm_A_vs_k](https://user-images.githubusercontent.com/17769945/54925747-ee838080-4f34-11e9-866d-d565a0c71788.png)


---------------------------------------------------------------------------------------------------------

# cross Validation

---------------------------------------------------------------------------------------------------------

I performed a 10 fold cross validation on data to find optimal value of k.

k = 140

According to the KNN score method accuracy of model at k=140 is 47.5

So, I think the model is slightly over fitting but its negligible.

![cross_val](https://user-images.githubusercontent.com/17769945/54925112-ad3ea100-4f33-11e9-85b7-4ee10f8ec1cc.png)

------------------------------------------------------------------------------------

I performed a 10 fold cross validation on norm_data to find optimal value of k.

k = 140

According to the KNN score method accuracy of model at k=140 is 47.5

So, I think the model is slightly over fitting but its negligible.

#
