#! usr/bin/env Python3

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter

import re




def extract_markdown_images(text: str) -> list[tuple]:

    extracted_pairs = []

    matches = re.findall(r"\[(.*?)\]{1}\(\w{1}.()\)", text)
    for match in matches:
        alt_text = re.findall(r"\[(.*?)\]", match)
        file_name = re.findall(r"\(.(gif|tft|jpe?g|bmp|hei.*|svg)\)", match)
        extracted_pairs.append((alt_text, file_name))
    
    return  extracted_pairs

def extract_markdown_links(text: str) -> list[tuple]:

    extracted_pairs = []

    matches = re.findall(r"\[(.*?)\]{1}\(https?:\/\/www\.(.*?)(\.\w{2,9}){1,2}\)", text)
    for match in matches:
        alt_text = re.findall(r"\[(.*?)\]", match)
        link_url = re.findall(r"\(https?:\/\/www\.(.*?)(\.\w{2,9}){1,2}\)", match)
        extracted_pairs.append((alt_text, link_url))
    
    return  extracted_pairs
