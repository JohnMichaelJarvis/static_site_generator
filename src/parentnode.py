#!usr/bin/env Python3

from htmlnode import HTMLNode

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
    