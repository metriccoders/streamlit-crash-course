import streamlit as st

st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', caption='Streamlit Logo')
st.title("This is a crash course from Metric Coders: www.metriccoders.com")
st.header("Welcome to Streamlit Crash Course by Metric Coders")

st.subheader("Learn the basics")

st.text("This is the simplest of all courses")

st.markdown("**This is a markdown text in streamlit**")

st.code('print("This is a python print statement)', language='python')
st.code('print(10 * 20)', language='python')

name = st.text_input("What is your name?")
st.write(f"Hello {name}")

ans = st.text_input("How is Metric Coders going?")
st.write(f"Ans: {ans}")

ans = st.text_input("Is it good?")
st.write(f"Tell me: {ans}")

ans_paragraph = st.text_area("Tell me about yourself?")
st.write(f"About yourself:{ans_paragraph}")

revenue = st.selectbox("Select your revenue?", ["$0", "$1-$100,000", ">$100,000"])
st.write(f"You selected: {revenue}")

city = st.selectbox("Select your city:", ["Bengaluru", "Sydney", "Singapore"])
st.write(f"You selected: {city}")

countries = st.multiselect("How many countries:", ["India", "Singapore", "USA"])
st.write(f"Countries: {countries}")

temperature = st.slider("Select the temperature now:", 0, 45, 25, 1)
st.write(f"Temperature:{temperature}")

distance = st.slider("What's the distance to your house?", 1, 100, 35, 10)
st.write(f"Distance:{distance}")

todays_date = st.date_input("Today's date")
st.write(f"today's date: {todays_date}")

todays_time = st.time_input("Time now:")
st.write(f"Time now: {todays_time}")


st.video('https://www.youtube.com/watch?v=B2iAodr0fOo')

st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')

st.sidebar.title("Metric Coders")
st.sidebar.text_input("Enter your name here:")

st.sidebar.button("Submit")
st.sidebar.text("Option 1")


col1, col2, col3 = st.columns(3)
col1.header("Column 1")
col2.header("Column 2")
col3.header("Column 3")
col1.text("Text 1")
col2.text("Text 2")
col3.text("Text 3")
col1.text_input("Text input 1")
col2.text_input("Text input 2")
col3.text_input("Text input 3")

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("Tab 1 content")

with tab2:
    st.write("Tab 2 content")

with tab3:
    st.write("Tab 3 content")


@st.cache_data
def expensive_func(a, b):
    return a * b

res = expensive_func(10, 20)
st.write(res)

@st.cache_resource
def another_expensive_func(a, b, c):
    return a * b * c


res = another_expensive_func(10, 20, 30)
st.write(res)

if "count" not in st.session_state:
    st.session_state.count = 0

incr = st.button("Increase")
if incr:
    st.session_state.count += 1

st.write(f"Counter: {st.session_state.count}")