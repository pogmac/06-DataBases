-- tworzymy tabelę
CREATE TABLE project
(
   id            int,
   name          varchar(255),
   start_date    date,
   end_date      date
);

-- dodajemy dane
INSERT INTO project
   (id, name, start_date, end_date)
VALUES (1, "mayhem", "2023.01.01", "2023.01.01");

INSERT INTO project
   (id, name, start_date, end_date)
VALUES (2, "apocalypse", "2023.01.10", "2023.01.14");

-- tworzymy tabelę
CREATE TABLE task
(
   id            int,
   project_id    int,
   name          varchar(255),
   description   varchar(255),
   status        varchar(255),		
   start_date    date,
   end_date      date
);

INSERT INTO task
   (id, project_id, name, description, status, start_date, end_date)
VALUES (1,1,"recruit_members", "recruit members of the project", "in progress",  "2023.01.10", "2023.01.14");

INSERT INTO task
   (id, project_id, name, description, status, start_date, end_date)
VALUES (2,1,"assign tasks", "assign tasks to the project members", "in progress",  "2023.01.12", "2023.01.23");

INSERT INTO task
   (id, project_id, name, description, status, start_date, end_date)
VALUES (3,2,"fire members", "fire members of the project", "not started", "2024.01.10", "2024.01.14");

INSERT INTO task
   (id, project_id, name, description, status, start_date, end_date)
VALUES (4,2,"closure", "cancel all the rent agreements for the project's activivies", "not started",  "2024.01.12", "2024.01.23");


SELECT a.*,b.* FROM project as a
  left join task as b
  on a.id = b.project_id


SELECT a.*,b.name as "task_name", b.description as 'task_decription', b.status as "task_satus", b.start_date, b.end_date FROM project as a
  left join task as b
  on a.id = b.project_id