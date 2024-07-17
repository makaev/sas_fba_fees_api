from selleramp_api_test import create_user
from selleramp_api_test import fba_fee_engine
import pytest


@pytest.fixture(scope="class")
def fixture_class_instance_for_user(request):
    user_cls = create_user.CreateUser()
    if request.cls is not None:
        request.cls.user_cls = user_cls
    return user_cls

@pytest.fixture(scope="class")
def fixture_class_instance_for_fee_engine(request):
    fee_engine_cls = fba_fee_engine.FbaFeeEngine()
    if request.cls is not None:
        request.cls.fee_engine_cls = fee_engine_cls
    return fee_engine_cls