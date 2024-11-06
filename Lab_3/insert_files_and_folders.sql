INSERT INTO folders (name, parent_id, owner_id)
VALUES ('Folder1', NULL, 1);
INSERT INTO folders (name, parent_id, owner_id)
VALUES ('Folder2', NULL, 1);
INSERT INTO folders (name, parent_id, owner_id)
VALUES ('Folder3', NULL, 1);

INSERT INTO files (filename, folder_id, owner_id, content)
VALUES ('example1.txt', 1, 1, decode('Sample content here', 'escape'));
INSERT INTO files (filename, folder_id, owner_id, content)
VALUES ('example2.txt', 1, 1, decode('Sample content here', 'escape'));
INSERT INTO files (filename, folder_id, owner_id, content)
VALUES ('example3.txt', 1, 1, decode('Sample content here', 'escape'));