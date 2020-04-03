from flask import Flask, request, redirect, url_for, flash, jsonify
import pickle
import numpy as np
import pandas as pd
import json

app = Flask(__name__)

def load_model():
    # Load model pipeline
    filename = './models/rfpipe_combined.pkl'
    model  = pickle.load(open(filename, 'rb'))
    return model

def get_breedlist():
    # Load list of breeds
    return pd.read_csv('./breedlist.csv')

def get_statelist():
    # Load list of states
    return pd.read_csv('./statelist.csv')

@app.route('/api/', methods=['POST'])
def makecalc():
    # check request format
    if request.method != 'POST':
        return('Error: Wrong input format. Please refer to the README for sample query format.')
    
    breeds = (breedlist.sort_values(by='breeds.primary')).loc[:,'breeds.primary']
    states = (statelist).loc[:,'Abb']

    featurelist = [input_state, input_age, input_gender, input_size, input_breedmix, input_breed]
    features = dict.fromkeys(featurelist,0)

    try: 
        user_query = request.get_json(force=True)
    except: 
        return 'Error : Wrong data format. Please refer to the README for example data format.'

    for feature in featurelist: 
        try:  
            features[feature]  = user_query[feature]
        except:  
            return 'Error: Please provide all of the required features in the format specified in the README.'

    if features['input_age'] not in ['Baby', 'Young', 'Adult', 'Senior']:
        return 'Error. Please refer to README for correct age format.'

    if features['input_age'] not in ['Male', 'Female']:
        return 'Error. Please refer to README for correct gender format.'

    if features['input_size'] not in ['Small', 'Medium', 'Large']:
        return 'Error. Please refer to README for correct size format.'
    
    if features['input_breedmix'] not in ['Yes', 'No']:
        return 'Error. Please put yes or no for is it a mixed breed.'

    if features['input_state'] not in states:
        return 'Error. Please enter the state abbreviation correctly. Please refer to the README for a list of state abbreviations.'

    if features['input_breed'].str.lower() not in [x.lower() for x in breeds]:
        return 'Error. Please enter the breed correctly. Please refer to the README for a list of breeds.'

    input_state_conv = statelist.loc[statelist['Abb']==input_state, 'Mod'].item()

    breedpop = breedlist.loc[breedlist['breeds.primary']==input_breed, 'breed_pop'].to_string(index=False).strip()
    input_breed_conv = breedlist.loc[breedlist['breeds.primary']==input_breed, 'breedconv'].item()

    model_input = [[input_age,input_gender, input_size, breedpop,  input_breed_conv, input_breedmix=='Yes', input_state_conv]]

    adpt_time = finalmodel.predict(model_input)[0]

    return jsonify(adpt_time)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", action="store", default="5000")
    args = parser.parse_args()
    port = int(args.port)

    print('Loading model and dependencies...')
    finalmodel = load_model() # load the model first
    breedlist = get_breedlist()
    statelist = get_statelist()
    app.run(debug=False, host = '127.0.0.1', port=port)