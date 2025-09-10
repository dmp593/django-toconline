from django.test import TestCase

from toconline.services import toconline, TocOnlineResource


class ProductsTestCase(TestCase):
    def test_get_products(self):
        toconline.list(TocOnlineResource.PRODUCTS)

    def test_create_and_delete_product(self):
        family = toconline.first(
            TocOnlineResource.ITEM_FAMILIES
        )

        product = toconline.create(
            TocOnlineResource.PRODUCTS,
            item_code=888888,
            item_description="Product to be deleted",
            item_family_id=family['id'],
            sales_price=100,
            sales_price_includes_vat=False,
            tax_code="NOR",
            type="Product"
        )

        toconline.delete(
            TocOnlineResource.PRODUCTS,
            product['id']
        )
