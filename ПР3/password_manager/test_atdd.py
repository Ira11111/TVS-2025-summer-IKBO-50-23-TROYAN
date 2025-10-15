import unittest
import os
from .pass_manager import PasswordManager


class PasswordManagerAcceptanceTests(unittest.TestCase):

    def setUp(self):
        # Используем тестовые файлы чтобы не затирать реальные данные
        self.test_storage = "test_passwords_acceptance.json"
        self.test_key = "test_master_key.key"

        # Создаем экземпляр менеджера паролей с тестовыми файлами
        self.pm = PasswordManager(storage_file=self.test_storage)

    def tearDown(self):
        if os.path.exists(self.test_storage):
            os.remove(self.test_storage)
        if os.path.exists(self.test_key):
            os.remove(self.test_key)

    def test_scenario_1_save_new_password(self):
        # Тестовые данные
        service = "GitHub"
        username = "developer@company.com"
        password = "MyPassword123"

        # Действие: сохраняем пароль
        save_result = self.pm.save_password(service, username, password)

        # Проверка: операция должна завершиться успешно
        self.assertTrue(save_result)

        # Проверка: пароль должен быть доступен для извлечения
        retrieved_password = self.pm.get_password(service, username)
        self.assertEqual(retrieved_password, password)

    def test_scenario_2_retrieve_saved_password(self):

        # Подготовка: сохраняем тестовый пароль
        service = "Email"
        username = "user@company.com"
        password = "EmailSecurePass789"
        self.pm.save_password(service, username, password)

        # Действие: извлекаем пароль
        retrieved_password = self.pm.get_password(service, username)

        # Проверка: извлеченный пароль должен соответствовать сохраненному
        self.assertEqual(retrieved_password, password)

    def test_scenario_3_update_existing_password(self):
        # Подготовка: сохраняем старый пароль
        service = "Bank"
        username = "client@bank.com"
        old_password = "OldBankPassword123"
        new_password = "NewSecureBankPass456"
        self.pm.save_password(service, username, old_password)

        # Проверка: убеждаемся что старый пароль сохранен
        initial_password = self.pm.get_password(service, username)
        self.assertEqual(initial_password, old_password)

        # Действие: обновляем пароль
        update_result = self.pm.update_password(service, username, new_password)

        # Проверка: операция обновления должна завершиться успешно
        self.assertTrue(update_result)

        # Проверка: пароль должен измениться на новый
        current_password = self.pm.get_password(service, username)
        self.assertEqual(current_password, new_password)
        self.assertNotEqual(current_password, old_password)

    def test_scenario_4_delete_password(self):
        # Подготовка: сохраняем тестовый пароль
        service = "УстаревшийСервис"
        username = "old_user@service.com"
        password = "TempPassword111"
        self.pm.save_password(service, username, password)

        # Проверка: убеждаемся что пароль существует
        initial_check = self.pm.get_password(service, username)
        self.assertEqual(initial_check, password)

        # Действие: удаляем пароль
        delete_result = self.pm.delete_password(service, username)

        # Проверка: операция удаления должна завершиться успешно
        self.assertTrue(delete_result)

        # Проверка: пароль больше не должен быть доступен
        with self.assertRaises(ValueError) as context:
            self.pm.get_password(service, username)

        # Проверка: должно быть понятное сообщение об ошибке
        self.assertIn("не найден", str(context.exception).lower())

    def test_scenario_5_security_authentication(self):
        # Подготовка: сохраняем тестовый пароль
        service = "SecureService"
        username = "secure@user.com"
        password = "VerySecurePass123"
        self.pm.save_password(service, username, password)

        # Проверка: попытка доступа к несуществующему паролю должна вызывать ошибку
        with self.assertRaises(ValueError) as context:
            self.pm.get_password("NonExistentService", "unknown@user.com")

        # Проверка: сообщение об ошибке должно быть информативным
        self.assertIn("не найден", str(context.exception).lower())

        # Проверка: попытка обновления несуществующего пароля должна возвращать False
        update_result = self.pm.update_password(
            "UnknownService",
            "ghost@user.com",
            "new_password"
        )
        self.assertFalse(update_result)


if __name__ == '__main__':
    unittest.main()