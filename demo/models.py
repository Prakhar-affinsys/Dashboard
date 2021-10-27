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
'''
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


class Apilogcn(models.Model):
    api = models.CharField(max_length=500, blank=True, null=True)
    stage = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=500, blank=True, null=True)
    channel = models.CharField(max_length=20, blank=True, null=True)
    bb_txn_id = models.CharField(max_length=500, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    exception = models.CharField(max_length=500, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apilogcn'


class AppChannelstate(models.Model):
    token = models.CharField(max_length=500, blank=True, null=True)
    expiry_date = models.CharField(max_length=500, blank=True, null=True)
    channel_id = models.CharField(max_length=500, blank=True, null=True)
    channel_code = models.CharField(max_length=500, blank=True, null=True)
    activation_status = models.CharField(max_length=500, blank=True, null=True)
    create_dt = models.DateTimeField()
    update_dt = models.DateTimeField()
    login_master = models.ForeignKey('PinLoginmaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_channelstate'
        unique_together = (('login_master', 'channel_id'),)


class ApprovalStatechangerequest(models.Model):
    action = models.CharField(max_length=100)
    requested_at = models.DateTimeField()
    request_payload = models.TextField(blank=True, null=True)
    operation_type = models.CharField(max_length=5)
    approval_state = models.CharField(max_length=30)
    object_pk = models.CharField(max_length=255, blank=True, null=True)
    object_repr = models.CharField(max_length=300, blank=True, null=True)
    change_state_user = models.ForeignKey('LocalusersLocaluser', models.DO_NOTHING, blank=True, null=True)
    request_user = models.ForeignKey('LocalusersLocaluser', models.DO_NOTHING, blank=True, null=True)
    action_key = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'approval_statechangerequest'
        unique_together = (('request_user', 'action', 'object_repr'),)


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
    additional_data = models.TextField(blank=True, null=True)

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


class BanksBeneficiarybank(models.Model):
    bank_name = models.CharField(max_length=100)
    bank_code = models.CharField(max_length=10)
    branch_code = models.CharField(max_length=10)
    bic = models.CharField(max_length=15)
    record_status = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'banks_beneficiarybank'
        unique_together = (('bank_name', 'bic'),)


class BotResponsecn(models.Model):
    channel = models.CharField(max_length=30, blank=True, null=True)
    message = models.CharField(max_length=250, blank=True, null=True)
    bot_response = models.TextField()
    timestamp = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey('Customerprofilecn', models.DO_NOTHING, db_column='customer', blank=True, null=True)
    user_session = models.ForeignKey('Usersessionscn', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bot_responsecn'


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
    decision_tree = models.TextField(blank=True, null=True)
    buttons = models.TextField(blank=True, null=True)
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


class CampaignBroadcasttimeline(models.Model):
    timestamp = models.DateTimeField()
    broadcast = models.ForeignKey(CampaignBroadcast, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_broadcasttimeline'


class CampaignCampaign(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    activation_status = models.CharField(max_length=100)
    creation = models.DateTimeField()
    last_modified = models.DateTimeField()
    campaign_type = models.ForeignKey('CampaignCampaigntype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_campaign'


class CampaignCampaignproductdetail(models.Model):
    campaign_variant = models.ForeignKey('CampaignCampaignvariant', models.DO_NOTHING)
    product = models.ForeignKey('CampaignProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_campaignproductdetail'


class CampaignCampaigntype(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'campaign_campaigntype'


class CampaignCampaignvariant(models.Model):
    decision_tree = models.TextField()
    campaign = models.ForeignKey(CampaignCampaign, models.DO_NOTHING)
    offer = models.ForeignKey('CampaignOfferdetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_campaignvariant'


class CampaignCategory(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'campaign_category'


class CampaignCreative(models.Model):
    language = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    offer_detail = models.ForeignKey('CampaignOfferdetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_creative'


class CampaignMedia(models.Model):
    path = models.CharField(max_length=500)
    url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_media'


class CampaignOfferdetail(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    activation_status = models.CharField(max_length=500)
    validity_start = models.DateTimeField()
    validity_end = models.DateTimeField()
    last_modified = models.DateTimeField()
    offer_type = models.ForeignKey('CampaignOffertype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_offerdetail'


class CampaignOffertype(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'campaign_offertype'


class CampaignProduct(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    validity_start = models.DateTimeField()
    validity_end = models.DateTimeField()
    price = models.CharField(max_length=200)
    processing_fee = models.CharField(max_length=200)
    service_tax = models.CharField(max_length=200)
    category = models.ForeignKey(CampaignCategory, models.DO_NOTHING)
    scope = models.ForeignKey('CampaignScope', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_product'


class CampaignScope(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'campaign_scope'


class ChatMessagesocialagent(models.Model):
    socialplatformmixin_ptr = models.OneToOneField('SocialconversationSocialplatformmixin', models.DO_NOTHING, primary_key=True)
    sender = models.CharField(max_length=13)
    body = models.TextField()
    chat_user = models.ForeignKey('LocalusersLocaluser', models.DO_NOTHING, blank=True, null=True)
    social_user = models.ForeignKey('LocalusersTempsocialuser', models.DO_NOTHING, blank=True, null=True)
    sentiment = models.CharField(max_length=100)
    intent = models.CharField(max_length=200, blank=True, null=True)
    message_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'chat_messagesocialagent'


class ConfigappConfiguration(models.Model):
    otp_expiry = models.IntegerField()
    otp_digits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'configapp_configuration'

'''
class Customerprofilecn(models.Model):
    customer = models.CharField(primary_key=True, max_length=150)
    fname = models.CharField(max_length=20, blank=True, null=True)
    lname = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    married = models.CharField(max_length=1, blank=True, null=True)
    metro = models.CharField(max_length=1, blank=True, null=True)
    employed = models.CharField(max_length=1, blank=True, null=True)
    income = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
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
        db_table = 'customerprofilecn'

