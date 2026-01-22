from textnode import TextNode, TextType

node = TextNode("This is a text node", TextType.ITALIC)

print(f"({repr(node.text)}, {repr(node.text_type.value)}, {repr(node.url)})")