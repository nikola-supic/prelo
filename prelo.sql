-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 01, 2021 at 03:03 PM
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
  `art` int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `artist`
--

INSERT INTO `artist` (`id`, `name`, `art`) VALUES
(1, 'Baja Mali Knindza', 1),
(2, 'Bojan Lukić', 1),
(3, 'Bora Drljača', 1),
(4, 'Braća Lekić', 1),
(5, 'Dusko Vulic Roca', 1),
(6, 'Gavro', 1),
(7, 'Goci Bend', 1),
(8, 'Goci I Lazo', 1),
(9, 'Hanka Paldum', 1),
(10, 'Indira Radić', 1),
(11, 'Jele', 1),
(12, 'Jele I Jovan Puzovic', 1),
(13, 'Katarina Kovačević', 1),
(14, 'Krajisnici Milos I Karadjordje', 1),
(15, 'Krajisnici Milos I Karađorđe', 1),
(16, 'Krajisnici Nedeljko I Dragan', 1),
(17, 'Krajisnici Zare I Goci', 1),
(18, 'Krajiška Grupa Manjača', 1),
(19, 'Magnifico', 1),
(20, 'Merima Njegomir', 1),
(21, 'Milica Krsmanovic', 1),
(22, 'Milimir Djuricic Djuka', 1),
(23, 'Miljan Miljanic', 1),
(24, 'Milomir Miljan Miljanic', 1),
(25, 'Milomir Miljanic', 1),
(26, 'Milomir Miljanic & Ivan Krgovic', 1),
(27, 'Milomir Miljanic & Lazo Pajcin', 1),
(28, 'Milomir Miljanic & M. Miljanic', 1),
(29, 'Milomir Miljanic Milan', 1),
(30, 'Milomir Miljanic Miljan', 1),
(31, 'Miloš Bubanja', 1),
(32, 'Nedeljko I Dragan', 1),
(33, 'Njegos Radjenovic Njego', 1),
(34, 'Pero I Milan', 1),
(35, 'Predrag Živković Tozovac', 1),
(36, 'Sinovi Manjace & Boco', 1),
(37, 'Sinovi Manjace', 1),
(38, 'Veseli Vrbljanci', 1),
(39, 'Zare & Goci', 1),
(40, 'Zare I Goci', 1),
(41, 'Zavicajno Jato', 1),
(42, 'Zoran Zoka Kulina', 1),
(43, 'Zorica Brunclik', 1),
(44, 'Četničke', 1),
(45, 'Žorž', 1),
(46, 'Антерија', 1),
(47, 'Даница Црногорчевић', 1);

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

-- --------------------------------------------------------

--
-- Table structure for table `playlist_song`
--

