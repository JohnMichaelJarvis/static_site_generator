from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

# node = TextNode("This is a text node", TextType.ITALIC)

# print(f"({repr(node.text)}, {repr(node.text_type.value)}, {repr(node.url)})")

node = LeafNode("p", "Hello, World!", {"style":"color: red; font-size: 16px"})

# print(node)
print(node)
# print('Tag: <p>\nValue: Hello, World!\nProps:\n  style="color:red; font-size: 16px"')