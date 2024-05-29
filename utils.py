import requests
from private_variables import *


class CreateComponentContent():
    url = "https://open-ai21.p.rapidapi.com/qa"

    payload = {
        "question": "tell body length of cheetah",
        "context": "The cheetah (Acinonyx jubatus) is a large cat native to Africa, central Iran and India (where it was reintroduced in 2022 after becoming extinct in the country in the 1950s). The cheetah is the fastest land animal, capable of running at 80 to 98 km/h (50 to 61 mph); as such, it has evolved specialized adaptations for speed, including a light build, long thin legs and a long tail. It typically reaches 67 to 94 cm (26 to 37 in) at the shoulder, and the head-and-body length is between 1.1 and 1.5 m (3 ft 7 in and 4 ft 11 in). Adults weigh between 21 and 72 kg (46 and 159 lb). Its head is small and rounded, with a short snout and black tear-like facial streaks. The coat is typically tawny to creamy white or pale buff and is mostly covered with evenly spaced, solid black spots. Four subspecies are recognised. This photograph, taken in the Okavango Delta in Botswana, shows two young cheetah brothers grooming each other after feeding."
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": RAPID_API_HOST
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())