import nlpcloud
class API:
    def __init__(self):
        self.client = nlpcloud.Client(
            "finetuned-llama-3-70b",
            "c1bb7a61dddcefba1f525f071b737a73db3d5fc4",
            gpu=True
        )

    def sentiment_analysis(self, text):
        return self.client.sentiment(text, target="NLP Cloud")


