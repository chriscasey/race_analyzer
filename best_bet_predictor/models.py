# from django.db import models
# 
# # Create your models here.
# 
# ####################################
# #list of all available track types
# ####################################
# TRACK_TYPES = (
#     ('1','1 furlong, dirt'),
#     ('2','2 furlongs, dirt'),
#     ('3','3 furlongs, dirt'),
#     ('4','1 furlong, grass'),
#     ('5','2 furlongs, grass'),
#     ('6','3 furlongs, grass')
# )
# 
# ####################################
# #information specific to each horse
# ####################################
# class Race(models.Model):
#   track_type = models.SmallIntegerField(choices=TRACK_TYPES)
#   num_horses = models.IntegerField()
#   best_bet = models.ForeignKey('horse')
#   race_result = [(models.ForeignKey('horse'), position)]
#   
# class MorningLineOdds(models.Model):
#     race = models.ForeignKey('race')
#     horse = models.ForeignKey('horse')
#     odds = models.FloatField()
#   
#   
# ####################################
# #information specific to each horse
# ####################################
# class Horse(models.Model):
#     trainer = models.ForeignKey('trainer')
#     owner =  models.ForeignKey('owner')
#     jockey =  models.ForeignKey('jockey')
#     known_races = models.FloatField()
#       
#   
# 
# ####################################
# #information specific to each jockey
# ####################################
# class Jockey(models.Model):
#     first_name = models.CharField(max_length=75, null=True, blank=True)
#     last_name = models.CharField(max_length=75, null=True, blank=True)
#     known_races = models.FloatField()
#     
# 
# ####################################
# #information specific to each owner
# ####################################
# class Owner(models.Model):
#     first_name = models.CharField(max_length=75, null=True, blank=True)
#     last_name = models.CharField(max_length=75, null=True, blank=True)
#     known_races = models.FloatField()    
# 
# 
# ####################################
# #information specific to each trainer
# ####################################
# class Trainer(models.Model):
#     first_name = models.CharField(max_length=75, null=True, blank=True)
#     last_name = models.CharField(max_length=75, null=True, blank=True)
#     known_races = models.FloatField()
#     
#     
#     
#     