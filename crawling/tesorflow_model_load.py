import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    df = pd.read_csv("data/weather_classification_data.csv")
    df['Cloud Cover'] = np.where(df['Cloud Cover'] == 'partly cloudy', 0,
                                 np.where(df['Cloud Cover'] == 'clear', 1,
                                          np.where(df['Cloud Cover'] == 'overcast', 2, 3)))
    # print(df['Season'].unique())
    df['Season'] = np.where(df['Season'] == 'Winter', 0,
                            np.where(df['Season'] == 'Spring', 1,
                                     np.where(df['Season'] == 'Summer', 2, 3)))
    # print(df['Location'].unique())
    df['Location'] = np.where(df['Location'] == 'inland', 0,
                              np.where(df['Location'] == 'mountain', 1, 2))
    # print(df['Weather Type'].unique())
    df['Weather Type'] = np.where(df['Weather Type'] == 'Rainy', 0,
                                  np.where(df['Weather Type'] == 'Cloudy', 1,
                                           np.where(df['Weather Type'] == 'Sunny', 2, 3)))
    df.keys()
    X = df[['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)',
            'Cloud Cover', 'Atmospheric Pressure', 'UV Index', 'Season',
            'Visibility (km)', 'Location']].values
    y = df[['Weather Type']].values
    X = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    y_train = tf.one_hot(y_train.flatten(), 4)
    y_test = tf.one_hot(y_test.flatten(), 4)

    model = tf.keras.models.load_model("weahterAnn_tf_2.15.0_version0")
    print(X_test.shape)
    print(X_test[20:21])
    predY = model.predict(X_test[20:21])
    print(int(tf.argmax(y_test[20:21][0], axis=0)))
    print(predY[1].argmax())
