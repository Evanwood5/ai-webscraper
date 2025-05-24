
import streamlit as st
from scrape import (
scrape_website,
split_dom_content,
clean_body_content,
extract_body_content,


)

from parse import parse_with_ollama

# title
st.title("AI Web Scraper")
#text input
url = st.text_input("Enter a Website URL: ")

#if this button is clicked then proceed
if st.button("Scrape Site"):
	st.write("Scrape Site")

	result = scrape_website(url)
	body_content = extract_body_content(result)
	cleaned_content = clean_body_content(body_content)
	st.session_state.dom_content = cleaned_content
	
	#expander allows us to view more content
	with st.expander("View DOM Content"):
		st.text_area("DOM Content", cleaned_content, height=300)


#promp user so we can now begin parsing the content
if "dom_content" in st.session_state:
	parse_description = st.text_area("describe what you want to parse?")
	
	if st.button("Parse Content"):
		if parse_description:
			st.write("parsing the content")

			dom_chunks = split_dom_content(st.session_state.dom_content)

			result = parse_with_ollama(dom_chunks,parse_description)
			st.write(result)