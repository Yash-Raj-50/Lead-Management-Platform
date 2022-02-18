CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `created_at` timestamp,
  `first_name` varchar(255),
  `last_name` varchar(255),
  `email` varchar(255),
  `phone_number` int,
  `password` varchar(255),
  `user_type` varchar(255),
  `is_staff` boolean,
  `is_superuser` boolean,
  `manager_id` int
);

CREATE TABLE `leads` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `created_at` timestamp,
  `name` varchar(255),
  `email_address` varchar(255),
  `phone_number` int,
  `state` varchar(255),
  `user_id` int
);

CREATE TABLE `remarks` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `created_at` timestamp,
  `remark` text,
  `lead_id` int,
  `user_id` int
);

ALTER TABLE `users` ADD FOREIGN KEY (`manager_id`) REFERENCES `users` (`id`);

ALTER TABLE `leads` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `remarks` ADD FOREIGN KEY (`lead_id`) REFERENCES `leads` (`id`);

ALTER TABLE `remarks` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
