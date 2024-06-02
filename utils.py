from typing import Any
import requests
from private_variables import *


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

        print(response.json())



class GetRelevantComponents:
    def __call__(self, component_name, component_content, user_prompt) -> Any:
        url = "https://open-ai21.p.rapidapi.com/qa"

        payload = {
            "question": f"Following is one of the components required for the application. Please modify the component to meet the user requirement. Do not add any additional feature as it is a {component_name}. Just modify the text elements and do nothing else. Do not return any extra words as well. \n\nThe component content: {component_content}\n\nUser requirement:{user_prompt}",
            "context": context
            }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": RAPID_API_HOST
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.json())