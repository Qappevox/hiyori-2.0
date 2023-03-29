import AI
from AI import classes, documents, lemmatizer, words
import random
import numpy as np
import tensorflow as tf
def start_training():
    training = []
    output_empty = [0] * len(classes)
    for document in documents:
        bag = []
        word_patterns = document[0]
        word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
        for word in words:
            bag.append(1) if word in word_patterns else bag.append(0)
        output_row = list(output_empty)
        output_row[classes.index(document[1])] = 1
        training.append([bag, output_row])
    random.shuffle(training)
    training = np.array(training)
    train_x = list(training[:,0])
    train_y = list(training[:,1])

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(128, input_shape = (len(train_x[0]), ),activation = 'relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(64, activation = tf.nn.relu))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(len(train_y[0]), activation = 'softmax'))
    sgd = tf.keras.optimizers.SGD(learning_rate = 0.0001, weight_decay= 1e-6, momentum= 0.999, nesterov=True)
    model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=['accuracy'])

    hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose= 1)
    model.save('AI_model.h5', hist)
    print('done!')

start_training()