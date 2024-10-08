# Система управления проектами

## Исходное задание

1. Напишите один-два ключевых варианта использования вашей системы
2. Определите приоритет в нефункциональных требованиях (производительность, безопасность, надежность …)
3. Создайте диаграмму контекста в Structruizr DSL
4. Определите основные контейнеры и создайте модели и диаграмму контекста на языке Structurizr DSL
5. Определите технологии и проставьте их на контейнерах и связях
6. Создайте одну диаграмму dynamic для архитектурно значимого варианта использования
7. Результат должен быть оформлен в виде следующих файлов, размещенных в вашем:
   - readme.md с текстом задания
   - workspace.dsl с моделью и view
   - documentation/doc.md – с текстовым описанием

Данную задачу и ее подзадачи требуется реализовать на основе следующей системы:
Управление проектами https://www.atlassian.com/ru/software/jira

Приложение должно содержать следующие данные:
- проект
- задача
- исполнитель

Реализовать API:
- Создание нового пользователя
- Поиск пользователя по логину
- Поиск пользователя по маске имя и фамилии
- Создание проекта
- Поиск проекта по имени
- Поиск всех проектов
- Создание задачи в проекте
- Получение всех задач в проекте
- Получение задачи по коду

## Описание проекта

Это проект системы управления проектами, вдохновленной Jira. Система позволяет создавать проекты, управлять задачами и назначать исполнителей.

### Основные функции

- Создание и управление проектами
- Создание и отслеживание задач в рамках проектов
- Управление пользователями и назначение исполнителей задачам

### Архитектура

Архитектура системы описана с использованием Structurizr DSL. Подробности можно найти в файлах `workspace.dsl` и `documentation/doc.md`.

### Компоненты системы

1. Web Application: Веб-интерфейс для взаимодействия пользователей с системой
2. API Application: RESTful API для программного взаимодействия с системой
3. Database: База данных PostgreSQL для хранения информации о проектах, задачах и пользователях

### API

Система предоставляет RESTful API для управления пользователями, проектами и задачами. Подробная документация API доступна в файле `documentation/doc.md`.

### Запуск проекта

Для запуска проекта используется Structurizr Lite, который уже клонирован внутрь проекта. Следуйте этим шагам для запуска:

1. Убедитесь, что у вас установлена Java 17 или выше.

2. Откройте терминал и перейдите в корневую директорию проекта.

3. Перейдите в директорию Structurizr Lite:

```bash
cd structurizr-lite
```

4. Соберите проект с помощью Gradle:

```bash
./gradlew build
```
5. Запустите Structurizr Lite, указав путь к вашему рабочему пространству:

Замените `/путь/к/вашему/рабочему/пространству` на актуальный путь к директории, содержащей ваш файл `workspace.dsl`.

6. После успешного запуска, откройте веб-браузер и перейдите по адресу:

```bash
http://localhost:8080
```

7. Теперь вы должны увидеть интерфейс Structurizr с вашим рабочим пространством, включая диаграммы и документацию проекта.

Примечание: Если вы внесете изменения в файл `workspace.dsl`, просто обновите страницу в браузере, чтобы увидеть обновления.

### Дополнительные возможности

- Для использования автоматической компоновки диаграмм, убедитесь, что у вас установлен Graphviz.
- Если вы хотите внести изменения в пользовательский интерфейс Structurizr, обратитесь к репозиторию [structurizr/ui](https://github.com/structurizr/ui).

### Устранение неполадок

- Если вы столкнулись с проблемами при запуске, убедитесь, что используете Java 17, так как это единственная протестированная версия для сборки и запуска из исходного кода.
- В случае ошибок, проверьте, что путь к рабочему пространству указан правильно и файл `workspace.dsl`существует в указанной директории.