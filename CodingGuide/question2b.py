'''
Design a document generator using the Builder Design
Pattern. Create a DocumentBuilder that creates documents of various types (e.g., PDF,
HTML, Plain Text). Implement the builder methods to format the document content and
structure according to the chosen type. Demonstrate how the Builder Design Pattern
allows for the creation of different document formats without tightly coupling the
document generation logic.
'''

# Document class to represent the final document
from abc import ABC , abstractmethod

class Document:
    def __init__(self):
        self.content = ""

    def add_content(self, content):
        self.content += content

    def __str__(self):
        return self.content


# Abstract DocumentBuilder class
class DocumentBuilder(ABC):
    def create_document(self):
        self.document = Document()

    @abstractmethod
    def add_heading(self, text):
        pass

    @abstractmethod
    def add_paragraph(self, text):
        pass

    @abstractmethod
    def add_line_break(self):
        pass

    def get_document(self):
        return self.document


# Concrete HTMLDocumentBuilder implementing DocumentBuilder
class HTMLDocumentBuilder(DocumentBuilder):
    def add_heading(self, text):
        self.document.add_content(f"<h1>{text}</h1>")

    def add_paragraph(self, text):
        self.document.add_content(f"<p>{text}</p>")

    def add_line_break(self):
        self.document.add_content("<br>")


# Director class to control the construction process
class DocumentDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_document(self):
        self.builder.create_document()
        self.builder.add_heading("Builder Design Pattern Example")
        self.builder.add_paragraph("This is an example of using the Builder Design Pattern to generate HTML documents.")
        self.builder.add_line_break()
        self.builder.add_paragraph("Builders allow for flexible and modular creation of different document formats.")
        self.builder.add_line_break()
        self.builder.add_paragraph("End of the example.")
        return self.builder.get_document()


# Client code
if __name__ == "__main__":
    html_builder = HTMLDocumentBuilder()
    director = DocumentDirector(html_builder)
    html_document = director.build_document()

    print(html_document)