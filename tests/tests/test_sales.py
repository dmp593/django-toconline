from django.test import TestCase

from toconline.services import (
    toconline,
    TocOnlineResource,
    TocOnlineDocumentKind
)


class SalesTestCase(TestCase):
    def test_create_sales_document(self):
        toconline.create(
            TocOnlineResource.COMMERCIAL_SALES_DOCUMENTS,
            document_type="FT",
            lines=[
                {
                    "item_type": "Product",
                    "description": "Produto de teste",
                    "quantity": 13,
                    "unit_price": 9.99
                }
            ]
        )

    def test_download_sales_document_pdf(self):
        first_document = toconline.first(
            TocOnlineResource.COMMERCIAL_SALES_DOCUMENTS
        )

        if not first_document:
            self.fail("No sales document found to download PDF.")

        pdf_content = toconline.download_document(
            pk=first_document['id'],
            kind=TocOnlineDocumentKind.DOCUMENT,
            n_copies=2
        )

        if not pdf_content or not isinstance(pdf_content, bytes):
            self.fail("Failed to download PDF content for the sales document.")
