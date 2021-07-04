import keras
encoder_inputs = keras.layers.Input(shape=(timestep, train_X.shape[2]))
encoder_l1 = keras.layers.LSTM(100, return_state=True)
encoder_outputs1 = encoder_l1(encoder_inputs)

encoder_states1 = encoder_outputs1[1:]
decoder_inputs = keras.layers.RepeatVector(train_Y.shape[2])(encoder_outputs1[0])
decoder_l1 = keras.layers.LSTM(100, return_sequences=True)(decoder_inputs,initial_state = encoder_states1)
decoder_outputs1 = keras.layers.TimeDistributed(keras.layers.Dense(train_Y.shape[2]))(decoder_l1)


model = keras.models.Model(encoder_inputs,decoder_outputs1)

#
model.summary()
reduce_lr = keras.callbacks.LearningRateScheduler(lambda x: 1e-3 * 0.90 ** x)

model.compile(optimizer=keras.optimizers.Adam(), loss=keras.losses.Huber())
history_e1d1=model.fit(train_X,train_Y,epochs=200,validation_data=(test_X,test_Y),
                            batch_size=14,verbose=1,callbacks=[reduce_lr])
