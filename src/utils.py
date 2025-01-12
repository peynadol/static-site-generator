from htmlnode import LeafNode
from textnode import TextType

def textnode_to_html_node(textnode):
    if textnode.text_type == TextType.NORMAL_TEXT:
        return LeafNode(None, textnode.value, None)
    
    elif textnode.text_type == TextType.BOLD_TEXT:
        return LeafNode("b", textnode.value, None)

    elif textnode.text_type == TextType.ITALIC_TEXT:
        return LeafNode("i", textnode.value, None)

    elif textnode.text_type == TextType.CODE_TEXT:
        return LeafNode("code", textnode.value, None)

    elif textnode.text_type == TextType.IMAGES:
        if 'src' not in textnode.props or 'alt' not in textnode.props:
            raise ValueError("Image type TextNode must have src and alt attributes")
        return LeafNode("img", "", {"src": textnode.props['src'], 'alt': textnode.props['alt']})

    elif textnode.text_type == TextType.LINKS:
        if 'href' not in textnode.props:
            raise ValueError("Link type TextNode must have an 'href' attribute.")
        return LeafNode("a", textnode.value, {"href": textnode.props['href']})
    else:
        raise ValueError("Invalid TextType: The TextNode type is not recognised.")
