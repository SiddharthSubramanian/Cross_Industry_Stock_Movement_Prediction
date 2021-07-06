import keras
encoder_inputs = keras.layers.Input(shape=(timestep, train_X.shape[2]))
encoder_outputs1 = keras.layers.LSTM(
    60, activation='elu', dropout=0.2, recurrent_dropout=0.2, 
    return_state=True, return_sequences=True)(encoder_inputs)
encoder_outputs1[1] = keras.layers.BatchNormalization(momentum=0.5)(encoder_outputs1[1])
encoder_outputs1[2] = keras.layers.BatchNormalization(momentum=0.5)(encoder_outputs1[2])
decoder_input = keras.layers.RepeatVector(train_Y.shape[1])(encoder_outputs1[1])

decoder_output1 = keras.layers.LSTM(60, activation='elu', dropout=0.2, recurrent_dropout=0.2,
 return_state=False, return_sequences=True)(
 decoder_input, initial_state=[encoder_outputs1[1], encoder_outputs1[2]])
attention = keras.layers.dot([decoder_output1, encoder_outputs1[0]], axes=[2, 2])
attention = keras.layers.Activation('softmax')(attention)
context = keras.layers.dot([attention, encoder_outputs1[0]], axes=[2,1])
context = keras.layers.BatchNormalization(momentum=0.5)(context)
decoder_combined_context = keras.layers.concatenate([context, decoder_output1])
decoder_outputs1 = keras.layers.TimeDistributed(keras.layers.Dense(train_Y.shape[2]))(decoder_combined_context)
model_attention = keras.models.Model(encoder_inputs,decoder_outputs1)
#
model_attention.summary()
opt = keras.optimizers.Adam(lr=0.01, clipnorm=1)
model_attention.compile(loss="mean_squared_error", optimizer=opt, metrics=['mse'])
reduce_lr = keras.callbacks.LearningRateScheduler(lambda x: 1e-3 * 0.90 ** x)
history=model_attention.fit(train_X,train_Y,epochs=100,validation_data=(test_X,test_Y),
                            batch_size=14,verbose=1,callbacks=[reduce_lr])
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

prediction = model.predict(test_X)
pred = []
original = []
for i in range(prediction.shape[0]):
  pred.append(prediction[i][0])
  original.append(test_Y[i][0])
pred = pd.DataFrame(list(map(np.ravel, pred)))
original = pd.DataFrame(list(map(np.ravel, original)))
pred.columns = Y.columns
original.columns = Y.columns
from sklearn.metrics import mean_absolute_error
for index,i in enumerate(original.columns):
  print(i)

  print("Mean absolute error price prediction : ",mean_absolute_error(original.iloc[:,index],pred.iloc[:,index]),end=", ")
  print()
