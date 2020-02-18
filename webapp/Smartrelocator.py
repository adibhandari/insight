import streamlit as st
import numpy as np
import pandas as pd
import pickle
from relocatortools import *
import warnings
import plotly.graph_objects as go

warnings.filterwarnings("ignore")


@st.cache(allow_output_mutation=True)
def get_breedlist():
    return pd.read_csv('./breedlist.csv')

@st.cache(allow_output_mutation=True)
def get_statelist():
    return pd.read_csv('./statelist.csv')

filename = './models/rfpipe_combined.pkl'
# @st.cache()
# def get_model(allow_output_mutation=True):
#     return pickle.load(open(filename, 'rb'))
# loadedmodel = get_model()
# finalmodel = deepcopy(loadedmodel)


finalmodel = pickle.load(open(filename, 'rb'))


loadedbrd = get_breedlist()
breedlist = loadedbrd
breeds = (breedlist.sort_values(by='breeds.primary')).loc[:,'breeds.primary']

loadedst = get_statelist()
statelist = loadedst
fullstates = (statelist).loc[:,'Full']


"""
# **Smart relocator**
"""

input_state = st.sidebar.selectbox(
    'Which state are you in?',
     fullstates,
     index=30,
    key = 'input_state')

input_age = st.sidebar.selectbox(
    'How old is the dog?',
     ['Baby', 'Young', 'Adult', 'Senior'],
    key = 'input_age')

input_gender = st.sidebar.selectbox(
    'What is the gender of the dog',
    ['Male', 'Female'],
    key = 'input_gender')

input_size = st.sidebar.selectbox(
    'How big is the dog?',
     ['Small', 'Medium', 'Large'],
    key = 'input_size')

input_breedmix = st.sidebar.selectbox(
    'Is it a mixed breed?',
     ['Yes', 'No'],
    key = 'breedmix')

input_breed = st.sidebar.selectbox(
    'What breed is it? (Primary breed for mixed breeds)',
     breeds,
     #index=113,
    key = 'breed')

btn = st.sidebar.button("Ready!")

if(btn):
    input_state_conv = statelist.loc[statelist['Full']==input_state, 'Mod'].item()
    input_state_map = statelist.loc[statelist['Full']==input_state, 'Abb'].item()

    breedpop = breedlist.loc[breedlist['breeds.primary']==input_breed, 'breed_pop'].to_string(index=False).strip()
    input_breed_conv = breedlist.loc[breedlist['breeds.primary']==input_breed, 'breedconv'].item()

    model_input = [[input_age,input_gender, input_size, breedpop,  input_breed_conv, input_breedmix=='Yes', input_state_conv]]

    adpt_time = finalmodel.predict(model_input)

    'Predicted time to adoption in', input_state_map, 'is :' , adpt_time[0]

    'Check out the interactive map below to see if your dog will do better at a shelter in another state!'

    statelist['Pred'] = statelist.apply(lambda x: get_predictions_all(x['Mod'], x['Abb'], input_state_map, model_input, finalmodel), axis=1)
    statelist['cat_time'] = statelist.apply(lambda x: convert_times(x['Pred']), axis=1)

    fig = go.Figure(data=go.Choropleth(
        locations=statelist['Abb'], # Spatial coordinates
        z = statelist['cat_time'], # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        text = statelist['Pred'],
        colorscale = 'magma_r',
        zmax=4,
        zmin=0,
        hoverinfo='location+text',
        colorbar={'tickmode':'array', 'tickvals':[0,1,2,3,4], 'ticktext':['<1 week','1 - 2 weeks','<1 month','<3 months','>3 months']},
        colorbar_title = None,
    ))
    fig.update_layout(
        title_text = 'Adoption times in the US',
        geo_scope='usa', # limite map scope to USA
    )
    st.plotly_chart(fig)


    """
    The predictions assume that your dogs are up to date on shots and have no special needs.\n
    *Note that dogs with special needs can take more than twice as long to get adopted.*
    """

    """
    Data collected using [Petfinder](https://www.petfinder.com) API.
    """
else:
    """
    Predict the adoption time for your dog by entering the details on the sidebar!
    """
