# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models, migrations


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class City(models.Model):
    state = models.ForeignKey('StateTable', models.DO_NOTHING)
    level2gid = models.CharField(max_length=15, blank=True, null=True)
    city_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'city'
        unique_together = (('state', 'level2gid', 'city_name'),)


class ClassTable(models.Model):
    class_key = models.IntegerField(blank=True, null=True)
    class_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'class_table'
        unique_together = (('class_key', 'class_name'),)


class Continent(models.Model):
    continent_name = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'continent'

    def __str__(self):
        return self.continent_name


class Country(models.Model):
    continent = models.ForeignKey(Continent, models.DO_NOTHING)
    level0gid = models.CharField(max_length=5, blank=True, null=True)
    country_name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'country'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FamilyTable(models.Model):
    family_key = models.IntegerField(blank=True, null=True)
    family_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'family_table'
        unique_together = (('family_key', 'family_name'),)


class Genus(models.Model):
    genus_key = models.IntegerField(blank=True, null=True)
    genus_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'genus'
        unique_together = (('genus_key', 'genus_name'),)


class Issue(models.Model):
    issue_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'issue'


class Kingdom(models.Model):
    kingdom_key = models.IntegerField(blank=True, null=True)
    kingdom_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'kingdom'
        unique_together = (('kingdom_key', 'kingdom_name'),)


class Localization(models.Model):
    city = models.ForeignKey(City, models.DO_NOTHING)
    localization_name = models.CharField(max_length=255)
    decimal_latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    decimal_longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localization'
        unique_together = (('city', 'localization_name', 'decimal_latitude', 'decimal_longitude'),)


class Log(models.Model):
    event_type = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    event_description = models.TextField()
    dataset_key = models.TextField()
    protocol = models.CharField(max_length=20)
    event_date = models.DateTimeField()
    last_parsed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class MemberOf(models.Model):
    researcher = models.ForeignKey('Researcher', models.DO_NOTHING)
    group = models.ForeignKey('ResearchGroup', models.DO_NOTHING)
    researcher_role = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'member_of'


class OrderTable(models.Model):
    order_key = models.IntegerField(blank=True, null=True)
    order_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'order_table'
        unique_together = (('order_key', 'order_name'),)


class Phylum(models.Model):
    phylum_key = models.IntegerField(blank=True, null=True)
    phylum_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'phylum'
        unique_together = (('phylum_key', 'phylum_name'),)


class Research(models.Model):
    gbifid = models.BigIntegerField(primary_key=True)
    research_groupid = models.ForeignKey('ResearchGroup', models.DO_NOTHING, db_column='research_groupid', blank=True, null=True)
    license_rights = models.ForeignKey('Rights', models.DO_NOTHING, db_column='license_rights')
    collection_code = models.CharField(max_length=30)
    ocurrenceid = models.CharField(unique=True, max_length=30)
    basis_of_record = models.CharField(max_length=30, blank=True, null=True)
    ocurrence_status = models.CharField(max_length=15, blank=True, null=True)
    preparations = models.CharField(max_length=15, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    event_remarks = models.TextField(blank=True, null=True)
    publishing_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='publishing_country')
    localization = models.ForeignKey(Localization, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'research'


class ResearchGroup(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    institution = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'research_group'


class ResearchIssue(models.Model):
    gbifid = models.OneToOneField(Research, models.DO_NOTHING, db_column='gbifid', primary_key=True)  # The composite primary key (gbifid, issue_id) found, that is not supported. The first column is selected.
    issue = models.ForeignKey(Issue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'research_issue'
        unique_together = (('gbifid', 'issue'),)


class ResearchedBy(models.Model):
    gbifid = models.OneToOneField(Research, models.DO_NOTHING, db_column='gbifid', primary_key=True)  # The composite primary key (gbifid, researcher_id) found, that is not supported. The first column is selected.
    researcher = models.ForeignKey('Researcher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'researched_by'
        unique_together = (('gbifid', 'researcher'),)


class Researcher(models.Model):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'researcher'


class Rights(models.Model):
    license = models.CharField(max_length=15)
    access_rights = models.CharField(max_length=100)
    rights_holder = models.CharField(max_length=50)
    institution_code = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'rights'


class Species(models.Model):
    species_key = models.IntegerField(blank=True, null=True)
    species_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'species'
        unique_together = (('species_key', 'species_name'),)


class StateTable(models.Model):
    country = models.ForeignKey(Country, models.DO_NOTHING)
    level1gid = models.CharField(max_length=15, blank=True, null=True)
    state_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'state_table'


class Taxon(models.Model):
    taxon_hierarchy = models.ForeignKey('TaxonHierarchy', models.DO_NOTHING)
    taxon_key = models.BigIntegerField(blank=True, null=True)
    scientific_name = models.CharField(max_length=80)
    generic_name = models.CharField(max_length=40, blank=True, null=True)
    specific_epithet = models.CharField(max_length=20, blank=True, null=True)
    infraespecific_epithet = models.CharField(max_length=20, blank=True, null=True)
    taxon_rank = models.CharField(max_length=12)
    taxonomic_status = models.CharField(max_length=12, blank=True, null=True)
    iucn_redlist_category = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxon'
        unique_together = (('taxon_hierarchy', 'taxon_key', 'scientific_name', 'generic_name', 'specific_epithet', 'infraespecific_epithet', 'taxon_rank', 'taxonomic_status', 'iucn_redlist_category'),)


class TaxonHierarchy(models.Model):
    kingdom = models.ForeignKey(Kingdom, models.DO_NOTHING)
    phylum = models.ForeignKey(Phylum, models.DO_NOTHING)
    class_table = models.ForeignKey(ClassTable, models.DO_NOTHING)
    order_table = models.ForeignKey(OrderTable, models.DO_NOTHING)
    family_table = models.ForeignKey(FamilyTable, models.DO_NOTHING)
    genus = models.ForeignKey(Genus, models.DO_NOTHING)
    species = models.ForeignKey(Species, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taxon_hierarchy'
        unique_together = (('kingdom', 'phylum', 'class_table', 'order_table', 'family_table', 'genus', 'species'),)


class TaxonSample(models.Model):
    gbifid = models.ForeignKey(Research, models.DO_NOTHING, db_column='gbifid')
    taxon = models.ForeignKey(Taxon, models.DO_NOTHING)
    verbatim_scientific_name = models.CharField(max_length=60, blank=True, null=True)
    repatriated = models.BooleanField()
    type_status = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxon_sample'

