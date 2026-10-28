import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    request_header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input = {
            "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, json=json_input, headers=request_header)

        response.raise_for_status() # Check for http errors
        formatted_response = json.loads(response.text)

        emotions = formatted_response['emotionPredictions'][0]['emotion']

        dominant_emotion = max(emotions, key = emotions.get)

        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion,
        }

    except requests.exceptions.Timeout:
        return {"error": "The request timed out. Please try again later."}
        
    except requests.exceptions.HTTPError as http_err:
        # Returns specific server errors (e.g., if status code is 400 due to empty input)
        return {"error": f"HTTP error occurred: {http_err}", "status_code": response.status_code}
        
    except requests.exceptions.RequestException as req_err:
        # Catches other network errors like connection failure or bad URL
        return {"error": f"Network error occurred: {req_err}"}
        
    except (KeyError, IndexError, ValueError) as data_err:
        # Catches structural changes, missing keys, or empty dictionary max() errors
        return {"error": f"Data parsing error: {data_err}"}

