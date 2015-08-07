data <- read.csv("hw1_data.csv")

# Question 12
frist_two_rows <- data[1:2,]

# Question 13
number_of_observations <- nrow(data)

# Question 14
last_two_rows <- tail(data, n=2)

# Question 15
result <- data[47,'Ozone']

# Question 16
missing_ozone <- sum(is.na(data['Ozone']))

# Question 17
mean_ozone <- mean(data['Ozone'][!is.na(data['Ozone'])])

# Question 18
mean_solor <- mean(subset(data, Ozone>31 & Temp>90)$Solar.R)

# Question 19
mean_temp <- mean(subset(data, Month==6)$Temp)

# Question 20
max_ozone <- max(subset(data, Month==5 & !is.na(Ozone))$Ozone)

