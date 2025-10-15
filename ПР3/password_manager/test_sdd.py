import unittest
from .pass_manager import PasswordManager


class SpecificationTests(unittest.TestCase):
    # Тесты на основе спецификаций по примерам

    def setUp(self):
        self.pm = PasswordManager('test_sdd_passwords.enc')

    def tearDown(self):
        import os
        if os.path.exists('test_sdd_passwords.enc'):
            os.remove('test_sdd_passwords.enc')
        if os.path.exists('test_sdd_secret.key'):
            os.remove('test_sdd_secret.key')

    def test_specification_1_github_save_and_retrieve(self):
        # Спецификация 1

        # Тестовые данные из спецификации
        service = "GitHub"
        username = "dev@company.com"
        password = "GhbPass123!"

        # Сохранение
        save_result = self.pm.save_password(service, username, password)
        self.assertTrue(save_result, "Пароль GitHub должен быть успешно сохранен")

        # Извлечение
        retrieved_password = self.pm.get_password(service, username)
        self.assertEqual(retrieved_password, password, "Должен вернуться корректный пароль GitHub")

    def test_specification_2_email_update(self):
        # Спецификация 2

        service = "Email"
        username = "user@mail.org"
        old_password = "OldMailPass"
        new_password = "NewMailPass456"

        # Сохраняем старый пароль
        self.pm.save_password(service, username, old_password)

        # Обновляем на новый
        update_result = self.pm.update_password(service, username, new_password)
        self.assertTrue(update_result, "Обновление пароля Email должно быть успешным")

        # Проверяем новый пароль
        current_password = self.pm.get_password(service, username)
        self.assertEqual(current_password, new_password, "Пароль Email должен быть обновлен")

    def test_specification_3_bank_save_and_delete(self):
        # Спецификация 3
        service = "Bank"
        username = "client@bank.com"
        password = "BankSecure789"

        # Сохраняем пароль
        self.pm.save_password(service, username, password)

        # Удаляем пароль
        delete_result = self.pm.delete_password(service, username)
        self.assertTrue(delete_result, "Удаление пароля Bank должно быть успешным")

        # Проверяем, что пароль удален
        with self.assertRaises(ValueError):
            self.pm.get_password(service, username)

    def test_specification_4_social_nonexistent_access(self):
        # Спецификация 4
        service = "Social"
        username = "social_user"

        # Попытка извлечения несуществующего пароля
        with self.assertRaises(ValueError) as context:
            self.pm.get_password(service, username)

        self.assertIn("не найден", str(context.exception))


if __name__ == '__main__':
    unittest.main()