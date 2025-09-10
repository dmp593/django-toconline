from django.test import TestCase
from faker import Faker
from faker.providers import phone_number

from toconline.services import toconline, TocOnlineResource


class CustomersTestCase(TestCase):
    def setUp(self):
        # use Faker to generate unique data to avoid "already exists" errors
        self.faker = Faker()
        self.faker.add_provider(phone_number)

    def test_get_customers(self):
        toconline.list(TocOnlineResource.CUSTOMERS)

    def test_get_first_customer(self):
        toconline.first(TocOnlineResource.CUSTOMERS)

    def test_create_customer(self):
        email = self.faker.unique.email()
        business = self.faker.company()

        toconline.create(
            TocOnlineResource.CUSTOMERS,
            business_name=business,
            contact_name=business,
            email=email,
            mobile_number='800201937',
            internal_observations='Created via unit test',
            tax_registration_number='999999990',
        )

        customer = toconline.first(TocOnlineResource.CUSTOMERS, email=email)

        if not customer:
            self.fail("Customer not found after creation.")

        toconline.delete(
            TocOnlineResource.CUSTOMERS, customer['id']
        )

    def test_create_customer_address(self):
        customer = toconline.create(
            TocOnlineResource.CUSTOMERS,
            business_name=self.faker.company(),
            contact_name=self.faker.name(),
            email=self.faker.unique.email(),
            mobile_number=self.faker.unique.phone_number(),
            internal_observations='Created via unit test',
            tax_registration_number='999999990',
        )

        toconline.create(
            TocOnlineResource.ADDRESSES,
            addressable_id=customer['id'],
            # addressable_type="Supplier",
            address_detail="Leiria não existe, 404",
            city="Leiria",
            postcode="2430-123",
            region="Leiria"
        )

        toconline.delete(
            TocOnlineResource.CUSTOMERS, customer['id']
        )

    def test_create_customer_email(self):
        email = self.faker.unique.email()
        business = self.faker.company()

        customer = toconline.create(
            TocOnlineResource.CUSTOMERS,
            business_name=business,
            contact_name='Mr. Foo',
            email=email,
            mobile_number='800201937',
            internal_observations='Created via unit test',
            tax_registration_number='999999990',
        )

        toconline.create(
            TocOnlineResource.CONTACTS,
            contactable_id=customer['id'],
            # contactable_type="Supplier",
            email=self.faker.unique.email(),
            is_primary=True,
            mobile_number=None,
            name=None,
            phone_number=None,
            position=None
        )

        toconline.delete(
            TocOnlineResource.CUSTOMERS, customer['id']
        )

    def test_delete_customer(self):
        email = self.faker.unique.email()
        business = self.faker.company()

        customer = toconline.create(
            TocOnlineResource.CUSTOMERS,
            business_name=business,
            contact_name=business,
            email=email,
            mobile_number='912345678',
            internal_observations='Created via unit test',
            tax_registration_number='999999990',
        )

        toconline.delete(
            TocOnlineResource.CUSTOMERS, customer['id']
        )
