from marker.v2.schema.text.line import Line
from tests.utils import setup_pdf_document


def test_document_builder():
    pdf_document = setup_pdf_document(
        "adversarial.pdf",
        document_builder_config={
            "force_ocr": False
        }
    )

    first_page = pdf_document.pages[0]
    assert first_page.structure[0] == '/page/0/Section-header/0'

    first_block = first_page.get_block(first_page.structure[0])
    assert first_block.text_extraction_method == 'surya'
    assert first_block.block_type == 'Section-header'
    first_text_block: Line = first_page.get_block(first_block.structure[0])
    assert first_text_block.block_type == 'Line'
    first_span = first_page.get_block(first_text_block.structure[0])
    assert first_span.block_type == 'Span'
    assert first_span.text == 'Subspace Adversarial Training'


if __name__ == "__main__":
    test_document_builder()
