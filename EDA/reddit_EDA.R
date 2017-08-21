reddit = read.csv('reddit.csv')
summary(reddit)
str(reddit)

table(reddit$employment.status)
levels(reddit$age.range)

library(ggplot2)
qplot(data=reddit, x=age.range)
qplot (data=reddit, x=income.range)
is.factor(reddit$income.range)
is.factor(reddit$age.range)

reddit$age.range <- ordered(reddit$age.range, levels = c('Under 18', '18-24', '25-34', '35-44', '45-54', '55-64', '65 or Above'))

                            
reddit$age.range <- factor(reddit$age.range, levels = c('Under 18', '18-24', '25-34', '35-44', '45-54', '55-64', '65 or Above'), ordered = T)