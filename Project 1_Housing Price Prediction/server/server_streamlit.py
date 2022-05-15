##streamlit run server_streamlit.py
import util
import streamlit as st

def main_streamlit():
    st.title("Price Prediction")
    ##st.write("Hello World Streamlit")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Housing Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    total_sqft = st.slider("total_sqft",min_value=500.0,max_value=5000.0, step=10.0)    
    st.write("Total Square Ft.", total_sqft)
    #location = st.text_input("location","Type Here")  
    location = st.selectbox("Select the location", util.get_location_names())
    st.write('You selected', location)  
    bhk = st.slider("bhk",min_value=1,max_value=10, step=1)   
    st.write("Total BHK", bhk) 
    bath = st.slider("bath",min_value=1,max_value=10, step=1)
    st.write("Total Bath", bath)
    estimated_price = ""
    if st.button("Predict"):
        estimated_price = util.get_estimated_price(location,total_sqft,bhk,bath)
        print(estimated_price)
        st.write('The predicted price is ', estimated_price)  
    #st.success = ('The predicted price is {} '. format(estimated_price))


if __name__ == "__main__":
    print("Starting Python Streamlit Server For Home Price Prediction...")
    util.load_saved_artifcats()
    main_streamlit()
    #app.run()