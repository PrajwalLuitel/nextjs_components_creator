from typing import Any
import requests
from private_variables import *
import re


context = """
You are a professional web developer and you are creating a web application using NextJs. You have a bunch of pre built components which can be reused to create the required application for the client. The client has some requirements and provides his requirement and asks questions. According to that, you've got to firstly identify the required components and then modify the content inside those components to match the user requirements.
"""

class CreateComponentContent:

    def __call__(self, components, user_prompt) -> Any:

        url = "https://open-ai21.p.rapidapi.com/qa"

        payload = {
            "question": f"Select the required components from the below as per the user requirement : \nComponents that you have: {components}, \nUser requirement: {user_prompt}\n\nPlease return a python list and no any additional texts.",
            "context": context
                }
        
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": RAPID_API_HOST
        }

        response = requests.post(url, json=payload, headers=headers)
        
        raw_result = response.json()['result']

        pattern = r'\[([^\]]*)\]'
        match = re.search(pattern, raw_result)

        grouped_match = match.group(1)

        splitted_match = grouped_match.split(",")

        final_result = [el.split("'") for el in splitted_match]
        
        return final_result




class GetRelevantComponents:
    def __call__(self, component_name, component_content, user_prompt) -> Any:
        url = "https://open-ai21.p.rapidapi.com/qa"

        payload = {
            "question": f"""Following is one of the components required for the application. 
            Do not modify the code as it is just a {component_name}. 
            Just modify the text elements such that a {component_name} would look like and do nothing else. Do not return any extra words as well. 
            
            The component content: {component_content}
            
            User requirement:{user_prompt}. 
            
            No extra word except the code.
            """,
            "context": context
            }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": RAPID_API_HOST
        }

        response = requests.post(url, json=payload, headers=headers)

        return response.json()['result']
