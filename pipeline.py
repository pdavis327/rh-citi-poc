"""
Operational pipeline. Insert description
"""
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier


class Pipeline:
    def __init__(self, args):
        self.log = logging.getLogger(__name__)
        self.args = args

    @property
    def params(self):
        """
        Gets a dict version of self.args
        :return: dict
        """
        return vars(self.args)

    def run_prediction(self):
        """
        Run the prediction pipeline: load data, train model, and evaluate
        """
        training_data = self.args.source_training_data

        self.log.info("Starting prediction process...")

        # Load the dataset
        df = pd.read_csv(training_data)

        # Prepare data for training
        X = df[["sepal length", "sepal width", "petal length", "petal width"]]
        y = df["species"]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        # Create and train the RandomForestClassifier model
        clf = RandomForestClassifier(n_estimators=100)
        clf.fit(X_train, y_train)

        # Make predictions using the test data
        y_pred = clf.predict(X_test)

        # Calculate and print model accuracy
        accuracy = metrics.accuracy_score(y_test, y_pred)
        self.log.info(f"Model accuracy: {round(accuracy, 2)}")
        print("Model accuracy:", accuracy)

        return accuracy

    def run(self):
        """
        Determines the operation to run (training or other)
        """
        if self.args.operation == "training":
            self.run_prediction()
        else:
            raise RuntimeError(f"Invalid operation: {self.args.operation}")

        return True  # Success if we reach this point
