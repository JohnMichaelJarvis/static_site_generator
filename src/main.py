#!/usr/bin/env python3

from textnode import TextNode


def main():
    test_node = TextNode(text="**Test**", text_type="bold", url="https://test.com")  # type: ignore

    print(test_node)


if __name__ == "__main__":
    main()
