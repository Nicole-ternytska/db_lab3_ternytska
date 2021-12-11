---------------------------
-- Populate Board_game table
---------------------------
INSERT INTO Board_game(game_id, game_name, play_time_id, rating)
VALUES(1, 'Gloomhaven', 2, 8.79),
(2, 'Twilight Imperium: Fourth Edition', 4, 8.70),
(3, 'Spirit Island', 2, 8.35),
(4, 'Napoleon Triumph', 3, 7.04),
(5, 'The Estates', 1, 7.49),
(6, 'Union Pacific', 1, 7.21),
(7, 'Fugitive', 2, 7.22),
(8, 'Rococo', 2, 7.58),
(9, 'Puerto Rico', 3, 7.99),
(10, 'Gaia Project', 3, 8.49),
(11, 'Paths of Glory', 4, 8.06);



---------------------------
-- Populate Play_time table
---------------------------
INSERT INTO Play_time (play_time_id, play_time)
VALUES(1, 60),
(2, 120),
(3, 240),
(4, 480);


---------------------------
-- Populate Geek  table
---------------------------
INSERT INTO Geek (geek_id, geek_name, age)
VALUES('SR41', 'Rick Jone', 20),
('PLO9', 'Yean Lee',49),
('BWQ67', 'Ann Bold',28),
('AHY44', 'Mila Wask',19),
('KLI65', 'Polly Beck',52),
('VCF09', 'Will Can',16),
('PIU95', 'Joy Xan',25),
('XWQ22', 'Rick Jone',27),
('ZAA23', 'Addy Loo',20);



---------------------------
-- Populate Collection table
---------------------------
INSERT INTO Collection (geek_id, game_id, geek_ranking)
VALUES('SR41', 8, 3),
('SR41', 1, 5),
('BWQ67', 4, 2),
('PLO9', 1, 5),
('PLO9', 11, 4),
('PLO9', 6, 2),
('PLO9', 4, 3),
('AHY44', 2, 3),
('AHY44', 8, 4),
('KLI65', 9, 1),
('VCF09', 10, 5),
('VCF09', 2, 2),
('VCF09', 5, 4),
('PIU95', 3, 4),
('PIU95', 7, 1),
('XWQ22', 6, 3),
('XWQ22', 2, 3),
('XWQ22', 10, 4),
('ZAA23', 1, 5),
('ZAA23', 7, 4),
('ZAA23', 5, 1),
('ZAA23', 9, 3);



