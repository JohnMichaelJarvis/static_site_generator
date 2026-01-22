#!/usr/bin/env python3

from textnode import TextNode, TextType


def main():
    test_node = TextNode("**Test**", TextType.BOLD, "https://test.com")  

    print(test_node)


if __name__ == "__main__":
    main()
