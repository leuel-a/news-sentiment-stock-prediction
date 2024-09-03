import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class TextProcessor:
    """This class removes stop words and applies sentiment scores for texts"""

    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')

        self.stop_words = set(stopwords.words('english'))

    def remove_stop_words(self, text: str) -> str:
        """Removes stop words from the provided text

        Args:
            :param text: The text string to process
            :type text: str

        Returns:
            :return: The text with stop words removed
            :rtype: str
        """

        words = word_tokenize(text.lower())
        filtered_words = [word for word in words if word not in self.stop_words]
        return ' '.join(filtered_words)
