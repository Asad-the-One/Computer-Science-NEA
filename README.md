# Computer Science NEA Project

As part of A-Level Computer Science, we are required to create a program/application. I have decided to do a game where you explore a maze blind, interacting with a text interface.

## Description

A maze exploration game where the player interacts with a floating window to control a blind character. They are to explore a maze, gathering items to help them reach the end while avoiding enemies, who are also blind. They can make use of items such as rocks to redirect enemies and traps to combat them. A visual aid of a map is shown to the player as they explore the maze. There are three difficulty levels that control enemy movement and item drop rates.

There will be multiple types of enemies that do different things when interacting with the user. Examples: A spirit that makes you forget parts of the map; slimes that make you smell delicious to more hostile enemies; enemies that will deal damage to you.

## Target audience

- Gamers
- Blind people

## Inspiration

The source of inspiration was a developer’s video on Instagram I saw, where it was instead world exploration with a story line, but I cannot seem to find it. A game with a similar concept is [this game](https://adianosbe.itch.io/the-imprecise-blind-mans-maze). Mine will have a full UI with various menus rather than being a CLI game.

## Algorithm descriptions

- *Auto generating new maps every game.*

- *Pathfinding algorithm for NPCs. React to sound and scent, but otherwise randomly roam the map.*

- Random generation of items in crates, and locations around the map.

- Tracking NPC movement and giving the user an idea of where they are via text outputs such as “You hear a rustle coming from ahead” and “The stench of something rotting bothers you”.

- General interactions. Moving around the map; checking your surroundings for dropped items and crates.

- Rendering a map for the user so they can track their location as they move. This is based on the idea that the character has good memory, and parts of the map can be “forgotten” when interacting with certain enemies.

- Login system for leaderboard access (optional).

- *Sync with a leaderboard in the cloud. Uses a hashing algorithm on the Python file to make a string and sends it to the cloud along with score and time so cheaters cannot modify the script.*

## Demonstrated skills

- OOP

- File handling

- Server communication

- GUI design
