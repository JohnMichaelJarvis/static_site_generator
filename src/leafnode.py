from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
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
            return "None"
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