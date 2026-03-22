import requests

def emotion_detector(text):
    """
    Detect emotions from text and return formatted output.
    """

    if not text:
        return {"error": "Invalid input! Try again."}

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    data = {
        "raw_document": {
            "text": text
        }
    }

    response = requests.post(url, json=data, headers=headers)
    result = response.json()

    emotions = result["emotionPredictions"][0]["emotion"]

    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions.get("anger", 0),
        "disgust": emotions.get("disgust", 0),
        "fear": emotions.get("fear", 0),
        "joy": emotions.get("joy", 0),
        "sadness": emotions.get("sadness", 0),
        "dominant_emotion": dominant_emotion
    }
