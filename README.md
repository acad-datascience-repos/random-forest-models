# Random Forest Classifier Assignment

## Problem Description

In this assignment, you will train a `RandomForestClassifier`, a powerful and widely used ensemble learning model. You will use the Wine dataset to classify types of wine.

## Instructions

1.  Open the `assignment.py` file.
2.  You will find a function definition: `train_random_forest_on_wine()`.
3.  Your tasks are to:
    *   Load the Wine dataset from `sklearn.datasets`.
    *   Split the data into training and testing sets (80% train, 20% test).
    *   Create and train a `RandomForestClassifier` model.
    *   Make predictions on the test set.
    *   Calculate and return the accuracy of the model.

## Hints

*   Use `load_wine()` to get the data.
*   Use `train_test_split` and set `random_state=42` for reproducibility.
*   The `RandomForestClassifier` is in `sklearn.ensemble`.
*   Use `model.fit()`, `model.predict()`, and `accuracy_score`.

## Further Exploration (Optional)

*   The trained model has an attribute `model.feature_importances_`. How can you use this to see which features are most important for the classification? Try plotting it with matplotlib.
*   What are some of the key hyperparameters of a Random Forest? Look at `n_estimators` and `max_depth`. How does changing them affect the model's performance?
*   What is the difference between a Random Forest and a single Decision Tree? (Hint: `sklearn.tree.DecisionTreeClassifier`)