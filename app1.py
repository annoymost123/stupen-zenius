import pickle
import streamlit as st

model = pickle.load(open('model_logisticregression.pkl', 'rb'))

def main():
    st.title("House Pricing")
    
    #iput variables 
    GarageCars= st.text_input('GarageCars')
    GarageArea= st.text_input('GarageArea')
    OverallQual= st.text_input('OverallQual')
    GrLivArea= st.text_input('GrLivArea')
    YearBuilt= st.text_input('YearBuilt')
    TotalBsmtSF= st.text_input('TotalBsmtSF')
    FullBath= st.text_input('FullBath')
    
    #prediction code
    if st.button('Predict'):
        makeprediction = model.predict([[GarageCars, GarageArea, OverallQuall, GrLivArea,YearBuilt, TotalBsmtSF,FullBath]])
        output = round(makeprediction[0],2)
        st.success('Sale Price {}'.format(output))
    
if __name__=='__main__':
    main()
