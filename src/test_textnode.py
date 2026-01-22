#!usr/bin/env/ python3

import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node.url, None)

    def test_dif_type(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(
            print(node), "TextNode('This is a text node', 'italic', 'None')"
        )


if __name__ == "__main__":
    unittest.main()
