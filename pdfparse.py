from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextLine, LTChar
from html import escape


def is_bold(element: LTTextBox | LTTextLine):
    """Check if the element is bold based on its font size and name."""
    text = element.get_text()
    if "Foreword" in text:
        print(text)
    for char in element:
        if "Foreword" in text:
            print("char: ", char)
            print(isinstance(char, LTChar))
        if isinstance(char, LTChar):
            font = char.fontname.lower()
            if "bold" in font:
                return True
    return False


def is_italic(element):
    """Check if the element is italic based on its font name."""
    for char in element:
        if isinstance(char, LTChar):
            font = char.fontname.lower()
            if "italic" in font or "oblique" in font:
                return True
    return False


def extract_text_and_convert_to_html(pdf_path):
    html_content = ""
    page_count = 0
    # Extract pages from the PDF
    for page_layout in extract_pages(pdf_path):
        # print(page_layout)
        print("page count: ", page_count)
        for element in page_layout:
            if isinstance(element, (LTTextBox, LTTextLine)):
                text = element.get_text()
                class_name = ""
                # Check if the text is bold
                if is_bold(element):
                    class_name += "font-bold "
                if is_italic(element):
                    class_name += "italic"
                html_content += f'<span className="{
                    class_name}">{escape(text)}</span><br>\n'
        page_count += 1
    return html_content


# Usage
pdf_path = 'siksastaka.pdf'
html = extract_text_and_convert_to_html(pdf_path)

# Save to an HTML file
with open('output.html', 'w') as f:
    f.write(html)
