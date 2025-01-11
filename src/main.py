from textnode import TextNode, TextType
import htmlnode

def main():
    text_node = TextNode('Dummy text', TextType.BOLD_TEXT, 'google.com')
    print(text_node)

    html_node = htmlnode.HTMLNode("p", "Hello World", ["test_obj"], {
        "href": "test href",
        "target": "_blank",
    })
    print(html_node)
    print(html_node.props_to_html())
if __name__ == "__main__":
    main()
