


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError


    def props_to_html(self):
        # this will take in a k,v dict
        # i need to convert that to a string representation
        # important to keep space between k and v
        # href="https://www.google.com" target="_blank"

        for k, v in self.props.items():
            return f" {k}=\"{v}\" {k}=\"{v}\""

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        elif self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        else:
            return False

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
