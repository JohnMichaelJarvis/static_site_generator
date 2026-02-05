#!usr/bin/env Python3

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Represent a "node" in an HTML document tree. It can be block level or inline, and is designed to only output HTML.

        Args:
            tag (str): Represents the HTML tag name (e.g. "p", "a", "h1", etc.). 
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

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Initialize from parent class
        super().__init__(tag, value, None, props)
        

    def to_html(self):
        """
        Renders a LeafNode as an html string.

        Raises:
            ValueError: If self.value is None

        Returns:
            str: A string with both self.tag and self.value formatted in HTML or "None" if self.tag is None. 
        """

        if self.value is None:
            raise ValueError(f"\nValueError: {self}\nThe LeafNode has a value of {self.value}. All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        """Print information regarding an LeafNode's tag, value, and props to the console"""
        MAX_LENGTH = 70
        tag_msg = self.tag if self.tag is not None else "None"
        value_msg = self.value[:MAX_LENGTH] if self.value is not None else "None"
        props = self.props_to_html()
        props_msg = "".join(props.split(maxsplit=1)) if props else "None Passed"
        
        msg = "\n".join([f"Tag: <{tag_msg}>", f"Value: {value_msg}","Props:", f"  {props_msg}"])

        return msg
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        """Convert the ParentNode and its children to an HTML string.
        Recursively converts this ParentNode and all its children to their HTML
        representations, wrapping the child HTML content with the parent's tag.
        
        Raises:
            ValueError: If the tag is None. All parent nodes must have a valid tag.
            ValueError: If children is None. All parent nodes must have at least one child.
        Returns:
            str: An HTML string with the parent tag wrapping the concatenated HTML representations of all children."""
     
        if self.tag is None:
            raise ValueError(f"\nValueError: {self}\nThe ParentNode's tag has a value of {self.tag}. All parent nodes must have a tag.")
        if self.children is None:
            raise ValueError(f"\nValueError: {self}\nThe ParentNode has a children value of {self.children}. All parent nodes must have a least one associated child.")
    
        return f"<{self.tag}>"+ "".join([child.to_html() for child in self.children]) + f"</{self.tag}>"
    
