library(dplyr)
library(tidyr)
library(stringr)

# first create variable names
rew = c("r2")#,"r2")#, "r3")
prob = c("p1", "p2", "p3")
mag = c("m1", "m2", "m3")

names_vector = rep(NA,9) # preassign vector; we have 3x3x3 combinations from vectors above

index =1 # this is just to assign the values inside the loop to the vector "names_vector"

assign_names <- function(){
  for (i in rew){
    for (j in prob){
      for (k in mag){
        #cat("index:", index, "\n")
        names_vector[index] = paste(i, j, k, ".png", sep = "")
        index = index + 1
      }
    }
  }
return(names_vector) # needs tor return 
}

names = assign_names() # names is the vector with the names produced in the function

names = unlist(names) # transform to vector
names_df = cbind(names, names)
names_df = as.data.frame(names_df) # create df with 2 cols, one for left stim and one for right stim
names(names_df) = c("fractal_left", "fractal_right") 

# now we permute and create all combinations 

# These two vectors are used to create all combinations
names_left = names_df$fractal_left #c("A", "B") 
names_right = names_df$fractal_right #c("A", "B")

# probs_left = c("low", "high")
# probs_right = c("low", "high")

# cat("stim left, stim_right", "prob_left\n")

conditions_vector = rep(NA, 81)

index = 1

create_cols = function(){
  for (i in names_left){
    for (j in names_right){
      #for (k in probs_left){
        #for (l in probs_right){
        conditions_vector[index] = paste(i, j, sep = ",")
        cat(i, j, "\n")#, k,l, "\n")
        index = index + 1
        #}
      #}
    }
  }
  return(conditions_vector)
}

conditions_df = create_cols()

# then just take the txt output and copy it to a txt file, then use excel.

#### Create other columns based on stim name ####
# conditions1 = read_table2("Dropbox/Projects/Caltech/Humans/Mapping Prefrontal Cortex/two_choice/conditions2.txt",
                          # col_names = FALSE, col_types = cols(X3 = col_skip())) # load txt file
conditions1 <- read.table("~/Dropbox/Projects/Caltech/Humans/Mapping Prefrontal Cortex/two_choice/conditions2", quote="\"", comment.char="")
names(conditions1) = c("fractal_left", "fractal_right") # name columns
conditions1 = as.data.frame(conditions1) # transform to data frame

# create cols with prob and magnitudes
conditions1 = conditions1 %>% mutate(left_prob = str_sub(fractal_left, 3, 4), right_prob = str_sub(fractal_right, 3, 4),
                       left_mag = str_sub(fractal_left, 5, 6), right_mag = str_sub(fractal_right, 5, 6)) %>%
                mutate(prob1 = ifelse(left_prob=="p1", .1,
                                                ifelse(left_prob=="p2", .5, .9)), 
                       prob2 = ifelse(right_prob=="p1", .1,
                                                 ifelse(right_prob=="p2", .5, .9)),
                       mag1 = ifelse(left_mag=="m1", 1,
                                               ifelse(left_mag=="m2", 2, 3)),
                       mag2 = ifelse(right_mag=="m1", 1,
                                                ifelse(right_mag=="m2", 2, 3)),
                       stim1 = paste("stim/juice/", fractal_left,sep=""),
                       stim2 = paste("stim/juice/", fractal_right, sep=""),
                       reward = "juice", resp_type="gaze")

# create csv file with conditions
write.csv(conditions1, "~/Dropbox/Projects/Caltech/Humans/Mapping Prefrontal Cortex/two_choice/conditions_juice.csv")
