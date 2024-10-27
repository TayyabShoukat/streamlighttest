import streamlit as st
import pandas as pd

# Adding title of your app
st.title('Single Page App')

# adding simple text
st.write('Here is a simple text')

# user input
number = st.slider('Pick a number', 0, 100, 10)

# print the text of number
st.write(f'You selected: {number}')

# adding a button
if st.button('Greeting'):
    st.write('Hi, hello there')
else:
    st.write('Goodbye')

# add radio button with options
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

# print the text of genre
st.write(f'You selected: {genre}')


# add a drop down list on the left sidebar
option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

# add your whatsapp number
st.sidebar.text_input('Enter your Name')

# add a file uploader
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# create a line plot
# Plotting
# Create a DataFrame
data = pd.DataFrame({
  'first column': list(range(1, 11,1)),
  'second column': list(range(2, 22, 2)),  # Adjusted to range 2 to 20
  'Third column': list(range(3, 33, 3)),  # Adjusted to range 3 to 30
  'Fourth column': [x ** 2 for x in range(1, 11)]
})

# Display the line chart
st.line_chart(data)
