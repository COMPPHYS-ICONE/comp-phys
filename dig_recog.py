from pattern_recog_func import *

md_clf1 = svm_train(X[:60],y[:60])
checker = 0
X_new = X[60:80]
y_new = y[60:80]
for i in range(20):
    num = md_clf1.predict(X_new[i].reshape(1, -1))[0]
    if num != y[i+60]:
        checker+=1
        print('Index:', i+60)
        print('Actual digit:', y[i+60])
        print('svm_prediction:', num)
        test_img = dig_img[i+60]
        plt.figure(figsize = (4, 4))
        plt.title('Actual Digit')
        plt.imshow(test_img, cmap = 'binary')
        plt.grid('off')
        plt.axis('off')

print('Total number of mis-identifications:',checker)
print('Success rate',(checker-(1./20)))

plt.figure(figsize = (4, 4))
plt.title('Unseen match from database')
plt.imshow(dig_img[15], cmap = 'binary')
plt.grid('off')
plt.axis('off')



unseen = mpimg.imread('unseen_dig.png') 

unseen_interp = interpol_im(unseen, plot_new_im = True)

prediction_unscaled = md_clf1.predict(unseen_interp.reshape(1, -1))[0]

unseen_rescaled = rescale_pixel(X, unseen_interp)


prediction_scaled = md_clf1.predict(unseen_rescaled.reshape(1, -1))[0]

print('The unscaled prediciton is:', prediction_unscaled)

print('The scaled prediction is:', prediction_scaled)

