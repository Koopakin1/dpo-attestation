# Настройка доступа к MCP серверу Sequential Thinking

## Введение

Этот документ описывает, как настроить доступ к MCP серверу Sequential Thinking, который позволяет структурировать мышление и анализировать сложные проблемы через последовательные этапы мышления.

## Установка и настройка

### Вариант 1: Использование uvx (без установки)

Этот способ позволяет запускать сервер без предварительной установки, используя uvx:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/arben-adm/mcp-sequential-thinking",
        "--with",
        "portalocker",
        "mcp-sequential-thinking"
      ]
    }
  }
}
```

### Вариант 2: Локальная установка

Если вы хотите установить пакет локально:

1. Убедитесь, что у вас установлен Python 3.10+ и uv
2. Установите пакет:
   ```bash
   uv pip install git+https://github.com/arben-adm/mcp-sequential-thinking
   ```

3. Конфигурация для локальной установки:
   ```json
   {
     "mcpServers": {
       "sequential-thinking": {
         "command": "mcp-sequential-thinking"
       }
     }
   }
   ```

## Интеграция с Claude Desktop

Для интеграции с Claude Desktop добавьте одну из вышеуказанных конфигураций в файл `claude_desktop_config.json`, который обычно находится в:

- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

## Запуск сервера вручную

Вы также можете запустить сервер вручную для тестирования:

```bash
# С использованием uvx
uvx --from git+https://github.com/arben-adm/mcp-sequential-thinking --with portalocker mcp-sequential-thinking

# После локальной установки
mcp-sequential-thinking
```

## Использование инструментов

После настройки сервер предоставляет следующие инструменты:

1. `process_thought` - записывает и анализирует новую мысль в процессе последовательного мышления
2. `generate_summary` - генерирует сводку всего процесса мышления
3. `clear_history` - сбрасывает историю мышления
4. `export_session` - экспортирует текущую сессию в файл
5. `import_session` - импортирует сессию из файла

## Проверка подключения

Для проверки подключения можно использовать скрипт отладки из репозитория:

```bash
uvx --from git+https://github.com/arben-adm/mcp-sequential-thinking debug_mcp_connection.py
```

## Устранение неполадок

1. Убедитесь, что Python 3.10+ установлен
2. Убедитесь, что пакет `uv` установлен: `pip install uv`
3. Проверьте права доступа к файлам и каталогам
4. Проверьте настройки брандмауэра и антивируса

## Требования

- Python 3.10 или выше
- UV package manager
- portalocker (для обеспечения потокобезопасности)

## Лицензия

MIT License