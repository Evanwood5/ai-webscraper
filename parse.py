#llm component
#donwloading ollama, this allows for us to run opensource LLMs locally on your own computer 
#dont need any api tokens from open AI

from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

#template from git hub

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)


model = OllamaLLM(model="llama3.1")

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_result = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({
            "dom_content": chunk,
            "parse_description": parse_description
        })
        # output so you know something is loading and happening
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_result.append(response)

    return parsed_result  

