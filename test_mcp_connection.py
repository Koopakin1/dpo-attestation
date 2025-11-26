#!/usr/bin/env python
"""
Тестирование подключения к MCP серверу Sequential Thinking
"""
import subprocess
import sys
import json
import time
from pathlib import Path


def test_mcp_server_connection():
    """
    Тестирует подключение к MCP серверу Sequential Thinking
    """
    print("Тестирование подключения к MCP серверу Sequential Thinking...")
    
    # Проверяем наличие uv
    try:
        result = subprocess.run(["uv", "--version"], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode != 0:
            print("Ошибка: uv не установлен или не найден в PATH")
            return False
        print("✓ uv установлен")
    except FileNotFoundError:
        print("Ошибка: uv не установлен")
        return False
    except subprocess.TimeoutExpired:
        print("Ошибка: Таймаут при проверке uv")
        return False

    # Пробуем запустить сервер через uvx
    try:
        print("\nЗапуск сервера через uvx...")
        # Запускаем сервер в фоновом режиме
        server_process = subprocess.Popen([
            "uvx", 
            "--from", "git+https://github.com/arben-adm/mcp-sequential-thinking",
            "--with", "portalocker",
            "mcp-sequential-thinking"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Ждем немного для запуска сервера
        time.sleep(3)
        
        # Проверяем, жив ли процесс
        if server_process.poll() is not None:
            # Процесс завершился, получаем ошибки
            _, stderr = server_process.communicate()
            print(f"Ошибка при запуске сервера: {stderr.decode()}")
            return False
        
        print("✓ MCP сервер запущен успешно")
        
        # Отправляем сигнал завершения процессу
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server_process.kill()
        
        print("✓ Тестирование подключения завершено успешно")
        return True
        
    except FileNotFoundError:
        print("Ошибка: mcp-sequential-thinking не найден")
        return False
    except subprocess.TimeoutExpired:
        print("Ошибка: Таймаут при запуске сервера")
        return False
    except Exception as e:
        print(f"Ошибка при тестировании подключения: {e}")
        return False


def check_config_files():
    """
    Проверяет наличие и корректность конфигурационных файлов
    """
    print("\nПроверка конфигурационных файлов...")
    
    config_files = ["mcp_config.json", "mcp_local_config.json"]
    
    for config_file in config_files:
        path = Path(config_file)
        if path.exists():
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                print(f"✓ {config_file} существует и корректен")
            except json.JSONDecodeError:
                print(f"✗ {config_file} содержит ошибки в формате JSON")
                return False
            except Exception as e:
                print(f"✗ Ошибка при чтении {config_file}: {e}")
                return False
        else:
            print(f"⚠ {config_file} не найден")
    
    return True


def main():
    """
    Основная функция для тестирования подключения к MCP серверу
    """
    print("="*60)
    print("Тестирование настройки доступа к MCP серверу")
    print("="*60)
    
    # Проверяем конфигурационные файлы
    config_ok = check_config_files()
    
    # Тестируем подключение к серверу
    connection_ok = test_mcp_server_connection()
    
    print("\n" + "="*60)
    print("Результаты тестирования:")
    print(f"Проверка конфигурации: {'✓ Пройдена' if config_ok else '✗ Ошибка'}")
    print(f"Тестирование подключения: {'✓ Пройдено' if connection_ok else '✗ Ошибка'}")
    
    if config_ok and connection_ok:
        print("\n✓ Все тесты пройдены успешно!")
        print("MCP сервер Sequential Thinking готов к использованию.")
        return True
    else:
        print("\n✗ Требуется устранение ошибок перед использованием MCP сервера.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)