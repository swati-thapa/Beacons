import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    le_name_mapping={'D13': 0, 'D14': 1, 'D15': 2, 'E15': 3, 'F08': 4, 'G15': 5, 'I01': 6, 'I02': 7, 'I03': 8, 'I04': 9, 'I05': 10, 'I06': 11, 'I07': 12, 'I08': 13, 'I09': 14, 'I10': 15, 'I15': 16, 'J01': 17, 'J02': 18, 'J03': 19, 'J04': 20, 'J05': 21, 'J06': 22, 'J07': 23, 'J08': 24, 'J10': 25, 'J15': 26, 'K01': 27, 'K02': 28, 'K03': 29, 'K04': 30, 'K05': 31, 'K06': 32, 'K07': 33, 'K08': 34, 'L01': 35, 'L02': 36, 'L03': 37, 'L04': 38, 'L05': 39, 'L06': 40, 'L08': 41, 'L09': 42, 'L15': 43, 'M01': 44, 'M02': 45, 'M03': 46, 'M04': 47, 'M05': 48, 'M06': 49, 'N01': 50, 'N02': 51, 'N03': 52, 'N04': 53, 'N05': 54, 'N06': 55, 'N15': 56, 'O01': 57, 'O02': 58, 'O03': 59, 'O04': 60, 'O05': 61, 'O06': 62, 'P01': 63, 'P02': 64, 'P03': 65, 'P04': 66, 'P05': 67, 'P06': 68, 'P15': 69, 'Q01': 70, 'Q02': 71, 'Q03': 72, 'Q04': 73, 'Q05': 74, 'Q06': 75, 'R01': 76, 'R02': 77, 'R03': 78, 'R04': 79, 'R05': 80, 'R06': 81, 'R15': 82, 'S01': 83, 'S02': 84, 'S03': 85, 'S04': 86, 'S05': 87, 'S06': 88, 'S07': 89, 'S08': 90, 'S15': 91, 'T01': 92, 'T03': 93, 'T04': 94, 'T05': 95, 'T15': 96, 'U01': 97, 'U02': 98, 'U03': 99, 'U04': 100, 'U05': 101, 'U15': 102, 'V15': 103, 'W15': 104}
    def get_key(val):
        for key, value in le_name_mapping.items():
            if val == value:
                return key

    result = get_key(prediction[0])

    output = result
    output1= int_features

    return render_template('index.html', prediction_location='Location is {}''Inputs are{}'.format(output,output1))

'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    output = result
    return jsonify(output)
'''
if __name__ == "__main__":
    app.run(port=5006, debug=True)