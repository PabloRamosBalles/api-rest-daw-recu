create database examen_daw_recu;
use examen_daw_recu;
create table persona(
    id int unsigned auto_increment primary key,
    nombre varchar(40),
    apellido varchar(80),
    edad int(3)
)