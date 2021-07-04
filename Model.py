import keras
encoder_inputs = keras.layers.Input(shape=(timestep, train_X.shape[2]))
encoder_l1 = keras.layers.LSTM(60, return_state=True)
encoder_outputs1 = encoder_l1(encoder_inputs)

encoder_states1 = encoder_outputs1[1:]
decoder_inputs = keras.layers.RepeatVector(train_Y.shape[1])(encoder_outputs1[0])
decoder_l1 = keras.layers.LSTM(60, return_sequences=True)(decoder_inputs,initial_state = encoder_states1)
decoder_outputs1 = keras.layers.TimeDistributed(keras.layers.Dense(train_Y.shape[2]))(decoder_l1)


model = keras.models.Model(encoder_inputs,decoder_outputs1)

#
model.summary()
reduce_lr = keras.callbacks.LearningRateScheduler(lambda x: 1e-3 * 0.90 ** x)

model.compile(optimizer=keras.optimizers.Adam(), loss=keras.losses.Huber())
history_e1d1=model.fit(train_X,train_Y,epochs=50,validation_data=(test_X,test_Y),
                            batch_size=14,verbose=1,callbacks=[reduce_lr])
plt.plot(history_e1d1.history['loss'])
plt.plot(history_e1d1.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

prediction = model_e1d1.predict(test_X)
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
