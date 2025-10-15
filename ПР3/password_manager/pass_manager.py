import json
import os
from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self, storage_file='passwords.enc'):
        self.storage_file = storage_file
        self.key = self._load_or_create_key()
        self.cipher = Fernet(self.key)

    def _load_or_create_key(self):
        # загрузка или создание ключа шифрования
        key_file = 'secret.key'
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
            return key

    def _encrypt_data(self, data):
        # шифрование данных
        return self.cipher.encrypt(data.encode()).decode()

    def _decrypt_data(self, encrypted_data):
        # дешифрование данных
        return self.cipher.decrypt(encrypted_data.encode()).decode()

    def save_password(self, service, username, password):
        # Cохранение пароля
        try:
            # Загрузка существующих данных
            passwords = self._load_passwords()

            # Сохранение нового пароля
            key = f"{service}:{username}"
            encrypted_password = self._encrypt_data(password)
            passwords[key] = encrypted_password

            # Сохранение в файл
            self._save_passwords(passwords)
            return True
        except Exception as e:
            print(f"Ошибка при сохранении пароля: {e}")
            return False

    def get_password(self, service, username):
        # Извлечение пароля
        key = f"{service}:{username}"
        passwords = self._load_passwords()

        if key not in passwords:
            raise ValueError(f"Пароль для {service}:{username} не найден")

        encrypted_password = passwords[key]
        return self._decrypt_data(encrypted_password)

    def update_password(self, service, username, new_password):
        # Обновление пароля
        try:
            key = f"{service}:{username}"
            passwords = self._load_passwords()

            if key not in passwords:
                raise ValueError(f"Пароль для {service}:{username} не найден")

            encrypted_password = self._encrypt_data(new_password)
            passwords[key] = encrypted_password

            self._save_passwords(passwords)
            return True
        except Exception as e:
            print(f"Ошибка при обновлении пароля: {e}")
            return False

    def delete_password(self, service, username):
        # Удаление пароля
        try:
            key = f"{service}:{username}"
            passwords = self._load_passwords()

            if key not in passwords:
                raise ValueError(f"Пароль для {service}:{username} не найден")

            del passwords[key]
            self._save_passwords(passwords)
            return True
        except Exception as e:
            print(f"Ошибка при удалении пароля: {e}")
            return False

    def _load_passwords(self):
        # Загрузка паролей из файла
        if not os.path.exists(self.storage_file):
            return {}

        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, Exception):
            return {}

    def _save_passwords(self, passwords):
        # Сохранение паролей в файл
        with open(self.storage_file, 'w') as f:
            json.dump(passwords, f, indent=2)
