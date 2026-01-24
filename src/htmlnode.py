#!usr/bin/env Python3

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Represent a "node" in an HTML document tree. It can be block level or inline, and is designed to only output HTML.

        Args:
            tag (str): Represents the HTML tag name (e.g. "P", "a", "h1", etc.). 
                -   Defaults to None: An HTMLNode without a tag will render as raw text.
            value (str): Represents the value of the HTML tag (e.g. the text inside a paragraph). 
                -   Defaults to None: An HTMLNode without a value will be assumed to have children.
            children (list): Holds HTMLNode objects r epresenting the children of this node. 
                -   Defaults to None: An HTMLNode without children will be assumed to have a value.
            props (dict): Holds key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://google.com"}. 
                -   Defaults to None: an HTMLNode without props will be assumed to have no attributes.
        """

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child classes should override this method.")
    
    def __eq__(self, other):
        """Check if two HTMLNode objects are equal"""
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and 
                self.value == other.value and 
                self.children == other.children and 
                self.props == other.props)
    
    def props_to_html(self):
        """ Returns a formatted string representing the HTML attributes of the node. For example, if self.props is:
            {
                "href": "https://www.google.com",
                "target": "_blank"
            }
            Then self.props_to_html() should return ' href="https://www.google.com" target="_blank"', with a leading space character included before both "href" and "target".
                
            If self.props is None or empty, then an empty string is returned.           
                """
        if not self.props or self.props is None:
            return ""

        return "".join([f' {key.strip('"')}="{value}"' for key, value in self.props.items()])

    
    
    def __repr__(self):
        """Print information regarding an HTMLNode's tag, value, children and props to the console"""
        MAX_LENGTH = 70
        tag_msg = self.tag if self.tag is not None else "None"
        value_msg = self.value[:MAX_LENGTH] if self.value is not None else "None"
        children_msg = str(self.children) if self.children is not None else "None"
        
        props = self.props_to_html()
        props_msg = "".join(props.split(maxsplit=1)) if props else "None"
        
        
        msg = "\n".join([f"Tag: <{tag_msg}>", f"Value: {value_msg}", "Children:", f" {children_msg}","Props:", f"  {props_msg}"])

        return msg


