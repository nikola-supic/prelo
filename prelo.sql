-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 30, 2021 at 01:49 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `prelo`
--

-- --------------------------------------------------------

--
-- Table structure for table `art`
--

CREATE TABLE `art` (
  `id` int(11) NOT NULL,
  `path` varchar(72) NOT NULL,
  `description` varchar(72) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `art`
--

INSERT INTO `art` (`id`, `path`, `description`) VALUES
(1, ':/art/images/art/art_1.png', 'BAJA MALI');

-- --------------------------------------------------------

--
-- Table structure for table `artist`
--

CREATE TABLE `artist` (
  `id` int(11) NOT NULL,
  `name` varchar(48) NOT NULL,
  `art` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `artist`
--

INSERT INTO `artist` (`id`, `name`, `art`) VALUES
(1, 'Baja Mali Knindza', 1),
(2, 'Braća Lekić', 1),
(3, 'Krajisnici Zare i Goci', 1);

-- --------------------------------------------------------

--
-- Table structure for table `chat`
--

CREATE TABLE `chat` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `friend_id` int(11) NOT NULL,
  `message` varchar(128) NOT NULL,
  `time` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chat`
--

INSERT INTO `chat` (`id`, `user_id`, `friend_id`, `message`, `time`) VALUES
(1, 1, 2, 'dadada', '2021-07-14 21:42:26'),
(2, 1, 2, 'dadada', '2021-07-14 21:42:49'),
(3, 1, 2, 'helou', '2021-07-15 11:01:51'),
(4, 2, 1, 'da_da', '2021-07-15 11:02:20'),
(5, 1, 2, 'dada', '2021-07-15 11:04:29'),
(6, 2, 1, 'dadadadadada', '2021-07-15 11:04:45'),
(7, 2, 1, 'dadadadadada', '2021-07-15 11:05:22'),
(8, 1, 2, 'da da da', '2021-07-15 11:07:17'),
(9, 2, 1, 'eeeee', '2021-07-15 11:07:31'),
(10, 1, 2, 'eee', '2021-07-15 11:08:19'),
(11, 2, 1, 'x', '2021-07-15 11:08:43'),
(12, 1, 2, 'xx', '2021-07-15 11:08:51'),
(13, 2, 1, 'dadadadadadeafaagaegea', '2021-07-15 11:10:38'),
(14, 1, 2, 'rerere', '2021-07-15 11:11:38'),
(15, 1, 2, 'gegegege', '2021-07-15 11:11:53'),
(16, 1, 2, 'dadada', '2021-07-15 11:12:00'),
(17, 1, 2, 'Тренутно слушам Braća Lekić - Alkoholičar', '2021-07-18 19:23:10'),
(18, 1, 2, 'Тренутно слушам Krajisnici Zare i Goci - Olivera', '2021-07-18 19:23:39');

-- --------------------------------------------------------

--
-- Table structure for table `friends`
--

CREATE TABLE `friends` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `friend_id` int(11) NOT NULL,
  `request` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `friends`
--

INSERT INTO `friends` (`id`, `user_id`, `friend_id`, `request`) VALUES
(3, 2, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `playlist`
--

CREATE TABLE `playlist` (
  `id` int(11) NOT NULL,
  `creator_id` int(11) NOT NULL,
  `name` varchar(48) NOT NULL,
  `description` varchar(72) NOT NULL,
  `public` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `playlist`
--

INSERT INTO `playlist` (`id`, `creator_id`, `name`, `description`, `public`) VALUES
(1, 1, 'Rade pjesme', 'Ovde su pjesme koje rade', 1),
(2, 1, 'second', 'description', 0);

-- --------------------------------------------------------

--
-- Table structure for table `playlist_song`
--

CREATE TABLE `playlist_song` (
  `id` int(11) NOT NULL,
  `playlist_id` int(11) NOT NULL,
  `song_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `playlist_song`
--

INSERT INTO `playlist_song` (`id`, `playlist_id`, `song_id`) VALUES
(1, 1, 2),
(2, 1, 3),
(3, 2, 1),
(4, 2, 3);

-- --------------------------------------------------------

--
-- Table structure for table `song`
--

CREATE TABLE `song` (
  `id` int(11) NOT NULL,
  `artist_id` int(11) NOT NULL,
  `name` varchar(48) NOT NULL,
  `art` int(11) NOT NULL DEFAULT 0,
  `path` varchar(128) NOT NULL,
  `length` int(11) NOT NULL,
  `added_by` varchar(48) NOT NULL,
  `bitrate` int(11) NOT NULL DEFAULT 128,
  `date_added` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `song`
--

INSERT INTO `song` (`id`, `artist_id`, `name`, `art`, `path`, `length`, `added_by`, `bitrate`, `date_added`) VALUES
(1, 1, '90', 1, 'songs\\Baja Mali Knindza - 90.mp3', 150, 'Server Admin', 128, '2021-07-29'),
(2, 2, 'Alkoholicar', 1, 'songs\\Braća Lekić - Alkoholičar.mp3', 146, 'Server Admin', 128, '2021-07-29'),
(3, 3, 'Olivera', 1, 'songs\\Krajisnici Zare i Goci - Olivera.mp3', 160, 'Server Admin', 128, '2021-07-29');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(32) NOT NULL,
  `last_name` varchar(32) NOT NULL,
  `username` varchar(32) NOT NULL,
  `email` varchar(48) NOT NULL,
  `password` varchar(128) NOT NULL,
  `salt` varchar(128) NOT NULL,
  `birthday` date NOT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT 0,
  `register_date` datetime NOT NULL DEFAULT current_timestamp(),
  `online` tinyint(1) NOT NULL DEFAULT 1,
  `last_online` datetime NOT NULL DEFAULT current_timestamp(),
  `art` int(11) NOT NULL DEFAULT 1,
  `ban` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `first_name`, `last_name`, `username`, `email`, `password`, `salt`, `birthday`, `admin`, `register_date`, `online`, `last_online`, `art`, `ban`) VALUES
(1, 'Никола', 'Шупић', 'dzast_nikola', 'nikola.supic09@gmail.com', '$2b$12$qPIjIy6sOYtA7m8yVfzm6e5DSlxP0v6HisV7A1tPjPG5d.XzncPX2', '$2b$12$qPIjIy6sOYtA7m8yVfzm6e', '1970-01-01', 1, '2021-07-29 15:05:32', 0, '2021-07-29 15:06:45', 1, 0),
(2, 'Nikola', 'Supic', 'dzast_nikola2', 'nikola.supic02@gmail.com', '$2b$12$dm1LNJEx2zx3r95ed3tRDOHFC1SDCGsC2aqJcqYEk5HkTkg.Qxwx6', '$2b$12$dm1LNJEx2zx3r95ed3tRDO', '1970-01-01', 0, '2021-07-29 15:07:23', 0, '2021-07-29 15:09:16', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `user_playlist`
--

CREATE TABLE `user_playlist` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `playlist_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_playlist`
--

INSERT INTO `user_playlist` (`id`, `user_id`, `playlist_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user_recent`
--

CREATE TABLE `user_recent` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `song_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_recent`
--

INSERT INTO `user_recent` (`id`, `user_id`, `song_id`) VALUES
(1181, 2, 2),
(1183, 2, 2),
(1185, 2, 2),
(1187, 2, 2),
(1188, 1, 2),
(1189, 2, 2),
(1190, 1, 2),
(1191, 2, 2),
(1192, 1, 2),
(1193, 2, 2),
(1194, 1, 2),
(1195, 2, 2),
(1196, 1, 2),
(1197, 2, 2),
(1198, 2, 2),
(1199, 2, 2),
(1200, 2, 2),
(1201, 2, 2),
(1202, 2, 2),
(1203, 2, 2),
(1204, 1, 2),
(1205, 1, 2),
(1206, 1, 2),
(1207, 2, 2),
(1208, 1, 3),
(1209, 2, 3),
(1210, 1, 2),
(1211, 2, 2),
(1212, 1, 2),
(1213, 1, 2),
(1214, 1, 2),
(1215, 1, 2),
(1216, 1, 2),
(1217, 1, 2),
(1218, 1, 2),
(1219, 1, 2),
(1220, 1, 2),
(1221, 1, 3),
(1222, 2, 2),
(1223, 2, 3);

-- --------------------------------------------------------

--
-- Table structure for table `user_song`
--

CREATE TABLE `user_song` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `song_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_song`
--

INSERT INTO `user_song` (`id`, `user_id`, `song_id`) VALUES
(1, 1, 2),
(2, 1, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `art`
--
ALTER TABLE `art`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `artist`
--
ALTER TABLE `artist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chat`
--
ALTER TABLE `chat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `friends`
--
ALTER TABLE `friends`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `playlist`
--
ALTER TABLE `playlist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `playlist_song`
--
ALTER TABLE `playlist_song`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `song`
--
ALTER TABLE `song`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_playlist`
--
ALTER TABLE `user_playlist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_recent`
--
ALTER TABLE `user_recent`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_song`
--
ALTER TABLE `user_song`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `art`
--
ALTER TABLE `art`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `artist`
--
ALTER TABLE `artist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `chat`
--
ALTER TABLE `chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `friends`
--
ALTER TABLE `friends`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `playlist`
--
ALTER TABLE `playlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `playlist_song`
--
ALTER TABLE `playlist_song`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `song`
--
ALTER TABLE `song`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user_playlist`
--
ALTER TABLE `user_playlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user_recent`
--
ALTER TABLE `user_recent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1224;

--
-- AUTO_INCREMENT for table `user_song`
--
ALTER TABLE `user_song`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
