-- SQLite is used

drop table if exists Entries;

create table Entries (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);
