# Required Packages
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from string import punctuation
import re

# run these commands in your command prompt before executing the code
#-----------------------------------
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
#-----------------------------------

class TextPreprocess:
     port_stemmer = PorterStemmer()
     wordnet_lemmatizer = WordNetLemmatizer()

     def __int__(self):
          pass

     def to_lower(self,text):
          text_lower = text.lower()
          return text_lower

     def remove_numbers(self,text):
          output = ''.join(word for word in text if not word.isdigit())
          return output

     def remove_punctuation(self,text):
          output = ''.join(c for c in text if c not in punctuation)
          return output

     def remove_Tags(self,text):
          cleaned_text = re.sub('<[^<]+?>', '', text)
          return cleaned_text

     def remove_stopwords(self,sentence):
          stop_words = stopwords.words('english')
          output = ' '.join([w for w in nltk.word_tokenize(sentence) if not w in stop_words])
          return output

     def tokenize_word(self,text):
          output = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
          return output

     def stemmer(self, tokenList):
          output = [self.port_stemmer.stem(word) for word in tokenList]
          return output

     def lemmatizer(self,tokenList):
          lemmatized_word = [self.wordnet_lemmatizer.lemmatize(word) for word in tokenList]
          output = " ".join(lemmatized_word)
          return output

     def normalizer(self, text):
          # Making all text to Lower case...
          lowerText = self.to_lower(text)
          # Removing Punctuation...
          clean_text = self.remove_punctuation(lowerText)
          # Removing numbers...
          clean_text = self.remove_numbers(clean_text)
          # Removing HTML tags...
          clean_text = self.remove_Tags(clean_text)
          # Removing Stopwords from text...
          clean_text = self.remove_stopwords(clean_text)
          # Splitting sentences into Tokens...
          wordTokens = self.tokenize_word(clean_text)
          # Stemming...
          stemmedList = self.stemmer(wordTokens)
          # Lemmatizing...
          lemmatizedText = self.lemmatizer(stemmedList)

          return lemmatizedText


