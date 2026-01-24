#!/usr/bin/env python3

from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    test_node = TextNode("**Test**", TextType.BOLD, "https://test.com")  

    test_node2 = HTMLNode("p", "Hello world!", props={"style":"color: red; font-size: 16px"})
    print(test_node2.props_to_html())
    print(test_node2)


if __name__ == "__main__":
    main()
