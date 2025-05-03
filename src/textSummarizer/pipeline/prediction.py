from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
    
    def predict(self, text: str) -> str:
        """
        Predict the summary of the given text using the pre-trained model.
        
        Args:
            text (str): The input text to summarize.
        
        Returns:
            str: The predicted summary of the input text.
        """
        # Load the tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 4, "max_length": 128}

        pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)
        
        print("Dialogue: \n", text)

        output = pipe(text, **gen_kwargs)[0]['summary_text']
        print("\nModel Summary: \n", output)

        return output