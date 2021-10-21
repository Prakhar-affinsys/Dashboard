from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
	name = models.CharField(max_length=100,blank=True, null=True)
	income = models.DecimalField(max_digits=10, decimal_places=2)
	age = models.IntegerField(blank=True, null=True)
	hometown = models.CharField(max_length=50, blank=True, null=True)
	zipcode = models.CharField(max_length=6, blank=True, null=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	date = models.DateTimeField(blank=True, null=True)

class Customerprofile(models.Model):
    customer = models.CharField(primary_key=True, max_length=150)
    fname = models.CharField(max_length=20, blank=True, null=True)
    lname = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    married = models.CharField(max_length=1, blank=True, null=True)
    metro = models.CharField(max_length=1, blank=True, null=True)
    employed = models.CharField(max_length=1, blank=True, null=True)
    income = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hometown = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    locale = models.CharField(max_length=20, blank=True, null=True)
    timezone = models.CharField(max_length=60, blank=True, null=True)
    last_interacted_time = models.DateTimeField(blank=True, null=True)
    needhelp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customerprofile'

class Userqueries(models.Model):
    customer = models.ForeignKey('Customerprofile', models.DO_NOTHING, db_column='customer', blank=True, null=True)
    user_session = models.ForeignKey('Usersessions', models.DO_NOTHING, blank=True, null=True)
    message = models.CharField(max_length=300, blank=True, null=True)
    channel = models.CharField(max_length=20, blank=True, null=True)
    context = models.CharField(max_length=50, blank=True, null=True)
    handled = models.CharField(max_length=1, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    intent1 = models.CharField(max_length=500, blank=True, null=True)
    score1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    intent2 = models.CharField(max_length=50, blank=True, null=True)
    score2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    intent3 = models.CharField(max_length=50, blank=True, null=True)
    score3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    model_type = models.CharField(max_length=20, blank=True, null=True)
    model_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    model_name = models.CharField(max_length=25, blank=True, null=True)
    button = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userqueries'
 
class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('LocalusersLocaluser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AnalyticsSocialevent(models.Model):
    event = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    agent = models.ForeignKey('LocalusersLocaluser', models.DO_NOTHING, blank=True, null=True)
    social = models.ForeignKey('LocalusersTempsocialuser', models.DO_NOTHING, blank=True, null=True)
    session = models.CharField(max_length=36)
    channel = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analytics_socialevent'



class ApiChatbankinguser(models.Model):
    mobile_no = models.CharField(unique=True, max_length=12)
    status = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'api_chatbankinguser'


class AuditlogLogentry(models.Model):
    object_pk = models.CharField(max_length=255)
    object_id = models.BigIntegerField(blank=True, null=True)
    object_repr = models.TextField()
    action = models.SmallIntegerField()
    changes = models.TextField()
    timestamp = models.DateTimeField()
    actor = models.ForeignKey('LocalusersLocaluser', models.DO_NOTHING, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    remote_addr = models.GenericIPAddressField(blank=True, null=True)
    additional_data = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditlog_logentry'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField('LocalusersLocaluser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class AxesAccessattempt(models.Model):
    user_agent = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=1025)
    path_info = models.CharField(max_length=255)
    attempt_time = models.DateTimeField()
    get_data = models.TextField()
    post_data = models.TextField()
    failures_since_start = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'axes_accessattempt'


class AxesAccesslog(models.Model):
    user_agent = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=1025)
    path_info = models.CharField(max_length=255)
    attempt_time = models.DateTimeField()
    logout_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axes_accesslog'


class CampaignBroadcast(models.Model):
    name = models.CharField(max_length=150)
    frequency = models.IntegerField()
    recurrence_pattern = models.CharField(max_length=2)
    start_timestamp = models.DateTimeField()
    activation_status = models.CharField(max_length=10)
    campaign_variant = models.ForeignKey('CampaignCampaignvariant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_broadcast'


class CampaignBroadcastbatch(models.Model):
    message_id = models.CharField(max_length=800, blank=True, null=True)
    sent = models.IntegerField()
    broadcast_history = models.ForeignKey('CampaignBroadcasthistory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_broadcastbatch'


class CampaignBroadcastcandidates(models.Model):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    locale = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    user_timezone = models.CharField(max_length=50, blank=True, null=True)
    uid = models.CharField(max_length=500)
    last_activity = models.DateTimeField()
    profile_pic = models.CharField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    primary_device_os = models.CharField(max_length=100, blank=True, null=True)
    device_type = models.CharField(max_length=100, blank=True, null=True)
    display_name = models.CharField(max_length=300, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    last_refresh_time = models.DateTimeField()
    social = models.ForeignKey('CampaignBroadcastchanneldetail', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_broadcastcandidates'


class CampaignBroadcastchanneldetail(models.Model):
    channel_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'campaign_broadcastchanneldetail'


class CampaignBroadcastchannels(models.Model):
    broadcast = models.ForeignKey(CampaignBroadcast, models.DO_NOTHING)
    channel = models.ForeignKey(CampaignBroadcastchanneldetail, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_broadcastchannels'


class CampaignBroadcastdetail(models.Model):
    message_title = models.CharField(max_length=50, blank=True, null=True)
    message_subtitle = models.CharField(max_length=250, blank=True, null=True)
    message_image = models.CharField(max_length=1000, blank=True, null=True)
    message_image_id = models.CharField(max_length=500, blank=True, null=True)
    decision_tree = models.JSONField(blank=True, null=True)
    buttons = models.JSONField(blank=True, null=True)
    quick_reply = models.CharField(max_length=100, blank=True, null=True)
    broadcast_channel = models.OneToOneField(CampaignBroadcastchannels, models.DO_NOTHING)
    content_type = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=100)
    salutation = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_broadcastdetail'


class CampaignBroadcasterrorlog(models.Model):
    message = models.TextField(blank=True, null=True)
    area = models.CharField(max_length=20)
    channel = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'campaign_broadcasterrorlog'


class CampaignBroadcasthistory(models.Model):
    sent = models.IntegerField()
    delivered = models.IntegerField()
    read = models.IntegerField()
    task_id = models.CharField(max_length=300, blank=True, null=True)
    is_started = models.BooleanField()
    status = models.CharField(max_length=2)
    scheduled_at = models.DateTimeField()
    broadcast_detail = models.ForeignKey(CampaignBroadcastdetail, models.DO_NOTHING)
    social = models.ForeignKey(CampaignBroadcastchanneldetail, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_broadcasthistory'


class CampaignBroadcastmessagehistory(models.Model):
    delivered = models.BooleanField()
    read = models.BooleanField()
    broadcast_batch = models.ForeignKey(CampaignBroadcastbatch, models.DO_NOTHING)
    candidate = models.ForeignKey(CampaignBroadcastcandidates, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_broadcastmessagehistory'


class CampaignBroadcastreport(models.Model):
    message = models.CharField(max_length=300)
    timestamp = models.DateTimeField()
    broadcast_candidate = models.ForeignKey(CampaignBroadcastcandidates, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_broadcastreport'


class Userstage(models.Model):
    customer = models.ForeignKey('Customerprofile', models.DO_NOTHING, db_column='customer', blank=True, null=True)
    user_session = models.ForeignKey('Usersessions', models.DO_NOTHING, blank=True, null=True)
    channel = models.CharField(max_length=100, blank=True, null=True)
    transaction_intent = models.CharField(max_length=200, blank=True, null=True)
    transaction_id = models.CharField(max_length=150, blank=True, null=True)
    stage = models.CharField(max_length=50, blank=True, null=True)
    stage_result = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    rmn = models.CharField(max_length=20, blank=True, null=True)
    customer_id = models.CharField(max_length=25, blank=True, null=True)
    national_id = models.CharField(max_length=20, blank=True, null=True)
    lastfourdigits = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userstage'

class Usersessions(models.Model):
    customer = models.ForeignKey('Customerprofile', models.DO_NOTHING, db_column='customer', blank=True, null=True)
    user_session_id = models.CharField(primary_key=True, max_length=100)
    timestamp = models.DateTimeField(blank=True, null=True)
    channel = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usersessions'