'''
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('LocalusersLocaluser', models.DO_NOTHING)

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


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class EchelonDeregistereduserscn(models.Model):
    chatbanking_id = models.CharField(max_length=500, blank=True, null=True)
    kyc_level = models.CharField(max_length=500, blank=True, null=True)
    cust_name = models.CharField(max_length=500, blank=True, null=True)
    cif = models.CharField(max_length=500, blank=True, null=True)
    rmn = models.CharField(max_length=500, blank=True, null=True)
    channel_id = models.CharField(max_length=500, blank=True, null=True)
    channel_code = models.CharField(max_length=500, blank=True, null=True)
    country_code = models.CharField(max_length=500, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    dereg_source = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'echelon_deregistereduserscn'


class EchelonQueuetxnscn(models.Model):
    rra_reference_id = models.CharField(max_length=500, blank=True, null=True)
    finacle_txn_id = models.CharField(max_length=500, blank=True, null=True)
    bb_txn_id = models.CharField(max_length=500, blank=True, null=True)
    api_payload = models.TextField(blank=True, null=True)
    account_no = models.CharField(max_length=500, blank=True, null=True)
    amount = models.CharField(max_length=500, blank=True, null=True)
    req_status = models.CharField(max_length=500, blank=True, null=True)
    submit_count = models.IntegerField(blank=True, null=True)
    first_payment_timestamp = models.DateTimeField(blank=True, null=True)
    last_submit_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'echelon_queuetxnscn'


class EchelonTrailcn(models.Model):
    channel_id = models.CharField(max_length=1000, blank=True, null=True)
    channel_code = models.CharField(max_length=1000, blank=True, null=True)
    rmn = models.CharField(max_length=1000, blank=True, null=True)
    cust_name = models.CharField(max_length=1000, blank=True, null=True)
    event_name = models.CharField(max_length=1000, blank=True, null=True)
    event_state = models.CharField(max_length=1000, blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'echelon_trailcn'


class LocalusersAgent(models.Model):
    max_concurrent = models.IntegerField()
    current_chats = models.IntegerField()
    user = models.OneToOneField('LocalusersLocaluser', models.DO_NOTHING)
    is_online = models.BooleanField()
    is_ready = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'localusers_agent'


class LocalusersAgentskill(models.Model):
    agent = models.ForeignKey(LocalusersAgent, models.DO_NOTHING)
    skill = models.ForeignKey('LocalusersSkill', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'localusers_agentskill'


class LocalusersLocaluser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    disabled = models.BooleanField()
    force_password_change = models.BooleanField()
    password_change_date = models.DateTimeField()
    session_key = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localusers_localuser'


class LocalusersLocaluserGroups(models.Model):
    localuser = models.ForeignKey(LocalusersLocaluser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'localusers_localuser_groups'
        unique_together = (('localuser', 'group'),)


class LocalusersLocaluserUserPermissions(models.Model):
    localuser = models.ForeignKey(LocalusersLocaluser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'localusers_localuser_user_permissions'
        unique_together = (('localuser', 'permission'),)


class LocalusersPasswordhistory(models.Model):
    created = models.DateTimeField()
    password = models.CharField(max_length=128)
    user = models.ForeignKey(LocalusersLocaluser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'localusers_passwordhistory'


class LocalusersRole(models.Model):
    rname = models.CharField(max_length=501)
    pages = models.CharField(max_length=501)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localusers_role'


class LocalusersRolerestriction(models.Model):
    group = models.OneToOneField(AuthGroup, models.DO_NOTHING, primary_key=True)
    max_users = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localusers_rolerestriction'


class LocalusersSkill(models.Model):
    skill_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'localusers_skill'


class LocalusersSocial(models.Model):
    channel_name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'localusers_social'


class LocalusersTempsocialuser(models.Model):
    username = models.CharField(max_length=200)
    channel_id = models.CharField(max_length=200)
    agent = models.ForeignKey(LocalusersLocaluser, models.DO_NOTHING, blank=True, null=True)
    social = models.ForeignKey(LocalusersSocial, models.DO_NOTHING)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone_number = models.CharFiesudold(max_length=300, blank=True, null=True)
    skill = models.CharField(max_length=200, blank=True, null=True)
    last_activity = models.DateTimeField()
    is_circulating = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'localusers_tempsocialuser'


class Oauth2ProviderAccesstoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    scope = models.TextField()
    application = models.ForeignKey('Oauth2ProviderApplication', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(LocalusersLocaluser, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    source_refresh_token = models.OneToOneField('Oauth2ProviderRefreshtoken', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_accesstoken'


class Oauth2ProviderApplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_id = models.CharField(unique=True, max_length=100)
    redirect_uris = models.TextField()
    client_type = models.CharField(max_length=32)
    authorization_grant_type = models.CharField(max_length=32)
    client_secret = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(LocalusersLocaluser, models.DO_NOTHING, blank=True, null=True)
    skip_authorization = models.BooleanField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_application'


class Oauth2ProviderGrant(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    redirect_uri = models.CharField(max_length=255)
    scope = models.TextField()
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
    user = models.ForeignKey(LocalusersLocaluser, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_grant'


class Oauth2ProviderRefreshtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=255)
    access_token = models.OneToOneField(Oauth2ProviderAccesstoken, models.DO_NOTHING, blank=True, null=True)
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
    user = models.ForeignKey(LocalusersLocaluser, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    revoked = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_refreshtoken'
        unique_together = (('token', 'revoked'),)


class PinLoginmaster(models.Model):
    chatbanking_id = models.CharField(max_length=20)
    rmn = models.CharField(unique=True, max_length=128)
    pin = models.CharField(max_length=255)
    kyc_level = models.SmallIntegerField()
    create_dt = models.DateTimeField()
    update_dt = models.DateTimeField()
    is_registered = models.CharField(max_length=1)
    is_blocked = models.CharField(max_length=1)
    block_reason = models.CharField(max_length=200)
    id_type = models.CharField(max_length=1)
    id_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pin_loginmaster'
        unique_together = (('id', 'rmn', 'chatbanking_id'),)


class RestFrameworkTrackingApirequestlog(models.Model):
    requested_at = models.DateTimeField()
    response_ms = models.IntegerField()
    path = models.CharField(max_length=200)
    remote_addr = models.GenericIPAddressField()
    host = models.CharField(max_length=200)
    method = models.CharField(max_length=10)
    query_params = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(LocalusersLocaluser, models.DO_NOTHING, blank=True, null=True)
    view = models.CharField(max_length=200, blank=True, null=True)
    view_method = models.CharField(max_length=200, blank=True, null=True)
    errors = models.TextField(blank=True, null=True)
    username_persistent = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rest_framework_tracking_apirequestlog'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(LocalusersLocaluser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class SocialconversationBroadcast(models.Model):
    content_type = models.CharField(max_length=50, blank=True, null=True)
    created_timestamp = models.DateTimeField()
    message_title = models.CharField(max_length=50, blank=True, null=True)
    message_subtitle = models.CharField(max_length=250, blank=True, null=True)
    message_image = models.CharField(max_length=1000, blank=True, null=True)
    filters = models.TextField(blank=True, null=True)
    buttons = models.TextField(blank=True, null=True)
    scheduled_at = models.DateTimeField(blank=True, null=True)
    sent = models.IntegerField()
    delivered = models.IntegerField()
    read = models.IntegerField()
    quick_reply = models.CharField(max_length=100, blank=True, null=True)
    task_id = models.CharField(max_length=300, blank=True, null=True)
    is_started = models.BooleanField()
    social = models.ForeignKey(LocalusersSocial, models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=2)
    message_image_id = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socialconversation_broadcast'


class SocialconversationBroadcastbatch(models.Model):
    message_id = models.CharField(max_length=800, blank=True, null=True)
    sent = models.IntegerField()
    broadcast = models.ForeignKey(SocialconversationBroadcast, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialconversation_broadcastbatch'


class SocialconversationBroadcastcandidates(models.Model):
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
    social = models.ForeignKey(LocalusersSocial, models.DO_NOTHING, blank=True, null=True)
    last_refresh_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'socialconversation_broadcastcandidates'


class SocialconversationBroadcasterrorlog(models.Model):
    message = models.TextField(blank=True, null=True)
    area = models.CharField(max_length=20)
    channel = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'socialconversation_broadcasterrorlog'


class SocialconversationBroadcastmessagehistory(models.Model):
    delivered = models.BooleanField()
    read = models.BooleanField()
    broadcast_batch = models.ForeignKey(SocialconversationBroadcastbatch, models.DO_NOTHING)
    candidate = models.ForeignKey(SocialconversationBroadcastcandidates, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialconversation_broadcastmessagehistory'


class SocialconversationBroadcastreport(models.Model):
    message = models.CharField(max_length=300)
    timestamp = models.DateTimeField()
    broadcast_candidate = models.ForeignKey(SocialconversationBroadcastcandidates, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socialconversation_broadcastreport'


class SocialconversationDirectMessage(models.Model):
    socialplatformmixin_ptr = models.OneToOneField('SocialconversationSocialplatformmixin', models.DO_NOTHING, primary_key=True)
    sentiment = models.CharField(max_length=100)
    channel_name = models.CharField(max_length=50)
    sender = models.CharField(max_length=255)
    receiver = models.ForeignKey(LocalusersTempsocialuser, models.DO_NOTHING)
    user = models.ForeignKey(LocalusersTempsocialuser, models.DO_NOTHING)
    body = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socialconversation_direct_message'


class SocialconversationFacebookcomment(models.Model):
    comment_id = models.CharField(primary_key=True, max_length=500)
    text = models.TextField()
    sentiment = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'socialconversation_facebookcomment'


class SocialconversationFacebookcommentthread(models.Model):
    socialplatformmixin_ptr = models.OneToOneField('SocialconversationSocialplatformmixin', models.DO_NOTHING, primary_key=True)
    channel_name = models.CharField(max_length=50)
    sender = models.CharField(max_length=255)
    comment = models.ForeignKey(SocialconversationFacebookcomment, models.DO_NOTHING, blank=True, null=True)
    in_reply_user = models.ForeignKey(LocalusersTempsocialuser, models.DO_NOTHING, blank=True, null=True)
    parent_comment = models.ForeignKey(SocialconversationFacebookcomment, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(LocalusersTempsocialuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialconversation_facebookcommentthread'


class SocialconversationFalloutsocialuser(models.Model):
    timestamp = models.DateTimeField()
    social_user = models.ForeignKey(LocalusersTempsocialuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialconversation_falloutsocialuser'


class SocialconversationFavEvents(models.Model):
    id_post = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'socialconversation_fav_events'


class SocialconversationMedia(models.Model):
    path = models.CharField(max_length=500)
    url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socialconversation_media'


class SocialconversationSentiment(models.Model):
    sentiment_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'socialconversation_sentiment'


class SocialconversationSentimentrelation(models.Model):
    sentiment = models.ForeignKey(SocialconversationSentiment, models.DO_NOTHING)
    direct_message = models.ForeignKey(SocialconversationDirectMessage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialconversation_sentimentrelation'


class SocialconversationSocialplatformmixin(models.Model):
    type = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'socialconversation_socialplatformmixin'


class SocialconversationSocialusernotes(models.Model):
    socialplatformmixin_ptr = models.OneToOneField(SocialconversationSocialplatformmixin, models.DO_NOTHING, primary_key=True)
    note = models.CharField(max_length=150)
    social_user = models.ForeignKey(LocalusersTempsocialuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialconversation_socialusernotes'


class SocialconversationTag(models.Model):
    tag_name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'socialconversation_tag'


class SocialconversationTagsocialmessage(models.Model):
    social_message = models.ForeignKey(SocialconversationSocialplatformmixin, models.DO_NOTHING)
    tag = models.ForeignKey(SocialconversationTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialconversation_tagsocialmessage'


class SocialconversationTweet(models.Model):
    status_id = models.CharField(primary_key=True, max_length=500)
    text = models.CharField(max_length=100, blank=True, null=True)
    sentiment = models.CharField(max_length=100)
    like = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'socialconversation_tweet'


class SocialconversationTweetCreateEvent(models.Model):
    status_id = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField()
    type = models.CharField(max_length=100)
    in_reply_to_status = models.CharField(max_length=100, blank=True, null=True)
    in_reply_to_userid = models.CharField(max_length=100, blank=True, null=True)
    text = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(LocalusersTempsocialuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialconversation_tweet_create_event'


class SocialconversationTwitterpost(models.Model):
    text = models.TextField()
    status_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'socialconversation_twitterpost'


class SocialconversationTwitterpostcomment(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField()
    sender = models.CharField(max_length=255)
    post = models.ForeignKey(SocialconversationTwitterpost, models.DO_NOTHING)
    user = models.ForeignKey(LocalusersTempsocialuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialconversation_twitterpostcomment'


class SocialconversationTwittertweet(models.Model):
    socialplatformmixin_ptr = models.OneToOneField(SocialconversationSocialplatformmixin, models.DO_NOTHING, primary_key=True)
    channel_name = models.CharField(max_length=50)
    sender = models.CharField(max_length=255)
    in_reply_user = models.ForeignKey(LocalusersTempsocialuser, models.DO_NOTHING, blank=True, null=True)
    parent_tweet = models.ForeignKey(SocialconversationTweet, models.DO_NOTHING, blank=True, null=True)
    tweet = models.ForeignKey(SocialconversationTweet, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(LocalusersTempsocialuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialconversation_twittertweet'
'''

