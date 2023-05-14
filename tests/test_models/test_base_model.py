import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_created_at_equal_updated_at_initially(self):
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_save_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dictionary(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)

    def test_to_dict_contains_all_attributes(self):
        model_dict = self.model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_to_dict_contains_correct_values(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_str_representation(self):
        expected_str = f"[{self.model.__class__.__name__}] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_create_instance_from_dict(self):
        model_dict = {
            'id': 'test_id',
            'created_at': '2023-05-14T12:34:56.789',
            'updated_at': '2023-05-14T12:34:56.789',
            'custom_attr': 'test_custom_attr'
        }
        model = BaseModel(**model_dict)
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime(2023, 5, 14, 12, 34, 56, 789000))
        self.assertEqual(model.updated_at, datetime(2023, 5, 14, 12, 34, 56, 789000))
        self.assertEqual(model.custom_attr, 'test_custom_attr')

if __name__ == '__main__':
    unittest.main()
