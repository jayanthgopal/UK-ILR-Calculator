import streamlit as st
import datetime
import pandas as pd
import numpy as np


def calculate_date(date, days):
  new_date = datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=days)
  return new_date.strftime('%Y-%m-%d')

def main():
  st.title('ILR Calculator')
  visa_date = st.date_input("Date of Visa")

  if st.button('ILR Eligibility Date'):
    st.write('Visa Date: {}'.format(visa_date))  
    new_date = calculate_date(str(visa_date), 1799)
    st.write('ILR Eligibility from {}'.format(new_date))
    
    # Create an empty dataframe
    data = pd.DataFrame(columns=["Random"])
    st.text("Original dataframe")
    
    # with every interaction, the script runs from top to bottom
    # resulting in the empty dataframe
    st.dataframe(data) 
    
    # persist state of dataframe
    session_state = SessionState.get(df=data)
    
    # random value to append; could be a num_input widget if you want
    random_value = np.random.randn()
    
    if st.button("Append random value"):
        # update dataframe state
        session_state.df = session_state.df.append({'Random': random_value}, ignore_index=True)
        st.text("Updated dataframe")
        st.dataframe(session_state.df)
    
    # still empty as state is not persisted
    st.text("Original dataframe")
    st.dataframe(data)

if __name__ == '__main__':
  main()
