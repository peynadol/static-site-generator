
import unittest
from textnode import TextNode  
from utils import textnode_to_html_node
from textnode import TextType
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):

    def test_text_node_equality(self):
        # Creating two identical TextNode objects
        text_node1 = TextNode("This is some text", TextType.NORMAL_TEXT, "http://example.com")
        text_node2 = TextNode("This is some text", TextType.NORMAL_TEXT, "http://example.com")
        
        # Test for equality
        self.assertEqual(text_node1, text_node2)
    
    def test_text_node_inequality(self):
        # Creating two different TextNode objects
        text_node1 = TextNode("This is some text", TextType.NORMAL_TEXT, "http://example.com")
        text_node2 = TextNode("This is some different text", TextType.NORMAL_TEXT, "http://example.com")
        
        # Test for inequality
        self.assertNotEqual(text_node1, text_node2)
    
    def test_repr(self):
        # Creating a TextNode and checking its string representation
        text_node = TextNode("Sample text", TextType.ITALIC_TEXT, "http://example.com")
        
        # Test the __repr__ method
        self.assertEqual(repr(text_node), "TextNode(Sample text, italic, http://example.com)")

    def test_invalid_text_type(self):
        # Test with an invalid TextType
        with self.assertRaises(ValueError):
            text_node = TextNode("Invalid type", "nonexistent_type")
    
    def test_url(self):
        # Test TextNode with URL
        text_node = TextNode("Link Text", TextType.LINKS, "http://example.com")
        self.assertEqual(text_node.url, "http://example.com")

    def test_no_url(self):
        # Test TextNode without URL (default should be None)
        text_node = TextNode("Plain Text", TextType.NORMAL_TEXT)
        self.assertIsNone(text_node.url)


if __name__ == '__main__':
    unittest.main()
