import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html_node = HTMLNode("p", "Hello World", "list goes here", {
        "href": "test href",
        "target": "_blank",})

        html_node2 = HTMLNode("p", "Hello World", "list goes here", {
        "href": "test href",
        "target": "_blank",})
        self.assertEqual(html_node, html_node2)


    def test_not_eq(self):
        html_node = HTMLNode("p", "Hello World", "list goes here", {
        "href": "test href",
        "target": "_blank",})

        html_node2 = HTMLNode("a", "Hello World", "list goes here", {
        "href": "test href",
        "target": "_blank",})
        self.assertNotEqual(html_node, html_node2)

    def test_is_none(self):
        html_node = HTMLNode()
        self.assertIsNone(html_node.tag)


    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main
