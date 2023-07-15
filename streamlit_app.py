import streamlit as st
import datetime

# def calculate_date(date, days):
#   new_date = datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=days)
#   return new_date.strftime('%Y-%m-%d')

def main():
  st.title('ILR Calculator')
  st.date_input("Date of Visa")
  st.write('Visa Date:', d)
  # new_date = calculate_date(date, 1799)
  # st.write('The date 1799 days from {} is {}'.format(date, new_date))

if __name__ == '__main__':
  main()
