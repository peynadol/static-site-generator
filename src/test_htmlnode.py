import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main
