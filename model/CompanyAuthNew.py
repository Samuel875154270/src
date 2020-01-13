from .BaseModel import *


class CompanyAuthNew(BaseModel):
    class Meta:
        db_table = "api_company_auth_new"

    # 字段定义
    appid = CharField(null=False, primary_key=True)
    appsecret = BigBitField()
    a_crmsaas = IntegerField()
    a_userapi = IntegerField()
    a_fundapi = IntegerField()
    a_platformapi = IntegerField()
    a_company = IntegerField()
    enabled = IntegerField()
