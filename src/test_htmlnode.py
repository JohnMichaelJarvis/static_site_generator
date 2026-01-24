#!usr/bin/env python3

import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "Hello world!", props={"style":"color: red; font-size: 16px"})
        node2 = HTMLNode("p", "Hello world!", props={"style":"color: red; font-size: 16px"})
        
        self.assertEqual(node, node2)

    def test_eq_false_attr(self):
        node = HTMLNode("p", "Hello world!", props={"style":"color: red; font-size: 16px"})
        node2 = HTMLNode("p", "Hello world!", props={"style":"color: blue; font-size: 16px"})
        self.assertNotEqual(node, node2)

    def test_eq_false_child(self):
        node = HTMLNode("p", "Hello world!", props={"style":"color: red; font-size: 16px"})
        node2 = HTMLNode("p", children=["p", "a"], props={"style":"color: red; font-size: 16px"})
        self.assertNotEqual(node, node2)

    def test_eq_false_tag(self):
        node = HTMLNode("p", "Hello world!", props={"style":"color: red; font-size: 16px"})
        node2 = HTMLNode("p", children=["p", "a"], props={"style":"color: red; font-size: 16px"})
        self.assertNotEqual(node, node2)

    def test_eq_children(self):
        node = HTMLNode("p", children=["p", "a"], props={"style":"color: red; font-size: 16px"})
        node2 = HTMLNode("p", children=["p", "a"], props={"style":"color: red; font-size: 16px"})
         
        self.assertEqual(node, node2)

    def test_none_passed(self):
        node = HTMLNode()
        for data_member in [node.tag, node.value, node.children, node.props]:
            self.assertIsNone(data_member)
         
    def test_repr(self):
       node = HTMLNode("p", "Hello world!", props={"style":"color: red; font-size: 16px"})
       self.assertEqual('Tag: <p>\nValue: Hello world!\nChildren:\n None\nProps:\n  style="color:red; font-size: 16px"', repr(node))

if __name__ == "__main__":
    unittest.main()
