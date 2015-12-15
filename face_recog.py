from pattern_recog_func import *

X = []
phys_dict = {0: 'Bohr', 1: 'Einstein'}

ein0 = mpimg.imread('ein0.jpeg')
ein1 = mpimg.imread('ein1.jpeg') 
ein2 = mpimg.imread('ein2.jpeg') 
ein3 = mpimg.imread('ein3.jpeg') 
ein4 = mpimg.imread('ein4.jpeg') 
ein5 = mpimg.imread('ein5.jpeg') 
ein6 = mpimg.imread('ein6.jpeg') 
ein7 = mpimg.imread('ein7.jpeg') 
ein8 = mpimg.imread('ein8.jpeg') 
ein9 = mpimg.imread('ein9.jpeg') 
ein10 = mpimg.imread('ein10.jpeg') 
bohr0 = mpimg.imread('bohr0.jpeg')
bohr1 = mpimg.imread('bohr1.jpeg') 
bohr2 = mpimg.imread('bohr2.jpeg') 
bohr3 = mpimg.imread('bohr3.jpeg') 
bohr4 = mpimg.imread('bohr4.jpeg') 
bohr5 = mpimg.imread('bohr5.jpeg') 
bohr6 = mpimg.imread('bohr6.jpeg') 
bohr7 = mpimg.imread('bohr7.jpeg') 
bohr8 = mpimg.imread('bohr8.jpeg') 
bohr9 = mpimg.imread('bohr9.jpeg') 

phys_list = [ein0, ein1, ein2, ein3, ein4, ein5, ein6, ein7, ein8, ein9, ein10, \
             bohr0, bohr1, bohr2, bohr3, bohr4, bohr5, bohr6, bohr7, bohr8, bohr9]


for i in phys_list:
    X.append(interpol_im(i, dim1 = 45, dim2 = 60))

X = np.vstack(X)
#print(X.shape)
y = np.array([1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0])
#print(y.shape)




checker = 0
for i in range(len(y)):
    Xtrain = np.delete(X, i, axis = 0)
    ytrain = np.delete(y, i)
    Xtest = X[i].reshape(1, -1)
    md_pca2, X_proj2 = pca_X(Xtrain, n_comp = 10)
    
    Xtrain_proj = md_pca2.transform(Xtrain)
    Xtest_proj = md_pca2.transform(Xtest)
    md_clf2 = svm_train(Xtrain_proj,ytrain)
    num = md_clf2.predict(Xtest_proj)[0]
    
    print(num)
    if num == y[i]:
        checker += 1
    else:
        pass
print('Percentage correct: {:f}%, {:d}'.format(100*(float(checker)/len(phys_list)), checker))


alpie = pca_svm_pred('unseen_phys1.jpg', md_pca2, md_clf2)
betbee = pca_svm_pred('unseen_phys2.jpg', md_pca2, md_clf2)
print('PCA+SVM prediction for physicist 1:', phys_dict[alpie])
print('PCA+SVM prediction for physicist 2:', phys_dict[betbee])
