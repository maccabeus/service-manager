

--
-- Database: `ervice_manager`
--

-- --------------------------------------------------------

--
-- Table structure for table `api_appsettings`
--

CREATE TABLE `api_appsettings` (
  `id` bigint(20) NOT NULL,
  `setting` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `value` varchar(250) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `api_appsettings`
--

INSERT INTO `api_appsettings` (`id`, `setting`, `value`) VALUES
(1, 'timezone', 'UTC'),
(2, 'opening_hour', '9'),
(3, 'closing_hour', '24');

-- --------------------------------------------------------

--
-- Table structure for table `api_customer`
--

CREATE TABLE `api_customer` (
  `id` bigint(20) NOT NULL,
  `name` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `date_created` date NOT NULL,
  `time_created` time(6) NOT NULL,
  `updated_at` datetime(6) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `api_employee`
--

CREATE TABLE `api_employee` (
  `id` bigint(20) NOT NULL,
  `name` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `department` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `date_created` date NOT NULL,
  `time_created` time(6) NOT NULL,
  `updated_at` datetime(6) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `api_employee`
--

INSERT INTO `api_employee` (`id`, `name`, `email`, `phone`, `department`, `date_created`, `time_created`, `updated_at`) VALUES
(1, 'John Luc', 'johnLuc@gmail.com', '+9 567 4455', 'Phone Repairs', '2021-06-01', '01:00:00.000000', NULL),
(2, 'John Luc', 'johnLuc@gmail.com', '+9 567 4455', 'Phone Repairs', '2018-05-09', '09:04:23.129000', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `api_holiday`
--

CREATE TABLE `api_holiday` (
  `id` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `api_holiday`
--

INSERT INTO `api_holiday` (`id`, `date`, `description`) VALUES
(1, '2021-01-01', 'New Year Holiday'),
(2, '2021-04-02', 'Good Friday'),
(3, '2021-07-01', 'Canada Day'),
(4, '2021-09-06', 'Labour Day'),
(5, '2021-05-30', 'test Holiday');

-- --------------------------------------------------------

--
-- Table structure for table `api_service`
--

CREATE TABLE `api_service` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `duration` double NOT NULL,
  `date_created` date NOT NULL,
  `time_created` time(6) NOT NULL,
  `updated_at` datetime(6) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `api_service`
--

INSERT INTO `api_service` (`id`, `name`, `description`, `duration`, `date_created`, `time_created`, `updated_at`) VALUES
(1, 'iPhone Screen Repairs', 'Amazing iPhone repair services', 120, '2021-06-27', '16:30:51.856098', NULL),
(2, '3 Bedroom Apartment Full House Cleaning', '3 Bedroom Apartment Cleaning', 4320, '2021-06-27', '16:33:10.296407', NULL),
(3, 'Hair Braiding', 'First Class Hair Braiding for all class of people', 240, '2021-06-27', '16:36:20.604893', NULL),
(4, 'Test Service', 'Test Service', 1, '2021-06-27', '16:33:10.296407', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `api_workorder`
--

CREATE TABLE `api_workorder` (
  `id` bigint(20) NOT NULL,
  `service_id` bigint(20) NOT NULL,
  `employee_id` bigint(20) NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL,
  `customer_id` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `duration` double NOT NULL,
  `date_created` date NOT NULL,
  `time_created` time(6) NOT NULL,
  `start_time` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `end_time` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `end_date` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `start_time_value` double NOT NULL,
  `end_time_value` double NOT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `done` bigint(20) NOT NULL,
  `deleted` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'api', '0001_initial', '2021-07-08 15:14:36.359878');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `api_appsettings`
--
ALTER TABLE `api_appsettings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_appsett_setting_203a94_idx` (`setting`);

--
-- Indexes for table `api_customer`
--
ALTER TABLE `api_customer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_custome_date_cr_b4a3c3_idx` (`date_created`),
  ADD KEY `api_custome_id_2c695e_idx` (`id`);

--
-- Indexes for table `api_employee`
--
ALTER TABLE `api_employee`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_employe_id_de9f32_idx` (`id`);

--
-- Indexes for table `api_holiday`
--
ALTER TABLE `api_holiday`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_holiday_date_1a4423_idx` (`date`);

--
-- Indexes for table `api_service`
--
ALTER TABLE `api_service`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_service_date_cr_35573f_idx` (`date_created`),
  ADD KEY `api_service_id_2f1f59_idx` (`id`);

--
-- Indexes for table `api_workorder`
--
ALTER TABLE `api_workorder`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_workord_date_cr_4d418a_idx` (`date_created`),
  ADD KEY `api_workord_custome_2f120d_idx` (`customer_id`),
  ADD KEY `api_workord_deleted_6d0c74_idx` (`deleted`),
  ADD KEY `api_workord_done_44c828_idx` (`done`),
  ADD KEY `api_workord_id_89db5c_idx` (`id`),
  ADD KEY `api_workord_start_t_08ff94_idx` (`start_time_value`),
  ADD KEY `api_workord_end_tim_191055_idx` (`end_time_value`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `api_appsettings`
--
ALTER TABLE `api_appsettings`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `api_customer`
--
ALTER TABLE `api_customer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `api_employee`
--
ALTER TABLE `api_employee`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `api_holiday`
--
ALTER TABLE `api_holiday`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `api_service`
--
ALTER TABLE `api_service`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `api_workorder`
--
ALTER TABLE `api_workorder`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;