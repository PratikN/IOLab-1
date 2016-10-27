-- Insert code to create Database Schema
-- This will create your .db database file for use
drop table if exists users;
drop table if exists trips;
drop table if exists makes;

create table users (
  id integer primary key,
  username text not null,
  password text not null
);

create table trips (
  id integer primary key,
  name text not null,
  destination text not null
);

create table makes (
  id integer primary key,
  trip_id integer not null,
  user_id integer not null,
  foreign key (trip_id) references trips(id),
  foreign key (user_id) references users(id)
);
