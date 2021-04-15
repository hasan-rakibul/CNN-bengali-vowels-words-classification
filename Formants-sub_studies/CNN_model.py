from collect_feature import *
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical


X_train, X_test, y_train, y_test=get_train_test(max_len=max_length)

print(X_train)
X_train=X_train.reshape(X_train.shape[0],max_length,6,1)
X_test=X_test.reshape(X_test.shape[0],max_length,6,1)
y_train_hot=to_categorical(y_train)
y_test_hot=to_categorical(y_test)
#print(y_train_hot.shape)
model=Sequential()
model.add(Conv2D(32,kernel_size=(2,2),activation='relu',input_shape=(max_length,6,1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(10,activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.adadelta(),metrics=['accuracy'])
model.fit(X_train,y_train_hot,batch_size=100,epochs=100,verbose=1,validation_data=(X_test,y_test_hot))