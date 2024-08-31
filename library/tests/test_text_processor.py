import unittest
import re

class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.cleaned_text = None

    def clean_text(self):
        self.cleaned_text = re.sub(r'[^a-zA-Z\s]', '', self.text).lower().strip()

    def remove_stop_words(self, stop_words):
        if self.cleaned_text is None:
            self.clean_text()
        words = self.cleaned_text.split()
        filtered_words = [word for word in words if word not in stop_words]
        self.cleaned_text = ' '.join(filtered_words)

class TestTextProcessor(unittest.TestCase):

    def test_clean_text_removes_non_alpha_characters(self):
        processor = TextProcessor("Hello, World!")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "hello world")

    def test_clean_text_converts_to_lowercase(self):
        processor = TextProcessor("123 ABC!!!")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "abc")

    def test_clean_text_with_empty_string(self):
        processor = TextProcessor("")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "")

    def test_remove_stop_words(self):
        processor = TextProcessor("this is a test")
        processor.remove_stop_words(['this', 'is'])
        self.assertEqual(processor.cleaned_text, "a test")

    def test_remove_stop_words_without_clean_text_called_first(self):
        processor = TextProcessor("This is a Test!")
        processor.remove_stop_words(['this', 'is'])
        self.assertEqual(processor.cleaned_text, "a test")

    def test_remove_stop_words_when_no_stop_words_present(self):
        processor = TextProcessor("hello world")
        processor.remove_stop_words(['not', 'present'])
        self.assertEqual(processor.cleaned_text, "hello world")

if __name__ == '__main__':
    unittest.main()