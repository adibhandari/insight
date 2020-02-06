def get_predictions_all(stateconv,statemap,input_state,modelinput,pipe):
    
    m_in = modelinput
    m_in[0][-1] = stateconv
    return pipe.predict(m_in)[0]

def convert_times(cat_time):
    if cat_time == '< 1 week':
        return 0
    elif cat_time == '1 - 2 weeks':
        return 1
    elif cat_time == '< 1 month':
        return 2
    elif cat_time == '< 3 months':
        return 3
    elif cat_time == '> 3 months':
        return 4