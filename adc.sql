-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2019 at 09:08 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `adc`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(1, 'first post', 'firstpost@gmail.com', '123456789', 'This is the beginning.', '2019-09-28 18:15:26'),
(2, 'Beginner', 'beginner@gmail.com', '8765456789', 'Test Message', NULL),
(3, 'Beginner', 'beginner@gmail.com', '8765456789', 'Test Message 2', '2019-10-02 12:15:33'),
(4, 'Incrementation', 'beginner@gmail.com', '8765456789', 'test', '2019-10-03 00:07:36'),
(5, 'hgh', 'rdd@gmail.com', '987654321', 'hfyf', '2019-10-04 11:44:55'),
(6, 'Beginner', 'beginner2@gmail.com', '', '', '2019-10-04 12:01:29'),
(7, 'Beginner', 'beginner2@gmail.com', '8765456789', 'test for manohar', '2019-10-04 12:02:01'),
(8, 'Umar', 'umarmoin98@gmail.com', '+91-98567327', 'Hi There.', '2019-10-30 01:28:25'),
(9, 'Aiman', 'aiman.hafeez18@gmail.com', '+91-7897708254', 'Hello Mohib. How Are you?\r\nCould Improve a bit', '2019-10-31 13:23:15');

-- --------------------------------------------------------

--
-- Table structure for table `notice`
--

CREATE TABLE `notice` (
  `sno` int(3) NOT NULL,
  `note` varchar(250) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `notice`
--

INSERT INTO `notice` (`sno`, `note`, `date`) VALUES
(1, 'OOPS - Object Oriented Programming Sucks - Not really.', '2019-10-19 21:04:16'),
(2, 'Be prepared for Failure. Cause Failure is always an option but losing to your failure is not. Good luck! This is Testing notice 2. First one was a silly mistake, My bad.', '2019-10-19 21:06:07'),
(3, 'Looks all good to me. Test 3', '2019-10-19 21:37:34'),
(4, 'Test 4. Filling up some rows in database to check for any errors.', '2019-10-19 21:38:13'),
(5, 'Test 5. Checking if pagination is working.', '2019-10-19 21:38:53'),
(8, 'yoo hoo', '2019-10-23 16:48:19');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'Will of Fire.', 'Let it Burn.', 'first-post', 'There can be no thought of finishing for ‘aiming for the stars.’ Both figuratively and literally, it is a task to occupy the generations. And no matter how much progress one makes, there is always the thrill of just beginning.', 'post-bg.jpg', '2019-10-23 18:22:15'),
(2, ' A Journey of a thousand miles.', 'Never fear to begin.', 'second-post', 'Thus out of small beginnings greater things have been produced by His hand that made all things of nothing, and gives being to all things that are; and, as one small candle may light a thousand, so the light here kindled hath shone unto many.', 'post-bg.jpg', '2019-10-06 00:18:01'),
(3, 'Novato Fiesta', 'We are Mephobians', 'third-post', 'Again a new batch of students will sit in same old classrooms, sit on same old DESKS & Benches, completely unaware of history or what stories, those things hold in them from the time of their dawn at this University. \r\n\r\n\"Khush to bahut honge tum aaj..haain\r\nCollege me azaadi hongi..kisi ne zaroor kaha hoga.\r\n\r\nDinbhar canteen main masti aur aaspaas chai ki tapki..\r\nJigri yaar tumhare honge..\r\nKisi ne zarur kaha hoga..\r\n\r\nNa zyada homework hoga..na zyada bandishe hongi..\r\nNa koi sarhad na taaren hongi.\r\nKisi ne zarur kaha hoga..\r\n\r\nChahe paido ke patte peele ho ya dhool hawa k sath ude\r\nDil ka mayura nach uthe..aise mausam sare honge.\r\nKisi ne zarur kaha hoga.\r\n\r\nLaddakh me jawani ke..goa ke pani ke.\r\nPlan ban ban ke dilo me utare honge.\r\nKisi ne zarur kaha hoga.\r\n\r\nMain Syed bol raha hu dil se..\r\nAise lamhe guzrenge..jaise na kabhi guzare honge..\r\nHar sapna tumhara..manjoor yaha hoga.\r\nKisi ne zaroor kaha hoga\"', 'IMG_0177.jpg', '2019-10-18 20:01:31'),
(5, 'Editing', 'Edit/Add Post', 'new-post', 'This message is just to test the credibility of this form to add/edit post as per the required conventions and need of the user.', 'noexist.png', '2019-10-18 21:33:45'),
(6, 'Test', 'Practice is best', 'ok', 'halaluyah', 'asd.png', '2019-10-18 21:40:02'),
(7, 'Test 2', 'Practice is best', 'ko', 'Testing new add post method', '', '2019-10-24 18:44:48'),
(9, 'Editing Posts', 'New Method', 'fourth-post', 'This post is for checking the newly implemented method for adding posts.', 'about-bg.png', '2019-10-24 18:50:54'),
(10, 'Optimization', 'Testing', 'optimize', 'Code is optimized', 'no', '2019-10-25 00:23:22'),
(11, 'Test', 'Presentation', 'hello-there', 'This is in the presentation', 'noexist.png', '2019-11-02 09:12:29');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `notice`
--
ALTER TABLE `notice`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `notice`
--
ALTER TABLE `notice`
  MODIFY `sno` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
