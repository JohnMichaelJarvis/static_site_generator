#!usr/bin/env python3

import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode



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
        self.assertEqual(node.to_html(), node.value)
         
    def test_to_html_value_is_none(self):
        node = LeafNode("p", None, {"style":"color: red; font-size: 16px"})
        self.assertRaises(ValueError)

    def test_repr(self):
       node = LeafNode("p", "Hello, World!", props={"style":"color: red; font-size: 16px"})
       self.assertEqual('Tag: <p>\nValue: Hello, World!\nProps:\n  style="color:red; font-size: 16px"', repr(node))

class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_missing_children(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_with_missing_grandchildren(self):
        child_node = ParentNode("span", [None, None]) 
        parent_node = ParentNode("div", child_node)
        self.assertRaises(TypeError, parent_node.to_html)

    def test_to_html_with_none_children_in_list(self):
        """Test that None children in the list raise an error when to_html is called"""
        child_node = ParentNode("span", [None, None])
        parent_node = ParentNode("div", [child_node])  # Pass as list
        self.assertRaises(AttributeError, parent_node.to_html)  # None has no to_html() method

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
class Test_TextNode_To_HTMLNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a code node")

    def test_link( self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.wikipedia.org")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://www.wikipedia.org"})

    def test_image( self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/250px-Python-logo-notext.svg.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/250px-Python-logo-notext.svg.png", "alt": "This is an image node" })



if __name__ == "__main__":
    unittest.main()
