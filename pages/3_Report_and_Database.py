import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from urllib.parse import urlparse

from api import get_collection, set_the_data

fetch = st.button("Fetch Collection")
if fetch:
    web_col_dict = get_collection()
    for web in web_col_dict:
        st.write("---")
        st.write("Website Name: ", web_col_dict[web]['name'])
        st.write("Site URL: ", web_col_dict[web]['url'])
        st.write("Trust Score by Perry Detector: ", web_col_dict[web]['tScore'])
        st.write("Unique Patterns found: ", web_col_dict[web]['uniquePattern'])
        st.write("Total Pattern Found: ", web_col_dict[web]['tPattern'])

st.divider()
with st.expander("Report a Dark Pattern"):
    with st.form("my_form"):
        st.write("Enter the details of the website you want to report.")
        site_name = st.text_input("Website Name")
        site_url = st.text_input("Website URL")
        trust_score = st.slider("Trust Score", 0, 100, 0)
        unique_pattern = st.text_input("Unique Pattern")
        total_pattern = st.text_input("Total Pattern")
        submitted = st.form_submit_button("Submit")
        if submitted:
            set_the_data(site_name, site_url, trust_score, unique_pattern, total_pattern)
            st.write("Submitted")

st.divider()
st.subheader("Database")
st.write("The following table contains the data of all the websites that have been reported.")
st.write("You can also download the data as a CSV file.")
csv_data_file = "csvdata/dark-patterns.csv"

data = pd.read_csv("csvdata/dark-patterns.csv")
st.dataframe(data)

# Extracting domain from the 'Website Page' column
data['Domain'] = data['Website Page'].apply(lambda x: urlparse(x).netloc)

# Counting the frequency of each domain and sorting them from most to least occurrences
domain_counts = data['Domain'].value_counts().sort_values(ascending=False)

st.divider()
st.subheader("Domain Counts")
st.write(domain_counts)

fig, ax = plt.subplots()
# only show top 10
ax.bar(domain_counts.index[:10], domain_counts.values[:10])
plt.title('Distribution of Domains')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Count')
plt.xlabel('Domain')
st.pyplot(fig)

st.divider()
st.subheader("Insights")
st.write("The following graphs show the distribution of the data collected.")

category_counts = data['Pattern Category'].value_counts()
type_counts = data['Pattern Type'].value_counts()
deceptive_counts = data['Deceptive?'].value_counts()

fig, ax = plt.subplots()
ax.bar(category_counts.index, category_counts.values)
plt.title('Distribution of Pattern Categories')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Count')
plt.xlabel('Pattern Category')
st.pyplot(fig)

fig, ax = plt.subplots()
ax.bar(type_counts.index, type_counts.values)
plt.title('Distribution of Pattern Types')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Count')
plt.xlabel('Pattern Type')
st.pyplot(fig)