CREATE TABLE `playlist_song` (
  `id` int(11) NOT NULL,
  `playlist_id` int(11) NOT NULL,
  `song_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `song`
--

CREATE TABLE `song` (
  `id` int(11) NOT NULL,
  `artist_id` int(11) NOT NULL,
  `name` varchar(48) NOT NULL,
  `art` int(11) NOT NULL DEFAULT 1,
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
(1, 1, 'Dinarsko Srce', 1, 'songs\\Baja Mali Knindza - Dinarsko Srce.mp3', 190, 'Server Admin', 192000, '2021-08-01'),
(2, 1, '90', 1, 'songs\\Baja Mali Knindza - 90.mp3', 150, 'Server Admin', 192000, '2021-08-01'),
(3, 1, 'Alkos nema perspektivu', 1, 'songs\\Baja Mali Knindza - Alkos nema perspektivu.mp3', 166, 'Server Admin', 192000, '2021-08-01'),
(4, 1, 'Arija Nebeska', 1, 'songs\\Baja Mali Knindza - Arija Nebeska.mp3', 247, 'Server Admin', 192000, '2021-08-01'),
(5, 1, 'Baba Ruža I Djed Nikola', 1, 'songs\\Baja Mali Knindza - Baba Ruža I Djed Nikola.mp3', 212, 'Server Admin', 192000, '2021-08-01'),
(6, 1, 'Badnjak', 1, 'songs\\Baja Mali Knindza - Badnjak.mp3', 140, 'Server Admin', 192000, '2021-08-01'),
(7, 1, 'Bez zavicaja', 1, 'songs\\Baja Mali Knindza - Bez zavicaja.mp3', 236, 'Server Admin', 192000, '2021-08-01'),
(8, 1, 'Bozic je', 1, 'songs\\Baja Mali Knindza - Bozic je.mp3', 248, 'Server Admin', 192000, '2021-08-01'),
(9, 1, 'Cuvaj mi se sine', 1, 'songs\\Baja Mali Knindza - Cuvaj mi se sine.mp3', 214, 'Server Admin', 192000, '2021-08-01'),
(10, 1, 'Da Ne Bjese Niksicana', 1, 'songs\\Baja Mali Knindza - Da Ne Bjese Niksicana.mp3', 114, 'Server Admin', 192000, '2021-08-01'),
(11, 1, 'Djedo', 1, 'songs\\Baja Mali Knindza - Djedo.mp3', 187, 'Server Admin', 192000, '2021-08-01'),
(12, 1, 'Duni vjetre preko jetre', 1, 'songs\\Baja Mali Knindza - Duni vjetre preko jetre.mp3', 172, 'Server Admin', 192000, '2021-08-01'),
(13, 1, 'Dva Galeba I Verige', 1, 'songs\\Baja Mali Knindza - Dva Galeba I Verige.mp3', 267, 'Server Admin', 192000, '2021-08-01'),
(14, 1, 'Evo Dzepa Dje Su Pare Bile', 1, 'songs\\Baja Mali Knindza - Evo Dzepa Dje Su Pare Bile.mp3', 182, 'Server Admin', 192000, '2021-08-01'),
(15, 1, 'Gresnik', 1, 'songs\\Baja Mali Knindza - Gresnik.mp3', 175, 'Server Admin', 192000, '2021-08-01'),
(16, 1, 'Idemo Malena', 1, 'songs\\Baja Mali Knindza - Idemo Malena.mp3', 201, 'Server Admin', 192000, '2021-08-01'),
(17, 1, 'Ja Sam Rođen Na Kosovu', 1, 'songs\\Baja Mali Knindza - Ja Sam Rođen Na Kosovu.mp3', 244, 'Server Admin', 192000, '2021-08-01'),
(18, 1, 'Jednom kada odem', 1, 'songs\\Baja Mali Knindza - Jednom kada odem.mp3', 215, 'Server Admin', 192000, '2021-08-01'),
(19, 1, 'Još Se Dana Sećam Ilindana', 1, 'songs\\Baja Mali Knindza - Još Se Dana Sećam Ilindana.mp3', 178, 'Server Admin', 192000, '2021-08-01'),
(20, 1, 'Kad sam bio mali', 1, 'songs\\Baja Mali Knindza - Kad sam bio mali.mp3', 218, 'Server Admin', 192000, '2021-08-01'),
(21, 1, 'Komunjare', 1, 'songs\\Baja Mali Knindza - Komunjare.mp3', 267, 'Server Admin', 192000, '2021-08-01'),
(22, 1, 'Krajino krvava haljino', 1, 'songs\\Baja Mali Knindza - Krajino krvava haljino.mp3', 162, 'Server Admin', 192000, '2021-08-01'),
(23, 1, 'Milice Kćeri', 1, 'songs\\Baja Mali Knindza - Milice Kćeri.mp3', 253, 'Server Admin', 192000, '2021-08-01'),
(24, 1, 'Morem plovi jedna mala barka', 1, 'songs\\Baja Mali Knindza - Morem plovi jedna mala barka.mp3', 176, 'Server Admin', 192000, '2021-08-01'),
(25, 1, 'Napaceni brat', 1, 'songs\\Baja Mali Knindza - Napaceni brat.mp3', 202, 'Server Admin', 192000, '2021-08-01'),
(26, 1, 'Ne Rodila Ni Njivo Ni Sljivo', 1, 'songs\\Baja Mali Knindza - Ne Rodila Ni Njivo Ni Sljivo.mp3', 246, 'Server Admin', 192000, '2021-08-01'),
(27, 1, 'Ne volim te Alija -', 1, 'songs\\Baja Mali Knindza - Ne volim te Alija -.mp3', 185, 'Server Admin', 192000, '2021-08-01'),
(28, 1, 'Ne volim te Alija', 1, 'songs\\Baja Mali Knindza - Ne volim te Alija.mp3', 182, 'Server Admin', 192000, '2021-08-01'),
(29, 1, 'Od Topole Do Topole', 1, 'songs\\Baja Mali Knindza - Od Topole Do Topole.mp3', 138, 'Server Admin', 192000, '2021-08-01'),
(30, 1, 'Oj Alija Nisi Vise Glavni', 1, 'songs\\Baja Mali Knindza - Oj Alija Nisi Vise Glavni.mp3', 174, 'Server Admin', 192000, '2021-08-01'),
(31, 1, 'Pevaj Srbijo', 1, 'songs\\Baja Mali Knindza - Pevaj Srbijo.mp3', 218, 'Server Admin', 192000, '2021-08-01'),
(32, 1, 'Placu Nekad I Bogati', 1, 'songs\\Baja Mali Knindza - Placu Nekad I Bogati.mp3', 267, 'Server Admin', 192000, '2021-08-01'),
(33, 1, 'Prosli su mi vozovi', 1, 'songs\\Baja Mali Knindza - Prosli su mi vozovi.mp3', 169, 'Server Admin', 192000, '2021-08-01'),
(34, 1, 'Ptico Moja, Beli Labude', 1, 'songs\\Baja Mali Knindza - Ptico Moja, Beli Labude.mp3', 262, 'Server Admin', 192000, '2021-08-01'),
(35, 1, 'Sa Manjace Krenuli Su Vuci', 1, 'songs\\Baja Mali Knindza - Sa Manjace Krenuli Su Vuci.mp3', 204, 'Server Admin', 192000, '2021-08-01'),
(36, 1, 'Stari Bagrem', 1, 'songs\\Baja Mali Knindza - Stari Bagrem.mp3', 223, 'Server Admin', 192000, '2021-08-01'),
(37, 1, 'Tata', 1, 'songs\\Baja Mali Knindza - Tata.mp3', 146, 'Server Admin', 192000, '2021-08-01'),
(38, 1, 'Ulicarka i lopov', 1, 'songs\\Baja Mali Knindza - Ulicarka i lopov.mp3', 177, 'Server Admin', 192000, '2021-08-01'),
(39, 1, 'Ulje Maslinovo', 1, 'songs\\Baja Mali Knindza - Ulje Maslinovo.mp3', 253, 'Server Admin', 192000, '2021-08-01'),
(40, 1, 'Vojvoda Neunistivi', 1, 'songs\\Baja Mali Knindza - Vojvoda Neunistivi.mp3', 173, 'Server Admin', 192000, '2021-08-01'),
(41, 1, 'Volela me kao druga', 1, 'songs\\Baja Mali Knindza - Volela me kao druga.mp3', 176, 'Server Admin', 192000, '2021-08-01'),
(42, 1, 'Vratice se Novak', 1, 'songs\\Baja Mali Knindza - Vratice se Novak.mp3', 244, 'Server Admin', 192000, '2021-08-01'),
(43, 1, 'Zove dinara', 1, 'songs\\Baja Mali Knindza - Zove dinara.mp3', 173, 'Server Admin', 128000, '2021-08-01'),
(44, 2, 'Heineken', 1, 'songs\\Bojan Lukić - Heineken.mp3', 175, 'Server Admin', 192000, '2021-08-01'),
(45, 3, 'Otisla Je Danijela', 1, 'songs\\Bora Drljača - Otisla Je Danijela.mp3', 194, 'Server Admin', 192000, '2021-08-01'),
(46, 4, 'Alkoholičar', 1, 'songs\\Braća Lekić - Alkoholičar.mp3', 146, 'Server Admin', 192000, '2021-08-01'),
(47, 5, 'Udarac U Prazno', 1, 'songs\\Dusko Vulic Roca - Udarac U Prazno.mp3', 154, 'Server Admin', 192000, '2021-08-01'),
(48, 6, 'Prži Li Ga Prži', 1, 'songs\\Gavro - Prži Li Ga Prži.mp3', 388, 'Server Admin', 192000, '2021-08-01'),
(49, 7, 'Korona', 1, 'songs\\Goci Bend - Korona.mp3', 230, 'Server Admin', 192000, '2021-08-01'),
(50, 7, 'Oj Gatacko Polje', 1, 'songs\\Goci Bend - Oj Gatacko Polje.mp3', 198, 'Server Admin', 192000, '2021-08-01'),
(51, 7, 'Ozenjenog Hteli Da Me Zene', 1, 'songs\\Goci Bend - Ozenjenog Hteli Da Me Zene.mp3', 190, 'Server Admin', 192000, '2021-08-01'),
(52, 7, 'Bi Li Kume Kumovao', 1, 'songs\\Goci Bend - Bi Li Kume Kumovao.mp3', 175, 'Server Admin', 192000, '2021-08-01'),
(53, 7, 'Gdje Si Brate, Gdje Si Imenjace', 1, 'songs\\Goci Bend - Gdje Si Brate, Gdje Si Imenjace.mp3', 199, 'Server Admin', 192000, '2021-08-01'),
(54, 7, 'Kad Ne Ide I Ne Stima', 1, 'songs\\Goci Bend - Kad Ne Ide I Ne Stima.mp3', 184, 'Server Admin', 192000, '2021-08-01'),
(55, 7, 'Kredit', 1, 'songs\\Goci Bend - Kredit.mp3', 200, 'Server Admin', 192000, '2021-08-01'),
(56, 7, 'Ljepotica S Pala', 1, 'songs\\Goci Bend - Ljepotica S Pala.mp3', 185, 'Server Admin', 192000, '2021-08-01'),
(57, 7, 'Policajka', 1, 'songs\\Goci Bend - Policajka.mp3', 184, 'Server Admin', 192000, '2021-08-01'),
(58, 7, 'Svira Frula, Svira Violina', 1, 'songs\\Goci Bend - Svira Frula, Svira Violina.mp3', 206, 'Server Admin', 192000, '2021-08-01'),
(59, 7, 'Udala Se Na Svadbi Joj Bio', 1, 'songs\\Goci Bend - Udala Se Na Svadbi Joj Bio.mp3', 167, 'Server Admin', 192000, '2021-08-01'),
(60, 7, 'Vakcina', 1, 'songs\\Goci Bend - Vakcina.mp3', 173, 'Server Admin', 192000, '2021-08-01'),
(61, 7, 'Vozi Me Na Pale', 1, 'songs\\Goci Bend - Vozi Me Na Pale.mp3', 228, 'Server Admin', 192000, '2021-08-01'),
(62, 8, 'Dje Si Kume Ljudski Maksimume', 1, 'songs\\Goci I Lazo - Dje Si Kume Ljudski Maksimume.mp3', 215, 'Server Admin', 192000, '2021-08-01'),
(63, 8, 'Ima Nesto Sto Kupiti Ja Ne Mogu', 1, 'songs\\Goci I Lazo - Ima Nesto Sto Kupiti Ja Ne Mogu.mp3', 229, 'Server Admin', 192000, '2021-08-01'),
(64, 8, 'Mala Se Zaljubila', 1, 'songs\\Goci I Lazo - Mala Se Zaljubila.mp3', 188, 'Server Admin', 192000, '2021-08-01'),
(65, 8, 'Sirotinja', 1, 'songs\\Goci I Lazo - Sirotinja.mp3', 256, 'Server Admin', 192000, '2021-08-01'),
(66, 9, 'Ali Pamtim Još', 1, 'songs\\Hanka Paldum - Ali Pamtim Još.mp3', 277, 'Server Admin', 192000, '2021-08-01'),
(67, 10, 'Srpkinja Je Mene Majka Rodila', 1, 'songs\\Indira Radić - Srpkinja Je Mene Majka Rodila.mp3', 244, 'Server Admin', 192000, '2021-08-01'),
(68, 11, 'Sta Ce Meni Teretana', 1, 'songs\\Jele - Sta Ce Meni Teretana.mp3', 204, 'Server Admin', 192000, '2021-08-01'),
(69, 12, 'Nismo Krivi Nas Dvojica', 1, 'songs\\Jele I Jovan Puzovic - Nismo Krivi Nas Dvojica.mp3', 181, 'Server Admin', 192000, '2021-08-01'),
(70, 13, 'Dal Si Momče Iz Nikšića', 1, 'songs\\Katarina Kovačević - Dal Si Momče Iz Nikšića.mp3', 197, 'Server Admin', 192000, '2021-08-01'),
(71, 14, 'Djavolica', 1, 'songs\\Krajisnici Milos I Karadjordje - Djavolica.mp3', 180, 'Server Admin', 192000, '2021-08-01'),
(72, 15, 'Dje Se Tvoji Kopaju', 1, 'songs\\Krajisnici Milos I Karađorđe - Dje Se Tvoji Kopaju.mp3', 219, 'Server Admin', 192000, '2021-08-01'),
(73, 16, 'Kupacica', 1, 'songs\\Krajisnici Nedeljko I Dragan - Kupacica.mp3', 170, 'Server Admin', 192000, '2021-08-01'),
(74, 16, 'Svercovana Gradja', 1, 'songs\\Krajisnici Nedeljko I Dragan - Svercovana Gradja.mp3', 198, 'Server Admin', 192000, '2021-08-01'),
(75, 17, 'Baraba', 1, 'songs\\Krajisnici Zare I Goci - Baraba.mp3', 166, 'Server Admin', 192000, '2021-08-01'),
(76, 17, 'Crna Dama', 1, 'songs\\Krajisnici Zare I Goci - Crna Dama.mp3', 178, 'Server Admin', 192000, '2021-08-01'),
(77, 17, 'Evo Brata', 1, 'songs\\Krajisnici Zare I Goci - Evo Brata.mp3', 249, 'Server Admin', 192000, '2021-08-01'),
(78, 17, 'Olivera', 1, 'songs\\Krajisnici Zare i Goci - Olivera.mp3', 160, 'Server Admin', 128000, '2021-08-01'),
(79, 17, 'Volim Zenu Crne Kose', 1, 'songs\\Krajisnici Zare I Goci - Volim Zenu Crne Kose.mp3', 160, 'Server Admin', 192000, '2021-08-01'),
(80, 18, 'Nevjesta', 1, 'songs\\Krajiška Grupa Manjača - Nevjesta.mp3', 163, 'Server Admin', 128000, '2021-08-01'),
(81, 15, 'Korona Virus', 1, 'songs\\Krajišnici Miloš I Karađorđe - Korona Virus.mp3', 200, 'Server Admin', 192000, '2021-08-01'),
(82, 19, 'Pukni Zoro', 1, 'songs\\Magnifico - Pukni Zoro.mp3', 185, 'Server Admin', 192000, '2021-08-01'),
(83, 20, 'Ivanova Korita', 1, 'songs\\Merima Njegomir - Ivanova Korita.mp3', 200, 'Server Admin', 192000, '2021-08-01'),
(84, 21, 'Oprastam Ti Sve', 1, 'songs\\Milica Krsmanovic - Oprastam Ti Sve.mp3', 241, 'Server Admin', 192000, '2021-08-01'),
(85, 22, 'Doci Cu Ti Na Komove', 1, 'songs\\Milimir Djuricic Djuka - Doci Cu Ti Na Komove.mp3', 219, 'Server Admin', 192000, '2021-08-01'),
(86, 23, 'Sveti Vasi', 1, 'songs\\Miljan Miljanic - Sveti Vasilije - Dobro Vece Rodni Kraju.mp3', 196, 'Server Admin', 192000, '2021-08-01'),
(87, 24, 'Sestrice Mila', 1, 'songs\\Milomir Miljan Miljanic - Sestrice Mila.mp3', 241, 'Server Admin', 192000, '2021-08-01'),
(88, 25, 'Još Ćemo Se Mi Ćerati', 1, 'songs\\Milomir Miljanic - Još Ćemo Se Mi Ćerati.mp3', 186, 'Server Admin', 192000, '2021-08-01'),
(89, 25, 'Uzece Ti Obraz', 1, 'songs\\Milomir Miljanic - Uzece Ti Obraz.mp3', 220, 'Server Admin', 192000, '2021-08-01'),
(90, 26, 'Pitaju Me Ko Sam', 1, 'songs\\Milomir Miljanic & Ivan Krgovic - Pitaju Me Ko Sam.mp3', 207, 'Server Admin', 192000, '2021-08-01'),
(91, 27, 'Republika Srpska', 1, 'songs\\Milomir Miljanic & Lazo Pajcin - Republika Srpska.mp3', 198, 'Server Admin', 192000, '2021-08-01'),
(92, 28, 'Izbeglica', 1, 'songs\\Milomir Miljanic & M. Miljanic - Izbeglica.mp3', 225, 'Server Admin', 192000, '2021-08-01'),
(93, 25, 'Budi Borac', 1, 'songs\\Milomir Miljanic - Budi Borac.mp3', 183, 'Server Admin', 192000, '2021-08-01'),
(94, 25, 'Dje U Ljetos Gazis Snijeg', 1, 'songs\\Milomir Miljanic - Dje U Ljetos Gazis Snijeg.mp3', 203, 'Server Admin', 192000, '2021-08-01'),
(95, 25, 'Dogodine U Prizrenu', 1, 'songs\\Milomir Miljanic - Dogodine U Prizrenu.mp3', 219, 'Server Admin', 192000, '2021-08-01'),
(96, 25, 'Eh Da Imam Takve Moci', 1, 'songs\\Milomir Miljanic - Eh Da Imam Takve Moci.mp3', 250, 'Server Admin', 192000, '2021-08-01'),
(97, 25, 'Idem Tamo Dje Me Vole', 1, 'songs\\Milomir Miljanic - Idem Tamo Dje Me Vole.mp3', 188, 'Server Admin', 192000, '2021-08-01'),
(98, 25, 'Je Li Svadba Ili Nije', 1, 'songs\\Milomir Miljanic - Je Li Svadba Ili Nije.mp3', 208, 'Server Admin', 192000, '2021-08-01'),
(99, 25, 'Kolo Sviraj Ne Foliraj', 1, 'songs\\Milomir Miljanic - Kolo Sviraj Ne Foliraj.mp3', 207, 'Server Admin', 192000, '2021-08-01'),
(100, 25, 'Samo Srbin Slavu Slavi', 1, 'songs\\Milomir Miljanic - Samo Srbin Slavu Slavi.mp3', 216, 'Server Admin', 192000, '2021-08-01'),
(101, 25, 'To Srpkinja Samo Radja', 1, 'songs\\Milomir Miljanic - To Srpkinja Samo Radja.mp3', 212, 'Server Admin', 192000, '2021-08-01'),
(102, 25, 'Ucini Mi Bar Toliko', 1, 'songs\\Milomir Miljanic - Ucini Mi Bar Toliko.mp3', 203, 'Server Admin', 192000, '2021-08-01'),
(103, 25, 'Zaduzbina', 1, 'songs\\Milomir Miljanic - Zaduzbina.mp3', 238, 'Server Admin', 192000, '2021-08-01'),
(104, 29, 'Sirocici', 1, 'songs\\Milomir Miljanic Milan - Sirocici.mp3', 223, 'Server Admin', 192000, '2021-08-01'),
(105, 30, 'Gledaj Orle', 1, 'songs\\Milomir Miljanic Miljan - Gledaj Orle.mp3', 186, 'Server Admin', 192000, '2021-08-01'),
(106, 30, 'Sine Moj', 1, 'songs\\Milomir Miljanic Miljan - Sine Moj.mp3', 221, 'Server Admin', 192000, '2021-08-01'),
(107, 30, 'Srpski Jerusalim', 1, 'songs\\Milomir Miljanic Miljan - Srpski Jerusalim.mp3', 223, 'Server Admin', 192000, '2021-08-01'),
(108, 31, 'Nikšićani Delije, Da Li Znate Dje Li Je', 1, 'songs\\Miloš Bubanja - Nikšićani Delije, Da Li Znate Dje Li Je.mp3', 218, 'Server Admin', 192000, '2021-08-01'),
(109, 32, 'Kupacica 2', 1, 'songs\\Nedeljko I Dragan - Kupacica 2.mp3', 230, 'Server Admin', 192000, '2021-08-01'),
(110, 33, 'Maturska', 1, 'songs\\Njegos Radjenovic Njego - Maturska.mp3', 207, 'Server Admin', 192000, '2021-08-01'),
(111, 34, 'U Kafanu Svrati', 1, 'songs\\Pero I Milan - U Kafanu Svrati.mp3', 233, 'Server Admin', 192000, '2021-08-01'),
(112, 35, 'Vlajna', 1, 'songs\\Predrag Živković Tozovac - Vlajna.mp3', 176, 'Server Admin', 192000, '2021-08-01'),
(113, 36, 'Milorad', 1, 'songs\\Sinovi Manjace & Boco - Milorad.mp3', 192, 'Server Admin', 192000, '2021-08-01'),
(114, 37, 'Austrija Nije Za Becara', 1, 'songs\\Sinovi Manjace - Austrija Nije Za Becara.mp3', 174, 'Server Admin', 192000, '2021-08-01'),
(115, 37, 'Sta Je Srbin Bez Bozica', 1, 'songs\\Sinovi Manjace - Sta Je Srbin Bez Bozica.mp3', 167, 'Server Admin', 192000, '2021-08-01'),
(116, 38, 'Direktor', 1, 'songs\\Veseli Vrbljanci - Direktor.mp3', 231, 'Server Admin', 192000, '2021-08-01'),
(117, 39, 'Garavusa', 1, 'songs\\Zare & Goci - Garavusa.mp3', 241, 'Server Admin', 192000, '2021-08-01'),
(118, 40, 'Preledzija Je To', 1, 'songs\\Zare I Goci - Preledzija Je To.mp3', 194, 'Server Admin', 192000, '2021-08-01'),
(119, 41, 'Becar', 1, 'songs\\Zavicajno Jato - Becar.mp3', 189, 'Server Admin', 192000, '2021-08-01'),
(120, 41, 'Ja Sam Puko', 1, 'songs\\Zavicajno Jato - Ja Sam Puko.mp3', 174, 'Server Admin', 192000, '2021-08-01'),
(121, 41, 'Snajka', 1, 'songs\\Zavicajno Jato - Snajka.mp3', 190, 'Server Admin', 192000, '2021-08-01'),
(122, 42, 'Gari Garo, Evo Brke, Ja Sam Lola, Soferska', 1, 'songs\\Zoran Zoka Kulina - Gari Garo, Evo Brke, Ja Sam Lola, Soferska.mp3', 783, 'Server Admin', 192000, '2021-08-01'),
(123, 43, 'Što Se Mala Uobrazi', 1, 'songs\\Zorica Brunclik - Što Se Mala Uobrazi.mp3', 208, 'Server Admin', 192000, '2021-08-01'),
(124, 44, 'Ide Vojska Od Nikšića', 1, 'songs\\Četničke - Ide Vojska Od Nikšića.mp3', 203, 'Server Admin', 192000, '2021-08-01'),
(125, 45, 'Neću Nidje', 1, 'songs\\Žorž - Neću Nidje.mp3', 186, 'Server Admin', 192000, '2021-08-01'),
(126, 46, 'Јунаци Са Кошара', 1, 'songs\\Антерија - Јунаци Са Кошара.mp3', 178, 'Server Admin', 192000, '2021-08-01'),
(127, 47, 'Вјера Наша Вјера Славна', 1, 'songs\\Даница Црногорчевић - Вјера Наша Вјера Славна.mp3', 188, 'Server Admin', 192000, '2021-08-01'),
(128, 47, 'Ој Јунаштва Свијетла Зоро', 1, 'songs\\Даница Црногорчевић - Ој Јунаштва Свијетла Зоро.mp3', 145, 'Server Admin', 192000, '2021-08-01'),
(129, 47, 'Ој Косово Косово', 1, 'songs\\Даница Црногорчевић - Ој Косово Косово.mp3', 165, 'Server Admin', 192000, '2021-08-01'),
(130, 47, 'Сини Јарко Сунце Са Косова', 1, 'songs\\Даница Црногорчевић - Сини Јарко Сунце Са Косова.mp3', 127, 'Server Admin', 192000, '2021-08-01');

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
(1, 'Никола', 'Шупић', 'dzast_nikola', 'nikola.supic09@gmail.com', '$2b$12$qPIjIy6sOYtA7m8yVfzm6e5DSlxP0v6HisV7A1tPjPG5d.XzncPX2', '$2b$12$qPIjIy6sOYtA7m8yVfzm6e', '1970-01-01', 1, '2021-07-29 15:05:32', 0, '2021-08-01 14:59:28', 1, 0),
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
(339, 1, 49),
(340, 1, 50),
(341, 1, 49),
(342, 1, 50),
(343, 1, 49),
(344, 1, 49),
(345, 1, 50),
(346, 1, 49),
(347, 1, 49),
(348, 1, 59),
(349, 1, 58),
(350, 1, 53),
(351, 1, 52),
(352, 1, 54),
(353, 1, 55),
(354, 1, 51),
(355, 1, 58),
(356, 1, 56),
(357, 1, 52),
(358, 1, 60);

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
(7, 1, 49),
(8, 1, 50);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `chat`
--
ALTER TABLE `chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `friends`
--
ALTER TABLE `friends`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `playlist`
--
ALTER TABLE `playlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `playlist_song`
--
ALTER TABLE `playlist_song`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `song`
--
ALTER TABLE `song`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=131;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user_playlist`
--
ALTER TABLE `user_playlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_recent`
--
ALTER TABLE `user_recent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=359;

--
-- AUTO_INCREMENT for table `user_song`
--
ALTER TABLE `user_song`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