class Userqueriescn(models.Model):
    message = models.CharField(max_length=250, blank=True, null=True)
    channel = models.CharField(max_length=20, blank=True, null=True)
    context = models.CharField(max_length=50, blank=True, null=True)
    handled = models.CharField(max_length=1, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    intent1 = models.CharField(max_length=50, blank=True, null=True)
    score1 = models.DecimalField(max_digits=30, decimal_places=30, blank=True, null=True)
    intent2 = models.CharField(max_length=50, blank=True, null=True)
    score2 = models.DecimalField(max_digits=30, decimal_places=30, blank=True, null=True)
    intent3 = models.CharField(max_length=50, blank=True, null=True)
    score3 = models.DecimalField(max_digits=30, decimal_places=30, blank=True, null=True)
    derived_intent = models.CharField(max_length=150, blank=True, null=True)
    category_name = models.CharField(max_length=50, blank=True, null=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    attribute_name = models.CharField(max_length=50, blank=True, null=True)
    customer = models.ForeignKey(Customerprofilecn, models.DO_NOTHING, db_column='customer', blank=True, null=True)
    user_session = models.ForeignKey('Usersessionscn', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userqueriescn'


class Usersessionscn(models.Model):
    user_session_id = models.CharField(primary_key=True, max_length=100)
    timestamp = models.DateTimeField(blank=True, null=True)
    channel = models.CharField(max_length=100, blank=True, null=True)
    customer = models.ForeignKey(Customerprofilecn, models.DO_NOTHING, db_column='customer', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usersessionscn'


class Userstagecn(models.Model):
    channel = models.CharField(max_length=100, blank=True, null=True)
    transaction_intent = models.CharField(max_length=200, blank=True, null=True)
    transaction_id = models.CharField(max_length=150, blank=True, null=True)
    stage = models.CharField(max_length=100, blank=True, null=True)
    stage_result = models.CharField(max_length=100, blank=True, null=True)
    stage_response = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    rmn = models.CharField(max_length=20, blank=True, null=True)
    transaction_code = models.CharField(max_length=10, blank=True, null=True)
    customer = models.ForeignKey(Customerprofilecn, models.DO_NOTHING, db_column='customer', blank=True, null=True)
    user_session = models.ForeignKey(Usersessionscn, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userstagecn'

'''
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
        db_table = 'userqueriescn'
 
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



'''