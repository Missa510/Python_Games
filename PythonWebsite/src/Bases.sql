CREATE DATABASE bd_flaskuwu;

CREATE TABLE contactos(
    Id_con INT AUTO_INCREMENT,
    fullname_con varchar(255) NOT NULL,
    telefono_con varchar(255) NOT NULL,
    email_con varchar(255) NOT NULL,
    PRIMARY KEY (Id_con)
);