import unittest
from .pass_manager import PasswordManager

class TestPasswordManager(unittest.TestCase):

    def setUp(self):
        self.pm = PasswordManager()
        self.test_data = {
            'service': 'github',
            'username': 'user@example.com',
            'password': 'secure_password_123'
        }

    def test_save_password(self):
        # сохранения пароля
        result = self.pm.save_password(
            self.test_data['service'],
            self.test_data['username'],
            self.test_data['password']
        )
        self.assertTrue(result)

    def test_retrieve_password(self):
        # извлечения пароля

        # Сначала сохраняем пароль
        self.pm.save_password(
            self.test_data['service'],
            self.test_data['username'],
            self.test_data['password']
        )

        # Затем извлекаем
        retrieved_password = self.pm.get_password(
            self.test_data['service'],
            self.test_data['username']
        )

        self.assertEqual(retrieved_password, self.test_data['password'])

    def test_retrieve_nonexistent_password(self):
        # обработка ошибки при извлечении несуществующего пароля
        with self.assertRaises(ValueError):
            self.pm.get_password('nonexistent_service', 'nonexistent_user')

    def test_update_password(self):
        # обновлени пароля

        # Сохраняем первоначальный пароль
        self.pm.save_password(
            self.test_data['service'],
            self.test_data['username'],
            self.test_data['password']
        )

        # Обновляем пароль
        new_password = 'new_secure_password_456'
        result = self.pm.update_password(
            self.test_data['service'],
            self.test_data['username'],
            new_password
        )

        self.assertTrue(result)

        # Проверяем, что пароль обновился
        updated_password = self.pm.get_password(
            self.test_data['service'],
            self.test_data['username']
        )
        self.assertEqual(updated_password, new_password)

    def test_delete_password(self):
        # удалениe пароля

        # Сначала сохраняем пароль
        self.pm.save_password(
            self.test_data['service'],
            self.test_data['username'],
            self.test_data['password']
        )

        # Удаляем
        result = self.pm.delete_password(
            self.test_data['service'],
            self.test_data['username']
        )

        self.assertTrue(result)

        # Проверяем, что пароль удален
        with self.assertRaises(ValueError):
            self.pm.get_password(self.test_data['service'], self.test_data['username'])


if __name__ == '__main__':
    unittest.main()