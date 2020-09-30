from flask import Flask,render_template,url_for,request
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message1 =request.form['message1']
        message2 =request.form['message2']
        # tokenization
        X_list = word_tokenize(message1) 
        Y_list = word_tokenize(message2)
        
        # sw contains the list of stopwords 
        sw = stopwords.words('english') 
        l1 =[];l2 =[]
        # remove stop words from string 
        X_set = {w for w in X_list if not w in sw} 
        Y_set = {w for w in Y_list if not w in sw}
        # form a set containing keywords of both strings 
        rvector = X_set.union(Y_set) 
        for w in rvector: 
            if w in X_set: l1.append(1) # create a vector 
            else: l1.append(0) 
            if w in Y_set: l2.append(1) 
            else: l2.append(0) 
        c = 0

# cosine formula 
        for i in range(len(rvector)): 
                c+= l1[i]*l2[i]
        
        
        cosine = c / float((sum(l1)*sum(l2))**0.5) 
       # print("similarity: ", cosine)
        return render_template('home.html', prediction_text='Similarity Score: {}'.format(cosine)) 

if __name__ == '__main__':
	app.run(debug=True)


