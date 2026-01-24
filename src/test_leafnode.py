#!usr/bin/env python3

import unittest

from leafnode import LeafNode
import leafnode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "Hello, World!", props={"style":"color: red; font-size: 16px"})
        node2 = LeafNode("p", "Hello, World!", props={"style":"color: red; font-size: 16px"})
        
        self.assertEqual(node, node2)

    def test_eq_false_attr(self):
        node = LeafNode("p", "Hello, World!", props={"style":"color: red; font-size: 16px"})
        node2 = LeafNode("p", "Hello, World!", props={"style":"color: blue; font-size: 16px"})
        self.assertNotEqual(node, node2)

    def test_eq_false_tag(self):
        node = LeafNode("p", "Hello, World!", props={"style":"color: red; font-size: 16px"})
        node2 = LeafNode("p", "Go away, world!", props={"style":"color: red; font-size: 16px"})
        self.assertNotEqual(node, node2)

    def leaf_to_html(self):
        node = LeafNode("p", "Hello, world!", {"style":"color: red; font-size: 16px"})
        self.assertEqual(node.to_html, "<p>Hello, world!</p>")


    def test_to_html_tag_is_none(self):
        node = LeafNode(None, "Hello, world!", {"style":"color: red; font-size: 16px"})
        self.assertEqual(node.to_html(), "None")
         
    def test_to_html_value_is_none(self):
        node = LeafNode("p", None, {"style":"color: red; font-size: 16px"})
        self.assertRaises(ValueError)

    def test_repr(self):
       node = LeafNode("p", "Hello, World!", props={"style":"color: red; font-size: 16px"})
       self.assertEqual('Tag: <p>\nValue: Hello, World!\nProps:\n  style="color:red; font-size: 16px"', repr(node))

if __name__ == "__main__":
    unittest.main()
