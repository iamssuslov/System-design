workspace {
    model {
        // Пользователь системы
        user = person "Пользователь системы" {
            description "Пользователь, который взаимодействует с приложением."
        }

        // Система управления файлами
        FileManagementSystem = softwareSystem "Система управления файлами" {
            description "Приложение для управления пользователями, папками и файлами."

            // API системы
            API = container "REST API" {
                description "Предоставляет возможности управления пользователями, папками и файлами через HTTP."
                technology "Python и Django"
            }
            
            // Компоненты API
            UserController = container "Управление пользователями" {
                description "Обрабатывает операции с пользователями."
                technology "Flask"
            }
            
            FolderController = container "Управление папками" {
                description "Обрабатывает операции с папками."
                technology "Flask"
            }
            
            FileController = container "Управление файлами" {
                description "Обрабатывает операции с файлами."
                technology "Flask"
            }


            // База данных
            Database = container "База данных" {
                description "Хранит информацию о пользователях, папках и файлах."
                technology "PostgreSQL"
            }
            
            // Сущности базы данных
            UserEntity = container "Данные пользователей" {
                description "Содержит информацию о пользователях."
            }

            FolderEntity = container "Данные папок" {
                description "Содержит информацию о папках."
            }

            FileEntity = container "Данные файлов" {
                description "Содержит информацию о файлах."
            }
        }

        // Взаимодействия
        user -> API "Взаимодействует с" "Напрямую или HTTP JSON"

        API -> UserController "Использует"
        API -> FolderController "Использует"
        API -> FileController "Использует"

        UserController -> Database "Читает/Записывает" "SQL"
        FolderController -> Database "Читает/Записывает" "SQL"
        FileController -> Database "Читает/Записывает" "SQL"

        Database -> UserEntity "Содержит"
        Database -> FolderEntity "Содержит"
        Database -> FileEntity "Содержит"
    }
    
    views {
        systemContext FileManagementSystem {
            include *
            autoLayout
        }
        
        container FileManagementSystem {
            include *
            autoLayout
        }
        
        dynamic FileManagementSystem {
            title "Создание пользователя"
            user -> API "Делает запрос к"
            API -> UserController "Создаёт пользователя с помощью"
            autoLayout
        }
        
        dynamic FileManagementSystem {
            title "Создание файла"
            user -> API "Делает запрос к"
            API -> FileController "Создаёт файл с помощью"
            autoLayout
        }
    
        dynamic FileManagementSystem {
            title "Создание папки"
            user -> API "Делает запрос к"
            API -> FolderController "Создаёт папку с помощью"
            autoLayout
        }

        theme default
    }
}
