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

if __name__ == '__main__':
  main()
