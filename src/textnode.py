from enum import Enum


class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """Compare self to another TextNode"""

        compare_text: bool = self.text == other.text
        compare_text_type: bool = self.text_type == other.text_type
        compare_url: bool = self.url == other.url

        if compare_text and compare_text_type and compare_url:
            return True

        return False

    def __repr__(self):
        """Return a string representation of the TextNode object."""
        return f"TextNode{self.text, self.text_type, self.url}"
