from textnode import TextNode, TextType

def main():
    text_node = TextNode('Dummy text', TextType.BOLD_TEXT, 'google.com')
    print(text_node)


if __name__ == "__main__":
    main()
