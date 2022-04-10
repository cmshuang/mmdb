# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ligand(models.Model):
    zinc_id = models.CharField(max_length=16)
    inchi = models.CharField(max_length=300, blank=True, null=True)
    inchi_key = models.CharField(max_length=27, blank=True, null=True)
    cansmi = models.CharField(max_length=200)
    nb_atoms = models.PositiveIntegerField()
    sdf_file = models.CharField(max_length=100)
    pose_count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ligand'


class Pose(models.Model):
    binding_affinity = models.FloatField()
    ligand = models.ForeignKey(Ligand, models.DO_NOTHING)
    protein = models.ForeignKey('Protein', models.DO_NOTHING)
    coor_file = models.CharField(max_length=100)
    sdf_file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pose'


class Protein(models.Model):
    pdb_id = models.CharField(max_length=4)
    protein_name = models.CharField(max_length=50)
    virus_name = models.CharField(max_length=50, blank=True, null=True)
    coor_file = models.CharField(max_length=100, blank=True, null=True)
    pdb_file = models.CharField(max_length=100)
    comment = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protein'
